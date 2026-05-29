---
name: onboarding-agente
description: Conduz o processo de incorporar um agente novo ao time da ALTOE — revisa definição, sugere modelo de IA, propõe skills, registra em Estrutura de Agentes IA e cria as primeiras issues de calibragem. Use quando Rodrigo decidir adicionar um agente novo ao time.
---

# Onboarding de Agente

Skill de Carmen para padronizar a incorporação de um agente novo ao time multiagente da ALTOE. Garante que cada agente entra com identidade clara, ferramentas adequadas e integração registrada.

## Workflow

### Step 1: Validar a Definição de Identidade

Antes de criar o agente na plataforma, validar com Rodrigo:

1. **Nome e descrição curta:** persona, formação, traços marcantes.
2. **Papel funcional:** o que esse agente é responsável por fazer? Onde sua atribuição começa e termina?
3. **Por que precisa existir:** que demanda recorrente justifica? Que gap fechado? (Se não houver resposta clara, **questionar antes de seguir**.)
4. **Personalidade e linguagem:** tom de comunicação, traços, signo (padrão da ALTOE).
5. **Não-sobreposição:** verificar que esse papel não duplica nem amputa atribuição de agente existente.

Se algum item estiver indefinido, conduzir conversa com Rodrigo para fechar antes de avançar.

### Step 2: Sugerir o Modelo de IA

Critérios de escolha:

| Workload predominante | Modelo recomendado |
|---|---|
| Coordenação, design, síntese executiva, escrita estratégica | Opus (mais caro, mais profundo) |
| Análise técnica, ingestão estruturada, pesquisa rotineira | Sonnet (equilíbrio) |
| Tarefas reativas, triagem, classificação simples | Haiku (rápido, barato) |
| Casos específicos onde outro provedor agrega | GPT, Gemini (justificar) |

Apresentar a recomendação com justificativa e aguardar aval do Rodrigo.

### Step 3: Propor Skills do Agente

Olhar para skills existentes em `Products/PKM/ai/skills/` e classificar:

1. **Skills existentes que servem:** atribuir as que cabem ao papel.
2. **Skills existentes que servem com adaptação:** sinalizar que adaptação seria necessária.
3. **Skills novas a criar:** propor com nome, descrição, justificativa.

Apresentar tabela comparativa antes de criar qualquer skill nova:

| Skill | Tipo | Justificativa |
|---|---|---|
| <nome> | existente / nova | Por que esse agente precisa |

Aguardar aprovação. **Não criar skills sem aval.**

### Step 4: Criar o Agente na Plataforma

1. Usar `multica agent create` (ou processo equivalente da Multica).
2. Preencher: nome, descrição, instruções (persona completa), modelo, max_concurrent_tasks padrão (6).
3. Capturar UUID retornado.
4. Verificar via `multica agent list --output json`.

### Step 5: Atribuir Skills

1. Para skills existentes: usar `multica agent skills set <agent-id> --skill-ids <ids>`.
2. Para skills novas: criá-las primeiro (`multica skill create`), depois atribuir.
3. Confirmar atribuição.

### Step 6: Registrar no Vault

Delegar à Cacilda:
- Atualizar `Areas/ALTOE Agricola/Estrutura de Agentes IA.md` com o novo agente (linha na tabela de Perfis dos Agentes, com Skills, Modelo, Papel).
- Se houver pasta de produtos relacionada (`Products/<área>/`), registrar referência ao novo agente.
- Manter padrão organizacional já estabelecido (skills atribuídas formalmente listadas, não planejadas).

### Step 7: Criar Issues de Calibragem

Para os primeiros casos do agente, criar issues de teste/calibragem:
- Issue de "Onboard de <Nome>" com primeiras tarefas.
- Issue de retrospectiva agendada (após 2-3 entregas reais) para validar se a definição funcionou.

### Step 8: Comunicar ao Time

Postar comentário em issue dedicada ou em `Estrutura de Agentes IA` informando:
- Novo agente, papel, skills.
- Quem deve acioná-lo e em que situações.
- Limites de atribuição (o que ele NÃO faz, para evitar sobreposição).

## Triggers

- "onboarding de agente"
- "novo agente no time"
- "vamos criar um agente para X"
- "incorpora o agente Y"
- Conclusão de retrospectiva que sinaliza necessidade de novo papel
- Sinalização proativa de Carmen sobre gatilho arquitetural

## Notas

- Onboarding bem feito é investimento; mal feito gera ruído de coordenação por meses.
- Não criar agente "porque seria legal". Criar quando demanda recorrente justifica.
- Sempre validar com Rodrigo antes de criar agente ou skill nova — é decisão estratégica e de custo.
- Persona é parte do design: agente sem identidade clara não comunica com tom consistente.
- Após onboarding, agendar retrospectiva curta após primeiras entregas para validar a definição.