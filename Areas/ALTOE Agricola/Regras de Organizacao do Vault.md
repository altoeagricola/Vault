---
tipo: Referência Interna
contexto: "[[ALTOE Agricola]]"
atualizado: 2026-05-03
---

# Regras de Organização do Vault

---

## Nomenclatura

- Sempre usar **ALTOE Agricola** (nome completo). Nunca abreviar para "ALTOE".

## Plugins Utilizados

- **Folder Note:** Cada pasta tem uma nota com o mesmo nome da pasta. Essa nota representa a própria pasta e recebe informações sobre ela. Em alguns casos, a folder note é apenas uma base/índice e não recebe conteúdo adicional.
- **Custom Sorting:** Não usar números de ordenação (01-, 02-, etc.) nos nomes de pastas ou notas. A ordenação é feita pelo plugin.

## Onde Incluir Cada Tipo de Informação

### Empresa
- **Areas/ALTOE Agricola/** — Informações sobre a empresa, equipe, serviços, diferencial, credenciamentos

### Bancos
- **Connections/Banks/** — Cada banco tem sua própria pasta e folder note. A nota Banks.base contém o quadro geral (base de dados).

### Região
- **Connections/Regioes/Marilandia/** — Informações sobre a região de Marilândia: produtores típicos, mercado local, contexto geográfico

### Conceitos de Negócio
- **Wiki-Comercial/** — Conceitos referentes às áreas de atuação da ALTOE Agricola. Exemplos: MCR (Manual de Crédito Rural), linhas de crédito, impedimentos de elegibilidade.

### Projetos de Crédito Rural
- **Products/Crédito-Rural/Projetos/** — Propostas já enviadas ao banco via sistema bancário (usando login da ALTOE Agricola). Distinção: "Proposta" = ainda não enviada. "Projeto" = já oficializado no banco.

### Projetos de Fomento
- **Products/Fomento/Projetos/** — Propostas aprovadas por instituições de fomento (FAPES, FAPESP, FAPEMG, FINEP, entre outras). Após aprovação, segue para contratação entre as partes (não passa por banco).

## Observações

- Informações que já existem no Vault devem ser respeitadas e complementadas, não duplicadas.
- Usar `[[wikilinks]]` para conectar notas entre pastas.
