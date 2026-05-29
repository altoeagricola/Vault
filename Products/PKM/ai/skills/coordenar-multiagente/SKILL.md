---
name: coordenar-multiagente
description: Conduz trabalho multiagente em fluxo contínuo — varredura proativa de paradas, sincronização de status mãe↔filhas, desbloqueio em cadeia, delegação com mention sem loop, escalação a humano e fechamento. Use sempre que houver issue-mãe com filhas, handoff entre agentes, dependência serial/paralela, ou quando Carmen for acionada sem pedido específico (varredura periódica). Triggers: "coordena com X e Y", "pega isso com o time", "leva isso pra frente", continuação de `planejar-atividades-time`, comentário em issue-mãe onde Carmen é dona da coordenação.
---

# Coordenar Multiagente

Skill que conduz trabalho colaborativo entre agentes em fluxo contínuo, com status sincronizado entre issue-mãe e filhas e mínima dependência de supervisão humana. Issue parada é falha de coordenação, não estado neutro.

## Princípios

1. **Fluxo > status descritivo.** Cada execução da skill encerra com fluxo ativo ou escalação explícita; nunca com "esperando".
2. **Mãe espelha filhas.** Status da issue-mãe sempre reflete o agregado das filhas — atualizar antes de sair.
3. **Pull, não push do Rodrigo.** Carmen varre proativamente; não espera ser pedida.
4. **Silêncio termina; `@` reinicia.** Default = não mencionar. Mention só em delegação nova, escalação humana ou desbloqueio explícito.

## Modos de Ativação

A skill opera em quatro modos. Detectar qual está em jogo antes de agir.

- **Modo A — Demanda nova.** Gatilho: pedido com escopo multiagente, saída de `planejar-atividades-time`, ou issue-mãe criada. Entrar em Steps 1→2.
- **Modo B — Resposta de agente/usuário.** Gatilho: comentário novo em issue onde Carmen é dona. Entrar em Steps 4→7→8.
- **Modo C — Varredura proativa (sweep).** Gatilho: execução periódica (cron) ou final de qualquer ação multiagente. Entrar em "Sweep de Fluxo" abaixo. É a defesa principal contra paradas.
- **Modo D — Loop operacional ativo.** Gatilho: atividade multiagente "grande" em curso (ver critérios abaixo). Carmen mantém pulso próprio via `/loop` com self-pacing dinâmico, varrendo a cadeia em alta frequência enquanto há filhas ativas e espaçando em fases de espera externa. Sai do loop quando todas as frentes fecham.

Antes de fechar qualquer execução em qualquer modo, **sempre** rodar o Sweep abreviado nas issues-mãe ativas (ver abaixo).

### Quando ativar o Modo D (loop operacional B.1)

Ativar `/loop` no início da execução **apenas** quando a atividade satisfaz pelo menos um dos critérios:
- 3+ filhas em execução paralela simultânea, ou
- 5+ filhas em cadeia serial-paralela com mais de um gate intermediário, ou
- Pedido explícito do Rodrigo de "manter o pulso" em atividade específica.

Para atividades menores (1-2 filhas, sem gates), seguir reativa — o custo de tokens do loop não compensa.

### Self-pacing dentro do Modo D

Carmen escolhe o intervalo do próximo despertar pelo estado da cadeia, não por relógio fixo:

| Estado da cadeia | Próximo despertar |
|---|---|
| Filha ativa há < 5 min (acabou de ser disparada) | 120–180 s — espera primeiro sinal |
| Múltiplas filhas em execução simultânea | 180–270 s — janela curta, fica em cache |
| 1 filha em execução, sem novidade recente | 600–900 s |
| Esperando decisão humana (Rodrigo, cliente) | 1800–3600 s — espaçar agressivamente |
| Nenhuma filha ativa, tudo em `done` | sair do loop |

Princípio: cache da Anthropic tem TTL de 5 min — abaixo disso o despertar é barato; acima de 5 min vale pagar o cache miss apenas se a espera for genuinamente longa.

## Workflow

### Step 1: Estabelecer Quem Faz O Quê

Antes de acionar qualquer agente, ter claro:
- **Dono** da próxima entrega.
- **Conteúdo mínimo** dessa entrega (formato e campos).
- **Quem depende dela** e por quê.
- **Prazo** ou "assim que possível".

Se algo estiver indefinido, resolver antes de delegar. Não delegar com escopo vago.

### Step 2: Delegar com Mention Estruturada

Mention `[@Nome](mention://agent/<uuid>)` apenas quando:
- For a **primeira** delegação concreta para o agente naquela issue.
- Houver pedido **acionável** (não acknowledgement, não thanks).
- O escopo estiver claro para execução sem perguntar.

Formato padrão:

```
[@Nome](mention://agent/<uuid>), preciso de [entrega] até [prazo].

Contexto:
- [link para fonte/issue mãe]
- [dados de entrada já disponíveis]

Saída esperada:
- [campos mínimos / formato]

Próximo passo após sua entrega: [quem usa, para quê]
```

