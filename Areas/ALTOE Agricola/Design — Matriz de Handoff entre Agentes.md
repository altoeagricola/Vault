---
tipo: Referência Operacional
contexto: "[[ALTOE Agricola]]"
status: rascunho — aguardando revisão do Rodrigo
origin: "Carmen — ALT-46 (2026-05-03)"
created: 2026-05-03
atualizado: 2026-05-03
relacionado:
  - "[[Design — Matriz RACI por Processo]]"
  - "[[Estrutura de Agentes IA]]"
---

# Design — Matriz de Handoff entre Agentes

Documento operacional que especifica, para os fluxos mais comuns, o que acontece em cada passo e quem aciona quem. O formato é: **evento disparador → ação imediata → encadeamento → fechamento**.

> **Status:** Rascunho. Sujeito a revisão e validação pelo Rodrigo antes de ser tratado como oficial.

---

## Como ler este documento

Cada fluxo segue a estrutura:

```
1. [Agente] faz X
2. → [Agente] recebe Y e faz Z
3. → [Agente] recebe W e faz V
...
n. Fechamento: o que marca o fim do fluxo e o que fica registrado
```

A seta `→` indica acionamento direto (issue ou menção). Ausência de seta indica que o agente é apenas **informado**, sem necessidade de ação imediata.

---

## Fluxo 1 — Eloi detecta alerta climático ou de mercado

**Disparador:** Eloi identifica sinal relevante (veranico, geada, alta/queda de preço, nova política pública)

```
1. Eloi cria síntese do alerta:
   - Tipo de evento (climático / preço / regulatório)
   - Regiões ou produtores possivelmente afetados
   - Janela temporal estimada
   - Impacto direto esperado

2. → Marta recebe:
   - Ativa contato proativo com produtores afetados via CRM
   - Gera briefing de visita/ligação contextualizado pelo alerta

3. → Mariano recebe:
   - Avalia impacto no fluxo de caixa dos produtores da carteira
   - Identifica produtores em risco financeiro imediato

4. → Brasilino recebe:
   - Verifica linhas de crédito emergencial disponíveis (Proagro, ABC Emergência, etc.)
   - Mapeia quais produtores se enquadram

5. Rodrigo é informado com síntese consolidada de ação tomada pelos agentes

6. Cacilda registra o alerta e as respostas no Vault
   (Journal ou nota de alerta datada em Areas/ALTOE Agricola/)

Fechamento: Eloi confirma resolução ou continuidade do sinal em nota de acompanhamento.
```

---

## Fluxo 2 — Marta conclui onboarding de novo produtor

**Disparador:** Marta finaliza o processo de onboarding e tem o briefing do cliente completo

```
1. Marta posta briefing do produtor contendo:
   - Perfil geral (nome, localização, cultura principal, área)
   - Histórico de crédito (se conhecido)
   - Objetivos declarados e oportunidades identificadas
   - Pendências documentais (se houver)
   - Próximas ações sugeridas

2. → Brasilino recebe:
   - Realiza perfilamento de crédito completo
   - Faz matching de linhas (Pronaf, Pronamp, etc.) com o perfil
   - Gera checklist documental por banco-alvo

3. → Tereza recebe:
   - Verifica validade e completude dos documentos do produtor
   - Emite alerta imediato se houver documento vencido ou faltante

4. → Mariano recebe:
   - Constrói perfil econômico-financeiro mínimo da propriedade
   - Solicita dados de safra/fluxo de caixa se necessário

5. → Eloi recebe (informativo):
   - Contextualiza o produtor com sinais de mercado relevantes
   - Alerta Marta se houver janela de oportunidade ou risco imediato

6. Cacilda registra ficha do produtor no Vault
   (Areas/ALTOE Agricola/ ou Connections/)

7. Rodrigo é informado:
   - Produtor onboardado
   - Oportunidades identificadas
   - Próximas ações consolidadas dos agentes

Fechamento: Brasilino entrega checklist ao Rodrigo/Marta; fluxo passa para "Submissão de projeto de crédito" se aplicável.
```

---

## Fluxo 3 — Tereza identifica documento vencido ou em risco

**Disparador:** Tereza detecta documento próximo do vencimento (≤ 60 dias) ou já vencido

```
1. Tereza emite alerta com especificidade:
   - Qual documento (CNH, certidão, IRPF, CCIR, etc.)
   - De quem (produtor, parceiro, sócio da empresa)
   - Data de vencimento
   - Operações bloqueadas ou em risco

2A. Se for documento de produtor:
   → Marta recebe:
      - Aciona comunicação com o produtor solicitando renovação
      - Registra no CRM: pendência, data, responsável

   → Brasilino recebe:
      - Identifica operações de crédito bloqueadas por esta pendência
      - Sinaliza se há prazo crítico na submissão de projeto

2B. Se for documento de parceiro (ICT, banco, prestador):
   → Alberico recebe (parceiros ICT):
      - Aciona o parceiro para renovação
      - Avalia impacto nos projetos de fomento vinculados

   → Rodrigo recebe diretamente (parceiro estratégico ou documento regulatório crítico)

3. Rodrigo é informado em casos que bloqueiam operação ativa
   (alerta de urgência — não apenas FYI)

4. Cacilda atualiza status documental no Vault
   (nota do produtor/parceiro ou dashboard de validade)

Fechamento: Tereza confirma regularização → Brasilino e Marta são informados → CRM e Vault atualizados.
```

