#!/usr/bin/env python3
"""
/monitorar-regulatorio Skill - MVP: Document Expiration Alerts

Monitors producer/client records in Vault for documents expiring within
a configurable threshold (default 60 days). Returns structured alerts
with producer info, document details, urgency level, and suggested actions.
"""

from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from enum import Enum
from typing import List, Dict, Optional, Any
import json


class DocumentCategory(Enum):
    """Document categories and their responsible teams/actions."""
    IDENTITY = "identity"  # CNH, CPF, RG
    FINANCIAL = "financial"  # IRPF, CCIR, DAP, CAF
    COMPLIANCE = "compliance"  # Certidões, proof of compliance
    CREDIT = "credit"  # MCR, credit agreements
    FOMENTO = "fomento"  # Agricultural subsidy programs
    ENVIRONMENTAL = "environmental"  # Environmental licenses
    OTHER = "other"


class UrgencyLevel(Enum):
    """Alert urgency based on days until expiration."""
    CRITICAL = "critical"  # 0-14 days
    WARNING = "warning"  # 15-30 days
    NOTICE = "notice"  # 31-60 days


DOCUMENT_ROUTING = {
    DocumentCategory.IDENTITY: {
        "contact": "producer_self_service",
        "action": "Renovar documento de identidade",
        "notes": "Produtor deve renovar junto aos órgãos públicos"
    },
    DocumentCategory.FINANCIAL: {
        "contact": "finance_team",
        "action": "Atualizar declarações financeiras",
        "notes": "Pode impactar análises de capacidade de pagamento"
    },
    DocumentCategory.COMPLIANCE: {
        "contact": "compliance_team",  # Tereza
        "action": "Verificar situação e coletar novo documento",
        "notes": "Necessário para manter conformidade"
    },
    DocumentCategory.CREDIT: {
        "contact": "brasilino",  # Credit specialist
        "action": "Validar requisitos do MCR/Crédito Rural",
        "notes": "Pode afetar elegibilidade para crédito"
    },
    DocumentCategory.FOMENTO: {
        "contact": "alberico",  # Agricultural support
        "action": "Verificar aderência a editais de fomento",
        "notes": "Oportunidades de apoio podem estar condicionadas"
    },
    DocumentCategory.ENVIRONMENTAL: {
        "contact": "rodrigo_via_issue",  # Environmental specialist
        "action": "Renovar licença ambiental",
        "notes": "Necessário para operação legal"
    },
    DocumentCategory.OTHER: {
        "contact": "cacilda",  # Vault manager
        "action": "Revisar e atualizar no Vault",
        "notes": "Documentação geral"
    }
}


@dataclass
class Document:
    """Document metadata for expiration tracking."""
    document_type: str
    issue_date: datetime
    expiration_date: datetime
    category: DocumentCategory
    notes: Optional[str] = None

    def days_until_expiration(self) -> int:
        """Calculate days until expiration (negative = already expired)."""
        return (self.expiration_date - datetime.now()).days

    def urgency_level(self) -> UrgencyLevel:
        """Determine urgency based on days until expiration."""
        days = self.days_until_expiration()
        if days <= 14:
            return UrgencyLevel.CRITICAL
        elif days <= 30:
            return UrgencyLevel.WARNING
        elif days <= 60:
            return UrgencyLevel.NOTICE
        else:
            return UrgencyLevel.NOTICE  # Won't be included in alerts beyond 60 days


