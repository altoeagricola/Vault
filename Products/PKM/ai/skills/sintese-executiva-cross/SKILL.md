---
name: sintese-executiva-cross
description: Produz síntese executiva cross-funcional integrando saídas de múltiplos agentes, fontes e domínios em um artefato organizacional/estratégico. Distinta da síntese-tendência — esta cobre síntese institucional, modelo de negócios, propostas, casos com múltiplos domínios.
---

# Síntese Executiva Cross-Funcional

Skill de Carmen para integrar dados, análises e decisões de múltiplos domínios em um documento executivo conciso, defensável e acionável. Diferente da `sintese-tendencia` do Eloi (mercado) e da `consolidar-nota-mae` (caso operacional rural): esta serve para sínteses institucionais, propostas, modelos de negócio, papers internos.

## Quando usar esta skill vs. as relacionadas

| Situação | Skill |
|---|---|
| Caso operacional rural concluindo (cliente, crédito, fomento) | `consolidar-nota-mae` |
| Inteligência de mercado / tendências de commodities | `sintese-tendencia` (Eloi) |
| Memo executivo institucional, modelo de negócios, proposta estratégica, paper interno | **`sintese-executiva-cross`** |

## Workflow

### Step 1: Definir o Documento

1. **Audiência:** Rodrigo? Stakeholder externo (parceiro, ICT, banco)? Comitê?
2. **Decisão a suportar:** o que essa síntese precisa permitir decidir?
3. **Tamanho-alvo:** geralmente 2-5 páginas. Síntese executiva passa de 5 página = falhou.
4. **Tom:** institucional formal, técnico-acessível, ou estratégico-visionário?

### Step 2: Coletar e Curar Insumos

Tipicamente envolve:
- Saídas de agentes especialistas (Eloi para mercado, Alberico para fomento, Brasilino para crédito, Tereza para regulação).
- Pesquisas externas estruturadas (`pesquisa-mercado` do Eloi).
- Documentos no Vault (editais, contratos, normativos).
- Decisões prévias do Rodrigo.

Para cada insumo, registrar: fonte, data, nível de confiança (fato verificado, claim comercial, inferência).

### Step 3: Estruturar a Narrativa

Estrutura padrão (adaptar conforme necessidade):

```markdown
---
title: <Título do Memo>
type: Executive Synthesis
author: Carmen
audience: <quem vai ler>
decision_supported: <decisão alvo>
date: YYYY-MM-DD
status: <draft | review | final>
---

# <Título>

## TL;DR
3-5 bullets. Recomendação no topo. Quem só ler isso deve sair com o essencial.

## Contexto e Motivação
Por que este memo existe agora. Qual janela ou pressão.

## Análise
### Dimensão 1 (ex: Mercado)
Síntese, com citação à fonte/agente.

### Dimensão 2 (ex: Regulação)
Idem.

### Dimensão 3 (ex: Capacidade interna)
Idem.

(quantas dimensões forem necessárias — geralmente 3 a 5)

## Convergências e Conflitos
O que as dimensões dizem em conjunto. Onde elas se reforçam, onde elas conflitam.

## Recomendação
Decisão proposta, com justificativa. Sempre indicar:
- O que é recomendado fazer.
- Por quê.
- Quem executa.
- Em quanto tempo.
- O que muda a recomendação se uma premissa cair.

## Riscos e Cenários
- Cenário base
- Cenário pessimista
- Cenário otimista (se relevante)

## Próximos Passos
Lista numerada, com responsável e prazo.

## Fontes
- Issues internas
- Documentos do Vault
- Fontes externas com data de acesso
- Agentes consultados
```

### Step 4: Aplicar Princípios de Síntese Executiva

Não-negociáveis:
1. **Recomendação no topo, justificativa em seguida.** Quem decide tem pouco tempo.
2. **Separar fato, claim e inferência.** Confusão aqui custa credibilidade.
3. **Quantificar quando possível.** "Mercado significativo" é fraco; "R$ 2,8 bi em 2024 (CONAB)" é forte.
4. **Citar fonte por afirmação, não no final.** Auditoria precisa rastrear ponto-a-ponto.
5. **Tom apropriado à audiência.** Memo para Rodrigo é diferente de memo para banco.
6. **Evitar prosa decorativa.** Memo executivo não é literatura.

### Step 5: Revisar e Validar

Aplicar skill `revisar-saida-operacional`. Em particular:
- Coerência entre as dimensões.
- Recomendação suportada pela análise.
- Riscos declarados, não escondidos.
- Sem contradição com decisões anteriores do Rodrigo (a menos que explicitamente revisadas).

### Step 6: Registrar no Vault

Delegar à Cacilda o registro do arquivo. Caminho típico:
- `Areas/Estrategia/<assunto>/<titulo>.md`
- `Products/<linha-de-produto>/Memos/<titulo>.md`
- Ou pasta específica do projeto/caso.

Confirmar com Cacilda o local correto conforme padrão do Vault.

## Triggers

- "síntese executiva"
- "memo executivo"
- "documento de decisão"
- "consolida em executivo"
- "monta o memo"
- Conclusão de pesquisa cross-funcional que precisa virar decisão

## Notas

- Esta skill **não** substitui o trabalho dos especialistas — depende deles.
- Carmen é a integradora; o conteúdo bruto vem dos agentes de domínio.
- Sempre preservar atribuição: dar crédito ao agente que produziu o insumo.
- Memo executivo é um produto deliberativo. Se a decisão já foi tomada, é registro, não síntese.
- Se a síntese expor um conflito sério entre agentes que muda a recomendação, tratar via skill `coordenar-multiagente` antes de fechar o memo.