---

## Fluxo 4 — Brasilino identifica mudança relevante no MCR ou normativo bancário

**Disparador:** Brasilino detecta alteração no MCR, resolução do BCB, portaria MAPA ou mudança operacional em banco parceiro (BB, Sicoob, Sicredi, Cresol, BNB)

```
1. Brasilino sintetiza a mudança:
   - Qual norma / resolução / portaria
   - O que mudou (taxa, prazo, limite, exigência documental, nova linha)
   - Operações ativas potencialmente afetadas
   - Janela de adaptação (se houver)

2. → Tereza recebe:
   - Atualiza checklists de conformidade afetados
   - Revisa alertas de vencimento vinculados a exigências alteradas

3. → Alberico recebe:
   - Verifica se a mudança abre ou fecha oportunidades em editais de fomento que cruzam com crédito rural

4. → Mariano recebe (informativo):
   - Avalia impacto financeiro (novos limites, taxas, prazos) sobre a carteira

5. Rodrigo aprova a síntese e define:
   - Se há ajuste necessário em processos operacionais
   - Se há comunicação a fazer com clientes afetados

6A. Se a mudança implica redesenho de processo:
   → Carmen recebe:
      - Mapeia o processo afetado
      - Propõe ajuste no fluxo operacional ou RACI
      - Retorna proposta para Rodrigo aprovar

6B. Se a mudança implica comunicação com clientes:
   → Marta recebe:
      - Prepara comunicação adequada ao perfil de cada produtor afetado

7. Cacilda atualiza notas relevantes no Vault:
   - WikiCR (se altera interpretação do MCR)
   - Checklists de banco (se altera exigências por instituição)

Fechamento: Brasilino confirma que operações ativas foram revisadas à luz da mudança; Rodrigo fecha o ciclo de validação.
```

---

## Fluxo 5 — Alberico identifica edital relevante

**Disparador:** Alberico detecta edital de fomento com boa aderência ao ecossistema ALTOE Agricola

```
1. Alberico publica nota de prospecção com:
   - Edital, órgão financiador, prazo de submissão
   - Score de aderência estimado (ecossistema × critérios do edital)
   - ICT(s) candidatas e lacunas de parceria identificadas
   - Próximos passos recomendados

2. Rodrigo recebe e decide:
   - Prosseguir com proposta? Sim → fluxo continua
   - Não prosseguir? → Alberico arquiva no pipeline com justificativa

3. → Marta recebe (se envolve parceiros no CRM):
   - Aciona contato com ICTs ou parceiros identificados por Alberico

4. → Brasilino recebe (se edital cruza com crédito rural):
   - Avalia conformidade e sinergia com operações existentes

5. → Eloi recebe (informativo):
   - Contextualiza com políticas públicas ou sinais de mercado relacionados

6. Cacilda registra nota do edital no Vault
   (Products/Fomento/Editais/)

7. Alberico lidera a elaboração da proposta com:
   - Rodrigo como aprovador de conteúdo
   - Carmen disponível para revisão de estrutura/fluxo

Fechamento: Proposta submetida → Alberico registra no pipeline → Rodrigo e Marta são informados.
```

---

## Fluxo 6 — Regularização concluída (Tereza fecha ciclo)

**Disparador:** Produtor ou parceiro regulariza documento identificado como pendente

```
1. Tereza confirma regularização:
   - Documento recebido, válido e dentro do prazo

2. → Brasilino recebe:
   - Operação de crédito desbloqueada pode prosseguir
   - Retoma checklist ou cronograma de submissão

3. → Marta recebe:
   - Atualiza CRM: pendência encerrada, próxima ação desbloqueada

4. Cacilda atualiza o Vault:
   - Status documental do produtor/parceiro atualizado

Fechamento: Tereza emite confirmação e fecha o alerta originado no Fluxo 3.
```

---

## Princípios de Handoff

1. **Clareza no disparo:** ao acionar outro agente, especifique sempre o que se espera como saída — não apenas "FYI".
2. **Um ponto de fechamento:** cada fluxo tem um agente responsável por confirmar o encerramento; evitar fluxos que "morrem no meio".
3. **Rodrigo é ponto de aprovação, não de execução:** não deve receber acionamentos para tarefas que um agente pode resolver sozinho.
4. **Cacilda registra, não decide:** o Vault é destino final de informação estruturada — Cacilda é informada, não consultada no meio do fluxo.
5. **Carmen entra em redesenho, não em rotina:** apenas quando um fluxo precisa ser ajustado estruturalmente Carmen é acionada; no dia a dia ela não participa dos handoffs.
