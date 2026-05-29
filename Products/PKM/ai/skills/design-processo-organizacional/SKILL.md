---
name: design-processo-organizacional
description: Desenha ou revisa processos organizacionais da ALTOE — RACI, cadência operacional, protocolos de handoff, fluxos de trabalho, gates entre fases. Use quando o usuário pedir desenho de processo, revisão de fluxo, matriz RACI, definição de cadência, mapeamento de responsabilidades, ou quando uma retrospectiva apontar processo com falha estrutural.
---

# Design de Processo Organizacional

Skill de Carmen para padronizar como processos da ALTOE são desenhados, documentados e revisados. Aplica-se a qualquer processo recorrente — operacional, de decisão, de comunicação, de revisão.

## Workflow

### Step 1: Diagnóstico

1. Identificar o processo que será desenhado/revisado:
   - É processo novo (nunca formalizado) ou existente?
   - Onde foi observada a necessidade? (retrospectiva, falha do Piloto 001, demanda nova)
   - Qual problema ele resolve? Qual sintoma seria eliminado?
2. Mapear estado atual:
   - O que acontece hoje informalmente?
   - Quem faz o quê? Onde há ambiguidade?
   - Onde está o gap (falta gate, falta dono, falta artefato)?

### Step 2: Escolher o Artefato Adequado

Nem todo processo precisa do mesmo formato. Escolher:

| Necessidade | Artefato |
|---|---|
| Definir responsabilidades em decisão multipessoa | **Matriz RACI** |
| Definir ritmo de execução repetida | **Cadência operacional** (diária/semanal/mensal) |
| Definir passagem de bastão entre agentes | **Protocolo de handoff** |
| Definir sequência de fases com gates | **Fluxo de trabalho com gates** |
| Definir critério de qualidade de entrega | **Template de entrega + checklist de aceitação** |
| Definir resposta a evento (vencimento, alerta) | **Playbook reativo** |

Mais de um artefato pode coexistir (ex: fluxo + RACI + templates).

### Step 3: Desenhar com Princípios Claros

Princípios não-negociáveis:
1. **Cada passo tem um dono único.** Responsabilidade compartilhada = responsabilidade nenhuma.
2. **Cada decisão tem um critério explícito.** "Quando X for verdadeiro, fazemos Y."
3. **Gates bloqueiam, não orientam.** Se um gate é violável "em casos especiais", não é gate.
4. **Handoffs têm formato declarado.** O que sai do agente A entra estruturado para o agente B.
5. **Toda saída tem critério de pronto.** Sem isso, retrabalho infinito.
6. **Quanto mais simples, melhor.** Processo bonito que ninguém segue é decoração.

### Step 4: Materializar em Markdown Estruturado

Padrão para registro no Vault (`Areas/Processos/<nome>.md`):

```markdown
---
title: <Nome do Processo>
type: Process Design
author: Carmen
status: <draft | active | superseded>
created: YYYY-MM-DD
updated: YYYY-MM-DD
applies_to: [casos / agentes / fases]
---

# <Nome do Processo>

## Objetivo
Uma frase: o que esse processo garante.

## Quando se aplica
Gatilhos / contexto.

## Atores
Lista dos agentes/papéis envolvidos.

## Fluxo / RACI / Cadência
(escolher artefato conforme Step 2)

## Gates / Critérios de Pronto
Lista bloqueante.

## Artefatos gerados
Saídas obrigatórias.

## Registros e Rastreabilidade
Onde fica registrado, como auditar.

## Histórico de Revisões
| Data | Versão | Mudança | Motivo |
```

### Step 5: Validar com o Time

Antes de marcar como `active`:
- Apresentar ao Rodrigo o desenho proposto.
- Validar com agentes afetados (especialmente quem é dono de cada passo).
- Pilotar em 1 caso real antes de marcar como padrão.
- Registrar feedback e ajustar.

### Step 6: Registrar no Vault e Comunicar

- Delegar à Cacilda o registro do arquivo em `Areas/Processos/`.
- Atualizar `Areas/ALTOE Agricola/Estrutura de Agentes IA.md` se o processo afetar papéis.
- Comunicar mudança no time (issue dedicada ou comentário em issue de retrospectiva).

## Triggers

- "desenha o processo"
- "monta o RACI"
- "define a cadência"
- "como o time deve fazer X"
- "revê o fluxo"
- Retrospectiva apontou processo com falha estrutural

## Notas

- Resista ao impulso de over-engineering. Processo deve ser proporcional ao problema.
- Documentar **por que** o processo existe é tão importante quanto **como** ele funciona.
- Processo sem dono de manutenção apodrece. Definir quem revisa e quando.
- Quando substituir processo antigo, marcar o anterior como `superseded` com link para o novo.