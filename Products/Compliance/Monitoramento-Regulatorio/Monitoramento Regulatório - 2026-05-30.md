---
tipo: relatorio-monitoramento-regulatorio
data_monitoramento: 2026-05-30
janela_dias: 60
periodo_monitorado: 2026-05-30 a 2026-07-29
responsavel: Tereza
issue: ALT-463
status: concluido
tags:
  - compliance
  - monitoramento-regulatorio
  - vencimento-documental
  - credito-rural
---

# Monitoramento Regulatório - 2026-05-30

## Escopo

Varredura documental no Vault para documentos de clientes/produtores com vencimento confirmado dentro da janela operacional de 60 dias ou já vencidos.

Fontes consultadas:

- `Connections/Clientes/`
- `Products/Crédito-Rural/Clientes/`
- `Products/Compliance/Monitoramento-Regulatorio/`
- alerta crítico existente `ALT-371`

Clientes/produtores encontrados no escopo operacional:

| Cliente/produtor | Situação documental |
| --- | --- |
| [[Sergio Jose Altoe]] | Dossiê documental estruturado; CAF saneado em 28/05/2026; ITR 2025 ainda sem quitação comprovada |
| Walquimar Comerio | Pastas criadas, sem documentos além de `.gitkeep` |

Arquivos documentais relevantes conferidos nesta rotina:

| Arquivo | Leitura de compliance |
| --- | --- |
| `Products/Crédito-Rural/Clientes/Sergio Jose Altoe/Checklist Documental - Sergio Jose Altoe.md` | Reavaliado em 2026-05-29; pacote segue não protocolável |
| `Products/Crédito-Rural/Clientes/Sergio Jose Altoe/Registro Documental - Pacote Sergio Jose Altoe.md` | Consolida CAF ativo até 28/05/2029, CND vigente até 25/11/2026 e ITR sem quitação |
| `Products/Crédito-Rural/Clientes/Sergio Jose Altoe/Docs Pessoais/Registro - CAF Sergio Jose Altoe.md` | CAF nº ES042024.01.001428279CAF ativo, atualizado em 28/05/2026, válido até 28/05/2029 |
| `Products/Crédito-Rural/Clientes/Sergio Jose Altoe/Docs Pessoais/Registro - Certidao Negativa RFB PGFN Sergio Jose Altoe.md` | CND RFB/PGFN válida até 25/11/2026, fora da janela de 60 dias |
| `Products/Crédito-Rural/Clientes/Sergio Jose Altoe/Docs Propriedade/Registro - ITR Sergio Jose Altoe.md` | DARF ITR 2025 vencido em 30/09/2025; não há comprovante de pagamento localizado |
| `Products/Crédito-Rural/Clientes/Sergio Jose Altoe/Docs Propriedade/Outorga Sergio Jose Altoe.md` | Declaração AGERH vigente até 10/04/2029, fora da janela |

## Resultado da Janela de 60 Dias

Não há documento com vencimento futuro confirmado entre 2026-05-30 e 2026-07-29.

Persiste um bloqueio crítico já vencido: o DARF do ITR 2025 segue sem comprovante de pagamento/quitação localizado no pacote.

| Documento | Cliente | Validade/vencimento confirmado | Dias até vencimento em 2026-05-30 | Classificação | Roteamento |
| --- | --- | ---: | ---: | --- | --- |
| [[Registro - ITR Sergio Jose Altoe]] - DARF ITR 2025 | [[Sergio Jose Altoe]] | 2025-09-30 | -242 | Crítico - quitação pendente | Brasilino/Tereza |
| [[Registro - CAF Sergio Jose Altoe]] | [[Sergio Jose Altoe]] | 2029-05-28 | 1094 | Fora da janela; saneado | Sem alerta de vencimento |
| [[Registro - Certidao Negativa RFB PGFN Sergio Jose Altoe]] | [[Sergio Jose Altoe]] | 2026-11-25 | 179 | Fora da janela; regularidade fiscal federal vigente | Sem alerta de vencimento |
| [[Registro - CNH Sergio Jose Altoe]] | [[Sergio Jose Altoe]] | 2027-08-04 | 431 | Fora da janela | Sem alerta |
| [[Outorga Sergio Jose Altoe]] | [[Sergio Jose Altoe]] | 2029-04-10 | 1045 | Fora da janela | Monitorar renovação futura |

Observações condicionais:

- A certidão de casamento de Sergio e Maria de Lourdes foi emitida em 2026-04-07. Não há vencimento legal objetivo registrado no dossiê, mas, se a Cresol aplicar política de recência de 90 dias, a utilidade operacional expira em 2026-07-06. Tratar como recência bancária condicional, não como vencimento documental confirmado.
- A CND RFB/PGFN de Sergio foi emitida em 2026-05-29 e vale até 2026-11-25. Ela reduz o risco de pendência fiscal federal do CPF, mas não substitui automaticamente comprovante específico do DARF ITR 2025 se a Cresol exigir prova de quitação por exercício.
- Os comprovantes de aposentadoria de abril/2026 ainda devem ser substituídos por extrato Meu INSS/CNIS completo com CPF antes do protocolo.

