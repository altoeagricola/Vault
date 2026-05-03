---
tipo: Referência
contexto: "[[ALTOE Agricola]]"
status: ativo
origin: "Carmen — ALT-24 (2026-05-03)"
created: 2026-05-03
atualizado: 2026-05-03T19:25Z
---

# Estrutura de Agentes IA — Referência Rápida

8 agentes em 3 camadas operando no Multica. Contexto completo, premissas e justificativas em [[Estrutura de Agentes IA - Contexto]].

---

## Sequenciamento de Implantação

| Fase | Agentes | Quando |
|------|---------|--------|
| **Agora** | Brasilino, Alberico | Base técnica disponível (Vault, MCR, editais, parceiros) |
| **3–6 meses** | Marta, Tereza | Carteira acima de 5–6 produtores ativos |
| **6–12 meses** | Eloi | Requer integração com fontes externas em tempo real |
| **12+ meses** | Mariano | Depende do produto de captura de dados do produtor |

---

## Plataformas e Modelos

| # | Nome | Camada | Modelo Configurado | Plataforma Indicada | Alternativa |
|---|------|--------|--------------------|---------------------|-------------|
| 1 | **Brasilino** | Áreas-Fim | Default | Claude — análise regulatória densa (MCR) | Gemini para PDFs longos |
| 2 | **Alberico** | Áreas-Fim | Default | Gemini Flash (monitoramento) + Claude Sonnet (redação) | Perplexity para varredura |
| 3 | **Mariano** | Áreas-Fim | gpt-5.4 | ChatGPT — Code Interpreter para cálculos e planilhas | Gemini + Google Sheets |
| 4 | **Eloi** | Inteligência | Default (Gemini) | Gemini Flash — Google Search embutido para alertas em tempo real | Perplexity |
| 5 | **Marta** | Inteligência | gpt-5.4 | Claude Haiku (rotina) + Sonnet (análises relacionais densas) | ChatGPT + Zapier |
| 6 | **Cacilda** | Operacional | claude-haiku-4-5-20251001 | Claude Haiku | — |
| 7 | **Carmen** | Operacional | claude-sonnet-4-6 | Claude Sonnet | — |
| 8 | **Tereza** | Operacional | claude-haiku-4-5-20251001 | Claude Haiku (checklists) + Gemini Flash (alertas de normas) | — |

---

## Perfis dos Agentes

| # | Nome | Papel | Responsabilidades Principais | Formação Ideal | Skills |
|---|------|-------|------------------------------|----------------|--------|
| 1 | **Brasilino** | Analista de Crédito Rural | Perfilamento de produtores; matching de linhas (Pronaf, Pronamp, demais); checklists por banco; estruturação de projetos técnicos; validação de conformidade; cronograma de contratações | Economia Rural / Agronomia; domínio MCR/BCB; experiência com BB, Sicoob, Sicredi, Cresol, BNB | `/enquadrar-produtor` `/checklist-banco` `/estruturar-projeto-cr` `/validar-conformidade` `/cronograma-contratacoes` |
| 2 | **Alberico** | Captador de Fomento | Varredura de editais (FAPES, FINEP, CNPq, BNDES etc.); matching edital × ecossistema; pipeline de propostas; elaboração de propostas; mapa de parceiros ICTs | Ciências Agrárias ou Inovação; experiência em agências de fomento; gestão de P&D (ABNT NBR, PMI) | `/scan-editais` `/match-edital` `/montar-proposta` `/alertar-prazo-edital` `/atualizar-pipeline-fomento` |
| 3 | **Mariano** | Coach Financeiro do Produtor | Registro de receitas/despesas por safra; fluxo de caixa agrícola; indicadores de margem por hectare e saca; simulações de impacto de crédito; relatórios em linguagem de campo | Economia / Contabilidade; agronegócio; sistemas de gestão rural (AgroReceita, Aegro) | `/registrar-lancamento-rural` `/calcular-fluxo-caixa-agro` `/simular-impacto-credito` `/gerar-relatorio-produtor` `/capturar-dados-safra` |
| 4 | **Eloi** | Inteligência de Mercado | Preços agrícolas (conilon, grãos); alertas climáticos INMET/Incaper; políticas públicas (Plano Safra, MCR, MAPA); movimentos de mercado; sínteses de tendência | Economia Agrícola / Jornalismo; CONAB, CEPEA, INMET; inteligência competitiva | `/monitorar-preco-conilon` `/alertar-clima-es` `/varrer-politicas-publicas` `/sintetizar-tendencia-mercado` `/briefing-conjuntura` |
| 5 | **Marta** | CRM e Relacionamento | Onboarding de clientes; histórico de relacionamento e próximas ações; alertas de oportunidade; ecossistema de parceiros; briefings de visita; follow-up de propostas | Administração / Marketing; CRM; agronegócio; forte orientação a relacionamento | `/onboarding-cliente` `/briefing-visita` `/alertar-oportunidade-cliente` `/atualizar-historico-rel` `/mapear-ecossistema-parceiros` |
| 6 | **Cacilda** | Curadora do Vault | Organização e consistência do Vault; manutenção de convenções; lint da wiki; qualidade da base de conhecimento; duplicatas e contradições | Biblioteconomia / Ciência da Informação; PKM (Zettelkasten, PARA, LYT); Obsidian | `/lint` `/ingest` `/ingest-business` `/auditoria-vault` `/detectar-duplicatas` `/verificar-links-quebrados` |
| 7 | **Carmen** | Design de Processos | Design de fluxos operacionais; estruturação de skills e workflows; arquitetura de integração entre agentes; retrospectivas e ajustes estruturais | Engenharia de Produção / Administração; BPM; transformação digital de PMEs | `/ingest-business` `/mapear-processo` `/diagnosticar-gargalo` `/propor-automacao` `/revisar-workflow` |
| 8 | **Tereza** | Compliance Documental | Validade de documentos (CNH, certidões, IRPF, CCIR); alertas de vencimento; mudanças regulatórias (BCB, MAPA, SNCR, JUCEES); completude de pacotes por banco; rastreabilidade de alterações contratuais | Direito / Administração; compliance e regulação; BCB, SNCR, CAR, INCRA | `/verificar-validade-docs` `/alertar-vencimento` `/monitorar-normas-bcb` `/checklist-documental-banco` `/rastrear-alteracao-contratual` |

---

## Tipo de Tarefa × Plataforma

| Tipo de Tarefa | Plataforma | Exemplo |
|----------------|-----------|---------|
| Varredura/monitoramento contínuo | Gemini Flash | Editais, alertas de preço, mudanças regulatórias |
| Análise regulatória densa | Claude Sonnet | MCR, conformidade de projetos, estruturação de crédito |
| Cálculos / modelos financeiros | ChatGPT GPT-4o | Fluxo de caixa, simulações de crédito |
| Comunicação / relatórios rotineiros | Claude Haiku | Briefings, follow-ups, relatórios simples |
