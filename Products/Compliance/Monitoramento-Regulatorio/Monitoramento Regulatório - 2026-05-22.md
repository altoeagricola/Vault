---
tipo: relatorio-monitoramento-regulatorio
data_monitoramento: 2026-05-22
janela_dias: 60
periodo_monitorado: 2026-05-22 a 2026-07-21
responsavel: Tereza
issue: ALT-327
status: concluido
tags:
  - compliance
  - monitoramento-regulatorio
  - vencimento-documental
  - credito-rural
---

# Monitoramento Regulatório - 2026-05-22

## Escopo

Varredura documental no Vault para documentos de produtores/clientes com vencimento confirmado entre 2026-05-22 e 2026-07-21.

Fontes consultadas:

- `Connections/Clientes/`
- `Products/Crédito-Rural/Clientes/`
- registros anteriores em `Products/Compliance/Monitoramento-Regulatorio/`

Clientes/produtores encontrados no escopo operacional:

| Cliente/produtor | Situação documental |
| --- | --- |
| [[Sergio Jose Altoe]] | Dossiê documental estruturado, com PDFs e registros markdown |
| Walquimar Comerio | Pastas criadas, sem documentos além de `.gitkeep` |

## Resultado da Janela de 60 Dias

Não há documento com data de vencimento confirmada dentro da janela de 60 dias.

| Documento | Cliente | Validade confirmada | Dias até vencimento | Classificação |
| --- | --- | ---: | ---: | --- |
| [[Outorga Sergio Jose Altoe]] | [[Sergio Jose Altoe]] | 2029-04-10 | 1054 | Fora da janela |

## Alertas por Urgência

| Urgência | Critério | Quantidade | Roteamento |
| --- | --- | ---: | --- |
| Crítico | 0-14 dias | 0 | Nenhum alerta a criar |
| Aviso | 15-30 dias | 0 | Nenhum alerta a criar |
| Notificação | 31-60 dias | 0 | Nenhum alerta a criar |

## Pendências Críticas de Extração

Os itens abaixo não entram como alerta de vencimento porque a data não está extraída ou validada. Continuam como pendência de completude documental, não como vencimento confirmado.

| Documento | Cliente | Categoria | Risco | Responsável operacional |
| --- | --- | --- | --- | --- |
| CNH | [[Sergio Jose Altoe]] | Identidade | validade não confirmada; PDF sem OCR útil | Cacilda/Tereza |
| CAF | [[Sergio Jose Altoe]] | Pronaf / crédito rural | impeditivo se vencido ou sem enquadramento | Brasilino/Tereza |
| RG/CPF de Sergio | [[Sergio Jose Altoe]] | Identidade | RG extraído parcialmente; emissão antiga em 1994 exige validação de aceitação bancária | Cacilda/Tereza |
| RG/CPF de Maria de Lourdes | [[Sergio Jose Altoe]] | Identidade / cônjuge | emissão/validade não confirmadas; PDF sem OCR útil | Cacilda/Tereza |
| CCIR 2025 | [[Sergio Jose Altoe]] | Imóvel rural | quitação, área, titularidade e validade não confirmadas | Brasilino/Tereza |
| ITR 2025 | [[Sergio Jose Altoe]] | Fiscal rural | quitação e vencimento do DARF não confirmados | Brasilino/Tereza |
| CAR | [[Sergio Jose Altoe]] | Ambiental | status SICAR, embargo e sobreposição não confirmados | Tereza/Rodrigo |
| Escritura | [[Sergio Jose Altoe]] | Titularidade | matrícula, ônus, titularidade e área não confirmados | Tereza/Cacilda |
| Certidão de casamento | [[Sergio Jose Altoe]] | Estado civil | regime de bens e averbações não confirmados | Tereza/Cacilda |
| Comprovante de aposentadoria | [[Sergio Jose Altoe]] | Renda | competência, valor e recência não confirmados | Mariano/Tereza |

## Observação Técnica

Foi tentada extração textual com `pdftotext`. A maioria dos PDFs críticos de Sergio Jose Altoe parece ser scan sem OCR processado. A outorga retornou texto e confirma emissão em 2026-04-10, com validade operacional já registrada até 2029-04-10. O RG de Sergio retornou texto parcial, incluindo data de expedição em 10.11.1994, mas isso não substitui validação bancária/visual.

## Roteamento

Como não há vencimentos confirmados na janela de 60 dias, não foram criados alertas de vencimento para especialistas nesta execução.

As pendências de extração permanecem roteadas operacionalmente: identidade e titularidade para Cacilda/Tereza; CAF, CCIR e ITR para Brasilino/Tereza; CAR para Tereza/Rodrigo; renda para Mariano/Tereza.

## Próxima Ação Recomendada

Priorizar OCR ou conferência visual dos PDFs críticos do caso Sergio Jose Altoe, preenchendo datas e campos materiais nos registros markdown. Enquanto CNH, CAF, CCIR, ITR, CAR, RGs, certidões e renda estiverem em `precisa_confirmar`, a rotina diária consegue dizer que não há vencimento confirmado, mas não consegue garantir ausência de documento vencido.

Para Walquimar Comerio, não há documento a monitorar enquanto as pastas permanecem vazias.
