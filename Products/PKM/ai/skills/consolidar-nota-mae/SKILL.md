---
name: consolidar-nota-mae
description: Gera o documento único de resultado consolidado para um caso, projeto ou piloto — síntese executiva, dados do caso, análises por agente, matriz de decisão, próximos passos e rastreabilidade. Use quando um caso operacional ou projeto multiagente estiver concluindo e for necessário transformar issues e comentários distribuídos em um artefato único apresentável para Rodrigo, cliente ou banco.
---

# Consolidar Nota-Mãe

Skill que padroniza o documento único de resultado por caso/projeto/piloto. Substitui a costura manual de comentários por um artefato narrativo coeso, rastreável e apresentável.

## Workflow

### Step 1: Coletar Insumos

1. Listar todas as issues filhas relacionadas ao caso (via `multica issue list --output json` filtrando por parent ou label do caso).
2. Para cada issue concluída, coletar:
   - Entrega final do agente dono.
   - Decisões importantes registradas em comentários.
   - Documentos/anexos referenciados.
3. Verificar se algo está pendente — se sim, resolver antes (ou registrar como pendência consciente).

### Step 2: Estruturar a Nota-Mãe

Padrão markdown obrigatório:

```markdown
---
title: <Caso/Projeto> — Nota-Mãe
type: Case Summary
case_id: <identificador>
date: YYYY-MM-DD
author: Carmen
status: <em andamento | concluído | bloqueado>
---

# <Caso/Projeto> — Nota-Mãe

## Síntese Executiva

(2-3 parágrafos: decisão operacional, riscos principais, recomendação)

## Dados do Caso

- **Cliente / contexto:** ...
- **Demanda original:** ...
- **Banco/parceiro identificado:** ...
- **Período de análise:** ...
- **Lacunas resolvidas / pendentes:** ...

## Análises Consolidadas

### Conformidade (Tereza)
- CAF/CAR status, impeditivos, prazos, validade documental.

### Contexto de Mercado (Eloi)
- Dados regionais, sazonalidade, produtividade, riscos climáticos.

### Capacidade Financeira (Mariano)
- Fluxo de caixa, simulações, cenários, separação dado documental/declarado/estimado.

### Enquadramento de Crédito (Brasilino)
- Linha adequada, condições, banco recomendado, requisitos pendentes.

### Alternativas de Fomento (Alberico)
- Programas aplicáveis, complementaridade ao crédito.

### Relacionamento (Marta)
- Próximos passos concretos, responsável, prazo, ponto de contato no cliente.

## Matriz de Decisão

| Recomendação | Por quê | Com quem | Até quando |
|---|---|---|---|

## Riscos e Cenários Alternativos

- **Cenário base:** ...
- **Cenário pessimista:** ...
- **O que mudaria a recomendação:** ...

## Próximos Passos

- [ ] Ação 1 — responsável — prazo
- [ ] Ação 2 — responsável — prazo

## Rastreabilidade

- Issue-mãe: [ALT-XXX](mention://issue/<uuid>)
- Issues filhas: [ALT-YYY](mention://issue/<uuid>), ...
- Documentos no Vault: links
- Decisões intermediárias: links para comentários relevantes
```

Adaptar seções quando o caso não for crédito rural (ex: projeto interno, edital, modelo de negócios). Manter sempre: síntese executiva, análises por especialista, matriz de decisão, próximos passos, rastreabilidade.

### Step 3: Validar Coerência

Antes de fechar:
- Síntese executiva é consistente com as análises detalhadas?
- Não há contradição entre análises de agentes diferentes?
- Próximos passos têm dono e prazo?
- Recomendação é acionável (não vaga)?

Se houver inconsistência, resolver com o agente responsável antes de publicar.

### Step 4: Registrar no Vault

Delegar à Cacilda (`[@Cacilda](mention://agent/<uuid>)`) o registro do arquivo no Vault:
- Caminho padrão: `Areas/Casos/<nome-do-caso>/Nota-Mae_<caso>.md` (confirmar com Cacilda padrão exato).
- Formato: markdown estruturado conforme Step 2.
- Frontmatter completo.

Carmen redige o conteúdo. Cacilda valida estrutura e registra no padrão do Vault.

### Step 5: Apresentar e Fechar

- Postar comentário na issue-mãe com link para a nota-mãe registrada.
- Resumir em 3-4 linhas o que está na nota.
- Aguardar validação do Rodrigo.
- Após validação, marcar issue-mãe como `done` e seguir com retrospectiva (skill `retrospectiva-operacional`) se foi caso/piloto relevante.

## Triggers

- "nota-mãe"
- "consolida o caso"
- "monta o documento final"
- "prepara para apresentar"
- "prepara para o banco"
- Caso/projeto multiagente em fase de fechamento

## Notas

- Nota-mãe não duplica conteúdo — sintetiza. Detalhe técnico fica nas issues filhas.
- Sempre incluir rastreabilidade. Documento órfão de fontes não tem credibilidade.
- Linguagem deve ser apresentável a stakeholders externos (cliente, banco), não jargão interno.
- Se o caso ainda está em andamento, marcar `status: em andamento` e atualizar a nota conforme o caso evolui.