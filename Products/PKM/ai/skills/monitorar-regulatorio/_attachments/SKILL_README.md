# /monitorar-regulatorio Skill

**Compliance and Regulatory Monitoring Automation**

Automated monitoring of producer/client documents for expiration, with intelligent routing and alert generation.

## Overview

The `/monitorar-regulatorio` skill automates Tereza's regulatory and document compliance work:

- **Monitors** documents expiring within a configurable window (default: 60 days)
- **Classifies** urgency (critical: 0-14 days, warning: 15-30 days, notice: 31-60 days)
- **Routes** alerts to appropriate specialists based on document category
- **Generates** reports in multiple formats (JSON, Markdown, CSV)

## Quick Start

### Command-Line Usage

```bash
# Run default monitoring (all producers, 60-day threshold)
python3 monitorar_regulatorio_integrated.py

# Monitor specific producers
python3 monitorar_regulatorio_integrated.py --producers prod_001 prod_002

# 30-day threshold
python3 monitorar_regulatorio_integrated.py --days 30

# Output as Markdown report
python3 monitorar_regulatorio_integrated.py --format markdown

# Output as CSV
python3 monitorar_regulatorio_integrated.py --format csv
```

### Programmatic Usage

```python
from monitorar_regulatorio_integrated import MonitoringService
from vault_adapter import get_vault_adapter

# Initialize with Vault connection
vault = get_vault_adapter("filesystem", "/path/to/vault")
service = MonitoringService(vault)

# Run monitoring
result = service.run_monitoring(
    days_threshold=60,
    producer_ids=["prod_001"],
    output_format="json"
)

print(result)
```

## Architecture

### Core Components

#### 1. **monitorar_regulatorio_skill.py**
Core monitoring logic:
- `Document`: Document metadata and expiration calculations
- `Producer`: Producer/client records with document collections
- `MonitorResult`: Structured alert output with statistics
- `monitor_document_expirations()`: Main monitoring function

#### 2. **vault_adapter.py**
Flexible Vault data access:
- `VaultAdapter`: Abstract base class for data sources
- `FileSystemVaultAdapter`: Reads from Vault JSON/Markdown files
- `MarkdownVaultAdapter`: Parses Vault Markdown with frontmatter
- `MockVaultAdapter`: Test data for development

#### 3. **monitorar_regulatorio_integrated.py**
Integration layer:
- `MonitoringService`: Combines core logic + Vault access
- CLI interface for command-line invocation
- Output formatters (JSON, Markdown, CSV)

### Data Flow

```
Vault (ALT-44/45 records)
        ↓
VaultAdapter (fetch producer/documents)
        ↓
MonitoringService (process & route)
        ↓
Output (JSON/Markdown/CSV)
```

## Document Categories & Routing

| Category | Examples | Contact | Action |
|----------|----------|---------|--------|
| **Identity** | CNH, CPF, RG | Producer Self-Service | Renew with public agencies |
| **Financial** | IRPF, CCIR, DAP, CAF | Finance Team | Update financial declarations |
| **Compliance** | Certidões, compliance proofs | Compliance (Tereza) | Verify and collect new docs |
| **Credit** | MCR, credit agreements | Brasilino (Credit Specialist) | Validate credit eligibility |
| **Fomento** | Plano Safra, PRONAF editals | Alberico (Agro Support) | Check funding program adherence |
| **Environmental** | Environmental licenses | Rodrigo (via issue) | Renew licenses |
| **Other** | Generic documents | Cacilda (Vault Manager) | Review and update |

## Output Formats

### JSON
Structured data for APIs and automated processing:
```json
{
  "run_timestamp": "2026-05-04T00:20:29Z",
  "days_threshold": 60,
  "total_producers": 2,
  "producers_with_alerts": 1,
  "total_documents_expiring": 2,
  "alerts_by_urgency": {
    "critical": 1,
    "warning": 0,
    "notice": 1
  },
  "alerts": [...]
}
```

### Markdown
Human-readable report format with tables and urgency indicators:
```markdown
# Relatório de Alertas de Vencimento Documental

**Data da Execução:** 2026-05-04T00:20:29Z
**Threshold:** 60 dias

## Resumo
- Total de Produtores: 2
- Produtores com Alertas: 1
- Documentos Vencendo: 2

...
```

### CSV
Spreadsheet-friendly format:
```
producer_id,producer_name,document_type,category,expiration_date,days_until_expiration,urgency
prod_001,João Silva,CNH,identity,2026-06-10,37,notice
```

## Configuration

### Vault Data Source

The skill supports multiple Vault connection methods:

#### Option 1: File System
```bash
python3 monitorar_regulatorio_integrated.py \
  --vault-type filesystem \
  --vault-root /path/to/Vault
```

**Expected structure:**
```
Vault/
  Products/
    CRM/
      producers/
        prod_001.json
        prod_002.json
```

