---
name: planejar-atividades-time
description: Decompõe uma demanda do Rodrigo em uma árvore estruturada de issues do time, com agente dono, dependências, sequência e critério de aceitação por nó. Use quando o usuário trouxer um pedido amplo, projeto novo, caso operacional novo, ou disser "monta o plano", "quebra isso em issues", "distribui para o time", "como vamos atacar isso".
---

# Planejar Atividades do Time

Skill que padroniza como Carmen recebe uma demanda e a transforma em um plano executável distribuído pelo time multiagente da ALTOE.

## Workflow

### Step 1: Entender a Demanda

1. Ler o enunciado original na íntegra. Não resumir prematuramente.
2. Identificar:
   - **Objetivo final:** o que o Rodrigo realmente quer obter.
   - **Critério de pronto:** como saberemos que está concluído.
   - **Constraints:** prazo, custo, sensibilidade, dependências externas.
   - **Ambiguidades:** perguntas que precisam ser resolvidas antes de delegar.
3. Se houver ambiguidade material que mude o plano, **perguntar antes de planejar**. Não chutar.

### Step 2: Mapear Frentes de Trabalho

1. Quebrar a demanda em frentes paralelas e sequenciais.
2. Para cada frente, perguntar:
   - Qual agente é o dono natural? (consultar `multica agent list` se em dúvida)
   - É bloqueante para outras frentes?
   - Tem precondição (dado, documento, decisão prévia)?
3. Identificar gates: pontos que **devem** ser concluídos antes de outras frentes começarem (ex: Fase 0 — precondições documentais).

### Step 3: Montar a Árvore de Issues

Estrutura padrão:

```
Issue-mãe (a demanda original, dona: Carmen)
├── Issue Fase 0 — precondições (dona: Tereza ou Cacilda, conforme natureza)
├── Issue frente A (dona: agente especialista)
├── Issue frente B (dona: agente especialista)
└── Issue de consolidação final (dona: Carmen ou Cacilda — depende do output)
```

Para cada issue filha, definir:
- **Título:** verbo + objeto + escopo claro
- **Descrição:** contexto, entrada, saída esperada, critério de aceitação
- **Assignee:** agente dono
- **Parent:** referência à issue-mãe ou predecessora
- **Status inicial:** `todo` (ou `blocked` se depender de outra)
- **Prioridade:** mapear conforme bloqueio do conjunto

### Step 4: Apresentar o Plano

Antes de criar issues, apresentar o plano ao Rodrigo em formato de tabela na issue-mãe ou comentário:

| # | Frente | Dono | Depende de | Saída esperada | Status sugerido |
|---|---|---|---|---|---|

E perguntar se aprova ou ajusta. **Não criar issues filhas sem aval explícito**, exceto quando Rodrigo já tiver dado autorização prévia.

### Step 5: Criar Issues e Atribuir

Após aprovação:
1. Usar `multica issue create` para cada nó, com `--parent` apontando para a issue-mãe.
2. Atribuir com `--assignee-id` (preferir UUID via `multica agent list`).
3. Setar status inicial coerente: `blocked` para issues com dependência ativa.
4. Subscrever-se à issue-mãe para acompanhar o progresso (ou já estar como assignee).

### Step 6: Comunicar e Acompanhar

- Postar na issue-mãe o resumo do plano executado, com links para todas as issues filhas.
- Acompanhar progresso conforme protocolo da skill `coordenar-multiagente`.

## Triggers

- "monta o plano"
- "quebra isso em issues"
- "distribui para o time"
- "como vamos atacar isso"
- "preciso de um plano"
- Demanda ampla recebida sem decomposição prévia

## Notas

- Sempre apresentar o plano antes de criar issues, salvo autorização prévia explícita.
- Respeitar ordem: precondições → frentes especializadas → consolidação.
- Issue-mãe é minha (Carmen). Issues filhas vão para os especialistas.
- Não duplicar trabalho: se já existe issue ativa cobrindo a frente, referenciar em vez de recriar.