---
titulo: Processo de Referencia para Levantamento de Custos
tipo: nota-canonica-lote
produto: MGg3
fase: MGg2
lote: 20210720Pa
campanha: Duda
status: canonico-inicial
confidencialidade: interno
created: 2026-05-20
updated: 2026-05-21
tags:
  - MGg3
  - MGg2
  - custos
  - lote-referencia
  - balanco-de-massa
---

# Processo de Referencia para Levantamento de Custos

## Identificacao

Esta nota consolida o ponto de referencia do lote `20210720Pa`, usado como processo-base para leitura de custos e balanco de massa da planta piloto MGgrafeno.

| Campo | Valor |
|---|---|
| Lote | `20210720Pa` |
| Campanha | Duda |
| Escala | P100 |
| Concentracao | 100 g/L |
| Carga de grafite | 10 kg, conforme padrao P100 |
| Equipamento de conversao | KonMix |
| Tempo de conversao | 5 h |
| Funcao no Vault | Eixo de rastreabilidade para custo/kg, rendimento por etapa e representatividade do lote |

## Fontes relacionadas

- [[MGG2-CTRL01_Controle-de-producoes]]
- [[MGG2-CTRL02_Volumes-quantidade-processadas]]
- [[MGG2-CTRL03_Balanco-Global-PPTX]]
- [[MGG2-CTRL04_Controle-de-Processos-2022]]
- [[MGG2-CTRL05_Balanco-Global-XLSX]]
- [[MGG2-CTRL06_Controle-documentos-processo-continuo]]
- [[MGG2-ANEXOA-BMG_Balanco-Massa-Global-PDF]]
- [[../../Descricao da Tecnologia/Parametros criticos PL100 e acabamento|Parametros criticos PL100 e acabamento]]
- [[../../Descricao da Tecnologia/Mapa de processo e correntes MGgrafeno|Mapa de processo e correntes MGgrafeno]]
- [[../../Descricao da Tecnologia/MGG2-ANEXOA-RELII_Rota-100gL-KonMix|Anexo A - Relatorio Ano II rota 100 g/L KonMix]]

## Validacao Anexo A - ALT-301

| Categoria | Registro |
|---|---|
| Dado observado | O lote `20210720Pa` esta rastreado no [[MGG2-ANEXOA-BMG_Balanco-Massa-Global-PDF]] como `AUMENTO DE CARGA 100 g/L DO KonMix 5 HORAS - CAMPANHA DUDA`, p. 15-16. |
| Premissa tecnica | `100 g/L` e mantido como concentracao nominal/rotulo operacional; quando o XLSX for usado, preservar a concentracao calculada separadamente. |
| Inferencia | O ganho defensavel para pitch tecnico e tempo/capacidade de conversao frente a `50 g/L 24 h`, nao rendimento percentual superior. |
| Lacuna | Representatividade estatistica do lote segue limitada, especialmente porque a rota usa decantacao estatica + discos, enquanto lotes posteriores usam decanter + discos. |
| Conflito | Nanografite/nanoplaca representa a maior massa do lote, mas nao deve ser declarada produto final comercial sem especificacao, acabamento/reprocesso e OPEX. |

## Regra de uso

- Usar esta nota como destino canonico para referencias ao lote `20210720Pa`.
- Nao usar links antigos para `Projects/MGgrafeno/Planta Piloto/...`; a camada tecnica do MGg2 fica em `Products/MGg3/MGg2`.
- Nao transformar o lote `20210720Pa` em premissa financeira final sem reconciliar os dados entre PPTX, XLSX, controle de producoes, volumes processados e parametros criticos.
- Claims de `triplicar producao` e `reducao 24x` devem permanecer como cenario/risco de comunicacao, nao como dado observado.

## Pendencias tecnicas

| Pendencia | Impacto |
|---|---|
| Representatividade do lote frente aos demais lotes Duda | Afeta o uso do lote como baseline de custo/kg. |
| Reconciliacao entre `Balanço Global.pptx` e `Balanço Global.xlsx` | Evita premissa financeira baseada em fonte isolada. |
| Custos unitarios de insumos, energia, HH, descarte e CQ | Necessarios para transformar massa/rendimento em custo de producao. |
| Diferenca entre rota estatica/discos e rota decanter/discos | Precisa ser preservada para nao comparar produtos com rotas distintas. |

## Status

Criada em saneamento da ALT-286 para substituir links antigos que apontavam para uma pasta inexistente em `Projects/MGgrafeno/Planta Piloto`.
