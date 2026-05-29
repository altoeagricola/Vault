---
root: "[[AiRA - Plataforma Inteligente de Apoio à Recomendação Agronômica]]"
tipo: nota-tecnica
documento: "Escopo, metodologia e etapas do processo de desenvolvimento"
created: 2026-05-28
updated: 2026-05-28
tags:
  - Fomento
  - proposta
  - FAPES
  - escopo
  - metodologia
  - Scrum
  - IA-generativa
---

# Escopo e Metodologia — AiRA

## Objetivo Geral

Desenvolver uma plataforma inteligente de apoio à recomendação agronômica baseada em **IA generativa conversacional**, com foco na interpretação e utilização estratégica de dados técnicos e comerciais do setor agropecuário. O sistema apoiará agrônomos e técnicos agrícolas na:

- análise de laudos laboratoriais;
- identificação de deficiências nutricionais;
- recuperação de recomendações históricas;
- geração assistida de sugestões técnicas;
- integração com catálogo de produtos e campanhas comerciais.

A solução **não substitui** o agrônomo; atua como ferramenta de apoio à decisão.

## Objetivos Específicos (resumo executivo)

1. Seleção e formação da equipe do projeto.
2. Capacitação da equipe em IA generativa, LLM, sistemas de regras, desenvolvimento web e Agricultura Digital.
3. Definição do *setup* de desenvolvimento e ferramentas de gestão.
4. Mapeamento dos processos organizacionais da parceira (avaliação agronômica, interpretação de laudos, recomendação técnica, indicação de produtos).
5. Mapeamento e estruturação das fontes de dados (laudos, documentos técnicos, planilhas, histórico, catálogo, campanhas).
6. Definição dos requisitos da solução junto à parceira.
7. Definição da arquitetura de alto-nível.
8. Desenvolvimento dos módulos de cadastro (propriedades, áreas de cultivo, cultivos, culturas, informações nutricionais, clientes, catálogo).
9. Desenvolvimento do mecanismo de leitura e extração de informações de laudos laboratoriais.
10. Desenvolvimento do mecanismo de regras para recomendação a partir de informações técnicas de especialistas.
11. Desenvolvimento do mecanismo de IA generativa para construção de contexto, alinhando recomendações agronômicas, catálogo de produtos e estratégias comerciais.
12. Validar a solução junto a agrônomos, técnicos e gestores da parceira (usabilidade, eficiência operacional, aderência).

O detalhamento dos 12 objetivos específicos no **Quadro 5 (Cronograma Físico M1–M24)** ainda **não foi preenchido** no Anexo II — está com o gabarito-padrão.

## Etapas do Processo de Desenvolvimento (10 etapas)

### Etapa 1 — Iniciação

**Objetivo:** estruturar administrativamente o projeto, organizar a equipe e definir recursos tecnológicos.

- Atividades: seleção e formação da equipe; *setup* de gestão (ferramentas, contatos, armazenamento); capacitação inicial em IA generativa, sistemas de regras, LLMs, web e Agricultura Digital; definição das tecnologias.
- Entregas: equipe formada; *setup* montado; capacitação realizada; tecnologias definidas.

### Etapa 2 — Levantamento e Modelagem Organizacional

**Objetivo:** compreender os processos organizacionais da parceira.

- Atividades: mapear processos (avaliação agronômica, interpretação de laudos, recomendação técnica, indicação de produtos); mapear fontes de dados (laudos, documentos, planilhas, histórico, catálogo, campanhas); identificar fluxos que se relacionam com a solução.
- Entrega: **Documento de Especificação Organizacional** com mapeamento de processos, mapeamento das principais fontes de dados, modelagem inicial dos fluxos do sistema e como esses fluxos se relacionam com os processos (incluindo fluxos humano-IA esperados).

### Etapa 3 — Levantamento e Modelagem Preliminares de Requisitos

**Objetivo:** identificar e modelar requisitos preliminares (passíveis de refino posterior).

