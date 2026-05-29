---
tipo: Dossie de Cliente Rural
cliente: "[[Sergio Jose Altoe]]"
produto: "[[Crédito-Rural]]"
linha_principal: "Pronaf Habitacao Rural"
banco_principal: "[[Cresol]]"
valor_solicitado: "R$ 100.000,00"
status: piloto_em_analise
issue_origem: "ALT-69"
created: 2026-05-04
updated: 2026-05-29
tags:
  - cliente-rural
  - dossie
  - credito-rural
  - piloto-operacional
---

# Sergio Jose Altoe - Dossie Rural

## 1. Localizacao no Vault

Este e o indice operacional do caso Sergio Jose Altoe. A estrutura correta fica assim:

| Camada                    | Local                                                                 | Uso                                              |
| ------------------------- | --------------------------------------------------------------------- | ------------------------------------------------ |
| Relacionamento/CRM        | [[Sergio Jose Altoe]]                                                 | ficha comercial, contato, funil, proximas acoes  |
| Dossie operacional        | esta nota                                                             | indice mestre do caso, rastreabilidade e decisao |
| Documentos pessoais       | `Products/Credito-Rural/Clientes/Sergio Jose Altoe/Docs Pessoais/`    | PDFs originais de identificacao e renda          |
| Documentos da propriedade | `Products/Credito-Rural/Clientes/Sergio Jose Altoe/Docs Propriedade/` | CCIR, ITR, CAR, escritura, outorga               |
| Documentos de avalista    | `Products/Credito-Rural/Clientes/Sergio Jose Altoe/Docs Avalista/`    | documentos de terceiros, se aplicavel            |
| Projeto de credito        | [[Pronaf Habitacao - Sergio Jose Altoe]]                              | nota da operacao/linha/banco                     |
| Banco                     | [[Cresol]]                                                            | pratica bancaria, contato e exigencias           |
| Regiao/mercado            | [[Marilandia]]                                                        | contexto territorial e mercado de conilon        |

Regra: documento bruto fica na pasta do cliente; analise fica em nota markdown; decisao fica no dossie. Sem isso, vira gaveta baguncada. E gaveta baguncada cobra juros.

## 2. Indice padrao do caso rural

| Bloco | Artefato final | Status | Link/Local |
| --- | --- | --- | --- |
| 1. Ficha CRM | ficha do cliente | iniciado | [[Sergio Jose Altoe]] |
| 2. Indice documental | lista de documentos encontrados | parcial | seções 3 e 4 deste dossie |
| 3. Checklist documental | existente / ausente / vencido / confirmar | produzido | [[Checklist Documental - Sergio Jose Altoe]] |
| 4. Enquadramento de credito | parecer linha/programa/banco | a produzir | [[Pronaf Habitacao - Sergio Jose Altoe]] |
| 5. Mercado conilon | briefing Marilandia/ES | a produzir | linkar quando entregue |
| 6. Analise financeira | capacidade de pagamento | a produzir | linkar quando entregue |
| 7. Fomento/subsidio | rotas alternativas | a produzir | linkar quando entregue |
| 8. Recomendacao final | seguir / seguir com pendencias / nao seguir | a produzir | linkar quando entregue |
| 9. Performance do piloto | falhas, gaps, pontos fortes | a produzir | linkar no fechamento do ALT-63 |

## 3. Documentos encontrados

### Docs Pessoais

| Arquivo | Tipo | Observacao organizacional |
| --- | --- | --- |
| [[Registro - CAF Sergio Jose Altoe]] | CAF | CAF renovado em 28/05/2026: situação ATIVA, validade 28/05/2029, enquadramento V; PDFs novos consultados em Downloads, sem cópia no Vault |
| [[Registro - Certidao Negativa RFB PGFN Sergio Jose Altoe]] | regularidade fiscal federal / CND | CND RFB/PGFN emitida em 29/05/2026, válida até 25/11/2026; PDF consultado em Downloads, sem cópia no Vault |
| `CERTIDAO DE CASAMENTO Sergio e Lourdes.pdf` | estado civil | importante para habitacao rural e composicao familiar |
| `CNH - SERGIO.pdf` | identificacao | padronizar nome em rodada futura |
| `COMP. DE APOSENTADORIA Maria de Lourdes e Sergio.pdf` | renda | entrada para analise financeira |
| [[Registro - Nota Fiscal Rural 250520001 Sergio Jose Altoe]] | renda rural / NF-e | NF-e de venda de 112 sacas de cafe conilon, total R$ 100.800,00; PDF nao anexado por instrucao do usuario; evidencia para renovacao do CAF no Sindicato Rural de Marilandia |
| `DOC - MOTO.pdf` | bem/veiculo | classificar se entra em patrimonio ou garantia |
| `RG + CPF - SERGIO.pdf` | identificacao | conferir CPF e validade/cadastro |
| `RG E CPF - MARIA DE LOURDES BERNABE ALTOE.pdf` | conjuge | vincular ao nucleo familiar |

