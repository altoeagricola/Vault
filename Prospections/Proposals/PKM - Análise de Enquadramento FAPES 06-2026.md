---
title: "PKM — Análise de Enquadramento no FAPES 06/2026 (Clusters de Inovação)"
type: analysis
status: archived
product: "[[Products/PKM/PKM]]"
origin: "[[FAPES 06-2026 Clusters de Inovacao]]"
cluster: "Comércio (Cluster 1)"
fit_score: medium
created: 2026-04-17
updated: 2026-04-17
tags:
  - Prospection
  - proposal-analysis
---

## Contexto

Esta nota analisa o potencial de enquadramento do produto [[Products/PKM/PKM|PKM]] no [[FAPES 06-2026 Clusters de Inovacao|Edital FAPES Nº 06/2026 — Apoio aos Clusters de Inovação Capixaba]]. O prazo da 2ª edição encerrou em **06/04/2026** — esta análise serve como base para a **3ª edição** do programa, a ser monitorada.

O PKM, em sua forma atual, é um sistema pessoal de gestão do conhecimento. Para fins deste edital, seria necessário reposicioná-lo como **produto inovador com aplicação empresarial**, o que implica um esforço de produtização que também é avaliado aqui.

---

## Síntese do Enquadramento

O PKM tem enquadramento **viável com ressalvas** no Cluster 1 (Comércio), sob o tema **Transformação Digital**, com reforço pelos temas transversais de **Automação e IA**. O produto carrega inovação genuína na camada de agente de IA, mas sua maturidade comercial atual é baixa — o que exigiria que o projeto de P&D proposto ao edital financiasse a transição da solução pessoal para um produto empresarial.

| Dimensão | Avaliação | Observação |
|----------|-----------|------------|
| Alinhamento temático | ✅ Alto | Transformação digital + IA se encaixam no Cluster 1 |
| Inovação tecnológica | ✅ Alto | Agente LLM como mantenedor de wiki é diferencial real |
| Maturidade do produto | ⚠️ Baixa | Solução pessoal, sem versão comercial ou clientes |
| Aplicabilidade setorial | ⚠️ Média | Requer adaptação para casos de uso do comércio |
| Capacidade de execução | ⚠️ A avaliar | Depende da estrutura jurídica da empresa proponente |
| Adequação ao edital | ✅ Média-alta | Subvenção cobre P&D para chegar à condição de certificação/comercialização |

---

## Enquadramento Temático

### Cluster 1 — Comércio: Transformação Digital

O PKM pode ser enquadrado como uma **plataforma de inteligência de conhecimento para empresas de comércio**, cobrindo:

- **CRM e Inteligência de Cliente**: o pipeline de ingestão pode ser configurado para processar transcrições de reuniões, interações de vendas e feedbacks de clientes — construindo uma base de conhecimento estruturada e consultável sobre comportamento do consumidor.
- **Automação de marketing e inteligência competitiva**: ingestão automatizada de artigos, relatórios de mercado e notícias do setor, com síntese por agente e geração de insights acionáveis.
- **Centralização e retenção do conhecimento organizacional**: problema crítico no varejo com alta rotatividade de equipe — o PKM endereça diretamente a captura e estruturação do conhecimento tácito.

### Temas Transversais: Automação e IA

A camada de agente LLM é o diferencial central e o núcleo de inovação do projeto:

- Agente autônomo para manutenção de wiki (ingestão, lint, síntese)
- Skills como workflows reutilizáveis (`/ingest`, `/conceptualize`, `/lint`)
- Automação agendada (ex.: `weekly-wiki-lint`)
- Validação de qualidade por hooks pré-operação
- Integração com Claude Code (Anthropic) como runtime de agente

Esses elementos configuram um **sistema de IA aplicada à gestão do conhecimento empresarial**, com potencial de publicação como produto SaaS ou licença de software.

---

## Proposta de Produto para o Edital

Para submissão ao edital, o projeto de P&D precisaria ser formulado como a criação de um **produto novo ou significativamente melhorado**, com resultado final em condição de ingressar em certificação, produção e/ou comercialização (exigência do edital, item 3.1).

### Framing recomendado

