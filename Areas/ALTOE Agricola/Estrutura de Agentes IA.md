---
tipo: Proposta Estratégica
contexto: "[[ALTOE Agricola]]"
status: proposta
origin: "Carmen — ALT-24 (2026-05-03)"
created: 2026-05-03
atualizado: 2026-05-03
---

# Estrutura de Agentes IA — Proposta 2026

Proposta elaborada pela Carmen com base na análise da [[ALTOE Agricola]] — 8 agentes organizados em 3 camadas. Informação viva para discussão, refinamento e implementação no momento adequado. Contexto completo em [[Products/PKM/ai/Instructions]].

---

## Premissas da Análise

A ALTOÈ Agricola é uma microempresa de consultoria agronômica e de crédito rural, recém-constituída (fev/2026), com dois clientes ativos, um portfólio de propostas de fomento em andamento e uma visão estratégica bem articulada — tornar-se a **primeira consultoria de crédito rural e fomento com alto grau de automação por IA** no ES. O fundador (Rodrigo Altoè) tem perfil incomum: PhD com 20+ anos de pesquisa aplicada + capacidade de visão sistêmica sobre IA. Isso é um ativo diferencial raro no setor.

O momento atual (2026) é exatamente o ponto de inflexão de adoção: early movers que estruturarem seus fluxos de IA agora estarão anos à frente quando a adoção se massificar em 2028-2030. A janela de vantagem competitiva está aberta — e é finita.

A estrutura proposta é organizada em **três camadas**, com sequenciamento por maturidade operacional.

---

## CAMADA 1 — Áreas-Fim (Core Business)

### 1. Agente de Crédito Rural

**Papel:** Analista e estruturador de operações de crédito rural.

**Atividades:**
- Perfilamento de produtores: porte, cultura, área, histórico, enquadramento Pronaf/Pronamp/demais
- Matching de linhas de crédito: dado um perfil, identifica a melhor linha disponível no MCR, com taxas, prazos e condições vigentes
- Checklists documentais por banco e por linha (BB, Sicredi, Sicoob, Cresol, BNB, Banestes)
- Estruturação de projetos técnicos de crédito — cálculo de receita esperada, despesas, fluxo de caixa da propriedade, capacidade de pagamento
- Validação de conformidade antes de submissão (o projeto atende à linha escolhida?)
- Acompanhamento de cronograma de contratações e vencimentos

**Justificativa:** É o coração operacional da empresa. Hoje esse processo inteiro passa pela capacidade analítica do Rodrigo. Um agente especializado libera tempo do fundador para tarefas de alto valor (relacionamento, fomento) e permite atender mais clientes sem contratar — o que é especialmente crítico para uma ME. O MCR já está sendo ingerido no Vault, o que dá a base de conhecimento regulatório para esse agente operar com precisão. Com a maturação da base de clientes, este agente evolui para o motor preditivo descrito na visão estratégica.

---

### 2. Agente de Fomento e Inovação

**Papel:** Analista e gestor de projetos de P&D e captação de recursos de fomento.

**Atividades:**
- Monitoramento contínuo de editais (FAPES, FINEP, CNPq, BNDES, MMA, MCidades, etc.) — varre fontes, ingere novas oportunidades, alerta com análise de aderência já pronta
- Matching edital × ecossistema: dado um edital, identifica qual proponente, quais ICTs parceiras, quais membros da equipe e quais argumentos estratégicos têm melhor encaixe
- Manutenção do pipeline de propostas: status, prazos, pendências, ações
- Suporte à elaboração de propostas: estrutura inicial, marcos, justificativas, cronograma físico-financeiro baseado em editais anteriores
- Relacionamento com ecossistema de parceiros (IFES, LUMA, Amigos do Campo, etc.): quem está disponível, quais ICTs têm NIT ativo, quais têm experiência com quais agências

**Justificativa:** A ALTOÈ Agricola já tem múltiplas propostas em andamento (Conilon Trace, Eco Café Circular, PKM-FAPES06, Alchemco, UNI, GERENCIAR IA, entre outros) e um mapa de ecossistema bem desenvolvido. O volume de editais relevantes para o perfil da empresa — agricultura, conilon, economía circular, digital — é grande e crescente. Um agente especializado nessa função permite operar em paralelo com múltiplos editais sem perder rastreabilidade nem prazo. A memória acumulada de propostas anteriores é o diferencial competitivo aqui: o agente aprende o que funcionou e o que não funcionou em cada agência.

