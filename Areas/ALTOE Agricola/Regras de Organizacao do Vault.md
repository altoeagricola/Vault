---
tipo: Referência Interna
contexto: "[[ALTOE Agricola]]"
atualizado: 2026-05-09
---

# Regras de Organização do Vault

Regras específicas da ALTOE Agricola para organização do Vault. Para instruções gerais de workflows de agentes (ingestão, queries, lint, git), ver [[Products/PKM/AI/Instructions|Instructions.md]].

---

## Nomenclatura

- Sempre usar **ALTOE Agricola** (nome completo). Nunca abreviar para "ALTOE".

## Plugins Utilizados

- **Folder Note:** Cada pasta tem uma nota com o mesmo nome da pasta. Essa nota representa a própria pasta e recebe informações sobre ela. Em alguns casos, a folder note é apenas uma base/índice e não recebe conteúdo adicional.
- **Custom Sorting:** Não usar números de ordenação (01-, 02-, etc.) nos nomes de pastas ou notas. A ordenação é feita pelo plugin.

## Onde Incluir Cada Tipo de Informação

### Empresa
- **Areas/ALTOE Agricola/** — Informações sobre a empresa, equipe, serviços, diferencial, credenciamentos, processos operacionais e cadências de revisão

### Bancos
- **Connections/Banks/** — Cada banco tem sua própria pasta e folder note. A nota Banks.base contém o quadro geral (base de dados).

### Clientes (Produtores)
- **Connections/Clientes/** — Fichas de clientes (CRM). Dados de relacionamento, histórico, próximas ações.
- **Products/Crédito-Rural/Clientes/** — Documentos e dossiês operacionais específicos por cliente.

### Parceiros
- **Connections/Parceiros/** — Fichas de parceiros estratégicos (ICTs, cooperativas, prestadores).

### Região
- **Connections/Regioes/Marilandia/** — Informações sobre a região de Marilândia: produtores típicos, mercado local, contexto geográfico

### Conceitos de Negócio (Comercial e Regulatório)
- **Wiki-Comercial/** — Conceitos referentes às áreas de atuação da ALTOE Agricola: MCR, linhas de crédito (Pronaf, Pronamp, ABC+), impedimentos de elegibilidade, editais de fomento. **Distinto do Wiki/**: Wiki-Comercial é domínio do negócio; Wiki/ é conhecimento geral (ciência, tecnologia, mercado).

### Projetos de Crédito Rural
- **Products/Crédito-Rural/Projetos/** — Projetos já oficializados no banco (via sistema bancário com login da ALTOE Agricola).
- **Products/Crédito-Rural/Propostas/** — Propostas ainda não enviadas ao banco.
- **Products/Crédito-Rural/Operacoes/Fichas/** — Templates operacionais, formulários e modelos de CSV.
- **Products/Crédito-Rural/WikiCR/** — Base de conhecimento regulatório: MCR, normativos BCB, manuais de banco.

### Projetos de Fomento
- **Products/Fomento/Projetos/** — Propostas aprovadas por instituições de fomento (FAPES, FAPESP, FAPEMG, FINEP, entre outras). Após aprovação, segue para contratação entre as partes.
- **Products/Fomento/Editais/** — Editais prospectados ou em análise (não aprovados ainda).
- **Products/Fomento/WikiF/** — Base de conhecimento sobre fomento: agências, marcos legais, argumentos vencedores.

### Documentos Pessoais e Empresariais
- **Areas/ALTOE Agricola/Documents/** — Documentos de identidade pessoal e empresarial: CNH, RG, CPF, IRPF, Contrato Social, CNPJ, certidões.

## Observações

- Informações que já existem no Vault devem ser respeitadas e complementadas, não duplicadas.
- Usar `[[wikilinks]]` para conectar notas entre pastas.
- Conteúdo gerado por agentes vai para `Wiki/` (conhecimento geral) ou `Wiki-Comercial/` (domínio do negócio) — nunca diretamente em `Areas/` ou `Products/` sem solicitação explícita.
