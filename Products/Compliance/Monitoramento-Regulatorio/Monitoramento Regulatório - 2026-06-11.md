---
tipo: relatorio-monitoramento-regulatorio
data_monitoramento: 2026-06-11
janela_dias: 60
periodo_monitorado: 2026-06-11 a 2026-08-10
responsavel: Tereza
issue: ALT-572
status: concluido
tags:
  - compliance
  - monitoramento-regulatorio
  - vencimento-documental
  - credito-rural
---

# Monitoramento Regulatorio - 2026-06-11

## Escopo

Varredura documental no Vault para documentos de clientes/produtores com vencimento confirmado dentro da janela operacional de 60 dias ou ja vencidos.

Fontes consultadas:

- `Connections/Clientes/`
- `Products/Crédito-Rural/Clientes/`
- `Products/Compliance/Monitoramento-Regulatorio/`
- `Areas/ALTOE Agricola/Bases/Clientes Marilândia/clientes.csv`
- alerta critico existente `ALT-371`

Clientes/produtores encontrados no escopo operacional:

| Cliente/produtor | Situacao documental |
| --- | --- |
| [[Sergio Jose Altoe]] | Dossie documental estruturado; CAF saneado em 28/05/2026; ITR 2025 ainda sem quitacao comprovada |
| Walquimar Comerio | Pastas criadas, sem documentos alem de `.gitkeep` |
| Base Clientes Marilandia | Base cadastral ampla, sem campo de validade/vencimento documental confirmado |

Arquivos documentais relevantes conferidos nesta rotina:

| Arquivo | Leitura de compliance |
| --- | --- |
| `Products/Crédito-Rural/Clientes/Sergio Jose Altoe/Checklist Documental - Sergio Jose Altoe.md` | Pacote segue nao protocolavel; ITR permanece como saneamento critico |
| `Products/Crédito-Rural/Clientes/Sergio Jose Altoe/Registro Documental - Pacote Sergio Jose Altoe.md` | Consolida CAF ativo ate 28/05/2029, CND vigente ate 25/11/2026 e ITR sem quitacao comprovada |
| `Products/Crédito-Rural/Clientes/Sergio Jose Altoe/Docs Pessoais/Registro - CAF Sergio Jose Altoe.md` | CAF no ES042024.01.001428279CAF ativo, atualizado em 28/05/2026, valido ate 28/05/2029 |
| `Products/Crédito-Rural/Clientes/Sergio Jose Altoe/Docs Pessoais/Registro - Certidao Negativa RFB PGFN Sergio Jose Altoe.md` | CND RFB/PGFN valida ate 25/11/2026, fora da janela de 60 dias |
| `Products/Crédito-Rural/Clientes/Sergio Jose Altoe/Docs Propriedade/Registro - ITR Sergio Jose Altoe.md` | DARF ITR 2025 vencido em 30/09/2025; nao ha comprovante de pagamento localizado |
| `Products/Crédito-Rural/Clientes/Sergio Jose Altoe/Docs Propriedade/Outorga Sergio Jose Altoe.md` | Declaracao AGERH vigente ate 10/04/2029, fora da janela |

## Resultado da Janela de 60 Dias

Nao ha documento com vencimento futuro confirmado entre 2026-06-11 e 2026-08-10.

Persiste um bloqueio critico ja vencido: o DARF do ITR 2025 segue sem comprovante de pagamento/quitacao localizado no pacote.

| Documento | Cliente | Validade/vencimento confirmado | Dias ate vencimento em 2026-06-11 | Classificacao | Roteamento |
| --- | --- | ---: | ---: | --- | --- |
| [[Registro - ITR Sergio Jose Altoe]] - DARF ITR 2025 | [[Sergio Jose Altoe]] | 2025-09-30 | -254 | Critico - quitacao pendente | Brasilino/Tereza |
| [[Registro - CAF Sergio Jose Altoe]] | [[Sergio Jose Altoe]] | 2029-05-28 | 1082 | Fora da janela; saneado | Sem alerta de vencimento |
| [[Registro - Certidao Negativa RFB PGFN Sergio Jose Altoe]] | [[Sergio Jose Altoe]] | 2026-11-25 | 167 | Fora da janela; regularidade fiscal federal vigente | Sem alerta de vencimento |
| [[Registro - CNH Sergio Jose Altoe]] | [[Sergio Jose Altoe]] | 2027-08-04 | 419 | Fora da janela | Sem alerta |
| [[Outorga Sergio Jose Altoe]] | [[Sergio Jose Altoe]] | 2029-04-10 | 1034 | Fora da janela | Monitorar renovacao futura |

Observacoes condicionais:

- A certidao de casamento de Sergio e Maria de Lourdes foi emitida em 2026-04-07. Nao ha vencimento legal objetivo registrado no dossie, mas, se a Cresol aplicar politica de recencia de 90 dias, a utilidade operacional expira em 2026-07-06. Em 2026-06-11 isso fica a 25 dias. Tratar como recencia bancaria condicional, nao como vencimento documental confirmado.
- A CND RFB/PGFN de Sergio foi emitida em 2026-05-29 e vale ate 2026-11-25. Ela reduz o risco de pendencia fiscal federal do CPF, mas nao substitui automaticamente comprovante especifico do DARF ITR 2025 se a Cresol exigir prova de quitacao por exercicio.
- Os comprovantes de aposentadoria de abril/2026 ainda devem ser substituidos por extrato Meu INSS/CNIS completo com CPF antes do protocolo.

