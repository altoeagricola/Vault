---
title: LEV-P100 v10 — Nota-Mae
type: Case Summary
case_id: ALT-440
date: 2026-05-29
author: Cacilda
status: concluido
root:
  - "[[MGgrafeno]]"
documento_final: "[[MGG3-LEV-P100-v10_Levantamento-Custos-Cenarios-Desenvolvimento-Producao-Consolidado]]"
issue_mae: ALT-440
issue_revisao_final: ALT-450
tags:
  - case
  - mggrafeno
  - lev-p100
  - nota-mae
---

# LEV-P100 v10 — Nota-Mae

## Sintese Executiva

O caso ALT-440 atualizou o levantamento de custos da P100 do MGgrafeno a partir da v9, reorganizando o material em dois cenarios operacionais distintos: **P100 Desenvolvimento** e **P100 Producao**. A versao final esta no Vault como [[MGG3-LEV-P100-v10_Levantamento-Custos-Cenarios-Desenvolvimento-Producao-Consolidado|MGG3-LEV-P100-v10]]; a [[MGG3-LEV-P100-v9_Levantamento-Custos-Recomissionamento-Consolidado|v9]] permanece preservada como base historica imediata.

Em Desenvolvimento, a P100 e tratada como planta piloto tecnica: OPEX base de **R$ 4,094 MM/ano** (R$ 341,2k/mes), faixa **R$ 3,65-4,84 MM/ano**, custo por campanha base **R$ 80k** e custo marginal de lote a la carte **R$ 18k/lote**. Em Producao, a P100 e tratada como linha dedicada em 1 turno: OPEX caso-base de **R$ 2,481 MM/ano** (R$ 206,75k/mes), igual nas tres condicoes de rendimento, com custo unitario por produto variando conforme a massa recuperada.

Recomendacao: a v10 esta pronta para apresentacao a Rodrigo e pode seguir para investidor como leitura economica, com ressalva expressa de que uso contratual ou due diligence exige reconciliacao CFO, RFQs e ingestao formal das fontes externas ainda faltantes.

## Dados do Caso

- **Cliente / contexto:** MGgrafeno, P100, revisao de custo para apresentacao executiva/investidor.
- **Demanda original:** remodelar o LEV-P100 v9 em dois cenarios claros, com premissas separadas e rastreabilidade numerica.
- **Periodo de analise:** 2026-05-28 a 2026-05-29.
- **Documento final:** [[MGG3-LEV-P100-v10_Levantamento-Custos-Cenarios-Desenvolvimento-Producao-Consolidado]].
- **Base preservada:** [[MGG3-LEV-P100-v9_Levantamento-Custos-Recomissionamento-Consolidado]].
- **Lacunas pendentes:** RFQs, ARTs/SAT/NR-12, reconciliacao com [[P100_Custo de Produção - CLT_2021  - 9 de agosto de 2021 (CERES)]], ingestao de `Levantamento de custos de Producao P100x2.xlsx`, `PIO-MGG-019` e `PIO-MGG-039`.

## Analises Consolidadas

### Inventario tecnico e documental

- **B1 / Valdemiro:** mapeou a v9, as premissas historicas de rendimento e as lacunas de escala, especialmente separacao em 200 L e ciclo real.
- **B2 / Cacilda:** diagnosticou `Products/MGg3/MGg2/Custos/`, destilou o padrao `MGG3-LEV-P100-vN_...`, confirmou a v9 como referencia intocada e indicou v10 como nova versao canonica.

### Premissas tecnicas e indiretos

- **C1 / Valdemiro:** separou Desenvolvimento e Producao, fechou a convencao de rendimento como % em massa relativa ao grafite seco alimentado e definiu o residual como fracao fisica sem receita no caso-base.
- **C2 / Eloi:** consolidou benchmark de indiretos empresariais para Producao, com faixa sensivel entre minimo, medio e maximo.

### Modelos economicos