- Atividades: levantamento preliminar de requisitos funcionais e não-funcionais; modelagem das entidades do sistema; levantamento e modelagem preliminares do conhecimento técnico de avaliação de laudo e recomendação; definição da arquitetura de alto-nível.
- Entrega: **Documento de Especificação de Requisitos** com requisitos F/NF, modelagem de entidades, definição das regras de avaliação de laudos e recomendação, arquitetura de alto-nível.

### Etapa 4 — Desenvolvimento dos Módulos de Cadastro de Informações

**Objetivo:** desenvolver módulos básicos (propriedades, áreas de cultivo, cultivos, culturas, informações nutricionais por cultura, clientes, catálogo de produtos). Desenvolvimento inspirado em Scrum (ciclo PDCA aplicado aos eventos e artefatos do Scrum).

- Atividades: desenvolvimento dos módulos de cadastro; desenvolvimento do mecanismo de leitura e extração de informações de laudos laboratoriais.
- Entrega: versão inicial da solução com módulos de cadastro implementados (usuários e login, propriedades, áreas, cultivos, culturas, info nutricionais, clientes, catálogo) + mecanismo de extração de laudos.

### Etapa 5 — Desenvolvimento do Mecanismo de Pré-Recomendação Agronômica

**Objetivo:** geração de pré-recomendações com base em regras técnicas de especialistas. Scrum / PDCA.

- Atividades: definir tipos de pré-recomendação; definir e refinar regras técnicas; pesquisar e definir a estrutura do mecanismo de regras agronômicas; implementar regras técnicas, cálculos agronômicos, parametrização de protocolos, recomendações, restrições técnicas, associação problema↔recomendação, histórico e avaliação do técnico-usuário.
- Entrega: versão da solução com mecanismo de pré-recomendação e histórico + avaliação do técnico-usuário.

### Etapa 6 — Desenvolvimento do Mecanismo de IA Generativa

**Objetivo:** construção de contexto via IA generativa alinhando recomendações, catálogo e estratégias comerciais. Scrum / PDCA.

- Atividades: definir tipos de conversa/interação suportados; definir LLM(s) a utilizar; definir estratégia de armazenamento vetorial para RAG; implementar camada RAG e geração de embeddings; desenvolver o assistente conversacional.

### Etapa 7 — Validação da Solução

**Objetivo:** validar junto aos técnicos da parceira (usabilidade, potencial de uso no dia-a-dia, aderência).

- Atividades: testes de validação (qualidade das recomendações, facilidade de uso, confiabilidade da solução, qualidade das respostas da IA); ajustes.
- Entregas: relatório de validação; versão ajustada.

### Etapa 8 — Implantação da Solução na Empresa

**Objetivo:** implantar para uso experimental pelos técnicos e gestores.

- Atividades: implantar software e disponibilizar acesso; capacitar a equipe da parceira.
- Entregas: software implantado; **1 capacitação de 4 horas** realizada.

### Etapa 9 — Acompanhamento do Projeto

**Objetivo:** monitorar continuamente atividades, entregas, dificuldades e ajustes de rota.

- Atividades: reuniões periódicas; acompanhamento de marcos e cronograma; versionamento contínuo do software; registro de decisões técnicas e gerenciais.
- Entregas: atas/registros de reuniões; versionamento do software; registros de decisões.

### Etapa 10 — Encerramento do Projeto

**Objetivo:** finalizar entregas garantindo adimplência junto à FAPES e ao IFES.

- Atividades: elaborar relatório de avaliação (equipe + empresa); prestação de contas à FAPES; relatórios FAPES e IFES; comunicação à AGIFES; relatórios dos bolsistas; encerramento dos contratos dos bolsistas.
- Entrega: relatórios e prestação de contas.

## Metodologia Scrum

Desenvolvimento iterativo e incremental (Sprints) com:

- entregas contínuas de funcionalidades;
- validação frequente junto aos usuários;
- adaptação e repriorização progressiva dos requisitos;
- *review* + *retrospectiva* ao final de cada Sprint, retroalimentando novo planejamento.

