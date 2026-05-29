---
titulo: Fornecedores de Insumos e Grafeno - Startup Grafeno
tipo: registro-documento
produto: MGg3
codigo_fonte: MGG3-FORN02
fonte_arquivo: "Fornecedores de Grafeno - Startup Grafeno.xlsx"
caminho_fonte: "Products/MGg3/MGg2/Fornecedores/Fornecedores de Grafeno - Startup Grafeno.xlsx"
nome_original: "Fornecedores de Grafeno.xlsx"
origem_local: "/Users/okumaaltoe/Documents/Startup Grafeno/Fornecedores de Grafeno.xlsx"
organizacao: Startup Grafeno / MGg3
tipo_documento: base de dados / matriz de fornecedores, insumos e utilidades
data_documento: 2023-2025
confidencialidade: interno
status_extracao: extraido_parcial
confianca_extracao: media
temas:
  - fornecedores de grafeno
  - insumos de producao
  - utilidades industriais
  - precificacao de insumos
  - cadeia de suprimento
  - custos P100 P500
produtos:
  - grafeno
  - grafite micronizado
  - graphene nanoplatelets
  - graphene oxide
  - reduced graphene oxide
riscos_uso:
  - cotacoes internas e dados comerciais nao devem ser divulgados externamente
  - valores misturam estimativas, consultas, compras e dados de estoque
  - familias de material distintas nao devem ser comparadas diretamente
  - nomes de fornecedores exigem normalizacao antes de criar Connections
  - precos podem estar defasados e dependem de volume, incoterm, frete, impostos e especificacao tecnica
links_relacionados:
  - "[[MGG3-FORN01_Fornecedores-grafeno]]"
  - "[[Benchmark internacional - fornecedores de grafeno]]"
  - "[[Custos de producao P100 P500]]"
  - "[[Saneamento custos P100 P500]]"
  - "[[Modelo de negocios MGgrafeno - orquestracao aplicada]]"
  - "[[Ecossistema brasileiro de grafeno]]"
  - "[[NanoXplore]]"
  - "[[Levidian]]"
  - "[[First Graphene]]"
  - "[[Versarien]]"
  - "[[HexoGraphene]]"
  - "[[Nanum]]"
  - "[[Thomas Swan]]"
  - "[[Universal Matter]]"
  - "[[Nacional de Grafite]]"
  - "[[Carbon Rivers]]"
  - "[[MstnLand]]"
atualizado: 2026-05-07
---
# MGG3-FORN02: Fornecedores de Insumos e Grafeno - Startup Grafeno

## Identificacao

| Campo | Valor |
|---|---|
| Arquivo original | `Fornecedores de Grafeno.xlsx` |
| Arquivo no Vault | `Fornecedores de Grafeno - Startup Grafeno.xlsx` |
| Origem | Pasta local `Startup Grafeno` |
| Aba | `Planilha1` |
| Linhas / colunas | 70 linhas, 15 colunas |
| Periodo das cotacoes | 2022-12 a 2025-06, com estimativas e consultas internas |
| Confidencialidade | Interno |
| Status | Extraido parcialmente; validacao externa de fornecedores concluida por Eloi; pendente reconciliacao de custos |

## Resumo executivo

Esta planilha complementa [[MGG3-FORN01_Fornecedores-grafeno]]. A fonte `MGG3-FORN01` cobre principalmente fornecedores/produtos de grafeno; esta fonte `MGG3-FORN02` adiciona uma camada anterior de insumos, utilidades e HH usada para custo de producao, alem de repetir/expandir a camada de fornecedores de grafeno.

Uso recomendado:

- alimentar a matriz de insumos e utilidades da leitura P100/P500;
- atualizar o saneamento de custos com valores de energia, agua/esgoto, gases, consumiveis e HH;
- validar fornecedores de grafeno, sem criar duplicidade em `Connections`;
- separar precos internos/cotacoes de fontes publicas verificadas.

## Estrutura da planilha

