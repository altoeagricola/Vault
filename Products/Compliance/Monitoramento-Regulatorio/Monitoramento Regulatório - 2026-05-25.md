---
tipo: relatorio-monitoramento-regulatorio
data_monitoramento: 2026-05-25
janela_dias: 60
periodo_monitorado: 2026-05-25 a 2026-07-24
responsavel: Tereza
issue: ALT-367
status: concluido
tags:
  - compliance
  - monitoramento-regulatorio
  - vencimento-documental
  - credito-rural
---

# Monitoramento Regulatório - 2026-05-25

## Escopo

Varredura documental no Vault para documentos de produtores/clientes com vencimento confirmado dentro da janela operacional de 60 dias ou já vencidos.

Fontes consultadas:

- `Connections/Clientes/`
- `Products/Crédito-Rural/Clientes/`
- registros anteriores em `Products/Compliance/Monitoramento-Regulatorio/`

Clientes/produtores encontrados no escopo operacional:

| Cliente/produtor | Situação documental |
| --- | --- |
| [[Sergio Jose Altoe]] | Dossiê documental estruturado, com conferência visual parcial em 2026-05-23 |
| Walquimar Comerio | Pastas criadas, sem documentos além de `.gitkeep` |

## Resultado da Janela de 60 Dias

Não há documento com vencimento futuro confirmado entre 2026-05-25 e 2026-07-24.

Há, porém, documentos já vencidos com data confirmada. Esses itens permanecem em alerta crítico porque bloqueiam ou podem bloquear protocolo bancário.

| Documento | Cliente | Validade/vencimento confirmado | Dias até vencimento | Classificação | Roteamento |
| --- | --- | ---: | ---: | --- | --- |
| [[Registro - CAF Sergio Jose Altoe]] | [[Sergio Jose Altoe]] | 2026-04-22 | -33 | Crítico - vencido | Brasilino/Tereza |
| [[Registro - ITR Sergio Jose Altoe]] - DARF ITR 2025 | [[Sergio Jose Altoe]] | 2025-09-30 | -237 | Crítico - quitação pendente | Brasilino/Tereza |
| [[Registro - CNH Sergio Jose Altoe]] | [[Sergio Jose Altoe]] | 2027-08-04 | 436 | Fora da janela | Sem alerta |
| [[Outorga Sergio Jose Altoe]] | [[Sergio Jose Altoe]] | 2029-04-10 | 1051 | Fora da janela | Monitorar renovação futura |

## Alertas por Urgência

| Urgência | Critério | Quantidade | Roteamento |
| --- | --- | ---: | --- |
| Crítico | vencido ou 0-14 dias | 2 | Brasilino/Tereza |
| Aviso | 15-30 dias | 0 | Nenhum alerta novo |
| Notificação | 31-60 dias | 0 | Nenhum alerta novo |

## Alertas Críticos

### CAF - Sergio Jose Altoe

- Documento: CAF nº ES042024.01.001428279CAF.
- Vencimento confirmado: 22/04/2026.
- Status em 25/05/2026: vencido há 33 dias.
- Impacto: impeditivo atual para rota Pronaf, conforme checklist e referência ao MCR 10-2.
- Ação requerida: renovar CAF antes de qualquer protocolo Pronaf; depois registrar novo PDF, número, emissão, validade e enquadramento.
- Responsáveis operacionais: Brasilino/Tereza.

### ITR 2025 - Sergio Jose Altoe

- Documento: DARF/recibo DITR 2025 localizado.
- Vencimento confirmado do DARF: 30/09/2025.
- Status em 25/05/2026: vencido há 237 dias, sem comprovante de pagamento localizado no pacote.
- Impacto: risco de pendência fiscal rural e travamento de análise bancária.
- Ação requerida: obter comprovante de quitação ou regularizar pagamento; cruzar área/titularidade com CCIR, CAR e escritura.
- Responsáveis operacionais: Brasilino/Tereza.

## Pendências de Completude Documental

Os itens abaixo não entram como alerta de vencimento futuro porque a data não está extraída ou porque a pendência é de validação/completude, não de prazo confirmado.

| Documento | Cliente | Categoria | Risco | Responsável operacional |
| --- | --- | --- | --- | --- |
| RG/CPF de Sergio | [[Sergio Jose Altoe]] | Identidade | números e datas ainda precisam ser extraídos e conferidos contra CNH/cadastro | Cacilda/Tereza |
| RG/CPF de Maria de Lourdes | [[Sergio Jose Altoe]] | Identidade / cônjuge | CPF/RG e exigência de anuência ainda precisam ser confirmados | Cacilda/Tereza |
| CAR | [[Sergio Jose Altoe]] | Ambiental | status online SICAR/IDAF, embargo e sobreposição não confirmados | Tereza/Rodrigo |
| Escritura / matrícula | [[Sergio Jose Altoe]] | Titularidade | matrícula, ônus, titularidade e área não confirmados | Tereza/Cacilda |
| Certidão atualizada de matrícula | [[Sergio Jose Altoe]] | Titularidade / garantia | não localizada; pode ser exigida pelo banco | Tereza/Cacilda |
| Projeto técnico, orçamento e cronograma | [[Sergio Jose Altoe]] | Projeto de crédito | ausentes; impedem protocolo da habitação rural | Brasilino/Tereza |
| Cadastro/limite/formulários Cresol | [[Sergio Jose Altoe]] | Banco | não localizados; necessários para submissão operacional | Brasilino/Tereza |
| IRPF ou declaração de isenção | [[Sergio Jose Altoe]] | Fiscal pessoal | não localizado; pode ser exigido pela Cresol | Brasilino/Tereza |

## Roteamento

- Alertas críticos de CAF e ITR devem ser tratados antes de protocolo bancário.
- Identidade e titularidade seguem com Cacilda/Tereza para completar extração e rastreabilidade.
- CAR segue com Tereza/Rodrigo para validação em sistema oficial.
- Projeto, enquadramento Pronaf, lista Cresol e regularidade fiscal seguem com Brasilino/Tereza.

## Próxima Ação Recomendada

Renovar CAF e comprovar quitação do ITR antes de qualquer tentativa de protocolo. Em paralelo, completar os blocos de CAR, escritura/matrícula e peça técnica da habitação. A rotina diária agora deve tratar CAF e ITR como alertas críticos vencidos até que os registros markdown sejam atualizados com novos comprovantes válidos.
