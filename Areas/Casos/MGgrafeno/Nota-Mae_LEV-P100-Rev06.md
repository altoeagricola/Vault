---
title: LEV-P100 Rev06 (Plentz-06) — Nota-Mãe
type: Case Summary
case_id: ALT-464
date: 2026-05-31
author: Carmen
status: concluido
root:
  - "[[MGgrafeno]]"
documento_final: "[[MGG3-LEV-P100-v10_Levantamento-Custos-Cenarios-Desenvolvimento-Producao-Consolidado]]"
documento_arquivado: "[[Products/MGg3/MGg2/Custos/Repositorio de versoes/MGG3-LEV-P100-v10_Levantamento-Custos-Cenarios-Desenvolvimento-Producao-Consolidado_PLENTZ05-ARQUIVADO|MGG3-LEV-P100-v10 Plentz05 arquivado]]"
issue_mae: ALT-464
issue_revisao_anterior: ALT-440
tags:
  - case
  - mggrafeno
  - lev-p100
  - nota-mae
  - rev06
---

# LEV-P100 Rev06 (Plentz-06) — Nota-Mãe

## Síntese Executiva

A Revisão Plentz-06 (ALT-464) corrigiu a principal limitação da v10 produzida na Revisão Plentz-05 (ALT-440): o relatório anterior havia reorganizado o material em dois cenários para o investidor, mas ao fazer isso perdeu 9 blocos técnico-analíticos da [[MGG3-LEV-P100-v9_Levantamento-Custos-Recomissionamento-Consolidado|v9]] — seções inteiras de premissas técnicas, CAPEX por pacotes, OPEX detalhado, glossário, rastreabilidade, gates SSMA e pendências controladas.

Esta revisão **restaurou todos esses blocos** e tornou a v10 uma sucessora cumulativa da v9, sem descontinuidade analítica. O arquivo final [[MGG3-LEV-P100-v10_Levantamento-Custos-Cenarios-Desenvolvimento-Producao-Consolidado]] (787 linhas) mantém o mesmo código de versão e path de produção; o draft anterior foi arquivado em `_PLENTZ05-ARQUIVADO.md`. Commit no Vault: `c294a1a`.

**O documento v10 (Rev06) está pronto para:**
- Apresentação técnica interna a Rodrigo e ao time
- Orientar planejamento de recomissionamento, orçamentação e priorização
- Leitura econômica preliminar para investidor ou banco, com ressalvas explícitas de §22

**O documento v10 (Rev06) ainda requer** RFQs, vistoria física, campanha gravimétrica e aprovações SSMA antes de uso contratual ou due diligence formal.

---

## Dados do Caso

- **Contexto:** MGgrafeno / P100. Corrigir a v10 Plentz-05 restaurando os 9 blocos técnicos perdidos, mantendo os dois cenários operacionais e tornando v10 sucessor sequencial da v9.
- **Demanda original:** "quero que o relatório v10 seja versão sequencial do v9, e não um relatório irmão" — Rodrigo, 2026-05-30.
- **Período de execução:** 2026-05-30 a 2026-05-31 (16 sub-issues, 1 dia).
- **Documento final:** [[MGG3-LEV-P100-v10_Levantamento-Custos-Cenarios-Desenvolvimento-Producao-Consolidado]] (787 linhas, commit `c294a1a`).
- **Documento arquivado:** [[Products/MGg3/MGg2/Custos/Repositorio de versoes/MGG3-LEV-P100-v10_Levantamento-Custos-Cenarios-Desenvolvimento-Producao-Consolidado_PLENTZ05-ARQUIVADO|MGG3-LEV-P100-v10 Plentz05 arquivado]] — preservado como leitura alternativa focada no investidor, sem as bases técnicas reincorporadas.
- **Bases:** [[MGG3-LEV-P100-v9_Levantamento-Custos-Recomissionamento-Consolidado]] (intocada como referência histórica); Nota-Mãe Plentz-05 em [[Nota-Mae_LEV-P100-v10]].

---

## Blocos Reincorporados da v9

