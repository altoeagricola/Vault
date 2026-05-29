---
titulo: Padrao de registro e rastreabilidade para precos de grafeno
tipo: padrao-operacional
produto: MGg3
subproduto: MGg2
codigo_fonte: MGG3-PAD-FORN02
escopo:
  - fornecedores de grafeno
  - cotacoes
  - benchmark internacional
  - inteligencia de mercado
status: aprovado
responsavel: Cacilda
aplicavel_a:
  - Eloi
  - Valdemiro
  - Julio
  - Carmen
fontes_base:
  - "[[Benchmark internacional - fornecedores de grafeno]]"
  - "[[Ecossistema brasileiro de grafeno]]"
  - "[[Inteligencia-de-Mercado-Grafeno-2026]]"
  - "[[MGG3-LEV-P100-v1_Levantamento-Custos-Recomissionamento]]"
  - "[[MGG3-FORN01_Fornecedores-grafeno]]"
  - "[[Padrao operacional - registros consultaveis MGg3]]"
confidencialidade: interno
atualizado: 2026-05-22
---
# MGG3-PAD-FORN02: Padrao de registro e rastreabilidade para precos de grafeno

## Objetivo

Definir o minimo obrigatorio para qualquer registro de preco, cotacao, compra, benchmark ou faixa estimada de grafeno usada na frente MGg3/MGgrafeno. A regra e simples: preco sem fonte datada, status de evidencia e condicao de comparabilidade nao entra em tabela comparativa nem em recomendacao.

Este padrao complementa [[Padrao operacional - registros consultaveis MGg3]] e deve ser usado junto do modelo [[Registro de evidencia de preco - grafeno]].

## Local recomendado no Vault

Registros individuais de evidencia de preco devem ficar em:

`Products/MGg3/MGg2/Fornecedores/Precos/`

Usar um arquivo por evidencia relevante, nao uma lista solta dentro de nota estrategica. A matriz comparativa pode continuar em [[Benchmark internacional - fornecedores de grafeno]], mas deve apontar para os registros individuais.

### Nomenclatura

Formato:

`MGG3-PRECO-AAAAMMDD-SEQ_<fornecedor>-<material>-<familia>.md`

Exemplos:

- `MGG3-PRECO-20250613-01_nanoxplore-0x-gnp.md`
- `MGG3-PRECO-20231129-01_thomas-swan-elicarb-f7p1518-gnp.md`
- `MGG3-PRECO-20260522-01_mstnland-gnp-marketplace.md`

Se a data exata nao existir, usar `AAAA0000` ou `AAAAMM00` apenas no codigo, mas marcar `data_fonte: desconhecida` e `status_confiabilidade: fraco`. Nao usar esse registro como recomendacao.

## Template curto de registro de evidencia

Copiar para cada registro individual:

```markdown
---
titulo:
tipo: registro-evidencia-preco
produto: MGg3
codigo_fonte: MGG3-PRECO-AAAAMMDD-SEQ
fornecedor_player:
material:
familia: # few-layer graphene | GNP | GO | rGO | grafite micronizado | dispersao | masterbatch | aditivo formulado | outro
especificacao:
forma_entrega: # po | dispersao aquosa | dispersao solvente | masterbatch | pellet | formulado | outro
preco:
moeda:
unidade: # kg | g | L | t | lote | outro
volume_moq:
incoterm:
data_fonte:
url_documento:
tipo_fonte: # publica | player_declarado | interna | confidencial | marketplace | compilacao | inferencia
status_confiabilidade: # forte | medio | fraco | obsoleto | nao_comparavel
confidencialidade: # publico | interno | confidencial | restrito | desconhecido
comparabilidade:
links_relacionados: []
responsavel:
atualizado:
---
# <codigo>: <fornecedor> - <material>

## Evidencia

| Campo | Valor |
|---|---|
| Fornecedor/player |  |
| Material |  |
| Familia |  |
| Especificacao |  |
| Forma de entrega |  |
| Preco |  |
| Moeda |  |
| Unidade |  |
| Volume/MOQ |  |
| Incoterm |  |
| Data da fonte |  |
| URL/documento |  |
| Tipo de fonte |  |
| Status de confiabilidade |  |
| Observacoes de comparabilidade |  |

## Uso permitido

- Pode usar em: 
- Nao pode usar em: 

## Observacoes

- 
```

## Regras de classificacao da evidencia

| Classe | Definicao | Como escrever | Uso permitido |
|---|---|---|---|
| Fato verificado | Dado confirmado em fonte publica, documento primario, filing, TDS/SDS, cotacao formal, pedido de compra ou registro interno rastreavel. | "Fonte X, datada de AAAA-MM-DD, informa..." | Pode sustentar comparacao, desde que especificacao e unidade estejam claras. |
| Fato declarado por player | Dado publicado ou enviado pelo proprio fornecedor, sem verificacao independente. | "O player declara..." | Pode mapear oferta e narrativa comercial; nao deve virar prova de mercado sem ressalva. |
| Evidencia interna | Dado vindo de planilha, email, compra, teste, nota tecnica ou documento do Vault. | "Evidencia interna do Vault indica..." | Uso interno; externo somente se autorizado e sem expor termos sensiveis. |
| Inferencia estrategica | Conclusao analitica derivada de varias evidencias. | "A leitura estrategica sugere..." | Pode orientar priorizacao; nao deve ser apresentada como fato de mercado. |
| Dado obsoleto | Preco, especificacao ou status superado por data, nova cotacao ou mudanca de mercado. | "Dado historico/obsoleto; manter para rastreabilidade." | Nao usar como preco atual; usar apenas para historico. |
| Nao comparavel | Evidencia sem especificacao, unidade, familia, data, volume/MOQ ou condicao comercial suficiente. | "Nao comparavel com a base atual por..." | Nao entra em media, ranking ou recomendacao. |

