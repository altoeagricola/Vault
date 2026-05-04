---
name: score-aderencia-edital
description: Gera ranking de parceiros recomendados para um edital de fomento usando a Matriz de Aderencia de Parceiros ICTs. Use quando houver um edital ingerido no Vault e o usuario pedir score, ranking, matching edital-parceiros, top parceiros, aderencia de ICTs, ou quando /ingest-business finalizar a ingestao de um novo edital de fomento.
---

# Score de Aderencia de Parceiros para Editais

**Especialista:** Alberico (Fomento)

Skill MVP para transformar um edital ja ingerido no Vault em uma recomendacao objetiva de parceiros. A primeira versao e deliberadamente simples: leitura manual do edital, consulta obrigatoria a matriz viva e registro do resultado em nota ou comentario.

## Quando Usar

| Situacao | Acao |
|---|---|
| Novo edital ingerido por `/ingest-business` | Rodar `/score-aderencia-edital` com o caminho da nota do edital |
| Usuario pergunta "quais parceiros para este edital?" | Gerar ranking Top 3 |
| Proposta em estruturacao precisa de ICT/parceiros | Comparar matriz, edital e gaps tecnicos |
| Parceiro ja escolhido precisa ser validado | Confirmar score, riscos e lacunas antes de submissao |

## Fontes Obrigatorias

1. **Edital-alvo:** nota em `Products/Fomento/Editais/` ou documento indicado pelo usuario.
2. **Matriz-base:** `Products/Fomento/WikiF/Matriz de Aderencia de Parceiros ICTs.md`.
3. **Notas complementares, se necessario:** propostas em `Products/Fomento/Propostas/`, parceiros em `Connections/`, argumentos em `Products/Fomento/WikiF/Argumentos Vencedores/`.

Nao gere ranking sem consultar a matriz. Se a matriz estiver ausente, incompleta ou conflitante, pare e reporte o bloqueio.

## Entrada

Aceita uma destas formas:

```text
/score-aderencia-edital Products/Fomento/Editais/FAPES 06-2026 Clusters de Inovação.md
/score-aderencia-edital edital:"FINEP AgriFam ICT 2026"
/score-aderencia-edital proposta:"Conilon Trace — FAPES 06-2026"
```

Se o edital nao estiver claro, pedir somente uma confirmacao: nome ou caminho da nota do edital.

## Workflow

### 1. Identificar o edital

Ler a nota do edital e extrair:

- orgao/chamada: FAPES, FINEP, CNPq, BNDES ou outro;
- tema tecnico central;
- exigencia de ICT, empresa proponente, produtor, cooperativa, campo experimental ou cartas de apoio;
- criterios de avaliacao que mencionem inovacao, impacto regional, maturidade tecnologica, equipe, mercado, ESG ou sustentabilidade;
- documentos e riscos de formalizacao.

### 2. Ler a Matriz de Aderencia

Consultar `Products/Fomento/WikiF/Matriz de Aderencia de Parceiros ICTs.md` e coletar, para cada parceiro:

- score do tipo de edital aplicavel;
- competencias;
- historico com ALTOE;
- status documental;
- riscos/gaps;
- melhor uso imediato.

Se o edital for hibrido, usar o tipo principal e aplicar ajuste qualitativo conforme o tema. Exemplo: FAPES com nucleo de sensores pode elevar Adilson/IFES Serra; FAPES com campo conilon pode elevar IFES Santa Teresa + Amigos do Campo.

### 3. Calcular o score ajustado

Partir do score da matriz para o tipo do edital e ajustar de -2 a +2 pontos, mantendo o teto de 12:

| Ajuste | Quando aplicar |
|---:|---|
| +2 | O edital exige exatamente a competencia forte do parceiro |
| +1 | O parceiro cobre criterio importante, mas nao central |
| 0 | A matriz ja representa bem o encaixe |
| -1 | Existe gap documental, operacional ou de historico relevante |
| -2 | Risco de conflito, baixa disponibilidade ou papel muito periférico |