- **D1 / Julio:** modelou Desenvolvimento por capacidade tecnica, campanha e lote a la carte; nao por OPEX dividido por 522 lotes nominais.
- **D2 / Julio:** modelou Producao com equipe fixa, OPEX mensal e tres condicoes de rendimento; alocacao por massa ponderada GPC=4, NPG=2, Nanografite=1.
- **E / Julio:** comparou os cenarios e ranqueou sensibilidades: indiretos C2, NPG, Nanografite, cadencia D1 e GPC.
- **F / Carmen:** reescreveu o relatorio unico em linguagem tecnico-executiva para investidor.
- **G / Cacilda:** revisou coerencia, validou a organizacao no Vault, consolidou esta nota-mae e registrou a recomendacao final.

## Matriz de Decisao

| Recomendacao | Por que | Com quem | Ate quando |
|---|---|---|---|
| Apresentar Desenvolvimento e Producao lado a lado | Os cenarios respondem perguntas economicas diferentes e nao devem ser misturados | Rodrigo | Antes do envio ao investidor |
| Usar media historica v9 como caso-base D2 | Conservadora e otimista funcionam como banda de defesa, nao como base unica | Rodrigo / Julio | Na revisao executiva |
| Manter equipe v9 de 8 pessoas em D1 | A equipe fixa do briefing pertence ao Cenario Producao; usar essa equipe em D1 subestimaria o piloto tecnico | Rodrigo / Valdemiro | Decisao ja validada |
| Manter OPEX D2 igual nas tres condicoes | A estrutura operacional e a mesma; muda a massa por produto e o R$/kg | Rodrigo / Julio | Decisao ja validada |
| Manter recomendacao sobre cenarios mistos no corpo | E guidance de uso para investidor, nao premissa numerica | Rodrigo | Decisao ja validada |
| Tratar fontes externas faltantes como pendencia controlada | As fontes ainda nao estao formalmente ingeridas no Vault | Cacilda / time documental | Antes de due diligence |

## Riscos e Cenarios Alternativos

- **Cenario base:** v10 apresentada como leitura economica para investidor, com D1 e D2 separados.
- **Cenario conservador:** usar rendimentos conservadores em Producao e faixa alta de indiretos C2; custo unitario e OPEX sobem.
- **Cenario otimista:** rendimentos melhoram, especialmente NPG e Nanografite; custo unitario cai, mas depende de validacao experimental.
- **O que mudaria a recomendacao:** preco de venda validado, offtake/pre-venda por produto, RFQs reais, regime tributario e estrutura administrativa.

## Proximos Passos

- [ ] Rodrigo revisar a v10 e decidir envio ao investidor — Rodrigo — imediato.
- [ ] Reconciliar folha carregada, CQ externo, manutencao, insumos, utilidades e custo marginal com RFQs e CERES 2021 — Julio/CFO — antes de uso contratual.
- [ ] Ingerir `Levantamento de custos de Producao P100x2.xlsx`, `PIO-MGG-019` e `PIO-MGG-039` — Cacilda/documental — antes de due diligence.
- [ ] Validar as tres condicoes de rendimento por campanha de balanco gravimetrico pos-recomissionamento — Valdemiro/operacao — antes de comprometer ramp-up.
- [ ] Definir estrutura societaria, regime tributario e papel diretor/gerente — Rodrigo — antes de fechar modelo financeiro de banco.
- [x] Corrigir frontmatter das skills `sinalizar-bloqueio` e `checklist-pre-entrega` com campo `description` — Cacilda — concluido nesta rodada para evitar nova falha de carregamento do runtime.

## Rastreabilidade

- Issue-mae: ALT-440.
- Issues filhas: ALT-442 (B1), ALT-443 (B2), ALT-444 (C1), ALT-445 (C2), ALT-446 (D1), ALT-447 (D2), ALT-448 (E), ALT-449 (F), ALT-450 (G).
- Documento final: [[MGG3-LEV-P100-v10_Levantamento-Custos-Cenarios-Desenvolvimento-Producao-Consolidado]].
- Base historica: [[MGG3-LEV-P100-v9_Levantamento-Custos-Recomissionamento-Consolidado]].
- Planilha historica: [[P100_Custo de Produção - CLT_2021  - 9 de agosto de 2021 (CERES)]].