## Status de confiabilidade

| Status | Criterio minimo |
|---|---|
| `forte` | Fonte primaria datada + material identificado + unidade + volume/MOQ ou contexto comercial + especificacao tecnica minima. |
| `medio` | Fonte datada e material identificado, mas falta algum campo comercial relevante, como MOQ, incoterm, frete ou TDS/SDS. |
| `fraco` | Fonte sem data completa, sem documento primario, sem especificacao tecnica ou baseada em marketplace/trader sem diligencia. |
| `obsoleto` | Evidencia antiga ou superada; manter por rastreabilidade, nao por validade atual. |
| `nao_comparavel` | Familia, forma de entrega ou unidade impedem comparacao direta com os demais materiais. |

Nenhuma recomendacao pode depender de registro `fraco`, `obsoleto` ou `nao_comparavel` sem dizer explicitamente que e lacuna, nao conclusao.

## Regras para fontes publicas, internas e confidenciais

### Fonte publica

- Registrar URL, data do documento ou data de acesso, tipo de documento e trecho/metricas relevantes.
- Marcar `confidencialidade: publico`.
- Mesmo sendo publica, separar claim promocional de evidencia tecnica; pagina comercial nao substitui TDS/SDS.

### Fonte declarada por player

- Usar `tipo_fonte: player_declarado`.
- Manter linguagem atribuida: "o fornecedor declara", "a empresa informa".
- Se nao houver documento tecnico, nao chamar de validado.

### Fonte interna

- Usar `tipo_fonte: interna` e `confidencialidade: interno`.
- Informar documento do Vault, planilha, email, issue ou nota tecnica de origem.
- Nao copiar dado sensivel para material externo; usar apenas faixa ou leitura agregada quando autorizado.

### Fonte confidencial ou restrita

- Usar `tipo_fonte: confidencial` e `confidencialidade: confidencial` ou `restrito`.
- Nao expor preco nominal fora do Vault sem autorizacao.
- Em sinteses externas, substituir por leitura qualitativa: "cotacao interna recente", "compra historica", "faixa confidencial".

### Marketplace, trader ou compilacao

- Usar `status_confiabilidade: fraco` ate haver TDS/SDS, amostra, fornecedor legal identificado e condicoes comerciais.
- Nao comparar diretamente com fornecedor industrial validado.

## Regras de comparabilidade

Antes de comparar preco/kg, preencher no minimo:

- familia do material: FLG, GNP, GO, rGO, grafite micronizado, dispersao, masterbatch ou aditivo formulado;
- especificacao: teor de carbono, numero de camadas, area superficial, tamanho lateral, pureza, umidade, cinzas e funcionalizacao quando existirem;
- forma de entrega: po, dispersao, masterbatch, pellet ou formulado;
- unidade e conversao: kg, g, litro, tonelada, lote; registrar densidade quando converter dispersao;
- volume/MOQ e incoterm: preco de amostra, laboratorio, bulk, FOB, CIF, DDP ou desconhecido;
- data da fonte e validade comercial;
- impostos, frete e cambio quando o dado entrar em custo MGg3.

Se qualquer campo essencial estiver ausente, escrever a lacuna na coluna `observacoes de comparabilidade` e rebaixar a confiabilidade.

## Checklist de revisao textual

Antes de entregar qualquer nota, tabela ou sintese de precos:

- Clareza: cada linha informa exatamente qual material, fornecedor, unidade e familia esta sendo comparado.
- Referencia: toda afirmacao quantitativa tem fonte datada, link/documento e tipo de fonte.
- Dado vs inferencia: fatos, declaracoes de player, evidencia interna e leitura estrategica aparecem separados.
- Confidencialidade: cotacoes, compras, emails e planilhas internas estao marcados como internos/confidenciais; nada sensivel foi convertido em claim publico.
- Links internos: fornecedor, fonte-base, benchmark, custo P100/P500 e registro individual de preco estao linkados.
- Comparabilidade: diferencas de especificacao, volume, incoterm, familia e data foram explicitadas.
- Obsolescencia: dado antigo ou sem data nao aparece como recomendacao atual.

## Aplicacao imediata para a frente ALT-339/ALT-340

- Eloi deve registrar cada evidencia externa de preco como `MGG3-PRECO-*` antes de consolidar ranking.
- Valdemiro deve usar apenas registros `forte` ou `medio` como entrada de custo; dados `fraco`, `obsoleto` ou `nao_comparavel` entram como lacuna.
- Julio deve separar benchmark publico de informacao interna/confidencial em qualquer material executivo.
- Carmen deve transformar comparacoes em inferencias estrategicas apenas quando a base estiver rastreavel por registro individual.

## Links relacionados

- [[Benchmark internacional - fornecedores de grafeno]]
- [[Ecossistema brasileiro de grafeno]]
- [[Inteligencia-de-Mercado-Grafeno-2026]]
- [[MGG3-LEV-P100-v1_Levantamento-Custos-Recomissionamento]]
- [[MGG3-FORN01_Fornecedores-grafeno]]
- [[Padrao operacional - registros consultaveis MGg3]]
- [[Protocolo de manutencao - novas fontes MGg3]]
- [[Registro de evidencia de preco - grafeno]]