---

### 3. Agente Financeiro do Produtor

**Papel:** Coach financeiro para os produtores-clientes da empresa.

**Atividades:**
- Registro de receitas e despesas da propriedade por cultura, safra e atividade
- Construção e atualização de fluxo de caixa agrícola com sazonalidade real (colheita do conilon, ciclos de café, etc.)
- Indicadores de margem por hectare, por saca e por ciclo
- Simulações de impacto de crédito no fluxo de caixa projetado ("se contratar esse Pronaf, como fica seu caixa no período de carência?")
- Relatórios periódicos para o produtor — simples, em linguagem de campo
- Captura e estruturação de dados que alimentam o motor preditivo de crédito

**Justificativa:** Este agente tem dupla função estratégica. Para o produtor, é um serviço de valor concreto e diferenciador que fortalece o vínculo com a consultoria — fidelização pelo valor prático, não apenas pela transação de crédito. Para a ALTOÈ Agricola, é o mecanismo de captura do ativo mais valioso do negócio: **dados financeiros reais de propriedades rurais**, que são a matéria-prima do motor preditivo. Quanto mais produtores usam, melhor o modelo fica. É o ciclo virtuoso descrito na visão estratégica. Esse agente não existe em nenhum concorrente no ES — e provavelmente não existe em escala no Brasil.

**Timing:** Este agente é o de maior prazo de implantação, pois depende da definição do modelo de captura de dados (formulário? integração? planilha conversacional?). Mas deve ser **projetado agora** para que os outros agentes sejam desenvolvidos com a arquitetura de dados compatível.

---

## CAMADA 2 — Inteligência e Relacionamento

### 4. Agente de Inteligência de Mercado

**Papel:** Monitor de sinais de mercado para crédito e fomento.

**Atividades:**
- Monitoramento de preços agrícolas relevantes (café conilon, grãos, outros conforme carteira de clientes)
- Acompanhamento de séries climáticas e alertas sazonais (INMET, Incaper-ES, Cemaden)
- Leitura de políticas públicas: Plano Safra anual, atualizações do MCR/BCB, portarias MAPA
- Mapeamento de movimentos de mercado: novas cooperativas, novos bancos entrando no crédito rural, fintechs agro
- Alertas proativos: "chuvas abaixo do normal previstas para o ES — produtores de conilon no pico do florescimento podem precisar de custeio emergencial"
- Síntese de tendências de mercado para informar decisões estratégicas da empresa

**Justificativa:** Este é o agente "sensor" do sistema. Sem inputs de mercado em tempo (quase) real, o motor preditivo do crédito opera no vácuo. Hoje esse papel é informal — o Rodrigo monitora por intuição e experiência. Um agente sistematiza essa função e escala o radar. No contexto do Espírito Santo, onde o conilon domina a pauta agrícola e onde variações climáticas têm impacto dramático na demanda de crédito de custeio, ter este agente é uma vantagem operacional imediata. Com a evolução das ferramentas de IA para acesso a dados em tempo real, este agente se tornará progressivamente mais sofisticado.

---

### 5. Agente de CRM e Relacionamento

**Papel:** Gestor de relacionamento com clientes e ecossistema de parceiros.

**Atividades:**
- Onboarding de novos clientes: coleta e organização de documentação (integra com `/ingest-business`), perfilamento inicial, identificação de oportunidades imediatas
- Manutenção de histórico de relacionamento: o que foi discutido, o que foi contratado, próximas ações
- Alertas de oportunidade para clientes existentes: "Sergio Altoè agora se enquadra na linha Pronaf Mais Alimentos com a nova safra — momento de contato"
- Manutenção do ecossistema: disponibilidade de ICTs, status de parceiros, atualização de redes de contato
- Pré-relatórios para visitas: o agente prepara um briefing do cliente antes de uma reunião (histórico, situação atual, oportunidades pendentes)
- Follow-up sistemático de propostas e contratos em aberto

**Justificativa:** A retenção e o crescimento orgânico da carteira de clientes são o pilar de sustentabilidade de qualquer consultoria. Com base de clientes pequena mas com intenção de crescer, ter um sistema de relacionamento estruturado desde o início estabelece a disciplina certa. A diferença entre uma consultoria que tem 20 clientes e uma que tem 200 não é só o número — é o custo operacional de manter o relacionamento com qualidade. Este agente é a solução de escala para esse desafio. Em perspectiva futurista: o relacionamento mediado por IA personalizada será, dentro de 3-5 anos, o padrão do setor de consultoria — quem construir isso agora terá a vantagem do aprendizado.

