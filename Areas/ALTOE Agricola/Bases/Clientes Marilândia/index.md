---
title: Base de Clientes — Marilândia
tipo: base_clientes
origem: Amigos do Campo
data_carga: 2026-05-27
total_registros: 2193
curador: Rodrigo
status: ativo
tags: [base, clientes, marilândia, crm, lgpd]
---

# Base de Clientes — Marilândia

Base herdada da **Amigos do Campo**, internalizada em 2026-05-27. Cobre produtores rurais da microrregião Marilândia/Colatina/Linhares (ES).

## Arquivos

| Arquivo                | Conteúdo                                        | Registros      |
| ---------------------- | ----------------------------------------------- | -------------- |
| `clientes.csv`         | Identidade dos clientes                         | 2.193          |
| `tag_perfil.csv`       | Tags de perfil por cliente                      | 256 atribuições |
| `interacoes.csv`       | Log de abordagens registradas                   | 19 interações  |
| `excecoes.csv`         | Registros com CPF pendente ou dados incompletos | 21             |
| `relatorio_carga.json` | Relatório de qualidade pós-carga                | —              |

## Cobertura pós-carga

| Campo | Cobertura |
|---|---|
| CPF válido | 100% (2.172/2.172) |
| Data de nascimento | 92% (2.009/2.172) |
| Telefone válido | 88% (1.921/2.172) |
| Cidade | 83% (1.824/2.172) — 348 com `cidade_pendente=true` |
| E-mail | 20% (446/2.172) |

## Concentração geográfica

| Cidade | Registros |
|---|---|
| Marilândia | 869 |
| Colatina | 491 |
| Linhares | 404 |
| Sem cidade (pendente) | 368 |
| Pancas | 20 |

## Política de acesso (LGPD)

**Campos restritos PII** (`cpf`, `data_nascimento`, `logradouro`, `bairro`, `cep`, `documento_ie`): acesso somente quando o cliente tiver projeto/operação ativa solicitada.

**Campos operacionais** (nome, cidade, telefone, email, tags, interações): acesso para Rodrigo, Carmen, Marta, Cacilda.

**Apenas agregado** (totais por cidade/tag): Eloi, Valdemiro, Antonietta.

Ver matriz completa em ALT-397.

## Base legal (LGPD)

- **Prospecção**: Legítimo interesse (art. 7º, IX) — documentado no ROP
- **Cliente ativo com operação**: Execução de contrato (art. 7º, V)
- **Retenção**: 5 anos sem interação → exclusão automática (com exceção para obrigação tributária)
- **Direitos do titular**: solicitação via e-mail para Rodrigo → execução pelo time de agentes

## Vocabulário de tags

**Porte**: `produtor_grande` · `produtor_medio` · `produtor_pequeno` · `produtor_arrendatario` · `produtor_proprietario`

**Comportamento financeiro**: `usa_custeio_anual` · `usa_investimento` · `nunca_financiou` · `inadimplente_historico`

**Infraestrutura**: `tem_secador` · `tem_irrigacao` · `tem_armazem`

**Cultura/Ciclo**: `cafe_conilon` · `cafe_arabica` · `pecuaria` · `gado_leite` · `gado_corte` · `pos_colheita_conilon_2026`

**Relacionamento**: `morador_exterior` · `responsavel_terceiro` · `visitamos_2026` · `mensagem_enviada_2026`

## Como atualizar

1. Para adicionar/corrigir dados de um cliente: edite diretamente o `clientes.csv` (coluna `cpf` é a chave)
2. Para registrar uma interação: adicione linha em `interacoes.csv` com o CPF do cliente
3. Para adicionar/remover tag: edite `tag_perfil.csv`
4. Para adicionar uma nova tag ao vocabulário: abra issue no workspace (tag nova precisa de aprovação do Rodrigo)
5. Atualize `ultimo_contato` no `clientes.csv` após cada interação — esse campo aciona a regra de retenção de 5 anos

## Listas de campanha

Notas abertas no Obsidian — acesse pela pasta `campanhas/`:

- [[Piloto 3 — Alto Rendimento]] — **6 produtores grandes** · visita presencial · maior prioridade
- [[Piloto 2 — Pós-Colheita Conilon]] — 10 produtores · proposta de custeio 2026/2027
- [[Piloto 1 — Marilândia]] — 10 produtores · abertura por WhatsApp

## Pendências

- **348 registros sem cidade** (`cidade_pendente=true`): preencher conforme abordagem/visita
- **21 registros sem CPF** (origem: Gabriely - PRIORIDADE MAIO): atualizar conforme abordagem dos produtores

---
*Carga executada por Carmen (ALT-401) · Aprovada por Rodrigo em 2026-05-27*
