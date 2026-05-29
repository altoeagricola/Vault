---
name: template-issue-filha
description: Template canônico para sub-issues em atividades multiagentes — garante que o agente receptor tenha contexto, escopo, critério de aceitação e protocolo de handoff explícito, eliminando paradas silenciosas na cadeia.
---

# template-issue-filha

Skill de referência para criar sub-issues bem estruturadas em atividades multiagentes. Garante que o agente receptor tenha tudo que precisa para começar imediatamente, **sem precisar de esclarecimentos**, e que ao concluir devolva sinal claro para a coordenadora **sem precisar ser caçado**.

## Quando usar
Sempre que criar uma issue para outro agente — seja diretamente pelo Multica ou via `multica issue create`. Use também ao revisar issues criadas que pareçam incompletas.

## Template obrigatório

```
[VERBO + QUEM + O QUÊ]
Exemplo: "Brasilino: analisar perfil de crédito do cliente João Silva"
Exemplo: "Mariano: simular impacto do Pronaf no fluxo de caixa safra 26"
```

### Corpo da issue

**Contexto**
[O que está acontecendo, qual é o projeto/caso, qual issue-mãe originou esta.]
Link para issue-mãe se houver: [MUL-XXX](mention://issue/<id>)

**Seu trabalho aqui**
[O que especificamente este agente precisa fazer. Seja direto e específico. Evite "analise e veja o que faz" — diga "gere o relatório X com os campos Y e Z".]

**Feito quando**
[Critério de aceitação verificável. O resultado precisa ter esta forma concreta:]
- [ ] [Item 1 concreto]
- [ ] [Item 2 concreto]

**Entradas disponíveis**
[Dados, documentos, links, comentários, resultados de etapas anteriores que o agente precisa.]
- Arquivo X em: ...
- Resultado do agente Y em: [comentário nesta issue / issue Z]
- Referência: ...

**Protocolo de handoff (obrigatório, copiar literalmente)**
- Ao concluir → postar comentário com a entrega **e** mover status para `in_review` (`multica issue status <id-desta-issue> in_review`).
- Se bloqueado → mover para `blocked` **e** mentionar a coordenadora (Carmen) com a razão concreta do bloqueio.
- Se runtime falhar (timeout, 502, skill quebrada, qualquer erro técnico) → postar comentário com o **erro literal** antes de exitar, mesmo que a entrega esteja incompleta. Filha silenciosa é tratada como falha pela coordenadora.

**Após concluir** *(opcional)*
[Próxima etapa esperada — quem recebe o resultado e o que faz com ele. Omitir se não souber.]
```

## Checklist antes de criar

- [ ] O título deixa claro quem faz e o quê?
- [ ] O critério de aceitação é verificável (não vago)?
- [ ] As entradas disponíveis estão listadas?
- [ ] O bloco **Protocolo de handoff** está incluído literalmente?
- [ ] O agente consegue começar imediatamente sem pedir mais informações?

## Regras de atribuição e disparo

- `--status todo` na criação → agente começa imediatamente. Esta é a forma confiável de disparar.
- `--status backlog` → aguarda promoção. **Atenção:** `multica issue status <id> todo` em filha que estava em `backlog` **NÃO dispara o agente assignee** — só `--status todo` na criação e mention em comentário disparam. Portanto, ao promover uma filha de `backlog`, sempre acompanhar a mudança de status de **um comentário com mention** do agente assignee + contexto curto do que foi destravado.
- Para séries obrigatórias (A→B→C): só o primeiro step vai como `todo`; os demais vão como `backlog` e são promovidos em cadeia (mudança de status + mention) à medida que cada step conclui.

## Pré-requisito: briefing operacional padrão em atividades grandes

Para qualquer atividade multiagente com 3+ filhas (ou 2+ paralelas com gates intermediários), a issue-mãe **deve** publicar antes das filhas um *briefing operacional* curto consolidando:
- objetivo único da atividade,
- base documental única (proibido cotejar versões antigas se a mãe não pediu),
- convenções fixas (unidades, vocabulário, escopo),
- protocolo de handoff (mesmo bloco acima),
- critério de pronto da entrega final.

O briefing reduz retrabalho na origem e elimina divergências interpretativas entre frentes. É pré-requisito, não opção.

## Não fazer

- Não criar filha sem o bloco Protocolo de handoff — coordenadora vai gastar tempo correndo atrás.
- Não promover filha de `backlog` para `todo` sem comentário+mention acompanhando — o agente não será disparado.
- Não criar filhas em cadeia serial todas como `todo` — só a primeira; as demais ficam `backlog` e sobem em cadeia.
