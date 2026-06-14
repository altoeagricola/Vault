# RFQ-SAT-Centrifugacao-P500-v1.0

**Projeto:** MGgrafeno / Memorando IFHAN v1.0  
**Pacote:** Centrifugacao P500  
**Documento:** RFQ formal + protocolo SAT  
**Versao:** v1.0  
**Data:** 2026-06-11  
**Responsavel tecnico:** Valdemiro / ALTOE  
**Status:** Pronto para envio a fornecedores; cotacao final depende de resposta externa.  

## 1. Controle de Revisao

| Versao | Data | Alteracao | Autor |
|---|---:|---|---|
| v1.0 | 2026-06-11 | Emissao inicial do pacote formal de RFQ e SAT para cotacao da centrifugacao P500 | Valdemiro |

## 2. Rastreamento da Premissa

Este pacote responde ao item aberto do memorando IFHAN v1.0: fechar a faixa de CAPEX incremental da centrifugacao P500. A premissa de referencia antes da RFQ e:

- **CAPEX incremental base:** R$ 2,8 MM.
- **Faixa atual:** R$ 2,1-4,2 MM.
- **Classe de estimativa:** AACE 4/5, adequada para fase conceitual/pre-orcamento executivo.
- **Entregavel desta versao:** pacote de cotacao + protocolo SAT. A cotacao fechada depende de proposta de fornecedor.

Fontes internas rastreaveis: issue ALT-582 e issue-mae ALT-577 do plano de negocios IFHAN v1.0.

## 3. Objetivo da RFQ

Solicitar proposta tecnico-comercial para fornecimento, instalacao assistida e aceite em campo de sistema de centrifugacao para a linha P500 do MGgrafeno, incluindo dimensionamento, garantias de desempenho, interfaces de processo, requisitos de seguranca, automacao minima, documentacao e protocolo de SAT.

A RFQ deve permitir comparar fornecedores em base comum e reduzir a faixa de CAPEX incremental de R$ 2,1-4,2 MM para uma faixa suportada por cotacoes firmes ou budgetary quotations.

## 4. Premissas de Engenharia para Cotacao

### 4.1 Base de Processo

Como a vazao detalhada de alimentacao, curva granulometrica, solvente e teor de solidos ainda nao estao anexados ao pacote, a cotacao deve ser estruturada por envelopes operacionais. O fornecedor deve declarar explicitamente a capacidade efetiva para cada envelope e indicar qual tecnologia recomenda.

| Parametro | Base para cotacao | Observacao |
|---|---|---|
| Linha de processo | P500 | Tratar como pacote critico do plano MGgrafeno v1.0 |
| Funcao de processo | Separacao/concentracao de solidos finos em suspensao | Aplicacao em rota de grafeno; risco de particulas finas e baixa sedimentabilidade |
| Regime de operacao | Continuo ou batelada, a justificar | Fornecedor deve indicar limitantes de cada alternativa |
| Produto/process stream | Suspensao de material carbonaceo/grafenico | Confirmar compatibilidade com solventes, pH e agentes dispersantes |
| Teor de solidos na alimentacao | Informar capacidade para 0,5%, 2,0% e 5,0% m/m | Cenários para dimensionamento; fornecedor pode propor outros se justificar |
| Temperatura de operacao | Ambiente a 60 graus C | Informar limites mecanicos e de vedacao |
| Materiais molhados | AISI 316L ou superior, ou alternativa justificada | Confirmar compatibilidade quimica |
| Qualidade requerida | Recuperacao de solidos, clarificacao do sobrenadante e reproducibilidade de lote | Fornecedor deve propor garantias mensuraveis |
| Disponibilidade mecanica esperada | >= 85% apos ramp-up | Informar plano de manutencao e sobressalentes |

### 4.2 Dados que o Fornecedor Deve Confirmar

O fornecedor deve devolver a proposta com:

1. Curva de capacidade por teor de solidos, viscosidade e densidade assumida.
2. Eficiencia esperada de recuperacao de solidos finos e limite de particula separavel.
3. Teor de solidos esperado no concentrado/torta e claridade/turbidez esperada no sobrenadante.
4. Consumo eletrico instalado e medio, consumo de ar comprimido, agua de selagem/lavagem e quaisquer utilities.
5. Necessidade de pre-tratamento: floculante, ajuste de pH, tanque de equalizacao, peneiramento, desaeracao ou controle de temperatura.
6. Limites de solvente, inflamabilidade, abrasividade, corrosividade e emissao.
7. Requisitos de limpeza: CIP, lavagem manual, tempo de troca de campanha e risco de contaminacao cruzada.
8. Requisitos de amostra para teste: massa/volume minimo, preparo e prazo de retorno de laudo.

## 5. Tecnologias Aceitaveis

