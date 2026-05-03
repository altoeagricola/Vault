---
title: "PKM — Análise de Enquadramento no FAPES 06/2026 (Clusters de Inovação)"
type: analysis
status: Em elaboração
product: "[[Products/PKM/PKM]]"
origin: "[[FAPES 06-2026 Clusters de Inovação]]"
cluster: "Alimentos e Bebidas (Cluster 2)"
fit_score: medium-high
deadline: 2026-05-06
coordenador: "[[Edgar O. Machado]]"
parceira-piloto: "[[ALTOE Agricola]]"
ict-target: "[[Julio C. Nardi]]"
created: 2026-04-17
updated: 2026-04-28
tags:
  - Prospection
  - proposal-analysis
---

## Contexto

Esta nota analisa o enquadramento do produto [[Products/PKM/PKM|PKM]] no [[FAPES 06-2026 Clusters de Inovacao|Edital FAPES Nº 06/2026]]. O prazo foi **prorrogado para 06/05/2026 às 17h59** — há janela real de submissão.

**Premissas confirmadas (28/04/2026):**

1. **Coordenador do projeto:** [[Edgar O. Machado]] — perfil TI, ex-CEFETES, arquiteto de dados.
2. **Parceira piloto:** [[ALTOE Agricola]] — testa o PKM em escala piloto como primeira cliente interna, no domínio de crédito rural e fomento agropecuário (Marilândia e municípios adjacentes, foco em café conilon).
3. **ICT parceira alvo:** [[Julio C. Nardi]] (IFES Colatina) — especialista em ontologia, potencial colaborador AI-KB/PKM. Parceria a ser confirmada.
4. O foco setorial regional é **café conilon**, cultura dominante na região central-serrana capixaba, com cadeia produtiva que envolve produtores, cooperativas, indústrias de torrefação e processamento.

## Correção a uma Premissa Inicial

> *Sinalização solicitada pelo usuário:* a hipótese de que o edital seria "principalmente voltado a alimentos e bebidas" **não se sustenta na leitura do edital nem na comunicação oficial da FAPES**.

O edital é **paritário** entre os dois clusters:

| Cluster | Orçamento | Projetos mínimos |
|---------|-----------|------------------|
| Comércio | R$ 6.000.000 | 10 |
| Indústria de Alimentos e Bebidas | R$ 6.000.000 | 10 |

Recursos remanescentes de um cluster **podem** ser redirecionados ao outro (item orçamentário), mas isso é uma regra de contingência — não um viés de desenho. A 2ª edição do programa Clusters de Inovação Capixaba manteve a mesma estrutura dual da 1ª edição.

**Implicação:** a estratégia de enquadramento deve escolher **um dos dois clusters** como eixo principal, sem assumir que alimentos e bebidas tem preferência intrínseca.

---

## Enquadramento Recomendado: Cluster 2 — Alimentos e Bebidas

Dado o recorte regional (café conilon em Marilândia) e o perfil da consultoria como proponente, o enquadramento mais defensável é o **Cluster 2 — Indústria de Alimentos e Bebidas**, tema principal **Rastreabilidade e Segurança Alimentar**, com reforço no tema transversal **Automação e IA**.

### Racional do enquadramento

O café conilon é, para fins do edital, uma commodity de entrada para a **indústria de bebidas** (torrefação, moagem, blending, produção de cafés solúveis, cápsulas). O elo industrial da cadeia — não a produção primária — é o que está coberto pelo cluster. A consultoria, ao desenvolver o PKM como piloto e oferecer a ferramenta para indústrias de torrefação e cooperativas com unidades de beneficiamento na região, entrega valor exatamente no segmento alvo do cluster.

### Proposta de produto

> **"Plataforma de Conhecimento Agroindustrial para a Cadeia do Café Conilon — curadoria assistida por IA de dados regulatórios, técnicos e de mercado para indústrias de torrefação e cooperativas de beneficiamento do Espírito Santo"**

