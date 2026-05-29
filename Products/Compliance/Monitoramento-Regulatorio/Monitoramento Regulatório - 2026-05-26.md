---
tipo: relatorio-monitoramento-regulatorio
data_monitoramento: 2026-05-26
janela_dias: 60
periodo_monitorado: 2026-05-26 a 2026-07-25
responsavel: Tereza
issue: ALT-375
status: concluido
tags:
  - compliance
  - monitoramento-regulatorio
  - vencimento-documental
  - credito-rural
---

# Monitoramento Regulatório - 2026-05-26

## Escopo

Varredura documental no Vault para documentos de produtores/clientes com vencimento confirmado dentro da janela operacional de 60 dias ou já vencidos.

Fontes consultadas:

- `Connections/Clientes/`
- `Products/Crédito-Rural/Clientes/`
- registros anteriores em `Products/Compliance/Monitoramento-Regulatorio/`
- issue de alerta crítico `ALT-371`

Clientes/produtores encontrados no escopo operacional:

| Cliente/produtor | Situação documental |
| --- | --- |
| [[Sergio Jose Altoe]] | Dossiê documental estruturado, com plano de saneamento atualizado em 2026-05-25 |
| Walquimar Comerio | Pastas criadas, sem documentos além de `.gitkeep` |

Arquivos documentais novos ou alterados desde o relatório de 2026-05-25:

| Arquivo | Leitura de compliance |
| --- | --- |
| `Products/Crédito-Rural/Clientes/Sergio Jose Altoe/Checklist Documental - Sergio Jose Altoe.md` | Brasilino reforçou o plano de saneamento; não há evidência nova de CAF renovado ou ITR quitado |

## Resultado da Janela de 60 Dias

Não há documento com vencimento futuro confirmado entre 2026-05-26 e 2026-07-25.

Persistem documentos já vencidos com data confirmada. Esses itens permanecem em alerta crítico porque bloqueiam ou podem bloquear protocolo bancário.

| Documento | Cliente | Validade/vencimento confirmado | Dias até vencimento | Classificação | Roteamento |
| --- | --- | ---: | ---: | --- | --- |
| [[Registro - CAF Sergio Jose Altoe]] | [[Sergio Jose Altoe]] | 2026-04-22 | -34 | Crítico - vencido | Brasilino/Tereza |
| [[Registro - ITR Sergio Jose Altoe]] - DARF ITR 2025 | [[Sergio Jose Altoe]] | 2025-09-30 | -238 | Crítico - quitação pendente | Brasilino/Tereza |
| [[Registro - CNH Sergio Jose Altoe]] | [[Sergio Jose Altoe]] | 2027-08-04 | 435 | Fora da janela | Sem alerta |
| [[Outorga Sergio Jose Altoe]] | [[Sergio Jose Altoe]] | 2029-04-10 | 1050 | Fora da janela | Monitorar renovação futura |

Observação: a certidão de casamento de Sergio e Maria de Lourdes foi emitida em 2026-04-07. Não há vencimento legal objetivo registrado no dossiê, mas se a Cresol aplicar política de recência de 90 dias, a utilidade operacional expira em 2026-07-06, dentro da janela. Tratar como ponto condicional, não como vencimento documental confirmado.

## Alertas por Urgência

| Urgência | Critério | Quantidade | Roteamento |
| --- | --- | ---: | --- |
| Crítico | vencido ou 0-14 dias | 2 | Brasilino/Tereza |
| Aviso | 15-30 dias | 0 | Nenhum alerta novo |
| Notificação | 31-60 dias | 0 | Nenhum vencimento confirmado; 1 ponto condicional de recência bancária |

## Alertas Críticos

### CAF - Sergio Jose Altoe

- Documento: CAF nº ES042024.01.001428279CAF.
- Vencimento confirmado: 22/04/2026.
- Status em 26/05/2026: vencido há 34 dias.
- Atualização recebida em 26/05/2026: renovação do CAF está sendo providenciada. Manter alerta crítico até que o novo documento seja anexado e o registro seja atualizado.
- Impacto: impede rota Pronaf enquanto não houver CAF ativo/vigente e coerente com CPF, renda, área da UFPA e atividade declarada.
- Ação requerida: renovar CAF; arquivar novo PDF; atualizar número, data de emissão, validade, enquadramento Pronaf, renda aferida e área UFPA no registro `Docs Pessoais/Registro - CAF Sergio Jose Altoe.md`.
- Responsáveis operacionais: Brasilino/Tereza.
- Roteamento existente: `ALT-371`, sem necessidade de issue duplicada.