| Bloco | Codigos | Conteudo | Status |
|---|---:|---|---|
| Insumos, utilidades e HH | 6 a 26 | consumiveis, gases, energia, agua/esgoto, HH operador/tecnico/analista/pesquisador | extraido parcial |
| Fornecedores e produtos de grafeno | 27 a 67 | produtos NanoXplore, Levidian/CamGraph, First Graphene, Versarien, Thomas Swan, AGM, Nacional de Grafite, CR Nano, Graphene Production, MstnLand, HexoGraphene e Nanum | extraido parcial |
| Totais | 69 a 70 | total e valor agregado de preco original | uso pendente; depende de entender escopo do total |

Colunas principais: `Cod`, `Nome`, `Supplier`, `Status`, `Quotation Data`, `Original Price`, `USD Price`, `Taxes %`, `Quant.`, `purchase cost USD`, `Unit`, `Quantity/pack`, `Price/Unit`, `Comments`.

## Insumos, utilidades e HH

| Codigo | Item | Fornecedor/status | Data | Valor extraido | Uso recomendado |
|---:|---|---|---|---|---|
| 6 | Esferas de Zircônia, consumível dos moinhos | Estimado | 2023-08-01 | USD 8.163,27/kg; custo com 20% = USD 9.795,92/kg | consumível crítico de moagem; validar durabilidade e taxa de reposição |
| 7 | Cilindro N2 10 m3 refil | OxiMinas; consultado | 2022-12-01 | USD 32,65 por 10 m3; USD 3,27/m3 | utilidade/gás; atualizar cotação |
| 8 | CO2 | Consultado | 2023-11-20 | USD 2,04/kg | utilidade/gás; confirmar fornecedor |
| 9 | PET micronizado 1 ton | Resipol; consultado | 2022-12-01 | USD 918,37/t; USD 0,918/kg | insumo de aplicação; separar de insumo de produção de grafeno |
| 10 | Aditivo agente de expansão BT Sulfonol Mel, bombona 50 kg | Tanquimica; consultado | 2022-12-01 | USD 70,31 por 50 kg; USD 1,41/kg | insumo de formulação; validar especificação |
| 11-12 | Energia ENEL SP TUSD/TE | ENEL; tabela SP | 2023-11-20 | TUSD USD 0,0808/kWh; TE USD 0,0532/kWh | referência tarifária; atualizar antes de projeção |
| 13-14 | Energia Ouro Branco | Consulta interna | 2023-12-05 | USD 0,106/kWh fora ponta; USD 0,514/kWh ponta | usar para cenário local; confirmar contrato/tarifa |
| 15-22 | Agua e esgoto SABESP | SABESP SP | 2023-11-20 | faixas de USD 1,47 a USD 5,71/m3 | referência SP; pode não valer para Ouro Branco |
| 23-26 | HH operador, técnico, analista, pesquisador | consulta interna / estimado | 2023-11-20 | operador USD 1.224/mês com encargos; técnico USD 2.449; analista USD 3.265; pesquisador pendente | separar salário, encargos e base mensal antes de usar |

## Fornecedores e produtos de grafeno

