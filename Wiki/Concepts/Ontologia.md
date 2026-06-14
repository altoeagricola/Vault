---
title: Ontologia
type: Concept
sources:
  - "W3C OWL 2 Web Ontology Language: https://www.w3.org/TR/owl2-overview/"
  - "W3C RDF: https://www.w3.org/RDF/"
  - "W3C SKOS Reference: https://www.w3.org/TR/skos-reference/"
  - "W3C JSON-LD 1.1: https://www.w3.org/TR/json-ld11/"
  - "[[Personal Knowledge Management]]"
related:
  - "[[Personal Knowledge Management]]"
  - "[[Julio C. Nardi]]"
created: 2026-04-26
updated: 2026-06-01
confidence: high
---

**Ontologia** é uma forma explícita de modelar um domínio de conhecimento: os tipos de coisas que existem, suas propriedades, suas relações e as regras que permitem interpretar essas relações. Na prática, ela transforma conhecimento disperso em uma estrutura legível por humanos e processável por máquinas.

No contexto deste Vault, ontologia não é um exercício acadêmico separado da operação. Ela é uma disciplina de organização: tornar conceitos, entidades, documentos, produtos, agentes e skills consistentes o suficiente para que o [[Personal Knowledge Management|PKM]] e o AI-KB possam ser consultados, auditados e evoluídos sem depender apenas de busca textual.

## Componentes fundamentais

| Componente | Papel no modelo | Exemplo neste Vault |
|---|---|---|
| Classes | Categorias do domínio | `Concept`, `Entity`, `Figure`, `Tool`, `Program` |
| Propriedades | Atributos estruturados | `sources`, `related`, `confidence`, `updated` |
| Relações | Conexões entre itens | `[[MCR]]` regula `[[Pronaf]]`; `[[Reflorestar — Bônus Polinizadores]]` depende de `[[ICMBio-PAN]]` |
| Instâncias | Casos concretos | Sergio Jose Altoe, um edital, uma operação de crédito, uma nota fonte |
| Restrições | Regras de validade | Toda página Wiki precisa ter `sources`, `related`, `updated` e `confidence` coerentes |

## Linguagens e padrões

| Padrão | Função prática |
|---|---|
| **RDF / RDFS** | Representar fatos como triplas sujeito-predicado-objeto e dar vocabulário básico ao grafo |
| **OWL** | Definir ontologias com semântica formal, classes, propriedades, indivíduos e regras de inferência |
| **SKOS** | Modelar vocabulários controlados, taxonomias, tesauros e esquemas conceituais mais leves |
| **JSON-LD** | Serializar dados ligados em JSON, facilitando integração com sistemas web e APIs |

Esses padrões não precisam ser adotados todos de uma vez. Para um Vault operacional, o primeiro passo é manter uma ontologia implícita limpa: tipos de página estáveis, frontmatter completo, links canônicos e nomes previsíveis. Só depois faz sentido formalizar partes do domínio em RDF/OWL.

## Ontologia, taxonomia e vocabulário controlado

- **Vocabulário controlado** define quais termos devem ser usados.
- **Taxonomia** organiza termos em hierarquias, como categoria e subcategoria.
- **Ontologia** inclui hierarquias, mas também relações arbitrárias, propriedades, restrições e regras de interpretação.

Uma taxonomia diz que `Pronaf` é uma linha/programa de crédito rural. Uma ontologia também pode dizer que `Pronaf` é regido pelo `MCR`, depende de enquadramento do produtor, tem fontes normativas e pode ser afetado por atualizações específicas do Banco Central.

## Relevância para PKM e AI-KB

O [[Personal Knowledge Management|PKM]] organiza o que se sabe. O AI-KB organiza como agentes agem sobre esse conhecimento. A ontologia é a ponte entre os dois:

- permite que agentes diferenciem fonte, síntese, conceito, entidade, programa e documento operacional;
- reduz ambiguidades entre nomes parecidos, aliases e links incompletos;
- sustenta lint automatizado de consistência, como órfãs, `sources` vazios e claims stale;
- abre caminho para consultas semânticas mais fortes, como "quais programas estaduais de PSA dependem de CAR e estão relacionados a crédito rural verde?";
- torna a base auditável, porque cada claim importante pode apontar para fonte, confiança e atualização.

## Cuidados práticos

Ontologias envelhecem quando a operação muda e o modelo não acompanha. Neste Vault, os sinais de alerta são simples:

- conceitos citados repetidamente sem página própria;
- páginas com `sources` vazio;
- aliases que resolvem por acaso, mas não por nome canônico;
- relações importantes só no corpo da nota, sem aparecer em `related`;
- claims de confiança baixa ou média sem revisão periódica.

## Próximos fios

- Formalizar um vocabulário mínimo para tipos de página do Vault.
- Separar melhor fonte primária, síntese interna e decisão operacional.
- Investigar se partes do domínio de crédito rural e fomento merecem uma ontologia própria.
- Avaliar com [[Julio C. Nardi]] se há ganho real em representar algum recorte do PKM em RDF/OWL, em vez de manter apenas convenções Markdown.
