---
title: Aprendizados Operacionais — Piloto 001
type: Operational Learning
case: Sergio Jose Altoe | Pronaf Habitação Rural
related:
  - "[[Products/Crédito-Rural/Clientes/Sergio Jose Altoe]]"
  - "[[ALTOE Agricola]]"
created: 2026-05-05
updated: 2026-05-06
status: finalized
---

# Aprendizados Operacionais — Piloto 001
## Caso: Sergio Jose Altoe | Pronaf Habitação Rural R$ 100 mil | ALTOE Agrícola

**Data:** 2026-05-05
**Orquestradora:** Carmen
**Objetivo:** Registrar aprendizados do primeiro piloto operacional real para garantir que o próximo caso seja mais coordenado, eficiente e com menos retrabalho.
**Status do piloto:** Funcional, com entregas em todas as 7 frentes, mas com fragilidades sistêmicas corrigíveis.
**Issues de referência:** ALT-63 (coordenação) / ALT-64 a ALT-71 (frentes) / ALT-71 (registro documental PDF→md)

---

## 1. O QUE FUNCIONOU BEM — PRESERVAR

1. **Competências técnicas individuais**: cada agente entregou no escopo com qualidade mínima adequada. Nenhuma frente ficou sem resultado.
2. **Proatividade de segurança (Cacilda)**: identificou e corrigiu credential leak (senha em plaintext no Git) sem ser solicitada.
3. **Honestidade nas premissas (Mariano)**: declarou explicitamente o que era estimado, documental ou declarado. Padrão a replicar em todas as análises financeiras.
4. **Leitura relacional rica (Marta)**: identificou contexto familiar, modelo multiproduto e potencial de recorrência sem que ninguém pedisse.
5. **Escalada eficiente (Tereza)**: quando bloqueada, escalou de forma clara e produtiva sem travar o processo.
6. **Análise além do escopo (Alberico)**: mapeou agenda futura de portfólio ALTOE além do caso imediato — boa prática quando não gera custo excessivo de tempo.

---

## 2. PROBLEMAS E GAPS IDENTIFICADOS

### 2.1 Gaps de Infraestrutura

| Gap | Impacto | Ação necessária |
|---|---|---|
| PDFs escaneados sem OCR | Todos os documentos críticos do cliente ilegíveis para os agentes; análises condicionais | OCR obrigatório antes de iniciar qualquer piloto |
| Push SSH falhando (GitHub) | Commits da Cacilda apenas no ambiente local — risco de perda | Resolver configuração SSH antes do próximo caso |

### 2.2 Gaps de Protocolo

| Gap | Impacto | Ação necessária |
|---|---|---|
| Sem nota-briefing do cliente no kickoff | Cada agente mapeou o mesmo terreno do zero; redundância e inconsistência | Carmen cria nota-briefing do cliente antes de abrir frentes |
| 7 frentes abertas simultaneamente sem precondições | Análises financeiras e de crédito condicionais a documentos não verificados | Tereza e Cacilda entregam primeiro (Fase 0); demais entram depois |
| Handoff Eloi→Mariano não formalizado | Mariano usou premissas próprias desconexas dos dados do Eloi | Eloi cria nota de handoff explícita para Mariano antes dele iniciar |
| CAF e CAR não verificados em sistema oficial | Potencialmente impeditivos para Pronaf; risco de retrabalho total | Gate obrigatório: CAFWeb + SICAR antes de qualquer análise financeira |
| Ausência de documento consolidado de resultado | 8 saídas dispersas em 7 issues filhas; impossível usar diretamente com banco | Cacilda cria nota-mãe consolidando todas as saídas ao final de cada caso |

### 2.3 Sobreposições Desnecessárias

| Par | Sobreposição | Solução |
|---|---|---|
| Tereza × Cacilda | Mapeamento documental duplicado (checklist de compliance vs. registros .md) | Tereza: análise de conformidade e validade; Cacilda: estrutura de registro e rastreabilidade |
| Brasilino × Alberico | Pronaf Habitação apareceu em ambas as análises de forma desconectada | Brasilino é referência técnica de crédito; Alberico complementa com alternativas não-bancárias, sem duplicar o objeto principal |

### 2.4 Qualidade de Entrega

| Agente | Problema | Solução |
|---|---|---|
| Brasilino | Tom informal (emojis, gírias) em análise técnica de crédito | Guideline de tom: estilo livre internamente; formal para entregas bancárias/cliente |
| Brasilino | Não incluiu a Cresol (banco já identificado pelo cliente) na matriz de linhas | Verificar sempre o banco mencionado no dossiê do cliente antes de montar a matriz |
| Todos | Ausência de referência cruzada explícita entre frentes | Cada agente deve citar os dados dos outros quando relevante; não trabalhar em silo |

---

## 3. PROTOCOLO PARA O PRÓXIMO CASO

### FASE 0 — Precondições (ANTES de abrir frentes de análise)

- [ ] **Cacilda**: executar OCR de todos os documentos do cliente; criar pasta estruturada no Vault com índice mestre
- [ ] **Carmen**: criar nota-briefing do cliente consolidando tudo que é conhecido (documentos disponíveis, banco identificado, demanda clara, pendências abertas)
- [ ] **Tereza**: verificar CAF no CAFWeb e CAR no SICAR; separar impeditivos reais de pendências saneáveis; entregar checklist de precondições

