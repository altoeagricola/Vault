---
titulo: Balanco Global XLSX
tipo: registro-operacional
produto: MGg3
fase: MGg2
status: extraido
confidencialidade: interno
fonte: Balanço Global.xlsx
periodo_coberto: 2021-01 a 2022-02
lote_referencia: 20210720Pa
created: 2026-05-20
updated: 2026-05-21
tags:
  - MGg3
  - MGg2
  - custos
  - balanco-de-massa
---

# Balanco Global XLSX

## Fonte original

- Arquivo no Vault: `Balanço Global.xlsx`
- Origem externa: `/Users/okumaaltoe/Documents/MGgrafeno 3.0/EVT-MGg3/Ingestao 20Maio2026/Controle_de_lotes/Balanço Global.xlsx`
- Estrutura: 30 abas, uma por lote/balanço.

## Escopo e periodo coberto

Planilha de balanço de massa por lote, cobrindo de `20210118Pa` a `20220221Pa`. Cada aba traz insumos, massas/volumes, concentração, produtos intermediários/finais, massa de sólidos, perdas e rendimentos calculados.

## Lote 20210720Pa

A aba `20210720Pa` é a fonte estruturada do lote [[Products/MGg3/MGg2/Custos/Controle operacional de lotes/Processo-Referencia-Levantamento-de-Custos|20210720Pa]], definido como referência de custos.

| Item | Valor |
|---|---:|
| H2O | 100,000 kg; 100,220 L |
| Aditivo | 0,10049 kg; 0,093916 L |
| Grafite | 10,015 kg; 4,552 L |
| Total inicial | 110,11549 kg; 104,86667 L |
| Concentração calculada | 95,502 g/L |
| Dispersão | 108,81549 kg |
| Diferença | 10,74549 kg |
| Perda total | 0,97730 kg |
| Grafite após correção | 9,89677 kg |

## Saídas e rendimentos do 20210720Pa

| Fração | Sólidos | Rendimento |
|---|---:|---:|
| Grafeno A | 0,05124 kg | 0,5176% |
| Grafeno B | 0,48050 kg | 4,8535% |
| Nanoplaca | 9,27279 kg | 93,6645% |
| Total | 9,80453 kg | 99,0357% |
| Perda de sólidos | 0,09547 kg | 0,9643% |

## Observacoes operacionais

- O balanço registra NH4OH no bloco de insumos/meio.
- A separação contém decantação/estática e discos, coerente com o registro da apresentação.
- Há amostras/testemunhos e descarte de amostragem registrados, relevantes para fechar massa antes de cálculo de custo/kg.

## Metricas economicas identificaveis

- Consumo de água, aditivo e grafite por lote.
- Massa seca produzida por fração.
- Rendimento por fração e perda de sólidos.
- Base direta para custo/kg do lote [[Products/MGg3/MGg2/Custos/Controle operacional de lotes/Processo-Referencia-Levantamento-de-Custos|20210720Pa]], desde que Mariano aplique preços de insumos, energia, HH e descarte.

## Lacunas

- Não há custo monetário, tempo de mão de obra, energia ou preço unitário.
- O campo de concentração calculada (95,502 g/L) difere do rótulo operacional 100 g/L; tratar como diferença entre nominal e calculado.
- A pasta externa citava `Balanco_Massa_Global.pdf`; nesta trilha foram ingeridos o XLSX/PPTX disponíveis em `Controle_de_lotes`.

## Complemento Anexo A PDF - ALT-301

| Categoria | Registro |
|---|---|
| Dado observado | [[MGG2-ANEXOA-BMG_Balanco-Massa-Global-PDF]] confirma o mesmo eixo do lote `20210720Pa` em fonte PDF auditavel: Campanha Duda, KonMix, 5 h, NH4OH, separacao estatica + discos. |
| Premissa tecnica | O XLSX continua sendo a fonte preferida para calculos; o PDF e a fonte de apresentacao/rastreabilidade por pagina. |
| Inferencia | O ganho defensavel da rota 100 g/L KonMix e capacidade temporal de conversao, mantendo cuidado com rendimento percentual. |
| Lacuna | Ainda faltam energia, HH, agua de lavagem, descarte, CQ e acabamento por produto para TEA/OPEX. |
| Conflito | Preservar `95,502 g/L` como concentracao calculada do XLSX e `100 g/L` como rotulo operacional nominal. |
