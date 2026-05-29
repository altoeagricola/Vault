---
name: revisar-saida-operacional
description: Revisa entregas finais antes da apresentação ao Rodrigo, cliente ou banco. Verifica completude, coerência entre agentes, gates respeitados, linguagem apropriada e riscos não declarados. Use quando uma entrega multiagente estiver fechando, antes de apresentar uma nota-mãe, antes de comunicação externa.
---

# Revisar Saída Operacional

Skill de revisão final por Carmen. Funciona como gate de qualidade entre o time e qualquer audiência externa (Rodrigo, cliente, banco, parceiro).

## Workflow

### Step 1: Receber a Entrega Completa

1. Confirmar que a entrega está **finalizada** pelos agentes responsáveis (não revisar parcial salvo se solicitado).
2. Reunir todos os artefatos: nota-mãe, anexos, dados, simulações.
3. Identificar a audiência: para quem vai? Tom, profundidade e formato dependem disso.

### Step 2: Checklist de Revisão

Aplicar este checklist na ordem. Se algum item falhar, **bloquear a entrega** e retornar para o agente responsável.

#### A. Completude

- [ ] Todas as seções obrigatórias estão preenchidas (nada com "TBD" ou "pendente").
- [ ] Anexos referenciados existem e são acessíveis.
- [ ] Próximos passos têm dono e prazo.
- [ ] Rastreabilidade: cada afirmação relevante tem fonte ou link.

#### B. Coerência entre agentes

- [ ] Não há contradição entre análises (ex: Mariano usa preço diferente do que Eloi reportou).
- [ ] Dados citados batem entre agentes (mesma data de referência, mesma unidade).
- [ ] Conclusões parciais convergem para a recomendação final (ou divergências estão explicitadas).

#### C. Gates respeitados

- [ ] Fase 0 (precondições) foi validada por Tereza, se for caso operacional rural.
- [ ] Documentação obrigatória presente conforme processo aplicável.
- [ ] Nenhum agente pulou seu critério de pronto.

#### D. Linguagem e formato

- [ ] Tom adequado à audiência (formal para banco, técnico-acessível para produtor, executivo para Rodrigo).
- [ ] Sem jargão interno não explicado.
- [ ] Sem typos óbvios, números mal formatados ou tabelas quebradas.
- [ ] Documento renderiza bem em markdown (preview no Vault ou no comentário Multica).

#### E. Riscos e incertezas

- [ ] Riscos principais estão declarados (não escondidos).
- [ ] Premissas estão explícitas (qual dado é documental, qual é estimado, qual é declarado pelo cliente).
- [ ] Cenários alternativos foram considerados quando a recomendação é sensível a premissas.

#### F. Acionabilidade

- [ ] Recomendação é específica (não "considerar opções").
- [ ] Próximos passos podem ser executados sem nova rodada de pergunta-resposta.
- [ ] Pendências sem dono são identificadas explicitamente, não escondidas.

### Step 3: Decisão de Revisão

Três saídas possíveis:

1. **Aprovar:** todos os itens passam. Comentar na issue: "Revisada e aprovada para apresentação. Sigo para [próximo passo]."
2. **Aprovar com ressalvas menores:** itens de forma (D) podem ser corrigidos por mim mesma sem retornar ao especialista. Documentar ajustes feitos.
3. **Bloquear e retornar:** falha em A, B, C, E ou F. Comentário pontual ao agente responsável, no padrão:

   ```
   [@Especialista](mention://agent/<uuid>), antes de seguir preciso de ajuste em:
   - [ponto específico] — porque [razão]
   - [ponto específico] — porque [razão]

   Quando ajustado, sigo com a apresentação.
   ```

   **Não usar mention para revisão estética.** Apenas para falhas materiais.

### Step 4: Registrar a Revisão

Quando aprovar, registrar comentário curto na issue-mãe com:
- Data e hora da revisão.
- Itens críticos verificados.
- Ressalvas (se houver).

Isso cria rastreabilidade e evita retrabalho em futura auditoria.

## Triggers

- "revisa antes"
- "valida a entrega"
- "antes de apresentar"
- "checa coerência"
- "está pronto para mostrar?"
- Fechamento natural após `consolidar-nota-mae` ou `coordenar-multiagente`

## Notas

- Esta skill é **bloqueante** por design: sem revisão, não há apresentação.
- Não substitui a revisão técnica do especialista. Foca em coerência sistêmica e qualidade de saída.
- Tempo médio esperado: 5-15 minutos por entrega. Se for muito mais, há problema estrutural na entrega original.
- Se um padrão de erro se repete em múltiplas revisões (ex: Mariano sempre esquece de citar Eloi), abrir issue de retrospectiva ou ajustar processo via skill `design-processo-organizacional`.