@dataclass
class Producer:
    """Producer/Client record structure (from ALT-44 & ALT-45)."""
    producer_id: str
    name: str
    type: str  # "producer" | "client" | "partner"
    documents: List[Document]

    def expiring_documents(self, days_threshold: int = 60) -> List[Document]:
        """Get documents expiring within threshold (includes already-expired)."""
        return [
            doc for doc in self.documents
            if doc.days_until_expiration() <= days_threshold
        ]

    def to_alert_dict(self, days_threshold: int = 60) -> Optional[Dict[str, Any]]:
        """Convert to alert structure if has expiring documents."""
        expiring = self.expiring_documents(days_threshold)
        if not expiring:
            return None

        return {
            "producer_id": self.producer_id,
            "producer_name": self.name,
            "producer_type": self.type,
            "document_count": len(expiring),
            "documents": [
                {
                    "type": doc.document_type,
                    "issue_date": doc.issue_date.isoformat(),
                    "expiration_date": doc.expiration_date.isoformat(),
                    "days_until_expiration": doc.days_until_expiration(),
                    "category": doc.category.value,
                    "urgency": doc.urgency_level().value,
                    "routing": DOCUMENT_ROUTING.get(
                        doc.category,
                        DOCUMENT_ROUTING[DocumentCategory.OTHER]
                    ),
                    "suggested_action": DOCUMENT_ROUTING.get(
                        doc.category,
                        DOCUMENT_ROUTING[DocumentCategory.OTHER]
                    )["action"],
                    "notes": doc.notes
                }
                for doc in sorted(
                    expiring,
                    key=lambda d: d.days_until_expiration()
                )
            ]
        }


@dataclass
class MonitorResult:
    """Result structure for monitoring run."""
    run_timestamp: str
    days_threshold: int
    total_producers: int
    producers_with_alerts: int
    total_documents_expiring: int
    alerts_by_urgency: Dict[str, int]
    alerts: List[Dict[str, Any]]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent, default=str)


def monitor_document_expirations(
    producers: List[Producer],
    days_threshold: int = 60,
) -> MonitorResult:
    """
    Monitor all producers for expiring documents.

    Args:
        producers: List of producer records with documents
        days_threshold: Window for alerts (default 60 days)

    Returns:
        MonitorResult with structured alert data
    """
    run_timestamp = datetime.now().isoformat()
    alerts = []
    urgency_counts = {
        "critical": 0,
        "warning": 0,
        "notice": 0
    }

    for producer in producers:
        producer_alert = producer.to_alert_dict(days_threshold)
        if producer_alert:
            alerts.append(producer_alert)
            # Count urgencies
            for doc in producer_alert["documents"]:
                urgency_counts[doc["urgency"]] += 1

    result = MonitorResult(
        run_timestamp=run_timestamp,
        days_threshold=days_threshold,
        total_producers=len(producers),
        producers_with_alerts=len(alerts),
        total_documents_expiring=sum(urgency_counts.values()),
        alerts_by_urgency=urgency_counts,
        alerts=sorted(
            alerts,
            key=lambda a: (
                # Sort by urgency (critical first)
                {
                    "critical": 0,
                    "warning": 1,
                    "notice": 2
                }.get(a["documents"][0]["urgency"], 3),
                # Then by days until expiration
                min(d["days_until_expiration"] for d in a["documents"])
            )
        )
    )

    return result


# ============================================================================
# Example usage (for testing before Vault integration)
# ============================================================================

if __name__ == "__main__":
    # Test data
    sample_producers = [
        Producer(
            producer_id="producer_001",
            name="João Silva",
            type="producer",
            documents=[
                Document(
                    document_type="CNH",
                    issue_date=datetime(2020, 5, 15),
                    expiration_date=datetime(2026, 6, 10),  # 38 days
                    category=DocumentCategory.IDENTITY,
                    notes="Vencimento próximo"
                ),
                Document(
                    document_type="CCIR",
                    issue_date=datetime(2023, 3, 1),
                    expiration_date=datetime(2026, 3, 1),  # Expired
                    category=DocumentCategory.FINANCIAL,
                    notes="Já vencido"
                ),
            ]
        ),
        Producer(
            producer_id="producer_002",
            name="Maria Santos",
            type="client",
            documents=[
                Document(
                    document_type="IRPF",
                    issue_date=datetime(2024, 1, 1),
                    expiration_date=datetime(2025, 4, 30),  # Already expired
                    category=DocumentCategory.FINANCIAL,
                ),
                Document(
                    document_type="Contrato de Fomento - Plano Safra",
                    issue_date=datetime(2025, 6, 1),
                    expiration_date=datetime(2026, 8, 31),  # 90 days
                    category=DocumentCategory.FOMENTO,
                ),
            ]
        ),
    ]

    # Run monitoring
    result = monitor_document_expirations(sample_producers, days_threshold=60)

    print(result.to_json())
