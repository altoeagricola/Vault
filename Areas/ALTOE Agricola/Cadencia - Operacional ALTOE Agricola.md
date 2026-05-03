---
tipo: Processo
contexto: "[[ALTOE Agricola]]"
status: ativo
origin: "Carmen — ALT-51 (2026-05-03)"
created: 2026-05-03
atualizado: 2026-05-03
---

# Cadência Operacional — ALTOE Agricola

Rituais recorrentes que mantêm o sistema de agentes em operação ativa, sem depender de acionamento manual do fundador para cada ciclo. Cada ritual tem responsável, frequência, formato de output esperado e local de registro.

Este documento cobre a cadência **operacional do negócio** (crédito, fomento, mercado, clientes, compliance). A cadência de revisão dos próprios agentes e da arquitetura do Vault está em [[Cadencia - Revisao de Agentes e Vault]].

---

## Princípios

- **Ritmo sustentável:** Cadências devem ser executáveis mesmo em semanas de alta demanda — o objetivo é criar um pulso regular, não sobrecarregar
- **Output concreto:** Cada ritual termina com um entregável claro (resumo, lista de ações, alerta) — não apenas "foi feito"
- **Registro rastreável:** Todo output vai para um local definido (issue, nota de Journal, nota do Vault) — sem saída oral ou efêmera
- **Integração entre agentes:** Os rituais são pontos de sincronização; o que um agente produz alimenta o próximo

---

## Cadência Semanal

### 1. Revisão do Pipeline de Crédito

**Quando:** Toda segunda-feira  
**Responsáveis:** Brasilino (operação) + Marta (relacionamento)  
**Output:** Comentário de resumo na issue de pipeline ou Weekly Summary em `Journal/Weekly/`

**Agenda:**
- Quais propostas avançaram desde a semana anterior?
- Quais travaram — e por qual motivo (documento pendente, banco lento, produtor ausente)?
- Quais ações de curto prazo são necessárias (ligar para produtor, cobrar banco, preparar documento)?
- Algum cliente novo a ser prospeccionado esta semana?

**Formato de output:**
```
## Pipeline de Crédito — Semana [XX]
**Avançaram:** [nomes + status novo]
**Travados:** [nome + motivo + próxima ação]
**Ações da semana:** [lista numerada]
**Novos leads:** [nome + origem]
```

---

### 2. Varredura de Sinais de Mercado

**Quando:** Toda quarta-feira  
**Responsável:** Eloi  
**Output:** Weekly Summary em `Journal/Weekly/` + alerta direto ao Rodrigo se sinal crítico

**Agenda:**
- Preço do conilon na semana (CEPEA, CONAB) — tendência de curto prazo?
- Alertas climáticos relevantes para o ES (INMET/INCAPER) — algum veranico ou evento extremo?
- Políticas públicas e regulatórias novas (Plano Safra, MCR, MAPA, BCB) — alguma mudança que afeta crédito ou fomento?
- Movimentos relevantes de bancos ou cooperativas (Sicoob, Sicredi, BB, BNB, Cresol) — abertura de linhas, mudança de taxa?

**Formato de output:**
```
## Sinais de Mercado — Semana [XX]
**Preço Conilon:** [R$/sc + variação]
**Clima ES:** [status + alertas ativos]
**Políticas:** [nenhuma / [descrição]]
**Bancos:** [nenhuma / [descrição]]
**Destaque da semana:** [1 parágrafo se houver sinal crítico]
```

---

### 3. Revisão de Alertas de Documentação

**Quando:** Toda sexta-feira  
**Responsável:** Tereza  
**Output:** Lista de vencimentos em issue específica ou Weekly Summary

**Agenda:**
- O que vence nas próximas 2 semanas? (CNH, certidões, IRPF, CCIR, contratos)
- O que vence entre 2 e 4 semanas? (alerta preventivo)
- Algum documento foi renovado e precisa ser registrado no Vault?
- Alguma nova norma BCB/MAPA/SNCR publicada que exige atualização de checklist?

