---
title: LEV-P100 Plentz-08 — Nota-Mãe
type: Case Summary
case_id: ALT-491
date: 2026-05-31
author: Cacilda
status: concluido
root:
  - "[[MGgrafeno]]"
documento_final: "[[MGG3-LEV-P100-v11_Levantamento-Custos-Cenarios-Desenvolvimento-Producao-Investidor-Consolidado]]"
documento_base: "[[MGG3-LEV-P100-v10_Levantamento-Custos-Cenarios-Desenvolvimento-Producao-Consolidado]]"
issue_mae: [ALT-491](mention://issue/12a23097-71ce-45a0-913a-b11e25b1d0ac)
issue_versionamento: [ALT-498](mention://issue/0d6d34f2-35aa-4770-aa78-44a4b77b46e6)
tags:
  - case
  - mggrafeno
  - lev-p100
  - nota-mae
  - plentz-08
---

# LEV-P100 Plentz-08 — Nota-Mãe

## Síntese Executiva

A Revisão Plentz-08 (ALT-491) transformou o relatório LEV-P100 em uma peça com porta de entrada explícita para o investidor IFHAN. A v11 preserva a [[MGG3-LEV-P100-v10_Levantamento-Custos-Cenarios-Desenvolvimento-Producao-Consolidado|v10 Plentz-07]] como base histórica e acrescenta a seção §2-A, logo após o resultado consolidado, com o cheque necessário para a P100 funcionar no Ano 1.

O número central para decisão é **R$ 5,73 MM no caso-base**, com faixa defensável de **R$ 4,99 MM a R$ 6,57 MM**. Esse cheque inclui CAPEX de recomissionamento, OPEX Desenvolvimento do Ano 1 e capital de giro; **não inclui** licenciamento CDTN/UFMG, que fica separado via edital de oferta tecnológica e com exigência de exclusividade pelo IFHAN.

A revisão também corrige a leitura de ocupação em §6.6: Ano 1 sem locação e sem condomínio; Ano 2+ com locação de **R$ 10 mil/mês** (R$ 120k/ano). Energia, manutenção e reparos de escopo condominial não foram somados de novo, porque já estão absorvidos por §6.4 e §6.5.

## Dados do Caso

- **Contexto:** MGgrafeno / P100. Fechamento da seção dedicada ao investidor IFHAN no relatório de custos.
- **Issue-mãe:** [ALT-491](mention://issue/12a23097-71ce-45a0-913a-b11e25b1d0ac).
- **Documento final:** [[MGG3-LEV-P100-v11_Levantamento-Custos-Cenarios-Desenvolvimento-Producao-Investidor-Consolidado]].
- **Base preservada:** [[MGG3-LEV-P100-v10_Levantamento-Custos-Cenarios-Desenvolvimento-Producao-Consolidado]].
- **Mudança principal:** inclusão de §2-A como abertura de plano de negócios do investidor, mais atualização de §6.6.

## Matriz de Decisão

| Decisão | Posição Plentz-08 | Justificativa |
|---|---|---|
| Cheque do Ano 1 | R$ 5,73 MM base; faixa R$ 4,99–6,57 MM | Soma CAPEX recomissionamento + OPEX Desenvolvimento + capital de giro; número rastreável a §5, §6.6 e §8.5 |
| Ocupação CDTN Ano 1 | R$ 0 | Sem locação e sem condomínio; energia já está no OPEX e reparos estão cobertos por manutenção/utilidades |
| Ocupação CDTN Ano 2+ | R$ 120k/ano | Locação de R$ 10 mil/mês, sem reajuste; sem condomínio autônomo salvo obrigação contratual distinta comprovada |
| Licenciamento CDTN/UFMG | Fora do cheque do Ano 1 | IFHAN paga à parte via edital de oferta tecnológica e exige exclusividade |
| Narrativa de investimento | Opção estratégica exclusiva, não promessa comercial | Racional IFHAN: materiais avançados, eficiência energética, cobre-grafeno e controle estratégico |
| Uso do relatório | Planejamento e negociação técnico-financeira | Mantém pendências de RFQ, vistoria, SAT e gates SSMA antes de orçamento executivo/contrato |

## Rastreabilidade das Filhas

| Issue | Frente | Entrega usada na v11 |
|---|---|---|
| [ALT-492](mention://issue/25873de5-ef7f-4ae9-9e2e-ea14d0acac71) | Premissas jurídicas | Ano 1 sem locação; licenciamento separado; exclusividade como premissa do equity story |
| [ALT-493](mention://issue/44de1e29-24a8-47ae-9eaf-f6dbae232738) | Dossiê IFHAN | Tese do investidor, ligação com energia/CES, régua US$ 50–200/kg e ângulo cobre-grafeno |
| [ALT-494](mention://issue/cc707c53-96db-4036-b8a3-a9e6aa57ac11) | Ocupação CDTN | Linha Ano 1 = R$ 0; Ano 2+ = R$ 120k/ano; regra anti-dupla-contagem com §6.4/§6.5 |
| [ALT-495](mention://issue/fdd8dbc3-5dfa-4ebd-b91b-95610c3516ba) | Modelo financeiro | Cheque IFHAN Ano 1: R$ 5,73 MM base, faixa R$ 4,99–6,57 MM, curva de caixa e sensibilidades |
| [ALT-496](mention://issue/622152af-0851-4330-b1a3-c91732aff0ae) | Equity story | Narrativa de opção estratégica exclusiva para IFHAN, com cobre-grafeno como aplicação prioritária |
| [ALT-497](mention://issue/cacde773-f920-4da7-ada8-1c074261874d) | Redação da seção | Texto integrado da seção §2-A, pronto para drop-in no relatório |
| [ALT-498](mention://issue/0d6d34f2-35aa-4770-aa78-44a4b77b46e6) | Versionamento e coerência | Publicação da v11/Plentz-08, atualização §6.6, changelog e esta nota-mãe |

## Próximos Passos

- [ ] Rodrigo revisar a v11 antes de envio externo ao IFHAN.
- [ ] Confirmar licenciamento CDTN/UFMG por edital e exclusividade antes de qualquer termo vinculante.
- [ ] Executar RFQs, vistoria física, SAT e gates SSMA antes de transformar a estimativa em orçamento executivo.
- [ ] Manter separadas as leituras: cheque do Ano 1 (§2-A), OPEX Desenvolvimento (§8) e projeção Produção/Anexo A (§9).
