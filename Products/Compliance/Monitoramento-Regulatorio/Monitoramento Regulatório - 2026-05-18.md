---
tipo: relatorio-monitoramento-regulatorio
data_monitoramento: 2026-05-18
janela_dias: 60
responsavel: Tereza
issue: ALT-191
status: concluido
tags:
  - compliance
  - monitoramento-regulatorio
  - vencimento-documental
  - credito-rural
---

# Monitoramento Regulatório - 2026-05-18

## Escopo

Varredura documental no Vault para documentos de produtores/clientes com possível vencimento entre 2026-05-18 e 2026-07-17.

Fontes consultadas:

- `Connections/Clientes/`
- `Products/Crédito-Rural/Clientes/`

Clientes/produtores encontrados no escopo operacional:

| Cliente/produtor | Situação documental |
| --- | --- |
| [[Sergio Jose Altoe]] | Dossiê documental estruturado, com PDFs e registros markdown |
| Walquimar Comerio | Pastas criadas, sem documentos além de `.gitkeep` |

## Resultado da Janela de 60 Dias

Não há documento com data de vencimento confirmada dentro da janela de 60 dias.

| Documento | Cliente | Validade confirmada | Dias até vencimento | Classificação |
| --- | --- | ---: | ---: | --- |
| [[Outorga Sergio Jose Altoe]] | [[Sergio Jose Altoe]] | 2029-04-10 | 1058 | Fora da janela |

## Alertas por Urgência

| Urgência | Critério | Quantidade |
| --- | --- | ---: |
| Crítico | 0-14 dias | 0 |
| Aviso | 15-30 dias | 0 |
| Notificação | 31-60 dias | 0 |

## Pendências Críticas de Extração

Os itens abaixo não entraram como alerta de vencimento porque a data não está extraída ou validada. Devem ser tratados como pendência de completude documental, não como vencimento confirmado.

| Documento | Cliente | Categoria | Risco | Responsável operacional |
| --- | --- | --- | --- | --- |
| CNH | [[Sergio Jose Altoe]] | Identidade | validade não confirmada | Cacilda/Tereza |
| CAF | [[Sergio Jose Altoe]] | Pronaf / crédito rural | impeditivo se vencido ou sem enquadramento | Brasilino/Tereza |
| RG/CPF de Sergio | [[Sergio Jose Altoe]] | Identidade | emissão/validade não confirmadas | Cacilda/Tereza |
| RG/CPF de Maria de Lourdes | [[Sergio Jose Altoe]] | Identidade / cônjuge | emissão/validade não confirmadas | Cacilda/Tereza |
| CCIR 2025 | [[Sergio Jose Altoe]] | Imóvel rural | quitação e validade não confirmadas | Brasilino/Tereza |
| ITR 2025 | [[Sergio Jose Altoe]] | Fiscal rural | quitação e vencimento do DARF não confirmados | Brasilino/Tereza |
| CAR | [[Sergio Jose Altoe]] | Ambiental | status SICAR não confirmado | Tereza/Rodrigo |
| Escritura | [[Sergio Jose Altoe]] | Titularidade | matrícula, ônus e área não confirmados | Tereza/Cacilda |
| Certidão de casamento | [[Sergio Jose Altoe]] | Estado civil | regime de bens e averbações não confirmados | Tereza/Cacilda |
| Comprovante de aposentadoria | [[Sergio Jose Altoe]] | Renda | competência e recência não confirmadas | Mariano/Tereza |

## Próxima Ação Recomendada

Priorizar OCR ou conferência visual dos PDFs críticos do caso Sergio Jose Altoe, preenchendo datas e campos materiais nos registros markdown. Sem isso, a automação diária não consegue diferenciar documento vigente de documento vencido para CNH, CAF, CCIR, ITR, RGs e certidões.

Para Walquimar Comerio, não há documento a monitorar enquanto as pastas permanecem vazias.