> **"Plataforma de Gestão do Conhecimento Empresarial com Agente de IA para o Setor de Comércio"**
>
> Desenvolvimento de uma solução SaaS de PKM corporativo que utiliza agentes de IA para automatizar a ingestão, organização e síntese de informações estratégicas de empresas de comércio, com foco em inteligência competitiva, retenção de conhecimento organizacional e apoio à tomada de decisão.

### Entregas do projeto (24 meses)

| Entrega | Descrição | Mês estimado |
|---------|-----------|--------------|
| MVP empresarial | Adaptação do vault para multiusuário e contexto corporativo | M6 |
| Integração com fontes comerciais | Conectores para CRM, e-mail, notas de reunião, ERPs | M12 |
| Interface de consulta | Frontend para queries em linguagem natural sobre a base de conhecimento | M16 |
| Piloto setorial | Implantação em 2–3 empresas de comércio capixabas parceiras | M20 |
| Certificação e lançamento | Produto em condição de comercialização / SaaS | M24 |

---

## Pontos Fortes

1. **Inovação tecnológica real**: o padrão LLM Wiki (Karpathy) aplicado a contexto empresarial é genuinamente inovador no mercado nacional.
2. **Fundamentos sólidos**: GTD + PARA + LLM fornecem base metodológica rigorosa e referenciada.
3. **Prova de conceito funcional**: o vault existente é prova de conceito — 88 fontes ingeridas, 55 páginas de wiki, 7 skills operacionais.
4. **Baixa contrapartida**: 5% financeira é acessível para startup/empresa pequena.
5. **Subvenção não reembolsável**: risco financeiro controlado — adequado para estágio de P&D.
6. **Alinhamento com ODS**: ODS 8 (trabalho decente) e ODS 9 (inovação) são facilmente argumentáveis.

## Riscos e Lacunas

1. **Ausência de empresa proponente formal**: o PKM é produto pessoal — seria necessário uma empresa ES registrada há ≥6 meses como proponente.
2. **Maturidade comercial baixa**: sem clientes, sem CNPJ, sem modelo de negócio definido — o projeto proposto teria que cobrir essa transição.
3. **Foco setorial forçado**: a adaptação para comércio especificamente (vs. uso genérico) adiciona escopo ao projeto.
4. **Vedação de editais anteriores**: verificar se a empresa proponente não foi contratada nos Editais 07/2024 ou 10/2025.
5. **Concorrência com soluções consolidadas**: Notion AI, Confluence + AI, Microsoft Copilot — necessário diferenciar no formulário de mérito.

---

## Comparação com Conilon Trace

O projeto [[Conilon Trace]], também enquadrado no FAPES 06-2026, oferece referência valiosa:

| Aspecto | Conilon Trace | PKM |
|---------|--------------|-----|
| Cluster | Alimentos e Bebidas | Comércio |
| Tema principal | Rastreabilidade + Blockchain | Transformação Digital + IA |
| Maturidade do produto | — | Baixa (pessoal → empresarial) |
| Diferencial tecnológico | Rastreabilidade de origem | Agente LLM para curadoria |
| Complexidade de produtização | — | Média-alta |

---

## Recomendação

**Não submeter na 2ª edição** (prazo encerrado). Para a **3ª edição**, recomenda-se:

- [ ] Definir estrutura jurídica: abrir empresa ES ou usar empresa existente como proponente
- [ ] Validar modelo de negócio: SaaS, licença, consultoria com implementação?
- [ ] Identificar 1–2 empresas de comércio capixabas parceiras para piloto (fortalecem a proposta de mérito)
- [ ] Mapear concorrentes diretos no mercado nacional e posicionamento diferencial
- [ ] Avaliar parceria com ICT/IES capixaba (IFES, UFES, FAESA) — não obrigatório mas valorizado na avaliação
- [ ] Monitorar lançamento da 3ª edição via FAPES (duvidas.inovacao@fapes.es.gov.br)
- [ ] Revisar esta análise quando o novo edital for publicado — temas e critérios podem mudar

---

## Fontes

- [[FAPES 06-2026 Clusters de Inovacao]]
- [[Products/PKM/PKM]]
- [[Products/PKM/ai/Instructions]]
