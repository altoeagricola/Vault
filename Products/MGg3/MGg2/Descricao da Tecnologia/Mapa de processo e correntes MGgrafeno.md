---
titulo: Mapa de processo e correntes MGgrafeno
tipo: mapa-processo
produto: MGg3
subproduto: MGg2
fonte_base: "[[KNOW-HOW-55.1-2024_Producao-de-Grafeno]]"
status: canonico-inicial
confidencialidade: interno
atualizado: 2026-05-21
---
# Mapa de processo e correntes MGgrafeno

## Leitura executiva

A tecnologia MGgrafeno organiza a producao em quatro modulos: conversao, separacao, acabamento e tratamento de residuos. A corrente critica para custo e balanco de massa e `c31`, a suspensao mae resultante da conversao. A partir dela, a separacao gera fracoes de produto: NG/NP, GPC e NPG.

## Modulos

| Modulo | Funcao | Saidas relevantes |
|---|---|---|
| Conversao | Delaminar/esfoliar grafite em fase liquida por cisalhamento, com agua e aditivo. | `c31`, suspensao mae contendo GPC, NPG e NG. |
| Separacao | Fracionar os materiais produzidos por decanter e por centrifuga de discos, preservando a origem da corrente. | `d01`, `d02`, `d03`, `d04` e aliases `s02/s03/s04`. |
| Acabamento | Secagem, concentracao, diafiltracao e troca de aditivo. | GPC seco por spray dryer ou liofilizacao, NPG seco, NG seco, GPC-C, GPC-BF. |
| Residuos / SSMA | Tratamento de residuos, monitoramento ambiental e agua para reuso. | Solido retido, filtrado tratado, agua de reuso, residuos externos e evidencias de compliance. |

## Correntes e produtos

| Codigo | Nome controlado | Tipo | Origem | Observacao |
|---|---|---|---|---|
| `c31` | Suspensao mae pos-conversao | intermediario | Modulo de conversao | Alimenta a primeira separacao; contem GPC, NPG e NG dispersos. |
| `d01` | Suspensao intermediaria pos-decanter | intermediario | Centrifuga decanter | Contem GPC + NPG em suspensao para segunda separacao. |
| `d02` | NG / Nanoplacas de Grafite / Nanografite | produto/subproduto | Torta umida da decanter | Produto de maior espessura; tambem aparece como `s02` na rota de discos. |
| `d03` | GPC / Grafeno de Poucas Camadas / Grafeno A | produto | Separacao apos rota com decanter | Produto alvo abaixo de 10 camadas; tambem aparece como `s03`. |
| `d04` | NPG / NanoPlaca de Grafeno / Grafeno B | produto | Separacao apos rota com decanter | Produto intermediario entre GPC e NG; tambem aparece como `s04`. |
| `s02` | NG / Nanografite | alias de rota | Centrifuga de discos | Manter como alias, nao como produto novo. |
| `s03` | GPC | alias de rota | Centrifuga de discos | Manter como alias, nao como produto novo. |
| `s04` | NPG | alias de rota | Centrifuga de discos | Manter como alias, nao como produto novo. |

## Produtos derivados de acabamento

| Produto | Origem | Tratamento |
|---|---|---|
| GPC seco por spray dryer | GPC em dispersao | Secagem por spray dryer. |
| GPC seco por liofilizacao | GPC em dispersao | Liofilizacao. |
| NPG seco | NPG umido/pasta | Liofilizacao. |
| NG seco | NG/torta umida | Liofilizacao. |
| GPC-C | GPC em dispersao | Concentracao por filtracao tangencial. |
| GPC-BF | GPC em dispersao | Diafiltracao/reducao de surfactante ou troca de aditivo. |

## Correntes SSMA e residuos

Fonte primaria: [[MGG2-RTF-VOLV_SSMA-Tratamento-Residuos]].

| Codigo | Nome controlado | Tipo | Origem | Observacao |
|---|---|---|---|---|
| `ssma-lq1` | Residuo liquido tipo 1 | residuo liquido | Lavagem de tanques, utensilios, piso, lotes-teste e amostras | ~18.000 L tratados ate julho de 2019; agua/aditivo/nano; fluxo interno SSMA. |
| `ssma-lq2` | Residuo liquido tipo 2 | residuo liquido perigoso | Frente de aplicacoes | 246 L; solventes, enxofre e solucao acida com nano; incineracao SEGRE. |
| `ssma-sol1` | Residuo solido tipo 1 | residuo solido em matriz | EPIs, papeis e embalagens impregnadas | 40 kg; aterro sanitario Classe I. |
| `ssma-sol2` | Residuo solido tipo 2 | nanomaterial livre em po | Restos de amostras e nanomateriais soltos | 86 kg; incineracao SEGRE; cenario de maior risco fisico. |
| `ssma-fp-solido` | Solido retido no filtro prensa | solido retido/reprocessavel | Tratamento do residuo liquido tipo 1 | Mistura rica em Grafeno B e nanoplaca; potencial de reaproveitamento, ainda sem rota economica fechada. |
| `ssma-agua-reuso` | Agua tratada SSMA | agua de reuso | Filtro prensa, membranas, carvao, resina, UV/osmose | Uso interno defendavel; DBO/DQO e falso negativo Raman exigem ressalva. |