Implicação contratual: o "contrato de desenvolvimento" **não fixa escopo rígido**; estabelece objetivos gerais, entregas prioritárias e mecanismos de acompanhamento contínuo — adequado a projetos de PD&I com requisitos voláteis. A cada ciclo, as funcionalidades previstas são reavaliadas, detalhadas e repriorizadas.

## Maturidade Tecnológica Alvo

**TRL 4–5** — protótipo funcional / prova de conceito tecnológica em cenário controlado ou ambiente relevante. **Não** se entrega produto comercial completo e pronto para operação em larga escala.

## Avanço Esperado em CT&I

- arquitetura de integração de dados estruturados e não estruturados (laudos, documentos, planilhas, histórico, catálogo, campanhas);
- aplicação de engenharia de prompts, RAG e representação de conhecimento agronômico ao contexto capixaba (lacuna na literatura aplicada brasileira);
- inovação organizacional na parceira (mudança cultural baseada em uso estratégico de dados);
- formação de RH local em IA aplicada ao agronegócio (área prioritária do Plano Estadual de CT&I do ES, SECTI-ES 2023);
- potencial de replicabilidade para outros segmentos do agronegócio (modelos preditivos, sensores, imagens de satélite — em iterações futuras).

## Exclusões de Escopo (proteção contra deriva)

1. Atividades não diretamente ligadas ao desenvolvimento, validação e demonstração da solução.
2. Substituição do trabalho profissional de agrônomos/técnicos — a solução é apoio à decisão; responsabilidade técnica permanece com profissionais habilitados.
3. Automação completa do processo de recomendação; geração de diagnósticos/prescrições definitivos sem supervisão humana; certificação técnica, homologação ou validação oficial junto a órgãos reguladores ou entidades de classe.
4. Manutenção corretiva/evolutiva, suporte contínuo após encerramento, garantias de operação comercial, hospedagem definitiva, sustentação de infraestrutura ou continuidade do desenvolvimento pós-financiamento.
5. Integração com sistemas corporativos da parceira. Aquisição/uso de equipamentos, sensores, IoT, drones, imagens de satélite ou outras tecnologias de agricultura digital não previstas.
6. Governança avançada de IA: trilhas completas de auditoria, controle de acesso avançado, monitoramento contínuo dos modelos, explicabilidade formal, gestão automatizada de riscos, certificações de governança de IA.

## Interdisciplinaridade

Áreas integradas: **Agronomia** (interpretação de laudos, deficiências nutricionais, manejo, recomendações); **Inteligência Artificial / LLMs / RAG**; **Engenharia de Software** (arquitetura, integração de dados, processamento de documentos não estruturados, interfaces); **Sistemas de Informação / processos de negócio** (fluxos agronômico-comerciais, relacionamento com clientes, estratégia comercial). Articulação universidade ↔ empresa ↔ ecossistema regional (Hélice Tríplice).

## Referências Citadas no Escopo (sintético)

ABNT ISO/IEC 38500:2018; Brasil — Lei 10.973/2004 (Inovação), LC 182/2021 (Marco das Startups), MAPA Plano de Transformação Digital (2023), Plano ABC+ (MAPA, 2021), Decreto 9.073/2017 (Acordo de Paris); CONFEA Código de Ética (2002); Davenport & Prusak (1998); EMBRAPA (2017); ES 2030 (2013); Etzkowitz & Leydesdorff (1995); FAO (2022); FDC/FINDES (2024); IBGE (2019); INCAPER (2023); IPCC (2021); Kamilaris & Prenafeta-Boldú (2018); Lewis et al. (2020) — RAG; Lumbantoning et al. (2022); Nonaka & Takeuchi (1995); O'Leary, Oljaca & Oljaca (2020); ONU (2015) — ODS; Prezotti et al. (2007) — Guia ES; Ribas (2021) — Scrum; Rubin (2018) — Scrum Essencial; SBCS (2017); SECTI-ES (2023); Shaikh et al. (2025); Sood et al. (2023); Taghizadeh-Mehrjardi et al. (2020); Yang et al. (2024); Zhu et al. (2025).

> Lista completa no Anexo II original — campo 3.13.