| Fornecedor na planilha | Produtos / grades | Leitura | Normalizacao |
|---|---|---|---|
| [[NanoXplore]] | NanoXplore 0X; NanoXplore 3X | 0X tem valor de estoque em 2023-11-28 e consulta por email em 2025-06-13 a USD 14/kg; custo com 20% = USD 16,80/kg | enriquecer nota existente; nao duplicar |
| [[Levidian]] | CAMGRAPH G1 BATCH; CAMGRAPH G3 BATCH | status comprado; valores altos e sensiveis | tratar `CamGraph` e `Cambridge Nanosystems` como alias/historico |
| [[First Graphene]] | PureGRAPH AQUA 5/10/20/50; PureGRAPH 5/10/20/50 | planilha grafa `Frist Graphene` | corrigir para canônico `First Graphene` |
| [[Versarien]] | GRAPHINK 2 Binder-Free anionic e non ionic | uma linha comprada; comentario compara dispersao a grafAMGg | validar especificacao primaria |
| [[Thomas Swan]] | Elicarb/GraphCore | F7P1518 informado a USD 82,50/kg em 2023-11-29; comentario: equivalente ao GrafBMGg | Connection criada; usar como fornecedor canônico Elicarb/GraphCore |
| Cambridge Nanosystems | CamGraph Graphene Powder batches | historico relacionado a CamGraph | nao criar duplicata; revisar junto a Levidian |
| [[Universal Matter]] / AGM / Applied Graphene Materials | Genable 1000/1200/1400/3000 | fornecedor historico de graphene materials | Connection criada como canônica; aliases AGM, Applied Graphene Materials e Genable |
| [[Nacional de Grafite]] / NG | Micrograf 99518UJ; 99503UJ; HC11 | grafite micronizado, nao grafeno acabado | Connection criada como insumo grafitico, nao fornecedor de grafeno acabado |
| [[Carbon Rivers]] / CR Nano | produto nao nomeado | consultado a USD 500/kg + 20% | Connection criada com CR Nano como alias; produto/grade ainda pendente |
| Graphene Production | FLG 1 kg, SH 38011000 | cotacao USD 400/kg + 20% | nome generico; manter pendente |
| [[MstnLand]] | Graphene Nano Platelets; rGO; GO | USD 827/kg para GNP; USD 5.063/kg para rGO/GO, antes de 20% | Connection criada; exige TDS/SDS e diligencia de qualidade |
| [[HexoGraphene]] | HexoGraphene | citado sem cotacao | enriquecer apenas como candidato citado |
| [[Nanum]] | Nanum | citado sem cotacao | enriquecer apenas como candidato citado |

## Controle de duplicidade

Antes de criar qualquer registro em `Connections`, aplicar as normalizações:

| Nome na planilha | Registro recomendado |
|---|---|
| Frist Graphene | [[First Graphene]] |
| Cambridge Nanosystems / CamGraph | [[Levidian]] como alias ou histórico, salvo evidência que exija separação |
| AGM / Applied Graphene Materials | [[Universal Matter]] como canônico, com aliases claros |
| NG | [[Nacional de Grafite]] como canônico |
| CR Nano | [[Carbon Rivers]] como canônico, com `CR Nano` como alias |
| Graphene Production | manter pendente até fonte primária |

## Validacao externa Eloi - 2026-05-07

Connections novas criadas com identidade publica clara:

- [[Thomas Swan]]: canônico para Thomas Swan / Elicarb / GraphCore.
- [[Universal Matter]]: canônico para Universal Matter / Applied Graphene Materials / AGM / Genable.
- [[Nacional de Grafite]]: canônico para NG / Micrograf, classificado como grafite micronizado e insumo grafitico.
- [[Carbon Rivers]]: canônico para Carbon Rivers / CR Nano; produto da planilha permanece pendente porque nao ha grade nomeada.
- [[MstnLand]]: canônico para MstnLand / MSTN Technologies, com cautela de fornecedor/trader e necessidade de TDS/SDS.

Aliases/pendencias sem nova Connection:

- `Cambridge Nanosystems` e `CamGraph` devem ficar em [[Levidian]].
- `Frist Graphene` deve ficar apenas como alias de [[First Graphene]].
- `Graphene Production` deve permanecer pendente; buscas publicas retornam resultados genericos de producao de few-layer graphene e nao confirmam de forma confiavel o fornecedor/produto `FLG_(1_KG)`.
- [[HexoGraphene]] e [[Nanum]] continuam como candidatos citados, sem cotacao ou produto nesta planilha.

## Campos para uso em custos

Cada valor deve ser transferido para a matriz de custo com status:

| Status | Uso |
|---|---|
| extraido | valor lido diretamente da planilha |
| estimado | valor indicado como estimativa ou calculado por premissa |
| defasado | valor antigo ou anterior a nova cotacao |
| pendente | valor sem fornecedor, sem especificacao ou incompleto |
| nao comparavel | valor de familia de material diferente ou unidade/base divergente |

## Proximas acoes

- Cacilda: auditar este registro, interlinks e inventario contra o padrao do Vault.
- Eloi: validacao de fornecedores/aliases concluida; Connections novas criadas apenas para canônicos claros e Graphene Production mantido pendente.
- Mariano: incorporar insumos, utilidades e HH no saneamento de custos P100/P500.
- Carmen: consolidar impactos em sourcing, risco de fornecimento e priorizacao estrategica MGg3 apos retornos dos agentes.