## Alertas por Urgência

| Urgência | Critério | Quantidade | Roteamento |
| --- | --- | ---: | --- |
| Crítico | vencido ou 0-14 dias | 1 | Brasilino/Tereza |
| Aviso | 15-30 dias | 0 | Nenhum alerta novo |
| Notificação | 31-60 dias | 0 | Nenhum vencimento confirmado; 1 ponto condicional de recência bancária |

## Alerta Crítico

### ITR 2025 - Sergio Jose Altoe

- Documento: DARF ITR 2025 nº 07.01.25253.1907525-9, valor R$ 30,65, com recibo DITR nº 08.22.52.24.50.77.
- Vencimento confirmado do DARF: 30/09/2025.
- Status em 30/05/2026: vencido há 242 dias, sem comprovante de pagamento/quitação localizado no pacote.
- Impacto: risco de pendência fiscal rural e travamento de análise bancária, especialmente no cruzamento com CCIR, CAR, CAF renovado e escritura.
- Ação requerida: obter comprovante bancário de pagamento ou consulta/certidão oficial de regularidade; se não pago, regularizar com encargos e arquivar quitação.
- Responsáveis operacionais: Brasilino/Tereza.
- Roteamento existente: `ALT-371`; alerta atualizado sem criação de issue duplicada.

## Pendências de Completude Documental

Os itens abaixo não entram como alerta de vencimento futuro porque a data não está extraída, não há vencimento objetivo, ou a pendência é de validação/completude.

| Documento | Cliente | Categoria | Risco | Responsável operacional |
| --- | --- | --- | --- | --- |
| RG/CPF de Sergio | [[Sergio Jose Altoe]] | Identidade | números e datas ainda precisam ser extraídos e conferidos contra CNH/cadastro | Cacilda/Tereza |
| RG/CPF de Maria de Lourdes | [[Sergio Jose Altoe]] | Identidade / cônjuge | CPF/RG e exigência de anuência ainda precisam ser confirmados | Cacilda/Tereza |
| Comprovante de aposentadoria | [[Sergio Jose Altoe]] | Renda | falta extrato INSS/CNIS completo com CPF e competência atual | Brasilino/Tereza |
| NF-e venda café conilon | [[Sergio Jose Altoe]] | Renda rural | chave de acesso ainda precisa validação antes de uso formal | Brasilino/Tereza |
| CND RFB/PGFN | [[Sergio Jose Altoe]] | Regularidade fiscal federal | vigente até 25/11/2026; autenticidade deve ser validada pelo código de controle antes de protocolo | Tereza/Cacilda |
| CAR | [[Sergio Jose Altoe]] | Ambiental | status online SICAR/IDAF, embargo e sobreposição não confirmados | Tereza/Rodrigo |
| Escritura / matrícula | [[Sergio Jose Altoe]] | Titularidade | matrícula, ônus, titularidade e área não confirmados | Tereza/Cacilda |
| Certidão atualizada de matrícula | [[Sergio Jose Altoe]] | Titularidade / garantia | não localizada; pode ser exigida pelo banco | Tereza/Cacilda |
| Coerência territorial do CAF renovado | [[Sergio Jose Altoe]] | Crédito rural / territorial | CAF 30,18 ha precisa conciliação contra CCIR, ITR, CAR e escritura | Brasilino/Tereza |
| Projeto técnico, orçamento e cronograma | [[Sergio Jose Altoe]] | Projeto de crédito | ausentes; impedem protocolo da habitação rural | Brasilino/Tereza |
| Cadastro/limite/formulários Cresol | [[Sergio Jose Altoe]] | Banco | não localizados; necessários para submissão operacional | Brasilino/Tereza |
| IRPF ou declaração de isenção | [[Sergio Jose Altoe]] | Fiscal pessoal | não localizado; pode ser exigido pela Cresol | Brasilino/Tereza |

## Roteamento

- ITR 2025 permanece crítico e continua roteado para Brasilino/Tereza via `ALT-371`.
- CAF permanece fora do alerta crítico de vencimento; manter apenas como pendência de coerência territorial e aceitação bancária do PDF novo.
- CAR segue com Tereza/Rodrigo para validação em sistema oficial.
- Identidade e titularidade seguem com Cacilda/Tereza para completar extração e rastreabilidade.
- Projeto, enquadramento Pronaf, lista Cresol, capacidade de pagamento e regularidade fiscal seguem com Brasilino/Tereza.

## Próxima Ação Recomendada

Manter o pacote de Sergio Jose Altoe como **não protocolar** para Cresol/Pronaf Habitação até que haja:

1. ITR 2025 quitado/regular comprovado.
2. CAR validado no SICAR/IDAF, sem embargo ou sobreposição restritiva.
3. Titularidade, matrícula e ônus conferidos.
4. CAF renovado aceito pelo banco e conciliado contra CCIR/ITR/CAR/escritura.
5. Projeto técnico, orçamento, cronograma e renda/capacidade finalizados.

Até esses pontos estarem fechados, a rotina diária deve manter o ITR como alerta crítico vencido e tratar o CAF como saneado quanto à validade.
