---
titulo: Padrao de registro e rastreabilidade para cotacoes de equipamentos
tipo: padrao-operacional
produto: MGg3
subproduto: MGg2
codigo_fonte: MGG3-PAD-FORN03
escopo:
  - fornecedores de equipamentos
  - cotacoes CAPEX
  - bens de capital
  - scale-up P500
status: aprovado
responsavel: Cacilda
confidencialidade: interno
atualizado: 2026-06-11
---
# MGG3-PAD-FORN03: Padrao de registro e rastreabilidade para cotacoes de equipamentos

## Decisao de schema

O padrao [[MGG3-PAD-FORN02_Padrao-registro-precos-grafeno]] continua restrito a precos de grafeno, insumos formulados e evidencias de material. Cotacoes de equipamento e bens de capital nao devem entrar em `Fornecedores/Precos/`, porque tem outra unidade economica, outra comparabilidade e outro uso: ancorar CAPEX, RFQ e engenharia.

Para equipamentos MGg3, usar este padrao proprio com codigo `MGG3-COT-*` e local canonico:

`Products/MGg3/MGg2/Fornecedores/CotacoesEquipamentos/`

## Nomenclatura

Formato:

`MGG3-COT-AAAAMMDD-SEQ_<fornecedor>-<equipamento>-<modelo>.md`

## Campos minimos

Todo registro de cotacao de equipamento deve explicitar fornecedor, equipamento/modelo, data da fonte, moeda, preco, unidade comercial, escopo incluido, Incoterm, ponto de entrega, prazo de entrega, condicao de pagamento, status de confiabilidade, condicao de comparabilidade, fonte primaria e relacao com o custo ou decisao tecnica que usa a evidencia.

## Regras de uso

- Cotacao formal de fornecedor com PDF ou e-mail primario pode ser `forte`, desde que modelo, escopo, moeda, Incoterm e data estejam claros.
- Cotacao FCA, FOB ou EXW nao deve ser tratada como custo posto na planta. O registro deve separar preco do equipamento de frete, seguro, nacionalizacao, tributos, montagem e E&I.
- Quando uma cotacao for tecnicamente inadequada para a aplicacao, manter o registro como evidencia rastreavel e marcar `uso_capex: descartado` ou equivalente.
- Valores convertidos, landed, instalados ou com contingencia pertencem aos documentos de custo, nao ao registro de cotacao. O registro preserva a fonte comercial.

## Links relacionados

- [[MGG3-PAD-FORN02_Padrao-registro-precos-grafeno]]
- [[MGG3-CUSTO-P500-v2_Escalonamento-Engenharia-P100-P500]]
- [[MGG3-CUSTO-P500_Projecao-KonMix]]
- [[Saneamento custos P100 P500]]