Ao criar sub-issues: paralelas com `--status todo`; seriais com primeira `todo` e demais `--status backlog` (promovidas via Step 8).

**Atenção — assimetria de trigger do backend:** `multica issue status <id> todo` em filha que estava em `backlog` **NÃO dispara o agente assignee**. Só `--status todo` na criação e mention em comentário disparam. Portanto: ao promover uma filha de `backlog`, **sempre** postar um comentário na filha com mention do agente + contexto curto. Mudar status sozinho é cosmético.

### Step 3: Follow-up Sem Loop

Regra de ouro: **re-acionar só se houver entrega ou pergunta nova**.

- Respondeu mas não entregou → lembrete direto, **sem @mention**.
- Entregou parcial → pedir o que falta, sem @mention.
- Entregou completo → registrar e seguir, sem agradecer com @.
- Travou/bloqueou → Step 5.

### Step 4: Integrar Entregas

Conforme cada agente entrega:
- Citar/anexar a entrega na issue-mãe.
- Verificar coerência: output do agente A serve para o agente B?
- Inconsistência → resolver antes de passar adiante (não empurrar problema).
- Atualizar Painel de Status (ver abaixo).

### Step 5: Escalar ao Rodrigo

Escalar quando:
- Decisão de negócio fora do escopo de qualquer agente (preço, parceiro, prioridade).
- Dois agentes discordam e a divergência muda a conclusão.
- Gate (ex: Fase 0) não cumprido.
- Prazo em risco com necessidade de mudar escopo.
- SLA triplicado em filha sem resposta (ver tabela abaixo).

Forma: comentário direto na issue-mãe com `@mention` ao Rodrigo (humano), descrevendo impasse e propondo 2-3 caminhos. Nunca escalar sem proposta.

### Step 6: Fechar a Coordenação

Antes de marcar `done`:
1. Todas as filhas em `done` ou `cancelled` com justificativa.
2. Nota-mãe consolidada via `consolidar-nota-mae`, se o caso justificar.
3. Aprendizados via `retrospectiva-operacional`, se foi caso/piloto relevante.
4. Painel final na issue-mãe marcado como "Encerramento" com link para nota-mãe.

### Step 7: Sincronizar Status Mãe ↔ Filhas

Espelhamento obrigatório ao final de toda execução:

| Estado agregado das filhas | Status da mãe |
|---|---|
| Qualquer uma `in_progress` | `in_progress` |
| Nenhuma `in_progress` + ao menos uma `blocked` | `blocked` |
| Todas em `backlog` (não promovidas) | `todo` |
| Todas `done`/`cancelled` (pré-revisão de fechamento) | `in_review` |
| Fechada após Step 6 | `done` |

Aplicar via `multica issue status <mae-id> <novo-status>` quando divergir. Comentar a mudança no Painel.

### Step 8: Desbloqueio em Cadeia

Quando uma filha entra em `done`:
1. Varrer filhas em `backlog` cuja dependência era essa.
2. Para cada uma com dependências resolvidas: `multica issue status <child-id> todo` **e em seguida** postar comentário com mention do agente assignee + resumo do insumo recém-disponível. A mudança de status sozinha não dispara o agente.
3. Comentar na filha promovida o que foi destravado e qual insumo está disponível agora.

Promoção em cadeia é responsabilidade de Carmen — nunca esperar Rodrigo pedir.

## Sweep de Fluxo (Modo C, Modo D e fechamento de toda execução)

Em Modo C/D completo, ou em versão abreviada ao final de Modo A/B, Carmen executa:

1. **Listar issues-mãe ativas** sob coordenação de Carmen (status `todo`, `in_progress`, `blocked`).
2. Para cada uma, listar filhas e calcular:
   - **Última atividade real por filha** — timestamp do último comentário do agente assignee, *não apenas* mudança de status. Status pode estar desalinhado com a entrega real.
   - Status agregado esperado (Step 7).
   - Divergência mãe vs. agregado → corrigir.
3. **Detectar entregas com status preso.** Para cada filha em `todo` ou `in_progress` cujo último comentário do assignee sinaliza conclusão (palavras-gatilho: "entreguei", "concluí", "pronto", "feito", ou bloco de resultado estruturado), tratar como entregue. Mover manualmente para `done` e disparar o próximo gate. *Não* esperar o agente corrigir o handoff.
4. **Detectar filhas silenciosas.** Para cada filha disparada há > 15 min sem nenhum comentário do assignee, suspeitar de falha de runtime (timeout, 502, skill com frontmatter inválida). Re-acionar via mention com pedido de status; se persistir > 30 min, escalar ao Rodrigo com a suspeita explícita.
5. **Detectar paradas** pelos SLAs abaixo. Para cada parada, aplicar ação correspondente.
6. **Promover filhas desbloqueadas** (Step 8).
7. **Atualizar Painel de Status** em cada issue-mãe que mudou.
8. **Comentar resumo do sweep** na issue de coordenação raiz se houve ação relevante; silêncio se nada mudou.

