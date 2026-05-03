---
tipo: Referência Operacional
contexto: "[[ALTOE Agricola]]"
status: rascunho — aguardando revisão do Rodrigo
origin: "Carmen — ALT-46 (2026-05-03)"
created: 2026-05-03
atualizado: 2026-05-03
relacionado:
  - "[[Design — Matriz de Handoff entre Agentes]]"
  - "[[Estrutura de Agentes IA]]"
---

# Design — Matriz RACI por Processo

Documento operacional que define, por tipo de processo, quem é **Responsável (R)**, **Aprovador (A)**, **Consultado (C)** e **Informado (I)** na equipe de agentes da ALTOE Agricola.

> **Status:** Rascunho. Sujeito a revisão e validação pelo Rodrigo antes de ser tratado como oficial.

---

## Legenda

| Sigla | Papel | Descrição |
|-------|-------|-----------|
| **R** | Responsável | Executa a tarefa — há sempre ao menos um R por processo |
| **A** | Aprovador | Valida ou decide — ponto de autoridade; há um único A por processo |
| **C** | Consultado | Fornece input antes ou durante a execução; comunicação bidirecional |
| **I** | Informado | Recebe o resultado; comunicação unidirecional |

---

## Agentes e Papéis

| Agente | Papel |
|--------|-------|
| **Rodrigo** | Fundador / Aprovador estratégico |
| **Brasilino** | Analista de Crédito Rural |
| **Alberico** | Captador de Fomento |
| **Mariano** | Coach Financeiro do Produtor |
| **Eloi** | Inteligência de Mercado |
| **Marta** | CRM e Relacionamento |
| **Tereza** | Compliance Documental |
| **Cacilda** | Curadora do Vault |
| **Carmen** | Design de Processos |

---

## Matriz RACI

| Processo | Rodrigo | Brasilino | Alberico | Mariano | Eloi | Marta | Tereza | Cacilda | Carmen |
|----------|---------|-----------|----------|---------|------|-------|--------|---------|--------|
| Submissão de projeto de crédito rural | A | R | — | C | I | C | C | I | — |
| Monitoramento de vencimento documental de produtores | A | C | — | — | — | I | R | I | — |
| Monitoramento de vencimento documental de parceiros (ICTs, bancos) | A | — | C | — | — | C | R | I | — |
| Rastreabilidade de contratos de parceria | A | — | C | — | — | C | R | I | — |
| Rastreabilidade de contratos de crédito | A | R | — | C | — | I | C | I | — |
| Submissão de proposta de fomento | A | C | R | — | C | I | C | I | C |
| Alerta de sinal de mercado (clima, preço, política pública) | A | C | C | I | R | I | — | I | — |
| Onboarding de novo cliente/produtor | A | C | — | C | I | R | C | I | — |
| Regularização documental de produtor | A | C | — | — | — | C | R | I | — |

---

## Detalhamento por Processo

### 1. Submissão de projeto de crédito rural (Pronaf, Pronamp, etc.)

**Quem executa:** Brasilino  
**Quem aprova:** Rodrigo  
**Quem é consultado:** Marta (perfil do cliente via CRM), Tereza (conformidade documental), Mariano (capacidade de pagamento e margem do produtor)  
**Quem é informado:** Marta (atualiza CRM com resultado), Cacilda (registra operação no Vault), Eloi (para correlação com contexto de mercado)

---

### 2. Monitoramento de vencimento documental de produtores

**Quem executa:** Tereza — monitora CNH, certidões, IRPF, CCIR de forma proativa  
**Quem aprova:** Rodrigo — quando o vencimento bloqueia uma operação ativa  
**Quem é consultado:** Brasilino — informa quais documentos são obrigatórios por banco e linha de crédito  
**Quem é informado:** Marta (impacto no relacionamento e comunicação com o produtor), Brasilino (impacto na operação de crédito), Cacilda (Vault)

---

### 3. Monitoramento de vencimento documental de parceiros (ICTs, bancos)