A plataforma consolida, num único ambiente mantido por agente LLM:

- **Base de conhecimento regulatória**: normas MAPA, ANVISA, certificações (Rainforest, UTZ, 4C, orgânico, fair trade), exigências de exportação
- **Inteligência de mercado**: preços CEPEA, tendências de consumo, compradores internacionais, câmbio
- **Rastreabilidade documental**: histórico de lotes, origem por propriedade/região, dados de beneficiamento, certificações vigentes
- **Curadoria técnica**: fichas de variedades clonais (Vitória, Diamante, Centenária), protocolos de pós-colheita, parâmetros de qualidade (tipos 2 a 8, bebidas)
- **Pipeline de propostas de fomento**: ingestão automatizada de editais (FAPES, FINEP, BANDES, BNDES), cruzamento com perfil do cliente, geração de briefings

### Alinhamento com os temas do Cluster 2

| Tema do edital | Como o PKM endereça |
|----------------|---------------------|
| Rastreabilidade e segurança alimentar | Curadoria documental estruturada de lotes, origens, certificações — acessível via consultas em linguagem natural |
| Automação e Indústria 4.0 (transversal) | Agente LLM que ingere fontes (editais, normas, relatórios), mantém wiki viva, gera sínteses — automação de trabalho cognitivo |
| Eficiência (transversal) | Redução de tempo de pesquisa e preparo de documentação técnica em cooperativas e torrefadoras de pequeno/médio porte |

---

## Enquadramento Alternativo: Cluster 1 — Comércio

Possível, porém menos aderente à realidade regional proposta. Exigiria enquadrar a consultoria como **empresa de comércio de serviços** e o PKM como ferramenta de transformação digital do seu próprio negócio. O edital, entretanto, dá exemplos de Comércio focados em varejo/e-commerce (CRM, logística reversa, meios de pagamento) — a consultoria como comércio é um esticamento conceitual.

Recomenda-se **não** perseguir essa rota como eixo principal.

---

## Pontos Fortes do Enquadramento Revisado

1. **Coerência regional forte**: Marilândia e municípios vizinhos formam o coração da produção de conilon no ES — o estado responde por ~70% da produção nacional de conilon, concentrada na região central. A proposta tem identidade territorial clara, fator valorizado na avaliação de mérito.
2. **Empresa proponente viável**: a consultoria já atua no domínio de editais de subvenção — tem maturidade institucional para executar projeto FAPES de 24 meses.
3. **Piloto interno + produto**: a consultoria se autoaplica como primeiro cliente (redução de risco de adoção), e o produto se projeta para a cadeia de torrefação e cooperativas.
4. **Inovação tecnológica real**: o padrão LLM Wiki aplicado à cadeia do café é inédito — não há concorrente direto no mercado nacional para este recorte.
5. **ODS alinhados**: ODS 8, 9, 12 e 17 todos defensáveis. Especialmente ODS 12 (produção/consumo responsável) pela ênfase em rastreabilidade.
6. **ICT parceira alvo definida**: [[Julio C. Nardi]] (IFES Colatina) — especialista em ontologia, perfil diretamente alinhado à arquitetura do PKM. Contato a ser formalizado. Alternativas: Incaper, UFES São Mateus.
7. **Contrapartida 5%**: acessível para a consultoria.

## Riscos e Lacunas

1. **Elegibilidade da consultoria**: confirmar sede ou filial ativa no ES, regularidade fiscal, e que **não foi contratada nos Editais 07/2024 (Tecnova III) nem 10/2025 (Nova Economia Capixaba)** — vedação explícita.
    - **Marco dos 6 meses de atividade (item 9.4 do edital, texto literal)**: *"A empresa proponente deverá estar ativa, demonstrando atividades e operações econômicas e financeiras a pelo menos 6 (seis) meses antes da data de publicação deste Edital."* O marco é **20/02/2026 (publicação)**, não a data de contratação — a empresa precisa estar ativa desde **20/08/2025 ou antes**. Prorrogações de submissão ou demora na contratação não afrouxam esse ponto.
    - A exigência é de "atividades e operações econômicas e financeiras" — CNPJ dormente não satisfaz. É necessário comprovar faturamento, movimentação e despesas no período.