---

## CAMADA 3 — Operacional Interno

### 6. Cacilda (já existe)

**Papel:** Bibliotecária e curadora do Vault.

**Atividades atuais:** Organização do Vault, consistência do PKM, manutenção de convenções de estrutura, lint da wiki.

**Evolução sugerida:** À medida que o Vault cresce e os outros agentes produzem mais conteúdo, Cacilda deve assumir um papel de **controle de qualidade da base de conhecimento** — garantindo que as páginas criadas pelos agentes de domínio (Crédito, Fomento) sejam consistentes entre si, sem contradições ou duplicidades.

---

### 7. Carmen (já existe)

**Papel:** Engenheira de processos e design organizacional.

**Atividades atuais:** Design de fluxos, estruturação de skills e workflows, avaliações organizacionais.

**Evolução sugerida:** Atuar como **arquiteta dos fluxos entre agentes** — definindo como os agentes se integram, quais handoffs existem entre eles (ex.: Fomento passa proposta para CRM acompanhar; Crédito aciona Mercado para validar contexto climático antes de uma operação), e como os processos evoluem conforme a empresa cresce. Ponto de contato para retrospectivas e ajustes estruturais.

---

### 8. Agente de Compliance e Documentação

**Papel:** Guardião da conformidade documental e regulatória.

**Atividades:**
- Monitoramento de validade de documentos: CNHs, certidões, IRPF, contratos (dos sócios, clientes e parceiros)
- Alertas de vencimento com antecedência suficiente para renovação sem urgência
- Acompanhamento de mudanças regulatórias: resoluções BCB, circulares MAPA, atualizações SNCR, portarias JUCEES
- Verificação de completude de pacotes documentais por banco (cada banco exige um conjunto específico)
- Checagem de conformidade de projetos de crédito antes de submissão
- Rastreabilidade de alterações contratuais e seus impactos (nova alteração contratual → quais bancos precisam ser notificados?)

**Justificativa:** O processo de cadastro bancário para crédito rural é notoriamente burocrático. Com múltiplos clientes e múltiplos bancos, manter o controle documental manualmente é um vetor de erro e perda de oportunidade (prazo de edital perdido por documento vencido, operação de crédito travada por certidão desatualizada). Este agente transforma compliance de tarefa reativa em processo proativo. No contexto regulatório brasileiro — especialmente crédito rural — esse é um ponto de dor alto e frequente.

---

## Sequenciamento Sugerido

| Fase | Agentes | Quando faz sentido |
|---|---|---|
| **Agora** | Crédito Rural, Fomento | Base técnica já existe (Vault, MCR, editais, parceiros); operam com os dados disponíveis hoje |
| **3-6 meses** | CRM, Compliance | Faz sentido quando a carteira de clientes cresce além de 5-6 produtores |
| **6-12 meses** | Inteligência de Mercado | Requer integração com fontes externas (preço, clima, políticas) — viável quando ferramentas de acesso a dados em tempo real estiverem mais maduras |
| **12+ meses** | Financeiro do Produtor | Depende de produto de captura de dados construído; mas o design deve começar agora |

---

## Observação Estrutural — Integração entre Agentes

Os agentes de domínio (Crédito, Fomento, CRM) **não são silos isolados** — precisam de um protocolo de handoff. Exemplos de integração a prever no design:

- Fomento detecta edital → aciona CRM para verificar disponibilidade de parceiros
- Crédito estrutura operação → aciona Compliance para verificar documentação do cliente
- Mercado detecta sinal climático → aciona CRM para pré-contato com produtores afetados
- Financeiro do Produtor atualiza dados → atualiza perfil do cliente no contexto do Crédito

Isso não exige que os agentes "conversem" diretamente hoje — pode ser mediado por issues no Multica ou por skills compartilhadas no Vault. Mas a lógica de fluxo deve estar clara desde o início para que cada agente seja desenhado com as saídas certas.

---

**Resumo:** 8 agentes no total (2 já existem), organizados em 3 camadas. O coração do sistema são os agentes de Crédito e Fomento, que operacionalizam as duas áreas-fim da empresa. A camada de inteligência (Mercado + CRM) é o que transforma a consultoria de reativa para preditiva. E a camada operacional (Cacilda + Carmen + Compliance) é a infraestrutura que garante que tudo funcione com consistência.
