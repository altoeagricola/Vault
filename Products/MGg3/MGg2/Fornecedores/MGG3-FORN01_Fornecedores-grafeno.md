---
titulo: Base de Fornecedores de Grafeno - MGg3
tipo: registro-documento
codigo_fonte: MGG3-FORN01
fonte_arquivo: "Fornecedores de Grafeno_Editado.xlsx"
caminho_fonte: "Products/MGg3/MGg2/Fornecedores/Fornecedores de Grafeno_Editado.xlsx"
nome_original: "Fornecedores de Grafeno_Editado.xlsx"
organizacao: MGg3 / inteligencia de mercado
tipo_documento: base de dados / matriz de fornecedores
data_documento: 2026
confidencialidade: interno
status_extracao: extraido_parcial
confianca_extracao: media
temas:
  - fornecedores de grafeno
  - matriz de insumos
  - inteligencia de mercado
  - cadeia de suprimento
  - players internacionais
produtos:
  - grafeno
  - aditivos de grafeno
aplicacoes:
  - concreto
  - polimeros
  - tintas
  - lubrificantes
metricas_chave:
  - lista de fornecedores
  - tipos de grafeno (grafico 0X, 3X, BS3, BS8, etc)
  - origem geografica
  - cotacoes
  - status de relacionamento
riscos_uso:
  - confidencialidade de cotacoes; nao compartilhar externamente
  - preco e disponibilidade de insumos variam; dados podem envelhecer rapidamente
  - cotacoes podem incluir termos comerciais sensiveis
  - players podem ter mudado nomes, consolidacoes ou saidas de mercado
links_relacionados:
  - "[[MGG3-FORN02_Fornecedores-insumos-grafeno-startup]]"
  - "[[Ecossistema brasileiro de grafeno]]"
  - "[[Validacao externa - players de mercado MGg3.0]]"
  - "[[Gerdau Graphene - Empresa]]"
  - "[[NanoXplore]]"
  - "[[BlackSwan Graphene]]"
  - "[[First Graphene]]"
  - "[[Levidian]]"
  - "[[Versarien]]"
  - "[[Polystell]]"
  - "[[Colorfix]]"
atualizado: 2026-05-07
---

# MGG3-FORN01: Base de Fornecedores de Grafeno - MGg3

## Identificacao

| Campo | Valor |
|---|---|
| Arquivo | `Fornecedores de Grafeno_Editado.xlsx` |
| Tipo | Base de dados / Matriz de fornecedores e insumos |
| Origem | Inteligência de mercado MGg3 |
| Tamanho | 60 KB |
| Data | 2026 |
| Confidencialidade | Interno |
| Status | Extraido parcialmente por Eloi em 2026-05-07; requer atualização periódica |

## Resumo executivo

Base de dados estruturada de fornecedores internacionais de grafeno para MGg3. A planilha contem uma aba principal (`Planilha1`) com 41 linhas uteis de insumos, codigos 27 a 67, incluindo produtos, fornecedores, status de consulta/compra, datas de cotacao, precos em USD, impostos estimados, unidade e comentarios.

Fonte complementar: [[MGG3-FORN02_Fornecedores-insumos-grafeno-startup]] adiciona os codigos 6 a 26 de insumos, utilidades e HH da pasta `Startup Grafeno`, alem de repetir a camada de fornecedores/produtos de grafeno. Usar as duas fontes como irmas; nao substituir uma pela outra sem reconciliacao.

Documento crítico para:
- sourcing de insumos em escala de produção;
- benchmarking de preço e qualidade;
- diversificação de fornecimento;
- validação de disponibilidade e lead times.

## Papel no briefing

Fonte primária para:
- entender matriz de fornecimento de grafeno para MGg3;
- validar viabilidade de custo de insumo em escala P500;
- identificar players críticos de mercado (fornecedores, competidores);
- analisar concentração de risco em fornecimento (dependência de poucos fornecedores);
- suportar negociacoes comerciais com fornecedores.

## Conteudo esperado (colunas)

- **Fornecedor**: nome empresa, país
- **Tipo de grafeno**: designação (0X, 3X, BS3, BS8, etc), camadas, tamanho partícula
- **Preço/cotação**: USD/kg ou similar
- **Tamanho mínimo**: MOQ (minimum order quantity)
- **Lead time**: tempo de entrega
- **Status**: ativo, descontinuado, em negoação
- **Notas**: relaçao existente, volume, contato técnico

## Extracao inicial Eloi - 2026-05-07

### Colunas identificadas

