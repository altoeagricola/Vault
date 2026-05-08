---
titulo: Modelo Operacional - Ficha Econômico-Financeira
tipo: template
formato: markdown
referencia: "[[Ficha Economico-Financeira Minima do Produtor]]"
finalidade: "Captura estruturada de dados financeiros de produtores em campo"
atualizado: 2026-05-04
---

# Ficha Econômico-Financeira — Modelo Operacional

Template para preenchimento de dados financeiros de produtor. Consulte [[Ficha Economico-Financeira Minima do Produtor]] para instruções detalhadas e regras de classificação.

## Estrutura de Preenchimento

| Campo | Tipo de Dado | Exemplo |
|-------|--------------|---------|
| **Data de Coleta** | Data (AAAA-MM-DD) | 2026-05-04 |
| **Nome do Produtor** | Texto | João da Silva |
| **Município** | Texto | Venda Nova do Imigrante |
| **Área Total (ha)** | Número | 50 |
| **Tipo: Área Total** | declarado/documental | declarado |
| **Área Cultivada (ha)** | Número | 35 |
| **Tipo: Área Cultivada** | declarado/documental | declarado |
| **Cultura Principal** | Texto | Conilon |
| **Culturas Secundárias** | Texto | Pimenta, Milho |
| **Área CCIR (ha)** | Número | 50 |
| **Tipo: Área CCIR** | documental | documental |

## Dados Produtivos (por cultura)

### Cultura 1

| Campo | Tipo de Dado | Exemplo |
|-------|--------------|---------|
| Nome da Cultura | Texto | Conilon |
| Área (ha) | Número | 25 |
| Produtividade Estimada | Número | 80 |
| Unidade | Texto | saca/ha |
| Preço Médio | Moeda | R$ 450,00 |
| Mês Início Colheita | Texto | Maio |
| Mês Fim Colheita | Texto | Setembro |
| Mês Principal Receita | Texto | Julho |

### Cultura 2 (se aplicável)

| Campo | Tipo de Dado | Exemplo |
|-------|--------------|---------|
| Nome da Cultura | Texto | Pimenta |
| Área (ha) | Número | 10 |
| Produtividade Estimada | Número | 15 |
| Unidade | Texto | tonelada/ha |
| Preço Médio | Moeda | R$ 3.500,00 |
| Mês Início Colheita | Texto | Janeiro |
| Mês Fim Colheita | Texto | Março |
| Mês Principal Receita | Texto | Fevereiro |

## Dados Financeiros — Declarados

| Campo | Tipo de Dado | Exemplo |
|-------|--------------|---------|
| Receita Bruta Estimada Safra | Moeda | R$ 110.000,00 |
| Tipo | declarado | declarado |
| Dívidas Existentes | Moeda | R$ 25.000,00 |
| Tipo | declarado | declarado |
| Prestações em Aberto | Moeda | R$ 8.000,00 |
| Tipo | declarado | declarado |
| Outras Receitas (família/propriedade) | Moeda | R$ 3.000,00 |
| Tipo | declarado | declarado |
| Despesas Fixas Mensais | Moeda | R$ 5.000,00 |
| Tipo | declarado | declarado |

## Dados Documentais

| Campo | Tipo de Dado | Exemplo |
|-------|--------------|---------|
| CCIR Apresentado | sim/não | sim |
| DAP/CAF Apresentado | sim/não | sim |
| IR Apresentado | sim/não | não |
| Renda Documental | Moeda | R$ 120.000,00 |
| Tipo | documental | documental |

## Dados Estimados

| Campo | Tipo de Dado | Exemplo |
|-------|--------------|---------|
| Custo Produção/ha | Moeda | R$ 2.500,00 |
| Tipo | estimado | estimado |
| Despesa Manutenção Safra | Moeda | R$ 15.000,00 |
| Tipo | estimado | estimado |
| Custo Total Estimado Safra | Moeda | R$ 87.500,00 |
| Tipo | estimado | estimado |

## Indicadores Calculados

| Indicador | Fórmula | Resultado |
|-----------|---------|-----------|
| **Receita Esperada Safra** | Σ(área × produtividade × preço) | R$ 110.000,00 |
| **Margem Bruta/ha** | (Receita - Custo) / Área Cultivada | R$ 642,86 |
| **Capacidade de Pagamento** | forte / média / apertada | média |

## Observações

Campo para registrar contexto adicional, restrições ou notas relevantes para análise.

---

## Uso Operacional

**Em Campo:** Use o arquivo CSV (`ficha_produtor_modelo.csv`) para preenchimento estruturado.

**No Vault:** Esta nota serve como referência do modelo e permite linking em notas de clientes, propostas e análises.

**Validação:** Consulte [[Ficha Economico-Financeira Minima do Produtor]] para regras de classificação (declarado/documental/estimado) antes de consolidar dados.
