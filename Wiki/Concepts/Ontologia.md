---
title: Ontologia
type: Concept
sources: []
related:
  - "[[Personal Knowledge Management]]"
  - "[[Julio C. Nardi]]"
created: 2026-04-26
updated: 2026-04-26
confidence: medium
---

**Ontologia** é a formalização explícita de um domínio de conhecimento: os conceitos que existem nesse domínio, suas propriedades, e as relações entre eles. Originada na filosofia (a rama que estuda o que existe e como as coisas se relacionam), o termo foi apropriado pela ciência da computação para nomear um artefato técnico — um modelo computável do mundo, ou de um pedaço dele.

## Componentes fundamentais

Uma ontologia computacional tipicamente define:

- **Classes (Conceitos)** — as categorias do domínio (ex: `Produtor Rural`, `Cultura`, `Linha de Crédito`)
- **Propriedades** — atributos das classes (ex: `area_plantada`, `taxa_juros`)
- **Relações** — como as classes se conectam entre si (ex: `Produtor` *solicita* `Financiamento`; `Financiamento` *é_regido_por* `MCR`)
- **Instâncias** — os indivíduos concretos que pertencem às classes (ex: João Silva, Pronaf Custeio)
- **Axiomas** — restrições lógicas que definem o que é válido no domínio

## Linguagens e padrões

| Linguagem | Propósito |
|-----------|-----------|
| **OWL** (Web Ontology Language) | Ontologias formais com raciocínio lógico (W3C) |
| **RDF / RDFS** | Grafos de conhecimento, tripletes sujeito–predicado–objeto |
| **SKOS** | Vocabulários controlados e taxonomias simples |
| **JSON-LD** | Linked Data em formato JSON, adotado por Schema.org |

## Ontologia vs. taxonomia vs. vocabulário controlado

Os três são formas de estruturar conhecimento, com graus crescentes de informalidade:

- **Vocabulário controlado** — lista de termos autorizados, sem relações entre eles
- **Taxonomia** — hierarquia de classes (é-um / subclasse-de)
- **Ontologia** — grafo completo: hierarquias + relações arbitrárias + axiomas lógicos

Uma ontologia pode incorporar uma taxonomia, mas o inverso raramente é verdadeiro.

## Aplicações em IA e sistemas de conhecimento

Ontologias são o substrato formal dos **grafos de conhecimento** — estruturas usadas por sistemas como o Google Knowledge Graph, Wikidata, e bases de conhecimento corporativas. Em contextos de IA:

- Permitem que agentes **raciocinem** sobre um domínio, não apenas recuperem dados
- Habilitam **queries semânticas** (SPARQL): "quais culturas podem ser financiadas pelo Pronaf Custeio com área menor que 4 módulos fiscais?"
- Facilitam **interoperabilidade** entre sistemas que usam terminologias diferentes
- Tornam o conhecimento **auditável e explicável** — diferente de embeddings vetoriais, uma ontologia é legível por humanos

## Relevância para este vault

A estrutura implícita do vault já é ontológica — `Concept`, `Entity`, `Figure`, `Summary` são classes; os wiki-links são relações; o frontmatter define propriedades. Formalizar essa taxonomia como uma ontologia OWL/RDF abriria possibilidades para:

- **AI-KB** — modelar formalmente `Skills`, `Commands`, `Agents`, `Prompts` e suas composições, permitindo que agentes raciocinem sobre capacidades disponíveis e as combinem automaticamente
- **[[Products/PKM/PKM|PKM]]** — tornar o grafo de conhecimento navegável por agentes de IA via SPARQL, em vez de depender de busca textual ou embeddings

[[Julio C. Nardi]], Professor Titular no IFES Campus Colatina e especialista em Ontology Engineering, é um colaborador potencial para esta formalização.