**Quem executa:** Tereza — rastreia certidões, contratos e habilitações de ICTs e parceiros comerciais  
**Quem aprova:** Rodrigo  
**Quem é consultado:** Alberico (para parcerias ICT vinculadas a projetos de fomento), Marta (para parcerias comerciais no CRM)  
**Quem é informado:** Alberico (impacto nos projetos de fomento), Cacilda (Vault)

---

### 4. Rastreabilidade de contratos de parceria

**Quem executa:** Tereza — monitora alterações, vigência e cláusulas relevantes  
**Quem aprova:** Rodrigo  
**Quem é consultado:** Alberico (contratos ICT e fomento), Marta (contratos comerciais)  
**Quem é informado:** Cacilda (Vault), Brasilino (se afeta operações de crédito)

---

### 5. Rastreabilidade de contratos de crédito

**Quem executa:** Brasilino — acompanha cronograma, parcelas, garantias e aditivos  
**Quem aprova:** Rodrigo  
**Quem é consultado:** Tereza (conformidade de alterações contratuais), Mariano (impacto no fluxo de caixa do produtor)  
**Quem é informado:** Marta (atualiza CRM), Cacilda (Vault)

---

### 6. Submissão de proposta de fomento (FAPES, FINEP, CNPq, etc.)

**Quem executa:** Alberico — varredura de editais, matching, estruturação e submissão  
**Quem aprova:** Rodrigo  
**Quem é consultado:** Brasilino (quando a proposta cruza com crédito rural), Eloi (contexto de políticas públicas relevantes), Carmen (revisão de estrutura e fluxo da proposta)  
**Quem é informado:** Marta (parceiros envolvidos, atualização do CRM), Cacilda (registra proposta no Vault), Tereza (conformidade documental da proposta)

---

### 7. Alerta de sinal de mercado (clima, preço, política pública)

**Quem executa:** Eloi — monitora e sintetiza sinais de CONAB, CEPEA, INMET, MAPA, BCB  
**Quem aprova:** Rodrigo — valida relevância estratégica e define ação  
**Quem é consultado:** Brasilino (linhas de crédito ativadas pelo sinal), Alberico (editais e políticas emergentes)  
**Quem é informado:** Marta (impacto nos clientes ativos — aciona CRM), Mariano (impacto financeiro na carteira), Cacilda (Vault), Carmen (se sinal implica redesenho de processo)

---

### 8. Onboarding de novo cliente/produtor

**Quem executa:** Marta — conduz o processo, preenche CRM, identifica oportunidades e próximas ações  
**Quem aprova:** Rodrigo  
**Quem é consultado:** Brasilino (perfilamento de crédito inicial), Mariano (perfil econômico-financeiro mínimo), Tereza (checklist documental por banco-alvo)  
**Quem é informado:** Cacilda (Vault), Eloi (sinais de mercado relevantes para o perfil daquele produtor), Carmen (para identificar ajustes de processo)

---

### 9. Regularização documental de produtor

**Quem executa:** Tereza — identifica pendências, monitora prazo, confirma regularização  
**Quem aprova:** Rodrigo — em casos que bloqueiam operação ativa  
**Quem é consultado:** Brasilino (quais documentos desbloqueiam qual operação), Marta (canal de comunicação com o produtor)  
**Quem é informado:** Marta (status para CRM e comunicação com o cliente), Brasilino (liberação para submissão), Cacilda (Vault)

---

## Regras Gerais de Operação

1. **Todo alerta com impacto operacional imediato** deve incluir: quem é afetado, qual operação, qual o prazo.
2. **Cacilda é sempre informada** quando um processo gera ou atualiza uma nota no Vault.
3. **Rodrigo aprova** apenas em pontos de decisão estratégica ou quando uma operação ativa é bloqueada.
4. **Carmen é consultada** em redesenhos de processo — não em execuções rotineiras.
5. **Conflito de RACI** (mais de um R, A ausente) deve ser escalado via issue para Carmen resolver.
