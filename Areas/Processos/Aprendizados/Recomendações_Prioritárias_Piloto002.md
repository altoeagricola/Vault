---
title: Recomendações Prioritárias — Piloto 002
type: Process Recommendation
derived_from: "ALT-77 — Avaliação de estrutura multiagente"
author: Carmen
status: pending_implementation
created: 2026-05-06
updated: 2026-05-06
reviewed: 2026-05-06
---

# Recomendações Prioritárias — Piloto 002

**Contexto:** Estas recomendações derivam da avaliação de Carmen (ALT-77) sobre a estrutura multiagente da ALTOE frente à proposta-objetivo da ferramenta. Foram identificadas como prioritárias para amadurecer a operação antes de um Piloto 002.

**Status:** Aguardando implementação. Estas recomendações funcionam como **gate de entrada para o próximo piloto operacional real**.

**Referência de aprendizagem:** [Aprendizados_Operacionais_Piloto001.md](Aprendizados_Operacionais_Piloto001.md)

---

## 1. Protocolo Fixo de Abertura de Caso

**Descrição:** Estabelecer um protocolo sequencial obrigatório para o kickoff de qualquer novo caso operacional.

**Fases de entrada (Fase 0 — Precondições):**
- Briefing consolidado do cliente (dados conhecidos, documentos disponíveis, demanda clara, lacunas)
- OCR obrigatório de todos os documentos
- Índice documental estruturado no Vault
- Verificação de CAF no CAFWeb e CAR no SICAR (sistema oficial)
- Banco identificado ou mapeado
- Lacunas iniciais mapeadas

**Por que:** O Piloto 001 abriu análises de mérito antes de garantir precondições documentais. Isso gerou análises boas mas condicionais. Sequenciar Fase 0 antes de Fases 1-3 reduz retrabalho, garante consistência de dados e melhora qualidade de decisão.

**Critério de conclusão para Piloto 002:** Nenhuma frente de análise (contexto, CRM, financeiro, crédito, fomento) inicia enquanto Fase 0 não estiver 100% completa e validada por Tereza.

---

## 2. Templates Obrigatórios por Agente

**Descrição:** Criar e manter templates de entrega para cada agente, com campos mínimos obrigatórios e handoff explícito.

**O que deve conter cada template:**
- Campos mínimos de dados (dados documentais, estimados, declarados — sempre distintos)
- Formato de saída (tabelas, listas, narrativas estruturadas conforme o papel)
- Handoff explícito: quem depende dessa entrega, dados que serão usados, prazo de passagem
- Referências cruzadas: citação de dados/aprendizados de outros agentes quando aplicável
- Critério de aceitação: quando a entrega está completa

**Por agente:**
- **Cacilda:** OCR, estrutura Vault, indexação, rastreabilidade documental
- **Tereza:** Checklist de conformidade, CAF/CAR em sistema oficial, impeditivos vs. pendências saneáveis
- **Eloi:** Briefing de mercado + nota de handoff para Mariano (com dados de entrada calibrados)
- **Mariano:** Simulação financeira (citando Eloi, distinguindo dado documental/estimado/declarado)
- **Brasilino:** Enquadramento de crédito (referenciando Tereza + Mariano + banco identificado, tom formal)
- **Alberico:** Mapa de alternativas de fomento (complementar, não duplicativo de Brasilino)
- **Marta:** Ficha CRM (com "próximo passo concreto" obrigatório, não apenas pendências)
- **Carmen:** Parecer final + próximos passos com responsáveis, prazos e ações concretas

**Critério de conclusão para Piloto 002:** Templates finalizados e disponíveis. Primeira frente a ser executada deve demonstrar uso de template e handoff explícito.

---

## 3. Nota-Mãe Final Consolidada por Caso

**Descrição:** Criar um documento único de resultado para cada caso operacional, consolidando análises, decisões e próximos passos.

**O que deve conter:**
- Síntese executiva (2-3 parágrafos com decisão operacional e riscos principais)
- Dados do cliente e contexto (identificação, demanda, banco identificado, lacunas resolvidas)
- Análises consolidadas:
  - Conformidade (Tereza): CAF/CAR status, impeditivos, prazos
  - Contexto de mercado (Eloi): dados regionais, sazonalidade, produtividade
  - Capacidade financeira (Mariano): fluxo de caixa, simulações, cenários
  - Enquadramento de crédito (Brasilino): linha adequada, condições, banco recomendado
  - Alternativas de fomento (Alberico): programas aplicáveis, complementaridade
  - Relacionamento (Marta): próximos passos concretos, responsáveis
