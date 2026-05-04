---
tipo: template
contexto: financeiro_produtor
status: draft
created: 2026-05-03
atualizado: 2026-05-03
---

# Ficha Economico-Financeira Minima do Produtor

## Objetivo

Capturar o minimo de dados para:

- estimar receita da safra
- estimar custo total
- calcular margem bruta por hectare
- avaliar capacidade de pagamento
- separar o que e numero declarado, documental e estimado

## Regra de classificacao dos dados

- `declarado`: informado pelo produtor, sem comprovacao imediata
- `documental`: extraido de documento, contrato, CCIR, DAP/CAF, IR ou equivalente
- `estimado`: calculado por media regional, historico ou premissa tecnica

## Campos da ficha

### 1. Identificacao da propriedade

| Campo | Tipo de dado | Formato | Observacao |
| --- | --- | --- | --- |
| Nome do produtor | declarado | texto | Nome completo ou razao de referencia |
| Municipio | declarado | texto | Cidade principal da propriedade |
| Area total (ha) | declarado | numero | Area total da propriedade |
| Area cultivada (ha) | declarado | numero | Area efetivamente em producao |
| Cultura principal | declarado | texto | Ex.: conilon |
| Culturas secundarias | declarado | texto | Ex.: pimenta, milho, gado |
| Area CCIR (ha) | documental | numero | Se houver divergencia, registrar observacao |

### 2. Dados produtivos por cultura

Repetir este bloco para cada cultura relevante.

| Campo | Tipo de dado | Formato | Observacao |
| --- | --- | --- | --- |
| Cultura | declarado | texto | Nome da cultura |
| Area da cultura (ha) | declarado | numero | Area destinada a essa cultura |
| Produtividade estimada | declarado | numero | Em sacas/ha ou unidade equivalente |
| Unidade de produtividade | declarado | texto | saca/ha, caixa/ha etc. |
| Preco medio esperado | declarado | moeda | Valor por saca ou unidade |
| Mes inicio colheita | declarado | texto | Ex.: maio |
| Mes fim colheita | declarado | texto | Ex.: agosto |
| Mes principal de receita | declarado | texto | Quando entra mais dinheiro |

### 3. Dados financeiros declarados

| Campo | Tipo de dado | Formato | Observacao |
| --- | --- | --- | --- |
| Receita bruta estimada da safra | declarado | moeda | Soma esperada da producao |
| Dividas existentes | declarado | moeda | Saldo aproximado das dividas |
| Prestacoes mensais em aberto | declarado | moeda | Quanto ja compromete por mes |
| Outras receitas da familia/propriedade | declarado | moeda | Salario, arrendamento, leite etc. |
| Despesas fixas mensais | declarado | moeda | Casa, energia, funcionarios, transporte |

### 4. Dados documentais

| Campo | Tipo de dado | Formato | Observacao |
| --- | --- | --- | --- |
| CCIR apresentado | documental | sim/nao | Marcar disponibilidade |
| Area do CCIR (ha) | documental | numero | Copiar do documento |
| DAP/CAF ou equivalente | documental | sim/nao | Marcar disponibilidade |
| Renda declarada em documento | documental | moeda | DAP/CAF, IR ou outro documento |
| IR apresentado | documental | sim/nao | Marcar disponibilidade |

### 5. Dados estimados

| Campo | Tipo de dado | Formato | Observacao |
| --- | --- | --- | --- |
| Custo de producao por hectare | estimado | moeda | Base regional ou historica |
| Despesa de manutencao por safra | estimado | moeda | Irrigacao, trato, reposicao, combustivel |
| Custo total estimado da safra | estimado | moeda | Area x custo/ha + manutencao |

## Indicadores-chave

### 1. Receita esperada por safra

Formula base:

`receita esperada = soma(area da cultura x produtividade x preco medio)`

### 2. Custo total estimado por safra

Formula base:

`custo total = soma(area da cultura x custo estimado por hectare) + despesas de manutencao`

### 3. Margem bruta por hectare

Formula base:

`margem bruta/ha = (receita esperada - custo total) / area cultivada`

### 4. Capacidade de pagamento estimada

Leitura simples:

- `forte`: sobra apos custo e prestacoes
- `media`: paga, mas com pouca folga
- `apertada`: risco de atraso ou necessidade de alongamento

Formula de apoio:

`capacidade liquida = receita esperada - custo total - dividas/prestacoes do ciclo`

## Linguagem de campo sugerida

Perguntas curtas, diretas:

- Quantos hectares tem no total e quantos estao plantados hoje?
- Qual e a cultura principal? Tem mais alguma entrando no caixa?
- Quanto voce espera colher por hectare?
- Em quais meses costuma entrar o grosso da receita?
- Hoje, quanto ja tem de divida ou prestacao em aberto?
- Pelo seu feeling, quanto essa safra deve faturar?

## Observacoes de uso

- Nao misturar numero documental com chute tecnico.
- Quando o numero for estimado, registrar a base da estimativa.
- Quando houver divergencia entre area declarada e area documental, manter as duas.
- Se faltar dado, deixar em branco e marcar pendencia, sem preencher por suposicao silenciosa.