2. **Limite da cadeia coberta**: o edital cobre **indústria** de alimentos e bebidas, não produção primária (lavoura). O projeto deve ser redigido com foco claro no elo industrial — torrefação, beneficiamento, processamento — e no apoio à consultoria como fornecedora de ferramentas a esse elo. Evitar linguagem que sugira atendimento direto ao produtor rural, pois pode ser interpretado como fora do escopo.
3. **Concorrência com [[Conilon Trace]]**: há outra proposta em desenvolvimento no vault voltada ao mesmo setor, no mesmo cluster, para o mesmo edital. Revisar sobreposição — há complementaridade ou canibalização? Possível oportunidade de **parceria ou submissão única** em vez de competição interna.
4. **Avaliação ad hoc externa**: mérito avaliado por pareceristas preferencialmente fora do ES — a redação precisa comunicar a relevância do conilon e da região sem assumir familiaridade do avaliador.
5. **Maturidade do produto**: PKM hoje é pessoal. O projeto de 24 meses cobre a transição, mas a narrativa precisa ser honesta sobre o TRL inicial e o salto pretendido.
6. **Uma proposta por empresa**: se a consultoria pretende submeter outra proposta, esta precisa ser a escolhida.

---

## Articulação com [[Conilon Trace]]

Ambas as propostas incidem sobre a cadeia do conilon e o Cluster 2 do mesmo edital. Antes de qualquer avanço, é necessário definir a relação entre elas:

- **Cenário A — Consolidação**: unir as duas propostas em uma única, usando o PKM como camada de conhecimento/curadoria e o Conilon Trace como camada de rastreabilidade operacional. Complementaridade natural.
- **Cenário B — Separação**: se forem empresas proponentes distintas, ambas podem ser submetidas (edital não impede submissões independentes de empresas diferentes); se for a mesma empresa, apenas uma pode concorrer.
- **Cenário C — Priorização**: escolher a mais madura para esta edição e reservar a outra para a 3ª edição ou outro edital (ex.: FINEP, BNDES Agro).

---

## Próximos Passos

- [x] Confirmar estrutura jurídica e elegibilidade da consultoria de crédito rural (sede/filial ES, ≥6 meses, regularidade, vedação de editais anteriores) ✅ 2026-04-29
- [x] Definir relação com [[Conilon Trace]] (consolidação, separação ou priorização) ✅ 2026-04-29
- [x] Confirmar parceria com [[Julio C. Nardi]] (IFES Colatina) como ICT — verificar se NIT foi apoiado pelo Edital FAPES 11/2025 ✅ 2026-04-29
- [x] Mapear 1–2 indústrias de torrefação ou cooperativas de beneficiamento como parceiras adicionais (cartas de anuência fortalecem o mérito) ✅ 2026-04-29
- [x] Levantar dados de mercado: tamanho da indústria capixaba de torrefação/beneficiamento de conilon, número de empresas potencialmente atendidas ✅ 2026-04-29
- [x] Rascunhar Anexo I (Formulário de Submissão) com foco no elo industrial da cadeia ✅ 2026-04-29
- [x] Definir cronograma de 24 meses com entregas claras: MVP empresarial → integrações setoriais (preços, certificações, editais) → piloto com consultoria e 1–2 indústrias → empacotamento SaaS ✅ 2026-04-29
- [x] Submeter via SigFapes até **06/05/2026 17h59** ✅ 2026-04-29

---

## Fontes

- [[FAPES 06-2026 Clusters de Inovacao]]
- [[Products/PKM/PKM]]
- [[Products/PKM/ai/Instructions]]
- FAPES, notícia oficial da prorrogação (fonte: fapes.es.gov.br)
