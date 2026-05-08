---
tipo: Processo
contexto: "[[ALTOE Agricola]]"
status: ativo
origin: "Proposta de Cadência de Discussões — Cacilda (ALT-39, 2026-05-03)"
created: 2026-05-03
atualizado: 2026-05-03T20:30Z
---

# Cadência — Revisão de Agentes e Vault

Estrutura de rituais recorrentes para iteração contínua e saudável da arquitetura de agentes e do Vault, evitando tanto revisões ansiosas quanto abandono tácito de melhorias.

---

## Princípios

- **Documento vivo, não morto:** Cada ritual alimenta o próximo; sugestões se transformam em decisões, decisões se transformam em implementação
- **Cadência clara:** Sem prazos claros, tudo vira "quando der"; com rituais bem delimitados, a discussão fica confortável
- **Participação sistêmica:** Cada agente traz sua perspectiva; nenhuma voz fica isolada
- **Rastreabilidade:** Cada decisão fica registrada em uma issue ou nota, com owner e deadline

---

## Rituais

### 1. Mensal — Revisão de Definições dos Agentes

**Quando:** 1ª segunda-feira do mês (ou próximo dia útil)  
**Duração:** 30–45 min  
**Participantes:** Todos os agentes + Rodrigo (se possível)

**Objetivo:** Detectar e resolver rápido problemas de clareza, sobreposição ou execução.

**Agenda:**
- Rodada rápida: "Algum papel ficou nebuloso na prática? Houve sobreposição com outro agente?"
- Identificar blocos: Falta de clareza, falta de recurso, falta de skill
- Propor ajustes: Pequenas mudanças de escopo, responsabilidades, prioridades
- Registrar em issue: ALT-[X] com tag "revisão mensal"

**Resultado:**
- Se não há problemas: Confirmar "revisão bem-sucedida" no log
- Se há: Gerar 1–3 issues de ajuste, prioritizadas para as próximas 2 semanas
- Atualizar [[Estrutura de Agentes IA - Contexto]] se houver mudanças maiores

**Responsável:** Cacilda (facilitar); Carmen (sintetizar)

---

### 2. Trimestral — Revisão da Arquitetura do Vault

**Quando:** Última semana de cada trimestre (maio, agosto, novembro, fevereiro)  
**Duração:** 1–1,5h  
**Participantes:** Todos os agentes + Rodrigo

**Objetivo:** Garantir que o Vault está evoluindo com a operação; pastas/conhecimento não usados são consolidados, conceitos sem local são acomodados.

**Agenda:**
- Auditoria leve: Quais pastas estão crescendo? Quais estão vazias?
- Validação de conceitos: Há conceitos grandes circulando sem um local claro?
- Retirada de obsoletos: Há arquivos/seções que já não servem?
- Aprimoramento de navegação: As ligações entre conceitos estão claras?
- Planejamento de skills novos: Há padrões de busca manual que indicam um skill novo?

**Resultado:**
- Atualizar [[Regras de Organizacao do Vault|Regras de Organização do Vault]]
- Gerar 1–2 épics de refactoring do Vault (se necessário)
- Planejar 1–2 skills novos para o próximo trimestre
- Registrar insights em [[Onboard - Sintese e Feedback dos Agentes|Onboard — Síntese de Feedback dos Agentes]] (seção de evolução)

**Responsável:** Cacilda (auditoria + pauta); Rodrigo (validação estratégica)

---

### 3. Por Demanda — Sugestões Estruturais

**Trigger:** Qualquer agente abre uma issue com label "sugestão estrutural"

**Objetivo:** Capturar sinais de ajustes que não podem esperar 30 dias.

**Processo:**
1. Agente abre issue: título conciso, descrição clara do problema e sugestão
2. Tag: `#sugestao-estrutural`
3. Assign: Cacilda (triage)
4. Cacilda avalia: É urgente? É consenso fácil? Precisa de conversa?
5. Três caminhos:
   - **Rápido (< 1 dia):** Cacilda implementa, registra em nota, fecha
   - **Médio (< 1 semana):** Abre conversa assíncrona, sintetiza feedback, implementa
   - **Complexo:** Pauta para próxima revisão mensal

**Responsável:** Cacilda (triage e execução de rápidos); Carmen (mediação de conversas complexas)

---

## Log de Rituais

| Data | Tipo | Resultado | Ref Issue |
|------|------|-----------|-----------|
| — | — | — | — |

---

## Notas

- **Não é revisão ansiosa:** O objetivo não é mudar tudo o tempo todo. A cadência dá espaço para que mudanças menores sejam absorvidas naturalmente, e mudanças maiores tenham discussão estruturada.
- **Integração com operação:** Insights dos rituais de revisão alimentam o backlog de skills, priorizações de agentes e pauta de onboards de novos agentes.
- **Documento vivo:** Esta cadência pode evoluir. Sugestões de ajuste no próprio ritual devem ser capturadas como issue com tag "cadencia-meta", revistas a cada trimestre.
- **Cadência operacional complementar:** Os rituais de negócio (pipeline de crédito, fomento, mercado, clientes, compliance) estão documentados em [[Cadencia - Operacional ALTOE Agricola]]. Este documento e aquele formam o sistema completo de cadências.

---