**Formato de output:**
```
## Alertas Documentais — Semana [XX]
**Vence em até 14 dias:** [cliente + documento + data]
**Vence entre 15-30 dias:** [cliente + documento + data]
**Renovados esta semana:** [cliente + documento]
**Normas novas:** [nenhuma / [referência]]
```

---

## Cadência Mensal

### 4. Revisão do Pipeline de Fomento

**Quando:** Primeira segunda-feira do mês  
**Responsável:** Alberico  
**Output:** Nota em `Journal/Monthly/` + atualização dos projetos no Vault

**Agenda:**
- Quais editais estão no radar para os próximos 60 dias?
- Status das propostas em andamento: em elaboração, submetidas, em avaliação, aprovadas?
- Quais prazos críticos existem no próximo mês?
- Algum novo edital relevante identificado para prospectar?

**Formato de output:**
```
## Pipeline de Fomento — [Mês/Ano]
**Editais no radar:** [nome + agência + prazo]
**Propostas em andamento:** [nome + status + próximo passo]
**Propostas submetidas aguardando resultado:** [nome + data envio]
**Aprovadas/Contratadas:** [nome + status contratação]
**Prazos críticos do mês:** [lista numerada]
```

---

### 5. Atualização de Fichas de Produtores e Clientes

**Quando:** Segunda semana do mês  
**Responsáveis:** Mariano (dados financeiros) + Marta (relacionamento e status comercial)  
**Output:** Atualização das fichas no Vault (Connections/) + summary em Monthly

**Agenda:**
- Houve novos dados financeiros de algum produtor ativo? (safra, colheita, venda, despesa)
- Algum cliente mudou de status comercial (prospecto → ativo, ativo → inativo)?
- Próximos passos de relacionamento com cada cliente ativo?
- Algum parceiro do ecossistema com mudança de status relevante?

**Formato de output:**
```
## Fichas de Clientes — [Mês/Ano]
**Atualizados:** [nome + campo atualizado]
**Mudança de status:** [nome + de → para]
**Próximas ações de relacionamento:** [lista por cliente]
**Parceiros com atualização:** [nome + mudança]
```

---

### 6. Revisão de Definições dos Agentes

**Quando:** Integrada com o ritual mensal de [[Cadencia - Revisao de Agentes e Vault]] (1ª segunda-feira do mês)  
**Responsável:** Carmen (síntese) + Cacilda (facilitação)  
**Output:** Conforme definido em [[Cadencia - Revisao de Agentes e Vault]]