Sempre explicar o ajuste em uma frase curta. Nao inventar capacidade nao registrada no Vault; quando houver inferencia, marcar como "inferido a partir da matriz".

### 4. Gerar o Top 3

Retornar:

- Top 3 parceiros recomendados;
- score final de cada um;
- papel recomendado na proposta;
- justificativa de aderencia;
- gaps que precisam ser fechados;
- parceiro complementar ou perfil a buscar, se o trio nao cobrir tudo.

Se dois parceiros tiverem papeis diferentes e complementares, preservar os dois mesmo que um score seja menor. Exemplo: ICT principal + campo de validacao + apoio de gestao.

### 5. Registrar o resultado

Preferencia de registro:

1. Se houver pasta do edital: criar ou atualizar `Products/Fomento/Editais/<Edital>/Score de Aderencia — Parceiros.md`.
2. Se o edital for uma nota solta em `Products/Fomento/Editais/`: criar nota irmã `Products/Fomento/Editais/Score de Aderencia — <Edital>.md`.
3. Se a analise foi pedida dentro de issue Multica: responder em comentario e informar se tambem criou nota no Vault.

## Template de Saida

```markdown
---
tipo: Score de Aderencia
area: Fomento
edital: "[[Nome do Edital]]"
matriz_base: "[[Matriz de Aderencia de Parceiros ICTs]]"
status: draft
responsavel: Alberico
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - Fomento
  - Parceiros
  - Score
---

# Score de Aderencia — Nome do Edital

## Leitura do Edital

- Orgao/chamada:
- Tema central:
- Tipo de edital usado na matriz:
- Exigencias de parceria:
- Criterios sensiveis:

## Top 3 Parceiros

| Rank | Parceiro | Score base | Ajuste | Score final | Papel recomendado |
|---:|---|---:|---:|---:|---|
| 1 | [[Parceiro]] | 0 | 0 | 0 | ICT principal / campo / gestao / mercado |
| 2 | [[Parceiro]] | 0 | 0 | 0 |  |
| 3 | [[Parceiro]] | 0 | 0 | 0 |  |

## Justificativas

### 1. [[Parceiro]]

- Aderencia:
- Ajuste aplicado:
- Gaps:
- Proxima acao:

### 2. [[Parceiro]]

- Aderencia:
- Ajuste aplicado:
- Gaps:
- Proxima acao:

### 3. [[Parceiro]]

- Aderencia:
- Ajuste aplicado:
- Gaps:
- Proxima acao:

## Gaps Gerais

- Competencias nao cobertas:
- Documentos pendentes:
- Riscos de formalizacao:
- Perfil de parceiro complementar a buscar:

## Recomendacao de Montagem

Composicao recomendada:

1. Parceiro principal:
2. Parceiro complementar:
3. Apoio operacional/mercado:

## Proximas Acoes

- [ ] Validar disponibilidade dos parceiros.
- [ ] Conferir documentos/certidoes exigidos pelo edital.
- [ ] Definir papel formal de cada parceiro.
- [ ] Obter cartas, termos ou anuencias necessarias.
```

## Criterios de Qualidade

- O Top 3 precisa estar conectado aos criterios do edital, nao apenas ao maior score bruto.
- Toda recomendacao deve apontar papel pratico: ICT principal, campo de validacao, gestao, mercado, articulacao territorial ou apoio tecnico.
- Todo gap deve virar acao verificavel.
- Nao fechar recomendacao se faltar informacao essencial do edital ou da matriz.

## Roadmap

- **Fase 1:** matching manual orientado por matriz, implementado nesta skill.
- **Fase 2:** parser estruturado para extrair criterios do edital automaticamente.
- **Fase 3:** trigger automatico apos `/ingest-business` e registro direto no Vault.
- **Fase 4:** historico de desempenho por parceiro com aprendizado a partir de submissao, parecer e aprovacao.

## Status

MVP pronto para uso manual.

**Data de criacao:** 2026-05-04  
**Versao:** 1.0.0