## Alertas por Urgencia

| Urgencia | Criterio | Quantidade | Roteamento |
| --- | --- | ---: | --- |
| Critico | vencido ou 0-14 dias | 1 | Brasilino/Tereza |
| Aviso | 15-30 dias | 0 | Nenhum vencimento documental confirmado; 1 ponto condicional de recencia bancaria |
| Notificacao | 31-60 dias | 0 | Nenhum vencimento confirmado |

## Alerta Critico

### ITR 2025 - Sergio Jose Altoe

- Documento: DARF ITR 2025 no 07.01.25253.1907525-9, valor R$ 30,65, com recibo DITR no 08.22.52.24.50.77.
- Vencimento confirmado do DARF: 30/09/2025.
- Status em 11/06/2026: vencido ha 254 dias, sem comprovante de pagamento/quitacao localizado no pacote.
- Impacto: risco de pendencia fiscal rural e travamento de analise bancaria, especialmente no cruzamento com CCIR, CAR, CAF renovado e escritura.
- Acao requerida: obter comprovante bancario de pagamento ou consulta/certidao oficial de regularidade; se nao pago, regularizar com encargos e arquivar quitacao.
- Responsaveis operacionais: Brasilino/Tereza.
- Roteamento existente: `ALT-371`; alerta atualizado sem criacao de issue duplicada.

## Pendencias de Completude Documental

Os itens abaixo nao entram como alerta de vencimento futuro porque a data nao esta extraida, nao ha vencimento objetivo, ou a pendencia e de validacao/completude.

| Documento | Cliente | Categoria | Risco | Responsavel operacional |
| --- | --- | --- | --- | --- |
| RG/CPF de Sergio | [[Sergio Jose Altoe]] | Identidade | numeros e datas ainda precisam ser extraidos e conferidos contra CNH/cadastro | Cacilda/Tereza |
| RG/CPF de Maria de Lourdes | [[Sergio Jose Altoe]] | Identidade / conjuge | CPF/RG e exigencia de anuencia ainda precisam ser confirmados | Cacilda/Tereza |
| Comprovante de aposentadoria | [[Sergio Jose Altoe]] | Renda | falta extrato INSS/CNIS completo com CPF e competencia atual | Brasilino/Tereza |
| NF-e venda cafe conilon | [[Sergio Jose Altoe]] | Renda rural | chave de acesso ainda precisa validacao antes de uso formal | Brasilino/Tereza |
| CND RFB/PGFN | [[Sergio Jose Altoe]] | Regularidade fiscal federal | vigente ate 25/11/2026; autenticidade deve ser validada pelo codigo de controle antes de protocolo | Tereza/Cacilda |
| CAR | [[Sergio Jose Altoe]] | Ambiental | status online SICAR/IDAF, embargo e sobreposicao nao confirmados | Tereza/Rodrigo |
| Escritura / matricula | [[Sergio Jose Altoe]] | Titularidade | matricula, onus, titularidade e area nao confirmados | Tereza/Cacilda |
| Certidao atualizada de matricula | [[Sergio Jose Altoe]] | Titularidade / garantia | nao localizada; pode ser exigida pelo banco | Tereza/Cacilda |
| Coerencia territorial do CAF renovado | [[Sergio Jose Altoe]] | Credito rural / territorial | CAF 30,18 ha precisa conciliacao contra CCIR, ITR, CAR e escritura | Brasilino/Tereza |
| Projeto tecnico, orcamento e cronograma | [[Sergio Jose Altoe]] | Projeto de credito | ausentes; impedem protocolo da habitacao rural | Brasilino/Tereza |
| Cadastro/limite/formularios Cresol | [[Sergio Jose Altoe]] | Banco | nao localizados; necessarios para submissao operacional | Brasilino/Tereza |
| IRPF ou declaracao de isencao | [[Sergio Jose Altoe]] | Fiscal pessoal | nao localizado; pode ser exigido pela Cresol | Brasilino/Tereza |

## Roteamento

- ITR 2025 permanece critico e continua roteado para Brasilino/Tereza via `ALT-371`.
- CAF permanece fora do alerta critico de vencimento; manter apenas como pendencia de coerencia territorial e aceitacao bancaria do PDF novo.
- CAR segue com Tereza/Rodrigo para validacao em sistema oficial.
- Identidade e titularidade seguem com Cacilda/Tereza para completar extracao e rastreabilidade.
- Projeto, enquadramento Pronaf, lista Cresol, capacidade de pagamento e regularidade fiscal seguem com Brasilino/Tereza.
- Base cadastral de Clientes Marilandia nao gerou alertas por vencimento: ha dados pessoais/cadastrais, mas nao ha documentos com validade extraida.

## Proxima Acao Recomendada

Manter o pacote de Sergio Jose Altoe como **nao protocolar** para Cresol/Pronaf Habitacao ate que haja:

1. ITR 2025 quitado/regular comprovado.
2. CAR validado no SICAR/IDAF, sem embargo ou sobreposicao restritiva.
3. Titularidade, matricula e onus conferidos.
4. CAF renovado aceito pelo banco e conciliado contra CCIR/ITR/CAR/escritura.
5. Projeto tecnico, orcamento, cronograma e renda/capacidade finalizados.

A rotina diaria deve manter o ITR como alerta critico vencido e tratar o CAF como saneado quanto a validade.