| Bloco | Seção v10 | Responsável | Observação |
|---|---|---|---|
| §4.1–§4.5 — Premissas técnicas e ciclo | §4.1–§4.5 | Valdemiro (F2.1 / ALT-468) | Ciclo 10,75 h e parâmetros por cenário adicionados |
| §5 — CAPEX por pacotes AACE Cl.4/5 | §5 | Julio (F2.2 / ALT-469) | Tabela de pacotes restaurada |
| §6.1–§6.6 — OPEX detalhado | §6.1–§6.6 | Julio (F2.2 / ALT-469) | Equipe 8×5, CQ US$5k/mês, matérias-primas, utilidades, manutenção, exclusões |
| §7 — Benchmark de indiretos de mercado | §7 | Eloi (F2.3 / ALT-470) | Tabela min/médio/máx ampliada com fontes auditáveis |
| §3 — Glossário 26 termos v9 | §3 | Cacilda (F2.4 / ALT-471) | 26 termos v9 + novos termos v10 (campanha, alocação 4:2:1, cenários) |
| §11 — Gates SSMA e compliance | §11 | Tereza (F2.5 / ALT-472) | Tabela com NRs, linha de bloqueio operacional preservada |
| §12 — Rastreabilidade (19 linhas v9 → 43) | §12 | Julio + Valdemiro (F2.6 / ALT-473) | 19 linhas v9 + 24 linhas dos cenários |
| §22 — Pendências controladas | §22 | Tereza (F2.5 / ALT-472) | Tabela v9 restaurada + pendências específicas de Produção |

---

## Números-Chave do Documento Final

| Indicador | Valor |
|---|---:|
| CAPEX incremental de recomissionamento | R$ 610.000 (AACE Cl.4/5, faixa R$ 430–915k) |
| Base bruta histórica dos equipamentos | R$ 1.680.560 (planilha 2021) |
| OPEX caixa recorrente (base v9) | R$ 2.396.908/ano |
| OPEX técnico completo (base v9) | R$ 2.563.484/ano |
| Custo médio v9 por kg | R$ 249/kg (10.315 kg/ano nominais) |
| **Cenário Desenvolvimento — OPEX caso-base** | **R$ 4.094.400/ano** (faixa R$ 3,65–4,84 MM) |
| **Cenário Produção — OPEX caso-base** | **R$ 2.481.000/ano** |
| Custo por produto — GPC | R$ 895/kg |
| Custo por produto — NPG | R$ 448/kg |
| Custo por produto — Nanografite | R$ 224/kg |

---

## Decisões Editoriais Tomadas

| Decisão | Justificativa |
|---|---|
| Manter o mesmo código v10 e path de produção | v10 é o código canônico do relatório; a descontinuidade estava no conteúdo, não no código |
| Arquivar a v10 Plentz-05 com sufixo `_PLENTZ05-ARQUIVADO` | Preserva o trabalho de cenários para investidor como leitura alternativa sem poluir o path de produção |
| Tratar a reconciliação CFO como "resolvida" (não mais pendente) | Julio (F2.2) realizou a reconciliação em §10; a nota "premissas CFO ainda pendentes" da Plentz-05 foi removida |
| Dois cenários operacionais não-misturáveis | A confusão entre Desenvolvimento e Produção gera análise econômica equivocada — explicitado em §1 |
| Alocação por complexidade 4:2:1 em Produção | GPC é produto de maior esforço técnico; método mais defensável que alocação por massa pura |

---

## Revisões Aplicadas (F4)

Todas as quatro revisões aprovaram sem bloqueio:

| Frente | Issue | Revisor | Decisão | Foco |
|---|---|---|---|---|
| F4.1 — Técnica | ALT-475 | Valdemiro | ✅ Go | Premissas técnicas e ciclo de 10,75 h coerentes com §4.1–§4.5 reincorporados |
| F4.2 — Econômica | ALT-476 | Julio | ✅ Go | CAPEX, OPEX e reconciliação v9↔v10 íntegros; indicadores unitários fechados em §10 |
| F4.3 — Compliance | ALT-477 | Tereza | ✅ Go | Gates SSMA presentes e com bloqueio explícito; linguagem de "infraestrutura piloto" preservada |
| F4.4 — Vault/Terminologia | ALT-478 | Cacilda | ✅ Go | Frontmatter completo; glossário 26+9 termos em ordem alfabética; wiki-links operando |

---

## Pendências Controladas (Prioridade Alta)

As pendências abaixo não impedem uso como relatório de planejamento, mas impedem uso contratual ou due diligence.

| Pendência | Prioridade |
|---|---|
| Validação do módulo de separação para 200 L (ciclo 10,75 h) | Alta |
| Vistoria física da P100 | Alta |
| RFQs / cotações formais para converter R$ 610k em orçamento contratável | Alta |
| Protocolo de comissionamento frio, quente e SAT | Alta |
| Campanha gravimétrica pós-recomissionamento (validar rendimentos D2) | Alta |
| Matriz NR-12/SSMA por equipamento | Alta |
| Licença/dispensa ambiental e enquadramento de resíduos | Alta |

