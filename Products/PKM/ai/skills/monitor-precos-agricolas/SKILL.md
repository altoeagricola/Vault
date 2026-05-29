---
name: monitor-precos-agricolas
description: Monitora cotações de commodities agrícolas (conilon, café, grãos) nas fontes CONAB, CEPEA e ESALQ/B3 e produz um boletim de preços com variações relevantes e alertas de movimento. Use quando o usuário disser "monitorar preços", "cotações do conilon", "preços do café", "boletim de mercado", ou por trigger agendado de monitoramento periódico.
---

# Monitoramento de Preços Agrícolas

Skill dedicada ao monitoramento contínuo de cotações de commodities agrícolas com foco em conilon e grãos. Produz boletins estruturados com variações percentuais, alertas e análise de movimento de preços.

## Workflow

### Step 1: Coleta de Dados

1. Consultar fontes oficiais:
   - **CONAB** (Companhia Nacional de Abastecimento): preços de grãos (soja, milho, arroz, feijão)
   - **CEPEA** (Centro de Estudos Avançados em Economia Aplicada): preços de conilon, café e derivados
   - **ESALQ/B3**: índices de commodities agrícolas

2. Registrar para cada commodity:
   - Preço atual (data/hora)
   - Preço de período anterior (dia anterior, semana anterior, mês anterior)
   - Variação percentual
   - Preço máximo e mínimo do período

### Step 2: Análise de Movimento

1. Classificar variações:
   - **Verde** (±0-2%): movimento normal
   - **Amarelo** (±2-5%): movimento relevante — atenção
   - **Vermelho** (>±5%): movimento significativo — alerta

2. Identificar padrões:
   - Tendência: alta, queda, estável
   - Volatilidade: crescente, decrescente, normal
   - Volume de negociação (se disponível)

### Step 3: Geração do Boletim

Produzir documento estruturado:

```
## Boletim de Preços Agrícolas — [Data]

### Resumo Executivo
- Commodities monitoradas: [lista]
- Período de análise: [intervalo]
- Alertas: [total]

### Cotações por Commodity

#### Conilon
| Indicador | Valor | Variação | Status |
|-----------|-------|----------|--------|
| Preço atual | R$ XX | +X% | [cor] |
| Tendência | [descrição] | | |

[idem para café, soja, milho, etc.]

### Alertas e Oportunidades
- [descrição de movimentos relevantes]
- [impactos esperados no setor]

### Fontes
- CONAB (acesso: YYYY-MM-DD HH:MM)
- CEPEA (acesso: YYYY-MM-DD HH:MM)
- ESALQ/B3 (acesso: YYYY-MM-DD HH:MM)
```

### Step 4: Registro em Log

Manter histórico de boletins em `Products/Eloi/monitoramento-precos/` com versionamento por data.

## Triggers

- "monitorar preços agrícolas"
- "cotações do conilon hoje"
- "preços do café"
- "boletim de mercado"
- Automático: agendado (diário/semanal conforme configurado)

## Notas

- Sempre incluir data/hora de acesso às fontes (explicita que dados são recentes)
- Contextualize variações com fatores externos relevantes (clima, safra, política)
- Se uma fonte estiver indisponível, informar explicitamente e usar apenas as disponíveis
