---
titulo: Controle de producoes MGgrafeno
tipo: registro-operacional
produto: MGg3
fase: MGg2
status: extraido
confidencialidade: interno
fonte: Controle de produções.xlsx
periodo_coberto: 2017-10 a 2022-03
lote_referencia: 20210720Pa
created: 2026-05-20
updated: 2026-05-20
tags:
  - MGg3
  - MGg2
  - custos
  - controle-de-lotes
---

# Controle de producoes MGgrafeno

## Fonte original

- Arquivo no Vault: `Controle de produções.xlsx`
- Origem externa: `/Users/okumaaltoe/Documents/MGgrafeno 3.0/EVT-MGg3/Ingestao 20Maio2026/Controle_de_lotes/Controle de produções.xlsx`
- Estrutura: abas `Produção`, `Acabamento`, `Formularios`, `Planilha1`.

## Escopo e periodo coberto

Registro mestre de lotes produzidos na planta piloto, cobrindo 127 registros de produção entre `20171003Pa` e `20220307Pa`. A planilha organiza lote, piloto, concentração, campanha, descrição operacional, objetivo, etapa de acabamento e formulários de análise.

## Lotes e campanhas

| Recorte | Dado extraido |
|---|---|
| Total de registros de produção | 127 lotes |
| Pilotos mais frequentes | P100: 44; P25: 26; P100-2: 24; P50: 20; P100-1: 9 |
| Concentrações registradas | 50 g/L e 100 g/L dominam a base; há um lote 75 g/L |
| Campanhas recorrentes | Otto, Prod. Cont. Camp. 01, Ana, BERTHA, KATRINA, Duda |
| Formularios | 127 linhas; traz códigos de formulários de conversão, separação e acabamento quando disponíveis |

## Lote 20210720Pa

O lote [[Products/MGg3/MGg2/Custos/Controle operacional de lotes/Processo-Referencia-Levantamento-de-Custos|20210720Pa]] aparece como registro P100, 100 g/L, campanha Duda.

| Campo | Valor |
|---|---|
| Lote | 20210720Pa |
| Piloto | P100 |
| Concentração | 100 g/L |
| Campanha | Duda |
| Equipamento / condição | Konmix 3.550 rpm, tanque inox, troca de base para NH4OH |
| Objetivo | Teste de aumento de carga de grafite 100 g/L; 5 h; decantação estática; discos 55 L/h |
| Formulários associados | 185, 192, 220 |

## Campanha Duda

| Lote | Piloto | Concentração | Condição operacional | Observação |
|---|---|---|---|---|
| 20210719Pa | P100 | 100 g/L | Konmix 3.550 rpm / NH4OH | 5 h; decanter em várias condições |
| [[Products/MGg3/MGg2/Custos/Controle operacional de lotes/Processo-Referencia-Levantamento-de-Custos|20210720Pa]] | P100 | 100 g/L | Konmix 3.550 rpm / NH4OH | 5 h; decantação estática; discos 55 L/h |
| 20210729Pa | P100 | 100 g/L | Konmix 3.550 rpm / NH4OH | 5 h; decanter 100G, 50 L/h; discos 55 L/h |
| 20210810Pa | P100 | 100 g/L | Konmix 3.550 rpm / NH4OH | 5 h; decanter 100G, 30 L/h; discos em várias vazões |
| 20210816Pa | P100 | 100 g/L | Konmix 3.550 rpm / NH4OH | 5 h; decantação estática; discos 64,8 L/h; recuperação s02 |

## Metricas economicas identificaveis

- A planilha não traz custo monetário, preço de insumo ou custo/kg.
- Métricas úteis para Mariano: volume nominal por piloto, concentração por lote, tempo/condição de processo por descrição, campanha e rastreio de formulário.
- O lote [[Products/MGg3/MGg2/Custos/Controle operacional de lotes/Processo-Referencia-Levantamento-de-Custos|20210720Pa]] deve ser cruzado com `Balanço Global.xlsx`, `Balanço Global.pptx`, `Controle de Processos 03_03_2022.xlsx` e `Volumes e quantidade processadas.xlsx` antes de virar premissa financeira.

## Lacunas

- A aba `Produção` registra o processo em texto livre; não substitui o balanço de massa.
- Não há colunas de consumo energético, custo de mão de obra, custo de insumo ou rendimento consolidado.
- A representatividade do lote 20210720Pa precisa ser validada contra os demais lotes Duda e contra a campanha posterior de produção contínua.