⛔ **Gate:** as Fases 1 e 2 só iniciam após Fase 0 concluída.

### FASE 1 — Contexto (inicia após Fase 0)

- [ ] **Eloi**: briefing de mercado + **nota de handoff para Mariano** com dados de entrada calibrados (preço, produtividade regional, premissas para simulação)
- [ ] **Marta**: ficha CRM com campo "próximo passo concreto" obrigatório

### FASE 2 — Análise de mérito (inicia após Fase 1)

- [ ] **Mariano**: simulação financeira usando dados da nota de handoff do Eloi (citar explicitamente)
- [ ] **Brasilino**: enquadramento de crédito referenciando conformidade da Tereza e capacidade do Mariano; incluir o banco já identificado pelo cliente; tom técnico-formal
- [ ] **Alberico**: mapa de alternativas complementares (não duplicar objeto principal do Brasilino)

### FASE 3 — Consolidação

- [ ] **Cacilda**: nota-mãe reunindo todas as saídas com índice e links internos
- [ ] **Carmen**: parecer final + próximos passos com responsáveis, prazo e ação concreta

---

## 4. APRENDIZADOS POR PAPEL

| Papel | Aprendizado principal |
|---|---|
| Carmen | Sequenciar antes de paralelizar. Gate de precondições (OCR, CAF, CAR) é obrigatório — não abrir análise de mérito sem ele. Criar nota-briefing do cliente no kickoff. |
| Cacilda | OCR é responsabilidade dela no início de cada caso. O que não está em texto pesquisável não existe para o time. Resolver SSH/GitHub antes do próximo piloto. |
| Tereza | Deve entregar checklist de precondições antes das demais frentes — não em paralelo. CAF e CAR: confirmar em sistema oficial, não só por existência de arquivo. |
| Eloi | Criar nota de handoff explícita para Mariano com dados de entrada calibrados. Dados regionais têm valor mas precisam de passagem formal. |
| Mariano | Verificar se Eloi já entregou antes de usar premissas próprias de produtividade. Sempre declarar qual dado é estimado vs. documental vs. declarado. |
| Brasilino | Tom formal para entregas técnicas. Incluir banco já identificado pelo cliente na matriz. Referenciar Tereza (conformidade) e Mariano (capacidade) no enquadramento. |
| Alberico | Alternativas complementares, não duplicação do objeto principal do Brasilino. Calibrar profundidade da análise ao que é acionável para o caso atual. |
| Marta | Campo "próximo passo concreto" é obrigatório no CRM — lacuna aberta sem ação proposta não fecha o ciclo relacional. |

---

## 6. Atribuição de Skills Existentes no Vault — 2026-05-06

Após a avaliação das skills existentes em `Products/PKM/ai/skills`, Carmen identificou que várias skills já estavam maduras para uso imediato, mas ainda não estavam formalmente atribuídas aos agentes na Multica. As skills foram importadas/registradas na plataforma e atribuídas conforme aderência de papel.

| Agente | Skills atribuídas | Papel operacional |
|---|---|---|
| Cacilda | `ingest-business`, `ingest`, `ingest-pdf`, `lint`, `conceptualize`, `ingest-youtube`, `ingest-tweet`, `ingest-product` | Dona da curadoria, ingestão, organização e saúde do Vault. |
| Carmen | `ingest-business`, `conceptualize`, `lint` | Revisão conceitual-processual, auditoria de coerência, estruturação de linguagem e processos. |
| Tereza | `monitorar-regulatorio`, `update-mcr` | Compliance documental, monitoramento de vencimentos e revisão normativa do MCR. |
| Brasilino | `update-mcr` | Dono técnico da atualização do Manual de Crédito Rural. |
| Alberico | `score-aderencia-edital`, `ingest-call` | Fomento, editais, chamadas públicas e matching de parceiros ICTs. |
| Eloi | Nenhuma skill existente atribuída | Não havia skill existente adequada para inteligência de mercado agro. Exige skill nova. |
| Mariano | Nenhuma skill existente atribuída | Não havia skill existente adequada para simulação financeira rural. Exige skill nova. |
| Marta | Nenhuma skill existente atribuída | Não havia skill existente adequada para CRM rural/relacionamento. Exige skill nova. |

**Aprendizado operacional:** As skills existentes já cobrem curadoria do Vault, ingestão documental, atualização normativa, compliance documental, editais/fomento e revisão conceitual. O time ainda não possui skills específicas para três funções críticas reveladas no Piloto 001: inteligência de mercado com handoff, simulação financeira rural e CRM rural com próximo passo concreto. A ausência dessas três skills não impede o registro das atribuições já realizadas, mas deve ser tratada como pendência estruturante antes de um Piloto 002.

---

## 5. REFERÊNCIAS

- Issue de coordenação: ALT-63
- CRM Sergio: ALT-64 | Cenário conilon: ALT-65 | Compliance: ALT-66
- Financeiro: ALT-67 | Fomento: ALT-68 | Vault: ALT-69 | Crédito: ALT-70
- Registro documental PDF→md: ALT-71
- Saída 9 (relatório completo de performance): ALT-63, comentário de 2026-05-05