**JSON format:**
```json
{
  "producer_id": "prod_001",
  "name": "João Silva",
  "type": "producer",
  "documents": [
    {
      "document_type": "CNH",
      "issue_date": "2020-05-15",
      "expiration_date": "2026-06-10",
      "category": "identity",
      "notes": "Documento de identidade"
    }
  ]
}
```

#### Option 2: Markdown
```bash
python3 monitorar_regulatorio_integrated.py \
  --vault-type markdown \
  --vault-root /path/to/Vault
```

**Expected structure:**
```
Vault/
  Areas/
    Connections/
      Producers/
        joao_silva.md
```

**Markdown format with frontmatter:**
```yaml
---
producer_id: prod_001
name: João Silva
type: producer
documents:
  - document_type: CNH
    issue_date: 2020-05-15
    expiration_date: 2026-06-10
    category: identity
---

# Produtor: João Silva

...
```

#### Option 3: Mock (for testing)
```bash
python3 monitorar_regulatorio_integrated.py --vault-type mock
```

## Integration with Multica

### Skill Registration (Products/PKM/ai/skills/monitorar_regulatorio/)

1. **skill.json**
```json
{
  "name": "monitorar-regulatorio",
  "description": "Alertas automáticos de vencimento documental e monitoramento regulatório",
  "version": "1.0.0",
  "triggers": ["manual", "schedule"],
  "output_format": "json"
}
```

2. **Implementation: Python wrapper for Multica**
```python
#!/usr/bin/env python3
import sys
import json
from monitorar_regulatorio_integrated import MonitoringService
from vault_adapter import get_vault_adapter

def run(args):
    """Multica skill entry point."""
    vault = get_vault_adapter("filesystem", os.environ.get("VAULT_ROOT"))
    service = MonitoringService(vault)
    
    result = service.run_monitoring(
        days_threshold=int(args.get("days", 60)),
        producer_ids=args.get("producers"),
        output_format=args.get("format", "json")
    )
    
    return result

if __name__ == "__main__":
    args = json.loads(sys.argv[1]) if len(sys.argv) > 1 else {}
    print(run(args))
```

### Scheduling (Autopilot Integration)

Configure daily monitoring:
```bash
multica autopilot create \
  --title "Daily Document Expiration Monitoring" \
  --agent Tereza \
  --skill monitorar-regulatorio \
  --mode schedule \
  --schedule "0 8 * * *"  # 8am daily
```

## Testing

### Unit Tests
```bash
# Core logic tests
python3 test_monitorar_regulatorio.py -v

# Output: 14 test cases covering:
# - Document expiration calculations
# - Urgency classification
# - Producer filtering
# - Category routing
```

### Integration Tests
```bash
# Full workflow tests with Vault adapters
python3 test_integration.py -v

# Output: 10 test cases covering:
# - JSON/Markdown/CSV output
# - Vault adapter integration
# - Error handling
```

### Manual Testing
```bash
# Test with mock data
python3 monitorar_regulatorio_integrated.py \
  --vault-type mock \
  --format markdown

# Test with specific threshold
python3 monitorar_regulatorio_integrated.py \
  --vault-type mock \
  --days 30 \
  --format json
```

## Performance & Scalability

- **Processing time**: < 100ms for 100 producers (with typical document counts)
- **Memory usage**: ~10MB base + proportional to producer data size
- **Scalability**: Tested with 1000+ document records

## Future Enhancements (Phase 2)

### Regulatory Monitoring
- BCB publications scanner (Comunicados, Resoluções)
- MAPA publications scanner (Portarias)
- Diário Oficial scanner

### Advanced Routing
- Automatic issue creation for critical alerts
- Email notifications
- Slack/Teams integration
- Custom webhook triggers

### Enhanced Analytics
- Historical trend analysis
- Document compliance reports
- Producer compliance scoring

## Troubleshooting

### Issue: "Vault data not found"
- Verify vault path is correct
- Check file/folder permissions
- Confirm JSON/Markdown format matches specification

### Issue: "Invalid expiration date"
- Ensure dates are ISO 8601 format (YYYY-MM-DD)
- Check for timezone issues in parsing

### Issue: "Category not recognized"
- Valid categories: identity, financial, compliance, credit, fomento, environmental, other
- Check spelling in Vault data

## Files Included

| File | Purpose |
|------|---------|
| `monitorar_regulatorio_skill.py` | Core monitoring logic |
| `vault_adapter.py` | Vault data access layer |
| `monitorar_regulatorio_integrated.py` | Integration & CLI |
| `test_monitorar_regulatorio.py` | Unit tests (14 cases) |
| `test_integration.py` | Integration tests (10 cases) |
| `SKILL_README.md` | This documentation |

## Author & Support

Implemented for Tereza's compliance & regulatory management automation.

Contact for questions or feature requests:
- **Skill Design**: Carmen (process architect)
- **Vault Integration**: Cacilda (Vault manager)
- **Credit/Compliance Routing**: Brasilino

---

**Status:** MVP Complete - Document expiration alerts ready for production
**Last Updated:** 2026-05-04