O fornecedor pode propor uma ou mais alternativas, desde que apresente justificativa tecnica:

- Centrifuga decanter de bancada/piloto-industrial ou industrial compacta.
- Centrifuga de discos, quando aplicavel a solidos finos e baixa carga de solidos.
- Centrifuga tubular ou basket, quando adequada a clarificacao fina ou campanhas batelada.
- Sistema hibrido com pre-filtracao, espessamento ou tanque de equalizacao, se tecnicamente necessario.

Tecnologias que dependam de consumiveis caros, uso intensivo de floculante ou baixa disponibilidade operacional devem ser destacadas como opcoes com ressalva, nao como base unica.

## 6. Escopo de Fornecimento Solicitado

### 6.1 Incluido no Escopo Base

O fornecedor deve cotar, no minimo:

1. Centrifuga completa com rotor/bowl, motor, acionamento, base/skid e protecoes.
2. Sistema de alimentacao imediato: bomba dosadora ou bomba de transferencia especificada, valvulas, conexoes e instrumentos essenciais.
3. Descarga de concentrado/torta e saida de sobrenadante/centrado, com conexoes sanitarias ou industriais adequadas.
4. Painel eletrico local, inversor de frequencia, botoeiras, alarmes e intertravamentos minimos.
5. Instrumentacao minima: rotacao, corrente do motor, vibracao ou alarme mecanico equivalente, temperatura critica, pressao/vazao quando aplicavel.
6. Documentacao tecnica: datasheet, GA drawing, P&ID do skid, lista de instrumentos, lista eletrica, manual de operacao e manutencao, lista de sobressalentes.
7. FAT no fornecedor, quando aplicavel, e SAT no site ALTOE.
8. Supervisao de montagem, start-up assistido e treinamento operacional.
9. Sobressalentes recomendados para 2 anos de operacao, separados entre criticos e consumiveis.
10. Embalagem, transporte ate site indicado e seguro, discriminados separadamente.

### 6.2 Opcionais Obrigatorios de Cotacao

Devem ser apresentados como linhas separadas:

1. CIP/lavagem automatizada.
2. Tanque de alimentacao/equalizacao com agitacao.
3. Sistema de inertizacao ou classificacao para atmosfera potencialmente inflamavel, se aplicavel ao solvente informado.
4. Upgrade de automacao para integracao PLC/SCADA.
5. Teste piloto com amostra ALTOE e relatorio de separacao.
6. Comissionamento estendido e pacote de treinamento avancado.
7. Contrato de manutencao preventiva por 12 meses.

### 6.3 Exclusoes que Devem Ser Declaradas

O fornecedor deve declarar explicitamente o que esta fora de escopo. Caso nao declarado, a ALTOE considerara o item incluso na avaliacao comparativa. Exclusoes esperadas:

- Obras civis e bases de concreto.
- Linha eletrica de alimentacao ate painel local.
- Tubulacao de processo fora dos limites do skid.
- Sistemas de utilidades da planta.
- Licencas ambientais e ARTs de instalacao, salvo quando ofertadas.
- Adequacoes prediais e classificacao de area.

## 7. Limites de Bateria

| Interface | Limite de bateria proposto | Responsavel base |
|---|---|---|
| Alimentacao | Flange/conexao de entrada no skid da centrifuga | Fornecedor no skid; ALTOE a montante |
| Concentrado/torta | Ponto de descarga no skid ou recipiente especificado | Fornecedor ate descarga |
| Sobrenadante/centrado | Flange/conexao de saida no skid | Fornecedor no skid; ALTOE a jusante |
| Eletrica | Bornes de entrada do painel local | ALTOE ate painel; fornecedor painel e cargas internas |
| Automacao | Sinais secos/analogicos ou protocolo informado | Fornecedor deve listar tags disponiveis |
| Ar/agua/utilities | Conexoes no skid | Fornecedor define consumo e qualidade requerida |

## 8. Garantias Solicitadas

O fornecedor deve propor garantias contratuais mensuraveis para:

1. Capacidade efetiva em pelo menos um envelope de operacao validado por amostra ou premissa aceita.
2. Recuperacao de solidos ou clarificacao minima, conforme metodo analitico acordado.
3. Estabilidade mecanica: vibracao, temperatura e corrente dentro dos limites do fabricante durante SAT.
4. Disponibilidade mecanica apos periodo inicial acordado.
5. Entrega de documentacao as-built e treinamento antes do aceite final.

Quando nao for possivel garantir desempenho por falta de amostra, o fornecedor deve apresentar proposta em duas etapas: teste piloto pago/creditavel + cotacao final revisada.

## 9. Matriz de Resposta do Fornecedor

Cada fornecedor deve preencher a matriz abaixo.