### Checklist de fechamento de gate

Antes de promover a próxima frente após uma filha entregar:
1. Aceitar (`done`) a filha entregue.
2. Registrar a entrega no Painel de Status da mãe (link/resumo de uma linha).
3. Promover próxima filha (Step 8) — status `todo` **e** comentário com mention do agente + insumos.
4. Loggar no Painel: "Próxima frente disparada — <agente> em <ALT-X>".

Sem esse checklist, gates ficam parados silenciosamente.

### SLA de espera (default — encurtar quando houver prazo na issue-mãe)

| Situação | Tempo sem ação | Ação Carmen |
|---|---|---|
| Filha recém-disparada, nenhum comentário do assignee | 15 min | Re-mention curto pedindo status; suspeita de falha de runtime |
| Filha `todo` há > 30 min sem qualquer sinal | 30 min | Escalar ao Rodrigo com suspeita de falha de runtime |
| Filha `todo` recém-acionada com sinal de vida | 4h | Lembrete direto, sem `@` |
| Filha `in_progress` sem comentário novo | 24h | Lembrete direto, sem `@` |
| Filha `blocked` sem comentário do dono | 12h | Mention ao dono pedindo desbloqueio concreto |
| Lembrete já enviado, sem reação | +24h | Mention concreta ao dono com novo prazo |
| 2x SLA estourado após mention | +24h | Escalar ao Rodrigo (Step 5) |
| Issue-mãe sem painel atualizado | 24h | Atualizar painel no próximo sweep |

## Painel de Status (comentário fixo na issue-mãe)

Toda issue-mãe sob coordenação mantém um comentário-painel atualizado. Em cada sweep ou mudança relevante, postar nova versão na raiz da issue-mãe (não em thread), substituindo conceitualmente a anterior.

Formato:

```
**Painel — atualizado em <RFC3339>**

Objetivo: <uma frase>
Status agregado: <todo|in_progress|blocked|in_review|done>

Filhas:
- [ALT-X] <título> — <status> — dono <agente> — última atividade <ts> — <obs curta>
- ...

Bloqueios atuais: <lista ou "nenhum">
Próxima ação Carmen: <o que farei no próximo sweep e quando>
Aguardando do Rodrigo: <decisão pendente, ou "nada">
```

Se Rodrigo só ler uma coisa na issue-mãe, é o painel. Ele é a fonte rápida de status — manter sempre em dia é parte do contrato da skill.

## Não Fazer

- Não usar @mention para agradecer, confirmar leitura ou sinalizar fechamento.
- Não promover filhas em paralelo quando a issue-mãe declarou ordem serial.
- Não silenciar paradas — ausência de movimento é sinal, não estado neutro.
- Não usar status da mãe como decoração — ele tem que refletir o agregado.
- Não esperar instrução do Rodrigo para abrir sweep — sweep é rotina.
- Não fechar execução sem rodar o Sweep abreviado.
- Não confiar em `multica issue status backlog→todo` para disparar agente; sempre acompanhar de mention com contexto.
- Não varrer apenas por status — varrer por último comentário do assignee captura entregas com handoff perdido.
- Não tratar filha silenciosa como filha pensando — > 15 min sem comentário após disparo é suspeita de falha de runtime, age sobre isso.
- Não ativar o Modo D (loop) em atividades pequenas (1-2 filhas, sem gates) — o custo de tokens não compensa.

## Pré-requisito de harness para fluxo verdadeiramente contínuo

A skill descreve o protocolo. Duas camadas de cadência o sustentam:

**Curto prazo — Modo D (loop operacional):** durante atividade multiagente "grande", Carmen mantém pulso próprio via `/loop` com self-pacing dinâmico (ver tabela acima). É o mecanismo imediato contra paradas intra-tarefa.

**Médio prazo — cron de sweep (Modo C):** para defesa contra paradas longas em atividades pausadas, agente agendado executa Carmen periodicamente. A aprovar com Rodrigo via skill `schedule`:
- Frequência: a cada 4h em dias úteis, 1x/dia em fins de semana.
- Escopo: issues `in_progress` ou `blocked` onde Carmen é assignee.
- Saída: Painel atualizado em cada uma, com ações tomadas no comentário de raiz.

**Longo prazo — plataforma Multica:** pedidos abertos ao time da plataforma reduzem a necessidade do loop:
- Trigger automático em `backlog→todo` por mudança de status (hoje só dispara em criação/mention).
- Notificação automática quando run morre por timeout/502/skill inválida.
- Alerta de desalinhamento status×comentário do assignee.

Quando esses três pedidos saírem, o Modo D fica reservado a casos de cadeia muito densa; nas demais, o Modo C com sweep agendado é suficiente.
