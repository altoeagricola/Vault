---
titulo: Volumes e quantidade processadas MGgrafeno
tipo: registro-operacional
produto: MGg3
fase: MGg2
status: extraido
confidencialidade: interno
fonte: Volumes e quantidade processadas.xlsx
periodo_coberto: 2017-10 a 2022-02
lote_referencia: 20210720Pa
created: 2026-05-20
updated: 2026-05-20
tags:
  - MGg3
  - MGg2
  - custos
  - volumes
---

# Volumes e quantidade processadas MGgrafeno

## Fonte original

- Arquivo no Vault: `Volumes e quantidade processadas.xlsx`
- Origem externa: `/Users/okumaaltoe/Documents/MGgrafeno 3.0/EVT-MGg3/Ingestao 20Maio2026/Controle_de_lotes/Volumes e quantidade processadas.xlsx`
- Estrutura: abas `Ano`, `Mes`, `2021`, `Planilha1`.

## Escopo e periodo coberto

Consolida quantidade de lotes, volume processado e estimativas de grafeno produzido. A base cobre a produção histórica desde 2017 e traz recorte específico de 2021, ano da campanha Duda e do lote [[Projects/MGgrafeno/Planta Piloto/Processo-Referencia-Levantamento-de-Custos|20210720Pa]].

## Volumes por ano

| Ano | Qtd. lotes | Volume processado |
|---|---:|---:|
| 2017 | 10 | 475 L |
| 2018 | 29 | 2.335 L |
| 2019 | 12 | 1.100 L |
| 2020 | 8 | 700 L |
| 2021 | 49 | 4.150 L |

## Configuração de linha

| Configuração | Quantidade | Volume |
|---|---:|---:|
| P5 | 2 | 10 L |
| P25 | 22 | 550 L |
| P50 | 17 | 850 L |
| P100 | 38 | 3.800 L |

## Fatores de produção indicativos

| Escala | Massa estimada de grafeno por lote |
|---|---:|
| 5 L | 1,6 g |
| 10 L | 3,2 g |
| 25 L | 2,1 g |
| 50 L | 14 g |
| 100 L (2018) | 120 g |
| 100 L (2019) | 44 g |
| 100 L (2021) | 44 g |

## Lote 20210720Pa

O lote [[Projects/MGgrafeno/Planta Piloto/Processo-Referencia-Levantamento-de-Custos|20210720Pa]] aparece nas abas `Mes` e `2021` como P100, 100 L, 100 g/L, campanha Duda, com Konmix 3.550 rpm em tanque inox e troca de base NH4OH.

Na aba `Mes`, a descrição do lote aponta: teste de aumento de carga de grafite 100 g/L; 5 h; decanter em várias condições. Na aba `2021`, o mesmo registro aparece no recorte anual.

## Metricas economicas identificaveis

- A planilha fornece denominadores para custo por lote, custo por litro processado e custo por kg estimado.
- O fator de 100 L em 2021 indica 44 g de grafeno por lote na planilha de volume. Esse valor precisa ser reconciliado com o balanço de massa do lote [[Projects/MGgrafeno/Planta Piloto/Processo-Referencia-Levantamento-de-Custos|20210720Pa]], que detalha grafeno A, grafeno B e nanoplaca.
- O volume anual de 2021 (4.150 L) é o principal recorte para estimar escala piloto em ano com campanha Duda.

## Lacunas

- Os fatores de massa por escala parecem ser estimativas agregadas; não substituem o rendimento medido por lote.
- Não há custo monetário, consumo energético, HH, preço de insumo ou custo de descarte.
- A aba mensal mistura histórico completo e recortes por ano; usar com cuidado para não duplicar volume.