| Coluna | Uso |
|---|---|
| Cod | Codigo interno do insumo, de 27 a 67 nesta planilha |
| Nome | Produto, grade ou familia de grafeno/grafite |
| Supplier | Fornecedor informado |
| Status | Situacao da informacao: valor de estoque, consulta, cotacao, comprado ou informado |
| Quotation Data | Data da cotacao quando preenchida |
| Original Price / USD Price | Preco original ou preco convertido/informado em USD |
| Taxes % | Imposto ou fator adicional, normalmente 20% em linhas cotadas |
| purchase cost USD / Price Unit | Custo calculado; algumas linhas possuem formulas quebradas por `#REF!` |
| Comments | Premissas ou equivalencias internas |

### Fornecedores e produtos extraidos

| Fornecedor na planilha | Produtos / grades | Evidencia na planilha | Validacao publica inicial |
|---|---|---|---|
| [[NanoXplore]] | NanoXplore 0X; NanoXplore 3X | Linhas 7-9; 0X com valor de estoque em 2023-11-28 e consulta por email em 2025-06-13; comentario: equivalente a LamaGrafMGg | Confirmado como fornecedor industrial de grafeno; enriquecer nota existente com grades 0X/3X e faixa de cotacao interna. |
| [[Levidian]] | CAMGRAPH G1 BATCH; CAMGRAPH G3 BATCH | Linhas 10-11; status comprado; formulas de conversao quebradas por `#REF!` | Confirmado publicamente; Levidian informa produto G3 e historico como Cambridge Nanosystems. Enriquecer nota existente com alias Cambridge Nanosystems/CamGraph. |
| [[First Graphene]] | PureGRAPH AQUA 5/10/20/50; PureGRAPH 5/10/20/50 | Linhas 12 e 15-22; supplier grafado como `Frist Graphene` | Confirmado publicamente; corrigir alias `Frist Graphene` para [[First Graphene]] e enriquecer com familia PureGRAPH/PureGRAPH AQUA. |
| [[Versarien]] | GRAPHINK 2 Binder-Free anionic; GRAPHINK 2 Binder-Free non ionic | Linhas 13-14; uma linha comprada; comentario compara dispersao a grafAMGg | Confirmado publicamente como player de graphene materials; validar especificamente GRAPHINK 2 em fonte primaria antes de usar especificacao. |
| [[Thomas Swan]] | Elicarb GNP M1P0953 / M1P0955 / F7P1518 / M1D1507 / F7D1515 / M2539 | Linhas 23-28; F7P1518 informado em 2023-11-29 a USD 82,50/kg; comentario: equivalente ao GrafBMGg | Confirmado publicamente via Elicarb Graphene; Connection criada. |
| Cambridge Nanosystems | CamGraph Graphene Powder batches 000006 a 000010 | Linhas 29-33 | Deve ser tratado como alias/historico de [[Levidian]], nao como duplicata isolada. |
| [[Universal Matter]] / AGM / Applied Graphene Materials | Genable 1000, 1200, 1400, 3000 | Linhas 34-37 | Confirmado publicamente; Connection criada como canônico Universal Matter. |
| [[Nacional de Grafite]] / NG | Micrograf 99518UJ; Micrograf 99503UJ; Micrograf HC11 | Linhas 38-40 | Confirmado publicamente como grafite micronizado, nao grafeno acabado. Importante para rota de exfoliacao ou insumo grafitico. |
| [[Carbon Rivers]] / CR Nano | Produto nao nomeado | Linha 41; consultado; USD 500/kg + 20% = USD 600/kg | Connection criada como Carbon Rivers; produto/grade ainda pendente. |
| Graphene Production | FLG 1 kg - Few Layer Graphene; NCM/SH 38011000 | Linha 42; cotacao USD 400/kg + 20% = USD 480/kg | Nao confirmado com fonte primaria pelo nome exato; manter como fornecedor pendente. |
| [[MstnLand]] | Graphene Nano Platelets; Reduced Graphene Oxide; Graphene Oxide | Linhas 43-45; consultado; USD 827/kg e USD 5.063/kg + 20% | Confirmado publicamente como MstnLand/MSTN Technologies com produtos de graphene materials; exige cuidado por perfil amplo de trading/industrial equipment. |
| [[HexoGraphene]] | HexoGraphene | Linha 46; sem fornecedor, cotacao ou status | Player ja validado; planilha apenas sinaliza candidato, nao cotacao. |
| [[Nanum]] | Nanum | Linha 47; sem fornecedor, cotacao ou status | Player ja validado; planilha apenas sinaliza candidato, nao cotacao. |

### Cotações e alertas de qualidade dos dados

