---
name: retrospectiva-operacional
description: Conduz retrospectiva ao final de um caso, projeto ou piloto — registra o que funcionou, gaps, sobreposições, ajustes de processo e recomendações para o próximo ciclo. Use quando um caso ou piloto for concluído ou quando Rodrigo pedir explicitamente.
---

# Retrospectiva Operacional

Skill de Carmen para fechar ciclos com aprendizado registrado. Sem retrospectiva, o time repete erros e perde ganhos.

## Workflow

### Step 1: Definir o Escopo da Retrospectiva

1. Qual ciclo está sendo fechado?
   - Caso operacional individual (um produtor, um edital, um projeto).
   - Piloto operacional (Piloto 001, 002, ...).
   - Sprint/ciclo temporal (mês, trimestre).
   - Marco específico (lançamento, decisão estratégica, mudança organizacional).
2. Quais agentes participaram? Quais issues estão no escopo?
3. Existe nota-mãe ou artefato consolidado de referência?

### Step 2: Coletar Sinais

1. **Issues envolvidas:** listar todas as issues filhas do ciclo (`multica issue list` filtrando por parent ou label).
2. **Tempos:** quando começou cada frente, quando terminou, onde houve atraso.
3. **Comentários relevantes:** ler comentários onde houve ajuste, dúvida, retrabalho ou bloqueio.
4. **Entregas:** comparar entrega real vs. critério de pronto declarado.
5. **Feedback humano:** se Rodrigo, cliente ou banco deram feedback, capturar.

### Step 3: Analisar em Quatro Dimensões

| Dimensão | Pergunta-chave |
|---|---|
| **O que funcionou** | Quais práticas geraram resultado e devem ser repetidas? |
| **Gaps** | O que faltou? (skill, dado, agente, processo, ferramenta) |
| **Sobreposições** | Onde dois ou mais agentes fizeram o mesmo trabalho ou competiram? |
| **Surpresas** | O que ninguém previu? (positivo ou negativo) |

Para cada item identificado, classificar:
- **Causa raiz:** processo, skill, dado, decisão humana, externo.
- **Impacto:** alto/médio/baixo.
- **Recorrência esperada:** problema único ou padrão.

### Step 4: Gerar Recomendações

Cada aprendizado deve virar **uma ação concreta**, não generalidade. Padrão:

| Aprendizado | Ação recomendada | Responsável | Prazo |
|---|---|---|---|

Tipos de ação típicos:
- Atualizar/criar skill (delegar criação).
- Ajustar processo (skill `design-processo-organizacional`).
- Atribuir skill já existente a agente que precisa.
- Corrigir lacuna documental no Vault.
- Sinalizar necessidade de novo agente (gatilho arquitetural).
- Ajustar instrução do agente.

### Step 5: Registrar no Vault

Padrão de arquivo: `Areas/Processos/Aprendizados/Aprendizados_<Ciclo>.md` (ou atualizar arquivo existente, ex: `Aprendizados_Operacionais_Piloto001.md`).

Estrutura padrão:

```markdown
---
title: Aprendizados — <Ciclo>
type: Retrospective
author: Carmen
ciclo: <identificador>
period: YYYY-MM-DD a YYYY-MM-DD
status: <draft | reviewed | actioned>
created: YYYY-MM-DD
---

# Aprendizados — <Ciclo>

## Contexto
Resumo do ciclo, escopo, participantes.

## O que Funcionou
- Item, com referência à evidência.

## Gaps Identificados
- Item, com causa raiz e impacto.

## Sobreposições
- Item, com agentes envolvidos.

## Surpresas
- Item, positivo ou negativo.

## Recomendações Acionáveis
| Aprendizado | Ação | Responsável | Prazo | Status |

## Sinais Arquiteturais
(seção opcional: gatilhos observados que indicam necessidade de novo agente, novo processo estruturante, ou mudança de modelo)

## Rastreabilidade
- Issues do ciclo
- Nota-mãe de referência
- Documentos relacionados
```

Delegar à Cacilda o registro do arquivo no Vault.

### Step 6: Comunicar e Acompanhar Implementação

- Postar resumo da retrospectiva na issue-mãe ou em issue dedicada.
- Para cada recomendação acionável, criar issue filha com responsável e prazo.
- Acompanhar implementação no próximo ciclo — abrir nova retrospectiva com referência cruzada.

## Triggers

- "retrospectiva"
- "lições aprendidas"
- "o que aprendemos"
- "fecha o piloto"
- "registra os aprendizados"
- Status `done` de issue-mãe relevante (caso, piloto, projeto)

## Notas

- Retrospectiva sem ação acionável é diário, não retrospectiva.
- Não procurar culpado: focar em sistema, não pessoa/agente.
- Sinalizar gatilhos arquiteturais (necessidade de novo agente, redesenho de processo) na seção dedicada — Carmen tem diretiva permanente de alertar Rodrigo nesses casos.
- Manter histórico: cada retrospectiva referencia a anterior. Aprendizado se acumula.