## Uso para custo e plano de negocios

- Custos devem ser agregados por modulo e depois alocados por corrente/produto.
- `c31` e o ponto de partida para rendimento de separacao; sem ele, o balanco de massa perde eixo.
- `d02/d03/d04` e `s02/s03/s04` nao devem virar produtos duplicados. Sao aliases/rotas de separacao que precisam preservar origem: `d` para decanter, `s` para centrifuga de discos.
- GPC-C e GPC-BF devem ser tratados como familias derivadas de acabamento, nao como substitutos simples de GPC.
- Para produtividade e custo, o baseline operacional continua `P100 KonMix 100 g/L 5 h`, conforme [[MGG2-RA2020-2021_Producao-Conversao-Separacao-Acabamento]]. Ensaios P25/Silverson Verso entram como desenvolvimento de parametros para conversao, nao como premissa financeira direta.

## Validacao Anexo A - ALT-301

| Categoria | Registro controlado |
|---|---|
| Dado observado | O PDF [[MGG2-ANEXOA-MAPA_Processos-Planta-Piloto-Rev05]] confirma a existencia de mapeamento formal Rev. 05 da planta piloto, com governanca de demanda, planejamento, caracterizacao, processo e residuos. |
| Dado observado | O PDF [[MGG2-ANEXOA-PROCFAB_Processo-Fabril-Piloto-2022]] reforca o fluxo conversao -> primeira separacao -> segunda separacao -> acabamento/caracterizacao/residuos. |
| Premissa tecnica | A taxonomia canonica desta nota continua em `Products/MGg3/MGg2/`; `Projects/MGgrafeno/` deve receber apenas vinculos de projeto atual quando houver decisao operacional. |
| Inferencia | O tratamento de residuos e CQ precisam entrar como modulos de custo/risco, porque aparecem no fluxo formal e nao sao apendices ambientais soltos. |
| Lacuna | O mapeamento de processo nao fecha massa, energia, HH, consumo de agua/lavagem ou rendimento por produto. |
| Conflito | Claims de nanografite como produto final devem preservar a distincao entre `d02/s02` como fracao maior/intermediaria e GPC/GPB como produtos de maior valor. |

## Validacao Volume V SSMA - ALT-309

| Categoria | Registro controlado |
|---|---|
| Dado observado | [[MGG2-RTF-VOLV_SSMA-Tratamento-Residuos]] confirma o modulo SSMA como fluxo operacional implementado, com classificacao, segregacao, tratamento interno, destinacao externa e monitoramento de ar. |
| Premissa tecnica | O solido retido no filtro prensa deve ser tratado como corrente potencialmente reaproveitavel, mas ainda sem especificacao comercial ou rota de reprocesso fechada. |
| Inferencia | A arquitetura de processo para TEA precisa incluir SSMA como modulo material: consumiveis, analises, HH, energia, perdas, destinacao e compliance. |
| Lacuna | A ausencia de balanco de massa ambiental impede transformar o Volume V em pacote de engenharia ambiental de escala. |

## Validacao Relatorio Anual 2020-2021 - ALT-308

| Categoria | Registro controlado |
|---|---|
| Dado observado | [[MGG2-RA2020-2021_Producao-Conversao-Separacao-Acabamento]] confirma a sequencia conversao -> separacao -> acabamento e detalha testes de decanter, filtracao tangencial, diafiltracao, secagem e custo. |
| Premissa tecnica | `P100 KonMix 100 g/L 5 h` e o baseline produtivo para capacidade/custo; P25/Silverson Verso e usado para desenvolvimento de parametros de conversao. |
| Inferencia | Nanografite permanece fracao relevante de massa e custo, mas nao deve ser promovida a produto comercial final sem especificacao, rota de acabamento/reprocesso e custo proprio. |
| Lacuna | A nota de mapa nao fecha energia especifica, perdas por gel/aditivo, qualidade comercial por produto nem custo de acabamento. |

## Alertas

- Links antigos do Vault que apontavam para `Projects/MGgrafeno/Planta Piloto/...` foram saneados na ALT-286 para o destino canonico do lote `20210720Pa`: [[Products/MGg3/MGg2/Custos/Controle operacional de lotes/Processo-Referencia-Levantamento-de-Custos|Processo de Referencia para Levantamento de Custos]].
- Validar divergencias do DOCX quando ele mencionar decantacao estatica ou rota alternativa para `s`. A regra controlada desta camada e `s` para centrifuga de discos.