### CREA - Luis Eduardo Gottardo

- Registro profissional: CREA ES-0045577/D.
- Atualização recebida em 26/05/2026: registro pago para o exercício de 2026, com validade material até dezembro/2026.
- Regra operacional: o atestado/certidão emitido pelo CREA tem validade curta, normalmente de 2 a 3 meses. Portanto, mesmo com o registro anual pago, deve ser solicitado novo atestado sempre que um protocolo bancário, edital ou cadastro exigir documento recente.
- Alerta futuro: reavaliar validade do CREA de Luis Eduardo em dezembro/2026 e solicitar novo atestado antes de submissões que dependam dele.

### ITR 2025 - Sergio Jose Altoe

- Documento: DARF ITR 2025 nº 07.01.25253.1907525-9, valor R$ 30,65, com recibo DITR nº 08.22.52.24.50.77.
- Vencimento confirmado do DARF: 30/09/2025.
- Status em 26/05/2026: vencido há 238 dias, sem comprovante de pagamento/quitação localizado no pacote.
- Impacto: risco de pendência fiscal rural e travamento de análise bancária, especialmente no cruzamento com CCIR, CAR e escritura.
- Ação requerida: obter comprovante bancário de pagamento ou consulta/certidão oficial de regularidade; se não pago, regularizar com encargos e arquivar quitação.
- Responsáveis operacionais: Brasilino/Tereza.
- Roteamento existente: `ALT-371`, sem necessidade de issue duplicada.

## Pendências de Completude Documental

Os itens abaixo não entram como alerta de vencimento futuro porque a data não está extraída ou porque a pendência é de validação/completude, não de prazo confirmado.

| Documento | Cliente | Categoria | Risco | Responsável operacional |
| --- | --- | --- | --- | --- |
| RG/CPF de Sergio | [[Sergio Jose Altoe]] | Identidade | números e datas ainda precisam ser extraídos e conferidos contra CNH/cadastro | Cacilda/Tereza |
| RG/CPF de Maria de Lourdes | [[Sergio Jose Altoe]] | Identidade / cônjuge | CPF/RG e exigência de anuência ainda precisam ser confirmados | Cacilda/Tereza |
| Comprovante de aposentadoria | [[Sergio Jose Altoe]] | Renda | falta extrato INSS/CNIS completo com CPF e competência atual | Brasilino/Tereza |
| CAR | [[Sergio Jose Altoe]] | Ambiental | status online SICAR/IDAF, embargo e sobreposição não confirmados | Tereza/Rodrigo |
| Escritura / matrícula | [[Sergio Jose Altoe]] | Titularidade | matrícula, ônus, titularidade e área não confirmados | Tereza/Cacilda |
| Certidão atualizada de matrícula | [[Sergio Jose Altoe]] | Titularidade / garantia | não localizada; pode ser exigida pelo banco | Tereza/Cacilda |
| Projeto técnico, orçamento e cronograma | [[Sergio Jose Altoe]] | Projeto de crédito | ausentes; impedem protocolo da habitação rural | Brasilino/Tereza |
| Cadastro/limite/formulários Cresol | [[Sergio Jose Altoe]] | Banco | não localizados; necessários para submissão operacional | Brasilino/Tereza |
| IRPF ou declaração de isenção | [[Sergio Jose Altoe]] | Fiscal pessoal | não localizado; pode ser exigido pela Cresol | Brasilino/Tereza |

## Roteamento

- Alertas críticos de CAF e ITR permanecem roteados em `ALT-371`.
- Não foi criada nova issue, para evitar duplicação do mesmo alerta ainda aberto.
- Identidade e titularidade seguem com Cacilda/Tereza para completar extração e rastreabilidade.
- CAR segue com Tereza/Rodrigo para validação em sistema oficial.
- Projeto, enquadramento Pronaf, lista Cresol, capacidade de pagamento e regularidade fiscal seguem com Brasilino/Tereza.

## Próxima Ação Recomendada

Manter o pacote de Sergio Jose Altoe como **não protocolar** para Cresol/Pronaf Habitação até que haja:

1. CAF vigente anexado e registro atualizado.
2. ITR 2025 quitado/regular comprovado.
3. CAR validado no SICAR/IDAF, sem embargo ou sobreposição restritiva.
4. Titularidade, matrícula e ônus conferidos.
5. Projeto técnico, orçamento, cronograma e renda/capacidade finalizados.

Até esses pontos estarem fechados, a rotina diária deve manter CAF e ITR como alertas críticos vencidos.