Lista completa em §22 do documento.

---

## Próximos Passos

- [ ] Rodrigo ler a v10 e decidir sobre apresentação ao banco / investidor — imediato.
- [ ] Agendar vistoria física da P100 — Rodrigo / Valdemiro — antes de converter R$ 610k em orçamento.
- [ ] Solicitar RFQs para pacotes de recomissionamento — Rodrigo / Julio — antes de compromisso financeiro.
- [ ] Executar campanha gravimétrica pós-recomissionamento — Valdemiro — valida ou invalida rendimentos D2.
- [ ] Resolver lacunas de plataforma D.1/D.2/D.5/D.6 para que a próxima revisão multiagente flua sem intervenção manual — ver ALT-456, ALT-458, ALT-481, ALT-482.

---

## Rastreabilidade Completa

- **Issue-mãe:** [ALT-464](mention://issue/e3b93760-b3d1-4468-ab0e-544991700023)
- **Revisão anterior:** [ALT-440](mention://issue/4edaa80f-47b0-4309-b732-3e99ca5f9d68) + [[Nota-Mae_LEV-P100-v10]]

| Fase | Issue | Assignee | Entrega |
|---|---|---|---|
| F0 — Estrutura-alvo v10 | [ALT-465](mention://issue/447ac547-6079-4350-92e6-441c91a0e503) | Carmen | Estrutura de 22 seções e mapa de reincorporação |
| F1.1 — Inventário de blocos | [ALT-466](mention://issue/f0520698-b1e9-40a7-85e1-254350010c51) | Carmen | Lista formal de 9 blocos a reincorporar com gap por omissão |
| F1.2 — Mapeamento de premissas | [ALT-467](mention://issue/7e482ee8-564d-4242-8836-2c47d4016c16) | Valdemiro | Tabela mantém/qualifica/reconcilia/descarta por premissa técnica |
| F2.1 — §4.1–§4.5 técnicas | [ALT-468](mention://issue/432a64f1-7aa8-40fa-b385-50527c13c985) | Valdemiro | Blocos de premissas, ciclo e parâmetros reincorporados |
| F2.2 — CAPEX, OPEX e reconciliação | [ALT-469](mention://issue/98da17bf-f801-43ab-b31f-e3cef93f46af) | Julio | §5, §6.1–§6.6, §10 reconciliação v9↔v10 |
| F2.3 — Indiretos de mercado | [ALT-470](mention://issue/44323d04-01c4-476e-848b-b239cc4af1e8) | Eloi | Benchmark 2026 com fontes auditáveis |
| F2.4 — Glossário | [ALT-471](mention://issue/c4709a22-065d-473c-a080-4447e227c8dd) | Cacilda | 26 termos v9 + termos v10 |
| F2.5 — Gates SSMA e pendências | [ALT-472](mention://issue/cb0eba0b-a456-4a20-af8b-950dd5076d79) | Tereza | §11 com NRs + §22 pendências controladas |
| F2.6 — Rastreabilidade §12 | [ALT-473](mention://issue/27df4ad9-137a-4121-8d70-09bdee0b4007) | Julio + Valdemiro | 43 linhas (19 v9 + 24 v10) |
| F3 — Síntese editorial | [ALT-474](mention://issue/6067b916-e710-41ac-bebe-7ba29472a28b) | Carmen | Documento integrado 787 linhas; §21 changelog; decisões editoriais |
| F4.1 — Revisão técnica | [ALT-475](mention://issue/694f4ff1-90b8-4c8e-bff9-d44c4f6729e1) | Valdemiro | Go |
| F4.2 — Revisão econômica | [ALT-476](mention://issue/c7f55221-5bca-4a8c-86f5-8ecfbe0781ff) | Julio | Go |
| F4.3 — Revisão compliance | [ALT-477](mention://issue/c47b7406-fbd6-48eb-9900-3a785ac13c3f) | Tereza | Go |
| F4.4 — Revisão Vault/terminológica | [ALT-478](mention://issue/d4af60b5-b734-4a6c-a889-27d31c717aed) | Cacilda | Go |
| F5.1 — Escrita final no Vault | [ALT-479](mention://issue/85736fc1-7449-4fd2-8526-6e6c4f790fe4) | Cacilda | Commit `c294a1a`; v10 anterior arquivada |
| F5.2 — Esta nota-mãe | [ALT-480](mention://issue/cc124008-c164-4b13-9b5e-79c5cecd11fe) | Carmen | Este arquivo |
