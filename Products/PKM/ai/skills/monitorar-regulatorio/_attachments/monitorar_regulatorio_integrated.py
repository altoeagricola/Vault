#!/usr/bin/env python3
"""
/monitorar-regulatorio Skill - Full Integration

Combines core monitoring logic with Vault data access.
Can be invoked as:
  - Direct Python: python monitorar_regulatorio_integrated.py
  - Multica CLI: /monitorar-regulatorio [options]
  - Automation: triggered by schedules or events
"""

import json
import sys
from typing import Optional, List
from datetime import datetime

from monitorar_regulatorio_skill import (
    Document, Producer, monitor_document_expirations, DocumentCategory
)
from vault_adapter import get_vault_adapter, VaultAdapter


class MonitoringService:
    """Main service for regulatory monitoring."""

    def __init__(self, vault_adapter: VaultAdapter):
        """
        Initialize monitoring service.

        Args:
            vault_adapter: VaultAdapter instance for data access
        """
        self.vault = vault_adapter

    def run_monitoring(
        self,
        days_threshold: int = 60,
        producer_ids: Optional[List[str]] = None,
        output_format: str = "json"
    ) -> str:
        """
        Run full monitoring workflow.

        Args:
            days_threshold: Window for document expiration alerts (default 60 days)
            producer_ids: Optional list of specific producers to monitor
            output_format: Output format ("json", "markdown", "csv")

        Returns:
            Formatted monitoring result
        """
        try:
            # Fetch producer data from Vault
            producer_data = self.vault.get_producers(producer_ids)

            # Convert to Producer objects with Document data
            producers = self._build_producer_objects(producer_data)

            # Run monitoring
            result = monitor_document_expirations(producers, days_threshold)

            # Format output
            if output_format == "json":
                return result.to_json()
            elif output_format == "markdown":
                return self._format_markdown(result)
            elif output_format == "csv":
                return self._format_csv(result)
            else:
                raise ValueError(f"Unknown output format: {output_format}")

        except Exception as e:
            return json.dumps({
                "error": str(e),
                "timestamp": datetime.now().isoformat(),
                "status": "failed"
            }, indent=2)

    @staticmethod
    def _build_producer_objects(producer_data: List[dict]) -> List[Producer]:
        """Convert Vault data to Producer objects."""
        producers = []

        for data in producer_data:
            try:
                # Convert document data to Document objects
                documents = []
                for doc_data in data.get("documents", []):
                    try:
                        doc = Document(
                            document_type=doc_data["document_type"],
                            issue_date=datetime.fromisoformat(
                                doc_data.get("issue_date", datetime.now().isoformat())
                            ),
                            expiration_date=datetime.fromisoformat(
                                doc_data["expiration_date"]
                            ),
                            category=DocumentCategory[doc_data.get("category", "OTHER").upper()],
                            notes=doc_data.get("notes")
                        )
                        documents.append(doc)
                    except (KeyError, ValueError) as e:
                        print(f"Warning: Could not parse document in {data['producer_id']}: {e}")
                        continue

                # Create Producer object
                producer = Producer(
                    producer_id=data["producer_id"],
                    name=data["name"],
                    type=data.get("type", "producer"),
                    documents=documents
                )
                producers.append(producer)

            except KeyError as e:
                print(f"Warning: Missing required field in producer data: {e}")
                continue

        return producers

    @staticmethod
    def _format_markdown(result) -> str:
        """Format result as Markdown."""
        lines = [
            "# Relatório de Alertas de Vencimento Documental",
            "",
            f"**Data da Execução:** {result.run_timestamp}",
            f"**Threshold:** {result.days_threshold} dias",
            "",
            "## Resumo",
            "",
            f"- Total de Produtores: {result.total_producers}",
            f"- Produtores com Alertas: {result.producers_with_alerts}",
            f"- Documentos Vencendo: {result.total_documents_expiring}",
            "",
            "### Urgência",
            "",
            f"- 🔴 **Critical** (0-14 dias): {result.alerts_by_urgency['critical']}",
            f"- 🟠 **Warning** (15-30 dias): {result.alerts_by_urgency['warning']}",
            f"- 🟡 **Notice** (31-60 dias): {result.alerts_by_urgency['notice']}",
            "",
        ]

        if result.alerts:
            lines.extend(["## Alertas Detalhados", ""])
            for alert in result.alerts:
                lines.extend([
                    f"### {alert['producer_name']} (ID: {alert['producer_id']})",
                    "",
                    f"**Tipo:** {alert['producer_type']}",
                    f"**Documentos vencendo:** {alert['document_count']}",
                    "",
                    "| Documento | Categoria | Vencimento | Dias | Ação |",
                    "|-----------|-----------|-----------|------|------|",
                ])
                for doc in alert["documents"]:
                    urgency_icon = {
                        "critical": "🔴",
                        "warning": "🟠",
                        "notice": "🟡"
                    }.get(doc["urgency"], "⚪")
                    lines.append(
                        f"| {urgency_icon} {doc['type']} | {doc['category']} | "
                        f"{doc['expiration_date'][:10]} | {doc['days_until_expiration']} | "
                        f"{doc['suggested_action']} |"
                    )
                lines.append("")
        else:
            lines.extend([
                "## ✅ Nenhum Alerta",
                "",
                "Todos os documentos estão em dia!"
            ])

        return "\n".join(lines)

    @staticmethod
    def _format_csv(result) -> str:
        """Format result as CSV."""
        lines = [
            "producer_id,producer_name,document_type,category,expiration_date,days_until_expiration,urgency,suggested_action"
        ]

        for alert in result.alerts:
            for doc in alert["documents"]:
                lines.append(
                    f'"{alert["producer_id"]}","{alert["producer_name"]}",'
                    f'"{doc["type"]}","{doc["category"]}",'
                    f'"{doc["expiration_date"]}",{doc["days_until_expiration"]}'
                    f',"{doc["urgency"]}","{doc["suggested_action"]}"'
                )

        return "\n".join(lines)


# ============================================================================
# CLI Interface
# ============================================================================

def main():
    """Command-line interface."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Monitoramento Regulatório - Alertas de Vencimento Documental"
    )
    parser.add_argument(
        "--days",
        type=int,
        default=60,
        help="Dias até vencimento para alertar (padrão: 60)"
    )
    parser.add_argument(
        "--producers",
        nargs="+",
        help="IDs específicos de produtores a monitorar"
    )
    parser.add_argument(
        "--format",
        choices=["json", "markdown", "csv"],
        default="json",
        help="Formato de saída (padrão: json)"
    )
    parser.add_argument(
        "--vault-type",
        choices=["filesystem", "markdown", "mock"],
        default="mock",
        help="Tipo de data source do Vault (padrão: mock)"
    )
    parser.add_argument(
        "--vault-root",
        help="Caminho raiz do Vault (obrigatório para filesystem/markdown)"
    )

    args = parser.parse_args()

    # Initialize service
    try:
        vault = get_vault_adapter(args.vault_type, args.vault_root)
        service = MonitoringService(vault)

        # Run monitoring
        result = service.run_monitoring(
            days_threshold=args.days,
            producer_ids=args.producers,
            output_format=args.format
        )

        print(result)
        return 0

    except Exception as e:
        print(json.dumps({
            "error": str(e),
            "timestamp": datetime.now().isoformat(),
            "status": "failed"
        }, indent=2), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