| Item | Valor extraido | Uso recomendado |
|---|---|---|
| NanoXplore 0X | USD 14/kg em consulta por email de 2025-06-13; custo calculado com 20% = USD 16,80/kg | Usar como referencia interna recente, nao como preco publico. Confirmar incoterm, volume, frete e especificacao. |
| Thomas Swan Elicarb F7P1518 | USD 82,50/kg em 2023-11-29; imposto 0%; comentario de equivalencia ao GrafBMGg | Bom candidato para benchmark tecnico; preco pode estar defasado. |
| CR Nano | USD 500/kg; custo calculado com 20% = USD 600/kg | Confirmar identidade e especificacao antes de comparar. |
| Graphene Production FLG | USD 400/kg; custo calculado com 20% = USD 480/kg | Manter como pendente ate validar fornecedor. |
| MstnLand GNP | USD 827/kg; custo calculado com 20% = USD 992,40/kg | Cotacao de marketplace/fornecedor amplo; exigir TDS/SDS e amostra caracterizada. |
| MstnLand rGO/GO | USD 5.063/kg; custo calculado com 20% = USD 6.075,60/kg | Nao comparar diretamente com GNP/few-layer graphene; familia quimica e aplicacoes podem ser diferentes. |

Algumas linhas de preco original possuem formulas quebradas por `#REF!`, principalmente Levidian e Versarien. Essas linhas nao devem ser usadas para custo final ate recuperar a taxa de cambio ou celula de referencia perdida.

### Connections a enriquecer sem duplicacao

Enriquecer notas existentes:

- [[NanoXplore]]: adicionar produtos `0X` e `3X`, cotacao interna de 2025-06-13 para 0X e comentario de equivalencia a LamaGrafMGg.
- [[Levidian]]: adicionar `CAMGRAPH G1`, `CAMGRAPH G3`, alias `CamGraph` e `Cambridge Nanosystems`.
- [[First Graphene]]: adicionar alias `Frist Graphene` por erro de grafia na planilha; incluir familias `PureGRAPH` e `PureGRAPH AQUA`.
- [[Versarien]]: adicionar `GRAPHINK 2 Binder-Free`, com cautela de validar especificacao primaria.
- [[HexoGraphene]] e [[Nanum]]: marcar que a planilha os cita apenas como candidatos, sem cotacao ou status.

Criar notas novas apenas se forem usados como fornecedores ativos:

- [[Thomas Swan]]: fornecedor Elicarb/GraphCore, validado publicamente.
- [[Universal Matter]]: canônico para `AGM`, `Applied Graphene Materials` e `Universal Matter GBR`.
- [[Nacional de Grafite]]: fornecedor brasileiro de grafite micronizado Micrograf; nao tratar como fornecedor de grafeno acabado.
- [[MstnLand]]: fornecedor/trader chines de graphene materials; requer diligencia de qualidade.
- [[Carbon Rivers]]: canônico para `CR Nano`; produto/grade ainda pendente.
- `Graphene Production`: manter pendente; nome generico demais sem fonte primaria confirmada.

### Fontes publicas consultadas

- NanoXplore: https://nanoxplore.ca/
- Levidian: https://www.levidian.com/graphene-products e https://www.levidian.com/about-us
- First Graphene: https://firstgraphene.net/
- Thomas Swan Elicarb: https://www.thomas-swan.us/chemical_products/elicarb/
- Universal Matter / Applied Graphene Materials: https://www.universalmatter.com/about-us/
- Nacional de Grafite Micrograf: https://www.grafite.com/micrograf
- Carbon Rivers / CR Nano: https://www.carbonrivers.com/cr-nano
- MstnLand: https://www.mstnland.com/
- Versarien: https://www.versarien.com/

## Lacunas e cautelas

- Confidencialidade de cotações; nao divulgar externamente.
- Preço e disponibilidade variam; dados podem ficar desatualizados rapidamente (revisao a cada 3-6 meses recomendada).
- Cotações podem incluir termos comerciais sensiveis (descontos por volume, cláusulas de NDA).
- Players podem ter mudado: consolidacoes, saidas de mercado, mudancas de nome ou aquisicoes. Ex.: Applied Graphene Materials deve ser normalizada junto a Universal Matter; Cambridge Nanosystems deve ser tratada como historico/alias de Levidian.
- Grafenos listados como "0X" ou "3X" podem ser designacoes comerciais ou internas; confirmar especificacao tecnica exata com fornecedor.
- Nao comparar diretamente grafite micronizado, graphene nanoplatelets, few-layer graphene, graphene oxide e reduced graphene oxide; sao familias distintas para aplicacoes e precificacao.

## Proximas acoes

- Eloi: validacao externa inicial concluida; proxima etapa e enriquecer Connections existentes e criar novas notas apenas para fornecedores priorizados.
- Atualizar cotações com base em contatos recentes (Mariano pode coordenar se houver negociacoes ativas).
- Criar matriz de risco de fornecimento (diversificacao, lead time, preço, estabilidade).
- Preparar sumário de fornecedores estrategicos (criticalidade, alternativas) para apresentacao a investidores.