| Item | Resposta requerida |
|---|---|
| Tecnologia proposta | Tipo de centrifuga, modelo, fabricante, pais de origem |
| Capacidade | Vazao por envelope 0,5%, 2,0% e 5,0% m/m de solidos |
| Separacao | Recuperacao de solidos, teor no concentrado, turbidez/qualidade do sobrenadante |
| Utilities | kW instalado, kWh estimado, ar comprimido, agua, inertizacao, outros |
| Materiais | Materiais molhados, vedacoes, elastomeros, compatibilidade quimica |
| Automacao | Painel, PLC, tags, alarmes, intertravamentos, comunicacao |
| Limpeza | CIP/manual, tempo de limpeza, partes desmontaveis |
| Layout | Dimensoes, peso, cargas, acesso para manutencao |
| Prazo | Lead time de fabricacao, FAT, entrega, montagem assistida, SAT |
| CAPEX | Preco base, opcionais, impostos, frete, seguro, cambio, validade |
| OPEX | Pecas de desgaste, consumiveis, mao de obra, manutencao preventiva |
| Riscos | Limitacoes tecnicas, dependencias de amostra, premissas criticas |
| Referencias | Instalacoes similares, contato tecnico, ano e escala |

## 10. Requisitos Comerciais da Cotacao

A proposta deve separar:

1. Equipamento principal.
2. Perifericos incluidos.
3. Opcionais.
4. Servicos de engenharia/documentacao.
5. FAT, teste piloto, SAT, treinamento e start-up assistido.
6. Frete, seguro, impostos e desembaraco, se aplicavel.
7. Sobressalentes 2 anos.
8. Condicoes de pagamento.
9. Garantia.
10. Validade da proposta.

O fornecedor deve informar se a cotacao e budgetary, firm price ou sujeita a revisao apos teste com amostra.

## 11. Criterios de Avaliacao ALTOE

| Criterio | Peso sugerido |
|---|---:|
| Aderencia tecnica ao envelope P500 | 30% |
| Evidencia de desempenho com solidos finos/grafenicos ou analogos | 20% |
| CAPEX total instalado comparavel | 20% |
| OPEX, manutencao e sobressalentes | 10% |
| Prazo, suporte local e disponibilidade de assistencia | 10% |
| Qualidade documental, FAT/SAT e garantias | 10% |

Classificacao recomendada:

- **Apto:** atende tecnicamente e permite cotacao de CAPEX com baixa ressalva.
- **Apto com ressalva:** depende de teste piloto, amostra ou opcional critico.
- **Nao apto:** nao demonstra separacao, escala, materiais ou suporte adequados.

## 12. Protocolo SAT

### 12.1 Objetivo do SAT

Verificar em campo que a centrifuga e seus perifericos foram entregues, montados, energizados, instrumentados e operam de modo seguro e conforme os requisitos acordados antes do aceite operacional pela ALTOE.

SAT nao substitui performance test de processo. Se a separacao com produto real depender de curva de ramp-up ou de amostra ainda nao validada, o SAT mecanico/funcional pode ser aceito com pendencia controlada para performance test posterior.

### 12.2 Pre-requisitos para Inicio

O SAT so deve iniciar quando:

1. Equipamento instalado e nivelado conforme manual do fabricante.
2. Checklist mecanico concluido: fixacao, protecoes, alinhamento, sentido de rotacao, lubrificacao e drenagens.
3. Alimentacao eletrica liberada, painel identificado e aterramento verificado.
4. Utilities disponiveis conforme datasheet.
5. Linhas de entrada/saida conectadas ou testadas com arranjo temporario aprovado.
6. Documentacao minima entregue: manual, datasheet final, lista de instrumentos, P&ID do skid, certificados aplicaveis.
7. Equipe ALTOE treinada para operacao assistida.
8. Plano de seguranca aprovado: bloqueio/etiquetagem, partes rotativas, ruido, respingos, produtos quimicos e EPI.

### 12.3 Etapas do SAT

| Etapa | Teste | Criterio de aceite |
|---|---|---|
| SAT-01 | Inspecao visual e documental | Sem dano de transporte; tagueamento e documentos conferem com pedido |
| SAT-02 | Verificacao mecanica a frio | Rotor livre, protecoes instaladas, lubrificacao e fixacoes conformes |
| SAT-03 | Energizacao controlada | Painel energiza sem falhas; alarmes basicos funcionam |
| SAT-04 | Giro sem carga | Rotacao nominal ou faixa especificada atingida sem vibracao/ruido anormal |
| SAT-05 | Teste de intertravamentos | Parada de emergencia, tampas/protecoes e alarmes criticos atuam |
| SAT-06 | Teste com agua ou fluido seguro | Sem vazamentos relevantes; vazao e descarga operam conforme sequencia |
| SAT-07 | Teste de alimentacao e descarga | Bomba, valvulas e pontos de coleta operam; nao ha obstrucao recorrente |
| SAT-08 | Teste com simulante ou amostra ALTOE, se disponivel | Separacao observada e parametros registrados; nao e performance guarantee se amostra nao foi base da proposta |
| SAT-09 | Registro de dados | Rotacao, corrente, vibracao/alarme, temperatura e vazao documentados |
| SAT-10 | Treinamento e handover | Operadores recebem instrucao basica e lista de pendencias e assinada |