- Matriz de decisão: o que é recomendado, por quê, com quem, até quando
- Rastreabilidade: links para todas as issues filhas e análises intermediárias

**Por que:** O Piloto 001 produziu 8 saídas distribuídas em 7 issues. A operação é rastreável internamente, mas pouco apresentável para banco, cliente ou tomada de decisão rápida. Uma nota-mãe consolida inteligência dispersa em artefato único.

**Formato:** Documento Markdown estruturado no Vault, seguindo padrão semelhante a este, com índice interno e links cruzados.

**Critério de conclusão para Piloto 002:** Ao final do caso, Cacilda entrega nota-mãe consolidada com todas as seções preenchidas. Carmen valida e assina. Nota fica disponível para Rodrigo, cliente ou banco sem necessidade de costura manual.

---

## 4. Pendências Estruturantes de Skills Antes do Piloto 002

**Contexto:** A revisão das skills existentes (ALT-79) mostrou que Eloi, Mariano e Marta ainda não possuem skills próprias adequadas aos papéis que exercem no fluxo operacional. Essas skills devem ser desenvolvidas antes de iniciar um Piloto 002, porque representam handoffs e entregas críticas que falharam ou ficaram incompletas no Piloto 001.

| Skill a desenvolver | Agente | Finalidade | Por que é estruturante antes do Piloto 002 |
|---|---|---|---|
| `handoff-mercado-financeiro` | Eloi | Produzir briefing de mercado com dados calibrados para Mariano: preço, produtividade, sazonalidade, riscos climáticos, premissas regionais e limites de confiança. | Corrige a falha do Piloto 001 em que o briefing de mercado não virou insumo formal para a simulação financeira. |
| `simular-capacidade-rural` | Mariano | Simular capacidade de pagamento separando dados documentais, declarados e estimados; citar explicitamente os dados de Eloi; apontar quais dados faltantes alteram a conclusão. | Garante análise financeira rastreável, coerente com o mercado e útil para crédito rural. |
| `registrar-ficha-crm-rural` | Marta | Criar ficha CRM com contexto relacional, origem da demanda, lacunas comerciais, objeções e próximo passo concreto obrigatório. | Evita lacunas sem responsável ou sem ação, fechando o ciclo relacional do cliente. |

**Condição adicional de liberação para Piloto 002:** Além de implementar protocolo fixo de abertura, templates por agente e nota-mãe final, a ALTOE deve resolver as três skills estruturantes de Eloi, Mariano e Marta. Carmen deve lembrar Rodrigo dessa pendência antes de abrir qualquer novo piloto operacional.

**Lembrete:** Antes de iniciar o Piloto 002, verificar se foram implementadas as três skills estruturantes pendentes: handoff de mercado para Eloi, simulação financeira rural para Mariano e ficha CRM rural para Marta. Sem essas três skills, o fluxo ainda fica vulnerável aos mesmos gaps do Piloto 001.

---

## Próximos Passos

1. **Implementação de Protocolo (Recomendação 1):** Definir Fase 0 como gate obrigatório, com checklist validável. Responsável: Carmen com Cacilda, Tereza.

2. **Templates (Recomendação 2):** Cada agente cria template de sua frente com campos, handoff, critério de aceitação. Responsável: cada agente, coordenado por Carmen.

3. **Nota-Mãe (Recomendação 3):** Definir estrutura padrão e template. Responsável: Cacilda com suporte de Carmen.

---

## Status de Implementação

| Recomendação | Status | Responsável | Prazo | Bloqueante para Piloto 002 |
|---|---|---|---|---|
| 1. Protocolo fixo | Pending | Carmen | - | ✅ Sim |
| 2. Templates | Pending | Todos | - | ✅ Sim |
| 3. Nota-mãe | Pending | Cacilda | - | ✅ Sim |
| 4. Skills estruturantes (Eloi, Mariano, Marta) | Pending | Eloi, Mariano, Marta | - | ✅ Sim |

**Condição de liberação para Piloto 002:** Todas as quatro recomendações/pendências estruturantes implementadas e validadas por Rodrigo. As três skills estruturantes (handoff-mercado-financeiro, simular-capacidade-rural, registrar-ficha-crm-rural) são bloqueantes equivalentes às recomendações 1-3.