Este ritual está documentado integralmente em [[Cadencia - Revisao de Agentes e Vault#1. Mensal — Revisão de Definições dos Agentes]]. Não há duplicação aqui — apenas referência cruzada para manter ambos os documentos coerentes.

---

## Cadência Trimestral

### 7. Revisão da Arquitetura do Vault

**Quando:** Última semana de cada trimestre (maio, agosto, novembro, fevereiro)  
**Responsáveis:** Cacilda + Carmen  
**Output:** Conforme definido em [[Cadencia - Revisao de Agentes e Vault]]

Documentado integralmente em [[Cadencia - Revisao de Agentes e Vault#2. Trimestral — Revisão da Arquitetura do Vault]].

---

### 8. Atualização de Status de Bancos e Parceiros

**Quando:** Última semana de cada trimestre  
**Responsáveis:** Tereza (bancos — compliance/credenciamento) + Cacilda (parceiros — Vault/Connections/)  
**Output:** Atualização das notas de bancos em `Connections/Banks/` + nota trimestral em `Journal/Quarterly/`

**Agenda:**
- Status de credenciamento por banco: credenciado ativo, em andamento, bloqueado, a iniciar?
- Algum banco abriu ou fechou linhas relevantes?
- Algum parceiro ICT com mudança de status (ativo, inativo, novo)?
- Algum parceiro cooperativa com mudança relevante (Sicoob Marilândia, Sicredi, Cresol)?

**Formato de output:**
```
## Status de Bancos e Parceiros — [Trimestre/Ano]
**BB:** [status + observação]
**Sicoob:** [status + observação]
**Sicredi:** [status + observação]
**Cresol:** [status + observação]
**BNB:** [status + observação]
**Parceiros ICT com atualização:** [nome + mudança]
**Cooperativas com atualização:** [nome + mudança]
```

---

## Por Demanda

### 9. Resposta a Sinal de Mercado Crítico

**Trigger:** Eloi detecta sinal com impacto imediato (alerta climático severo, mudança de MCR, abertura emergencial de linha)  
**Responsável:** Eloi (detecção) → Brasilino ou Alberico (ação, conforme tipo)

**Processo:**
1. Eloi abre issue com título `[ALERTA] [tipo]: [descrição]` e priority alta
2. Eloi descreve o sinal, o impacto estimado e os clientes/propostas potencialmente afetados
3. Assign ao agente responsável pela ação (Brasilino para crédito, Alberico para fomento, Marta para CRM)
4. O agente acionado avalia e age em até 24h

---

### 10. Sugestão Estrutural de Qualquer Agente

**Trigger:** Qualquer agente identifica algo que não funciona como esperado no design dos processos  
**Responsável:** Carmen (triage e mediação)  
**Label:** `sugestão estrutural`

**Processo:** Ver [[Cadencia - Revisao de Agentes e Vault#3. Por Demanda — Sugestões Estruturais]]

---

## Template: Como Documentar Cada Ritual

Todo output de ritual deve usar o seguinte formato básico para garantir rastreabilidade:

```markdown
---
tipo: Registro de Ritual
ritual: [nome do ritual]
frequência: [semanal/mensal/trimestral]
data: [YYYY-MM-DD]
responsável: [nome(s) do(s) agente(s)]
---

# [Nome do Ritual] — [Período]

[Conteúdo conforme o formato de output específico do ritual]

## Ações Geradas
- [ ] [ação] — responsável: [nome] — prazo: [data]

## Observações
[Qualquer contexto que não se encaixa no formato estruturado]
```

**Onde arquivar:**
- **Resumos semanais:** `Journal/Weekly/[YYYY]-W[XX].md`
- **Resumos mensais:** `Journal/Monthly/[YYYY]-[MM].md`
- **Resumos trimestrais:** `Journal/Quarterly/[YYYY]-Q[N].md`
- **Issues com ações:** Multica, com labels correspondentes

---

## Mapa de Responsabilidades

| Ritual | Frequência | Responsável Principal | Co-responsável | Output |
|--------|------------|----------------------|----------------|--------|
| Pipeline de Crédito | Semanal (seg) | Brasilino | Marta | Weekly Summary + issues |
| Sinais de Mercado | Semanal (qua) | Eloi | — | Weekly Summary + alerta |
| Alertas Documentais | Semanal (sex) | Tereza | — | Weekly Summary + issue |
| Pipeline de Fomento | Mensal (1ª seg) | Alberico | — | Monthly Summary + Vault |
| Fichas de Clientes | Mensal (2ª sem) | Mariano | Marta | Monthly Summary + Vault |
| Revisão de Agentes | Mensal (1ª seg) | Carmen | Cacilda | Ver [[Cadencia - Revisao de Agentes e Vault]] |
| Revisão do Vault | Trimestral | Cacilda | Carmen | Ver [[Cadencia - Revisao de Agentes e Vault]] |
| Bancos e Parceiros | Trimestral | Tereza | Cacilda | Quarterly Summary + Vault |
| Alerta de Mercado | Por demanda | Eloi | Brasilino/Alberico | Issue urgente |
| Sugestão Estrutural | Por demanda | Carmen | — | Issue com label |

---

## Log de Rituais

| Data | Ritual | Resultado | Ações Geradas |
|------|--------|-----------|---------------|
| — | — | — | — |

---

## Integração com Outros Documentos

- [[Cadencia - Revisao de Agentes e Vault]] — rituais de meta-revisão (agentes e Vault); integrados por referência, sem duplicação
- [[Estrutura de Agentes IA]] — referência de papéis e responsabilidades por agente
- [[Estrutura de Agentes IA - Contexto]] — justificativas e lógica de integração entre agentes
- [[ALTOE Agricola]] — visão estratégica do sistema como um todo