### 12.4 Dados Minimos a Registrar no SAT

- Data, local, equipe presente e modelo/numero de serie.
- Condicoes de instalacao e utilities.
- Fluido de teste e volume processado.
- Rotacao, corrente, temperatura, vibracao/alarme e tempo de operacao.
- Vazao de alimentacao e volumes/massas de saida.
- Observacoes de vazamento, espuma, entupimento, aquecimento ou ruido.
- Fotos do equipamento instalado, painel e interfaces.
- Pendencias abertas, responsavel e prazo.

### 12.5 Criterios de Reprovacao

O SAT deve ser reprovado ou aceito com pendencia critica quando ocorrer:

1. Falha de seguranca, intertravamento ou parada de emergencia.
2. Vibracao, ruido, aquecimento ou corrente fora dos limites do fabricante.
3. Vazamento relevante em condicao normal de teste.
4. Impossibilidade de atingir rotacao ou vazao minima declarada para o teste.
5. Ausencia de documentacao essencial para operacao segura.
6. Divergencia material entre equipamento entregue e escopo comprado.

### 12.6 Aceite Condicional

Pendencias nao criticas podem ser aceitas condicionalmente quando:

- Nao afetam seguranca.
- Nao impedem operacao assistida.
- Têm responsavel, prazo e criterio de fechamento documentados.

Exemplos: etiqueta final, documento as-built complementar, sobressalente nao critico em transito, ajuste fino de layout sem impacto operacional.

## 13. Marcos Contratuais Recomendados

| Marco | Liberacao sugerida |
|---|---:|
| Pedido aprovado e desenhos preliminares aceitos | 10-20% |
| FAT ou teste funcional no fornecedor aprovado | 30-40% |
| Entrega no site ALTOE | 20-30% |
| SAT aprovado | 10-20% |
| Pendencias finais/documentacao as-built | 5-10% |

Para proposta sem FAT, recomenda-se reter parcela maior ate SAT aprovado.

## 14. Riscos Tecnicos Principais

1. **Risco de escala e sedimentabilidade:** suspensoes grafenicas finas podem nao responder como solidos minerais convencionais. Mitigacao: exigir teste com amostra ou curva de capacidade por envelope.
2. **Risco de contaminacao/qualidade:** materiais molhados, vedacoes ou desgaste podem contaminar produto. Mitigacao: exigir lista de materiais e plano de limpeza.
3. **Risco de CAPEX incompleto:** fornecedores podem excluir perifericos essenciais. Mitigacao: matriz de escopo e limites de bateria obrigatorios.
4. **Risco de OPEX oculto:** pecas de desgaste, floculantes e limpeza podem dominar custo operacional. Mitigacao: linha separada de OPEX e sobressalentes 2 anos.
5. **Risco de integracao:** bombas, valvulas e automacao podem ficar entre fornecedor e EPC. Mitigacao: escopo minimo do skid e lista de sinais.

## 15. Saida Esperada da RFQ

Apos retorno dos fornecedores, a ALTOE devera consolidar:

1. Tabela comparativa tecnico-comercial.
2. Faixa revisada de CAPEX incremental P500.
3. Itens incluidos/excluidos por fornecedor.
4. Recomendacao tecnica: apto, apto com ressalva ou nao apto.
5. Decisao sobre necessidade de teste piloto antes de compra.

Enquanto nao houver cotacao externa, a faixa R$ 2,1-4,2 MM permanece como premissa AACE 4/5, mas deixa de estar sem pacote de cotacao formal.

## 16. Anexo A - Modelo de E-mail de Envio

Assunto: RFQ ALTOE MGgrafeno - Sistema de Centrifugacao P500

Prezados,

Solicitamos proposta tecnico-comercial para o sistema de centrifugacao P500 conforme pacote RFQ/SAT anexo. Pedimos que a resposta siga a matriz da Secao 9, com separacao clara entre equipamento base, opcionais, servicos, FAT/SAT, sobressalentes, frete/impostos e condicoes comerciais.

Caso a performance dependa de teste com amostra, favor propor escopo, prazo, custo e credito comercial aplicavel em caso de compra do equipamento.

Atenciosamente,  
ALTOE
