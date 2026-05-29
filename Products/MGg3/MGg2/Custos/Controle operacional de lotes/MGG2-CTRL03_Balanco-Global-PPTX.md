---
titulo: Balanco Global PPTX
tipo: apresentacao-operacional
produto: MGg3
fase: MGg2
status: extraido
confidencialidade: interno
fonte: Balanço Global.pptx
periodo_coberto: 2021-03 a 2022-02
lote_referencia: 20210720Pa
created: 2026-05-20
updated: 2026-05-21
tags:
  - MGg3
  - MGg2
  - custos
  - balanco-de-massa
---

# Balanco Global PPTX

## Fonte original

- Arquivo no Vault: `Balanço Global.pptx`
- Origem externa: `/Users/okumaaltoe/Documents/MGgrafeno 3.0/EVT-MGg3/Ingestao 20Maio2026/Controle_de_lotes/Balanço Global.pptx`
- Estrutura: 44 slides com balanços de massa por campanha/lote.

## Escopo e periodo coberto

Apresentação com balanços de massa de campanhas Ana, Duda, Nicolas e lotes KonMix subsequentes. Cobre principalmente 2021-03 a 2022-02, com foco em rendimento de processo, massa de grafeno A, grafeno B, nanoplaca de grafite e perda mássica total.

## Campanhas cobertas

| Campanha | Periodo / lotes | Observação |
|---|---|---|
| Ana | 20210301Pa a 20210622Pa | Validações Silverson, 50 a 100 g/L |
| Duda | 20210720Pa a 20210824Pa | KonMix, aumento de carga 100 g/L, troca de base NH4OH/NaOH |
| Nicolas | 20211025Pa a 20211206Pa | KonMix, P100, decanter/discos |
| Produção contínua | 20211214Pa a 20220214Pa | Lotes P100 com dados de rendimento e perda mássica |

## Lote 20210720Pa

O slide 15 define explicitamente o processo de referência: **Campanha Duda - Lote [[Products/MGg3/MGg2/Custos/Controle operacional de lotes/Processo-Referencia-Levantamento-de-Custos|20210720Pa]] - AUMENTO DE CARGA 100 g/L DO KonMix 5 HORAS**.

| Parâmetro | Valor |
|---|---|
| Equipamento | KonMix |
| Concentração | 100 g/L |
| Tempo de conversão | 5 h |
| Água | 100 kg |
| Aditivo | 0,1 kg |
| Base | NH4OH |
| Grafite | 10,01 kg |
| Separação | Decantação estática; discos 3600 rpm, 55 L/h |
| Grafeno A | 68,32 kg totais; 0,051 kg sólidos; 0,75 g/L; RP 0,52% |
| Grafeno B | 1,37 kg totais; 0,4805 kg sólidos; umidade 62,93%; RP 4,85% |
| Nanoplaca de grafite | 26,15 kg totais; 9,2728 kg sólidos; umidade 64,18%; RP 93,66% |
| Perda mássica total | 0,10 kg; 0,96% sobre grafite inicial |

## Comparativo Campanha Duda

| Lote | Condição | Grafeno A RP | Grafeno B RP | Nanoplaca RP | Perda mássica |
|---|---|---:|---:|---:|---:|
| [[Products/MGg3/MGg2/Custos/Controle operacional de lotes/Processo-Referencia-Levantamento-de-Custos|20210720Pa]] | KonMix 100 g/L, 5 h, estática/discos | 0,52% | 4,85% | 93,66% | 0,96% |
| 20210729Pa | KonMix 100 g/L, 5 h, decanter 50 L/h | 0,54% | 5,19% | 79,83% | 14,9% |
| 20210810Pa | KonMix 100 g/L, 5 h, decanter 30 L/h | 0,45% | 4,08% | 80,44% | 15,0% |
| 20210816Pa | KonMix 100 g/L, 5 h, estática/discos 64,8 L/h | 0,49% | 3,83% | 87,82% | 7,86% |

## Metricas economicas identificaveis

- Principal insumo mensurável: grafite inicial por lote (10,01 kg no 20210720Pa).
- Saídas úteis para custo/kg: massa seca de grafeno A, grafeno B e nanoplaca; rendimento por fração; perda mássica total.
- O lote [[Products/MGg3/MGg2/Custos/Controle operacional de lotes/Processo-Referencia-Levantamento-de-Custos|20210720Pa]] tem perda mássica muito menor que outros lotes Duda com decanter, ponto que Mariano deve testar antes de assumir representatividade.

## Lacunas

- Não há preço de insumo, energia, mão de obra, tempo de setup, limpeza ou custo de separação.
- O arquivo é apresentação; os números devem ser reconciliados com `Balanço Global.xlsx` antes de uso em modelo.

## Complemento Anexo A PDF - ALT-301

| Categoria | Registro |
|---|---|
| Dado observado | O PDF [[MGG2-ANEXOA-BMG_Balanco-Massa-Global-PDF]] preserva uma versao auditavel de 44 paginas do mesmo conjunto operacional, incluindo p. 15-16 para o lote `20210720Pa`. |
| Premissa tecnica | Para comunicacao tecnica, usar `100 g/L KonMix 5 h` como rotulo nominal rastreado ao lote, mantendo detalhes de NH4OH, decantacao estatica e discos. |
| Inferencia | A comparacao com `50 g/L 24 h` sustenta ganho de tempo/capacidade, nao aumento percentual de rendimento. |
| Lacuna | O PPTX/PDF nao substitui reconciliacao com XLSX para concentracao calculada, perdas e massa seca. |
| Conflito | Nanoplaca/nanografite majoritaria nao deve ser tratada como produto final vendavel sem especificacao e custo de reprocesso/acabamento. |