### Docs Propriedade

| Arquivo | Tipo | Observacao organizacional |
| --- | --- | --- |
| `CCIR 2025 Sergio Altoe.pdf` | imovel rural | documento-chave para credito rural |
| `ESCRITURA Sergio Altoe.pdf` | propriedade | conferir titularidade e confrontacoes |
| `ITR 2025 Sergio Altoe.pdf` | fiscal rural | conferir situacao e exercicio |
| [[Outorga Sergio Jose Altoe]] | outorga | nota operacional ja existe; confirmar validade no PDF |
| `Outorga-Sergio-Jose-Altoe.pdf` | outorga original | manter junto da nota operacional |
| `RECIBO DO CAR E CAR Sergio Altoe.pdf` | ambiental | conferir recibo, status e area |

## 4. Regras de nomeacao

### Notas markdown

Usar sempre:

`<Tipo de artefato> - <Nome do cliente>.md`

Exemplos:

| Artefato | Nome correto |
| --- | --- |
| Dossie mestre | `Sergio Jose Altoe - Dossie Rural.md` |
| Checklist documental | `Checklist Documental - Sergio Jose Altoe.md` |
| Analise financeira | `Analise Financeira - Sergio Jose Altoe.md` |
| Enquadramento | `Enquadramento Credito - Sergio Jose Altoe.md` |
| Recomendacao | `Recomendacao Final - Sergio Jose Altoe.md` |

### PDFs e anexos

Usar:

`<Tipo> - <Nome Cliente> - <Ano ou Competencia>.pdf`

Exemplos:

| Atual | Recomendado quando houver higienizacao |
| --- | --- |
| `CNH - SERGIO.pdf` | `CNH - Sergio Jose Altoe.pdf` |
| `RG + CPF - SERGIO.pdf` | `RG CPF - Sergio Jose Altoe.pdf` |
| `ITR 2025 Sergio Altoe.pdf` | `ITR - Sergio Jose Altoe - 2025.pdf` |

Nao renomear em massa durante o piloto sem validar links, porque ha documentos operacionais em uso.

## 5. Regras de linkagem

- Toda nota do caso deve linkar para [[Sergio Jose Altoe]] e para este dossie.
- Todo parecer de credito deve linkar para [[Pronaf Habitacao - Sergio Jose Altoe]], [[Cresol]] e a norma/programa correspondente.
- Toda analise de mercado deve linkar para [[Marilandia]] e citar fontes no proprio artefato.
- Toda pendencia documental deve aparecer em dois lugares: checklist documental e ficha CRM.
- Toda recomendacao final deve separar dado documental, dado declarado, estimativa e decisao.
- Se o mesmo documento servir para varios produtos, nao duplicar PDF: linkar o arquivo ou a nota do documento.

## 6. Falhas de organizacao percebidas

| Falha | Impacto | Correcao recomendada |
| --- | --- | --- |
| Sergio tinha documentos e projeto, mas nao tinha ficha CRM em `Connections/Clientes` | o cliente existia como pasta, nao como relacionamento rastreavel | ficha criada e deve ser mantida como entrada comercial |
| Link para `Connections/People/Sergio Jose Altoe` sem nota correspondente | backlinks quebrados e perda de rastreabilidade | usar [[Sergio Jose Altoe]] em Clientes como canonical |
| Projeto dizia "documentacao completa" sem indice verificavel | conclusao forte demais sem checklist | criar checklist documental antes de submeter |
| PDFs com nomes inconsistentes | dificulta busca, automacao e revisao futura | padronizar nomes em rodada propria |
| Outorga mistura nota operacional com credenciais sensiveis | risco de exposicao e acoplamento indevido | mover credenciais para local seguro/gerenciador; deixar no Vault apenas referencia operacional |
| Caso ainda nao tinha dossie mestre | analises dos agentes ficariam soltas | usar esta nota como indice unico do caso |

## 7. Modelo reutilizavel

Para o proximo cliente rural, criar nesta ordem:

1. `Connections/Clientes/<Nome Cliente>.md`
2. `Products/Credito-Rural/Clientes/<Nome Cliente>/<Nome Cliente> - Dossie Rural.md`
3. `Docs Pessoais/`, `Docs Propriedade/`, `Docs Avalista/`, `Projetos/`
4. `Checklist Documental - <Nome Cliente>.md`
5. `Enquadramento Credito - <Nome Cliente>.md`
6. `Analise Financeira - <Nome Cliente>.md`
7. `Recomendacao Final - <Nome Cliente>.md`

O dossie mestre deve ser o primeiro lugar consultado e o ultimo lugar atualizado.
