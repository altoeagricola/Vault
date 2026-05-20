---
titulo: Controle de Processos 03_03_2022
tipo: registro-operacional
produto: MGg3
fase: MGg2
status: extraido
confidencialidade: interno
fonte: Controle de Processos 03_03_2022.xlsx
periodo_coberto: 2017-10 a 2022-03
lote_referencia: 20210720Pa
created: 2026-05-20
updated: 2026-05-20
tags:
  - MGg3
  - MGg2
  - custos
  - processo
---

# Controle de Processos 03_03_2022

## Fonte original

- Arquivo no Vault: `Controle de Processos 03_03_2022.xlsx`
- Origem externa: `/Users/okumaaltoe/Documents/MGgrafeno 3.0/EVT-MGg3/Ingestao 20Maio2026/Controle_de_lotes/Controle de Processos 03_03_2022.xlsx`
- Estrutura: 21 abas, incluindo banco de dados, capacidade produtiva, rendimentos P100, controles de pH, condutividade, vazão, análises de água e outliers.

## Escopo e periodo coberto

Controle técnico de processo da planta piloto. A aba `Planilha2` traz 100 registros estruturados entre `20171003Pa` e `20210810Pa`; a aba `Banco de dados` replica/expande o cadastro em formato maior. As abas de controle estatístico avaliam rendimento, resíduos, teor de umidade, aditivo, pH, condutividade e vazão.

## Capacidade produtiva indicada

| Fração | Rendimento médio | kg/lote | kg/mês | kg/ano |
|---|---:|---:|---:|---:|
| Grafeno de poucas camadas | 0,4586% | 0,045407 | 0,394284 | 4,731409 |
| Nanoplaca de grafeno | 3,6527% | 0,361678 | 3,140573 | 37,686871 |
| Nanografite | 86,6177% | 8,577614 | 74,482284 | 893,787414 |

## Lote 20210720Pa

O lote [[Projects/MGgrafeno/Planta Piloto/Processo-Referencia-Levantamento-de-Custos|20210720Pa]] aparece no banco de dados, na aba `Planilha2`, nas abas de água/pH/condutividade e em `Rendimentos -P100`.

| Campo | Valor |
|---|---|
| Código | 103 |
| Tanque | Inox, 100 L |
| Tempo de conversão | 5 h |
| Configuração | Simples |
| Cisalhador | Konmix / KonMix-138 |
| Rotor-estator | Furos quadrados |
| Rotação | 3.550 rpm |
| Grafite | 10.000 g a 10.015 g; razão 100 g/L |
| Aditivo | Titon X-100; 100 g; 0,1% m/m no meio líquido |
| Base / meio | NH4OH |
| 1ª separação | Estática |
| 2ª separação | Discos |
| Vazão discos | 55,2 L/h |
| pH água / ajuste | 7,6 / 10,6 |
| Condutividade inicial | 3,8 |
| Rendimento P100 | 0,211682%; média das médias 0,894576; LSC 1,599850; LIC 0,189302; amplitude 0,423365 |

## Controles de processo relevantes

| Aba | Uso para custo/TEA |
|---|---|
| `Rendimentos -P100` | Base para rendimento de grafeno em P100 e detecção de lote fora de controle |
| `Padrão 2021_RP%` | Controle estatístico de rendimento de processo |
| `Padrão 2021_Resíduos%` | Estimativa de resíduo/perda |
| `Padrão 2021_TU%` | Teor de umidade por fração |
| `Padrão 2021_Aditivo%` | Consumo relativo de aditivo |
| `Controle-pH` | pH inicial, pH ajustado e pH de correntes de separação |
| `Condutividade` / `Controle de condutividade` | Condutividade nas etapas de processo |
| `Vazão` | Vazão e temperatura para lotes P100 contínuos |

## Metricas economicas identificaveis

- Rendimento por fração e capacidade anual indicada são as métricas mais próximas de premissas econômicas.
- Consumo de grafite, aditivo e base por lote aparece de forma estruturada para o lote [[Projects/MGgrafeno/Planta Piloto/Processo-Referencia-Levantamento-de-Custos|20210720Pa]].
- Vazão de separação e tempo de conversão permitem estimar gargalo operacional, mas ainda faltam consumo energético e HH.

## Lacunas

- A planilha não contém preços, custo/kg, CAPEX, OPEX monetário ou custo de descarte.
- Algumas abas são controles estatísticos, não tabelas normalizadas; usar filtros com cuidado.
- Há divergência de escrita do aditivo (`Titon`/`Triton` X-100) que deve ser saneada antes de compra/cotação.
