---
titulo: P500 - Escalonamento de engenharia P100 para P500
tipo: analise-viabilidade-tecnico-economica
produto: MGg3
status: preliminar_defensavel_para_due_diligence
confidencialidade: interno
data: 2026-06-10
fontes:
  - "[[MGG3-LEV-P100-v12_Levantamento-Custos-Cenarios-Desenvolvimento-Producao-Investidor-Consolidado]]"
  - "[[MGG3-CUSTO-P500_Projecao-KonMix]]"
  - "[[Saneamento custos P100 P500]]"
  - "P100_Custo de Produção - CLT_2021 - 9 de agosto de 2021 (CERES).xlsx"
  - "P500_Custo de Produção - 1 turno - KonMix - MGg 3.0.xlsx"
  - "Technical offer of KRB-15Kw (3group) Inline homogenizer machine.pdf"
  - "Technical offer of KRB-75Kw (3group) Inline homogenizer machine.pdf"
  - "Gmail - Fw_ RE_ Technical consultation - New equipment.pdf"
  - "Gmail - Fw_ RE_ Technical consultation - New equipment_.pdf"
---

# P500 - Escalonamento de engenharia P100 para P500

## 1. Conclusao executiva

A planilha KonMix P500 demonstra potencial real de ganho de escala, mas sua leitura original mistura quatro efeitos: escala fisica, rendimento mais agressivo, overhead zerado e manutencao/CQ subestimados. A versao reconciliada abaixo separa esses efeitos e usa a P100 Producao D2 da v12 como base comparavel.

Resultado base recomendado para memorando IFHAN:

| Indicador | P100 Producao D2 | P500 reconciliada base | Leitura |
|---|---:|---:|---|
| Grafite alimentado | 5.220 kg/ano | 26.000 kg/ano | P500 = 4,98x a P100 |
| Produto tecnico total | 5.157 kg/ano | 25.688 kg/ano | rendimento comum 2021, sem melhora embutida |
| OPEX caixa comparavel | R$ 2,481 MM/ano | R$ 4,02 MM/ano | +62% de OPEX para ~5x produto |
| OPEX tecnico completo | R$ 2,481 MM/ano na D2, sem depreciacao | R$ 4,30 MM/ano | inclui depreciacao gerencial P500 |
| Custo medio fisico caixa | R$ 481/kg | R$ 157/kg | reducao ~67% |
| Custo medio fisico tecnico | R$ 481/kg | R$ 168/kg | reducao ~65% |
| CAPEX incremental P500 ate centrifugacao | nao aplicavel | R$ 2,8 MM base | faixa R$ 2,1-4,2 MM |
| Classe de estimativa | AACE 4/5 | AACE 4/5 | exige RFQ, layout e SAT |

Leitura curta: a P500 continua economicamente atraente mesmo apos saneamento. O custo unitario cai por escala operacional, mas nao para os valores originais KonMix sem ressalvas. A faixa defensavel para investidor e de aproximadamente R$ 145-195/kg medio caixa, ou R$ 155-210/kg tecnico completo, antes de impostos, margem, perdas comerciais e capital de giro.

## 2. Premissas fisicas reconciliadas

| Campo | P100 comparavel | P500 reconciliada |
|---|---:|---:|
| Regime | 1 turno, producao dedicada | 1 turno, producao dedicada |
| Lote economico | 200 L / 20 kg grafite | 500 L / 50 kg grafite |
| Lotes/mes | 21,75 | 43,33 |
| Lotes/ano | 261 | 520 |
| Grafite/lote | 20 kg | 50 kg |
| Grafite/ano | 5.220 kg | 26.000 kg |
| Rendimento GPC/FLG | 0,80% | 0,80% |
| Rendimento NPG/GNP | 5,00% | 5,00% |
| Rendimento nanografite | 93,00% | 93,00% |
| Perdas | 1,20% | 1,20% |
| Produto total/ano | 5.157 kg | 25.688 kg |

Correcao aplicada: a P500 original KonMix usa 1,5% GPC, 7,5% NPG, 90% nanografite e 1,0% perdas. Para comparacao com a P100, voltei ao rendimento comum de 2021: 0,8% / 5,0% / 93,0% / 1,2%. Sem esse ajuste, o ganho aparente de custo do GPC e do NPG fica inflado por rendimento, nao por escala.

## 3. Fatores de escalonamento CAPEX

Formula usada:

`C2 = C1 * (S2/S1)^n`

onde `n` e o expoente de capacidade-custo. A razao de escala fisica adotada e `S2/S1 = 5`.

| Equipamento | Expoente base | Fator 5^n | Fonte e justificativa |
|---|---:|---:|---|
| Cisalhador / misturador de alto cisalhamento | 0,70 | 3,08x | Usei o expoente de agitadores/motores de mistura como proxy tecnico. Peters, Timmerhaus & West listam agitadores/motores na faixa de expoentes de ~0,69 para 5-20 hp; a regra geral dos seis-decimos e valida como ordem de grandeza, mas o proprio texto alerta que 0,6 e simplificacao. |
| Tanques inox agitados / tanques de processo | 0,57 | 2,50x | Peters, Timmerhaus & West listam tanques de aco carbono 10^2-10^4 gal com expoente 0,57; para tanque inox pequeno/agitado, 0,57 e proxy conservador moderado. |
| Centrifuga decanter / solid bowl | 0,67 | 2,94x | Peters, Timmerhaus & West listam centrifuga solid bowl com expoente 0,67 em funcao da potencia/capacidade. |
| Centrifuga de discos / separador centrifugo | 0,49 | 2,20x | Peters, Timmerhaus & West listam separador centrifugo com expoente 0,49. Usei 0,49 para a centrifuga de discos, separada do decanter. |

Fontes externas consultadas: Peters, Timmerhaus & West, *Plant Design and Economics for Chemical Engineers*, secao "Estimating Equipment Costs by Scaling", que recomenda usar a regra custo-capacidade apenas para equipamentos similares e dentro de razao ate 10x; PDH/Whitesides, *Process Equipment Cost Estimating by Ratio and Proportion*, que explicita a regra dos seis-decimos e a variacao de expoentes de 0,3 a 1,0; AACE RP 18R-97 para classificacao de estimativa.

### 3.1. Atualizacao Konmix 2026 - selecao do cisalhador P500

Consulta tecnica UFMG/CDTN-Konmix, maio-junho/2026: o equipamento atual e KRB 4/3, 4 kW, 3500 rpm, vazao operacional de referencia 4,7 m3/h e velocidade linear do rotor no maximo de aproximadamente 20,5 m/s. O requisito de Flavio Plentz para tanque de 500 L e vazao minima de 25 m3/h para manter o tempo de processamento; vazao maior e aceitavel se as condicoes de cisalhamento forem mantidas nas camaras.

| Modelo | Status de cotacao | Vazao informada | Potencia / rotacao | Leitura tecnica |
|---|---|---:|---|---|
| KRB 15/3 | Cotado em 05/05/2026 | 10 m3/h nominal; 12-15 m3/h com agua/liquido fluido | 15 kW; 3500 rpm | Insuficiente para P500. Mesmo no limite superior informado para agua, fica abaixo dos >=25 m3/h exigidos para o tanque de 500 L. |
| KRB 55/3 | Citado, nao cotado | 45-50 m3/h | 1450/1740 rpm | Atende a vazao e, segundo Konmix, pode manter a mesma velocidade linear/cisalhamento do KRB 4/3; e tecnicamente o menor modelo adequado, mas falta RFQ/preco formal. |
| KRB 75/3 | Cotado em 06/05/2026 | 60 m3/h | 75 kW; 1740 rpm; 220 V/60 Hz/3-fases | Atende com folga, permite reduzir tempo de processamento e tem cotacao real. Konmix afirma que a velocidade linear pode ser igualada ao KRB 4/3 no maximo, preservando as condicoes de processo. |

Recomendacao: usar o KRB 75/3 como base de CAPEX da P500 porque e o unico modelo tecnicamente adequado com cotacao formal. O KRB 55/3 deve permanecer como alternativa preferencial de otimizacao custo/capacidade em novo RFQ, pois atende 45-50 m3/h contra requisito de >=25 m3/h, mas hoje nao ha preco para ancorar a estimativa. O KRB 15/3 deve ser descartado para P500 por vazao insuficiente.

Evidencias de cotacao: [[MGG3-COT-20260506-01_konmix-inline-homogenizer-krb75-3]] e a evidencia de descarte [[MGG3-COT-20260505-01_konmix-inline-homogenizer-krb15-3]], ambas vinculadas a [[KONMIX-FORN01_Ficha-fornecedor-equipamentos]]. O padrao de registro e [[MGG3-PAD-FORN03_Padrao-registro-cotacoes-equipamentos]], separado do padrao de precos de grafeno/material.

Ressalva eletrica obrigatoria: para KRB 55/3 ou KRB 75/3, a Konmix alerta corrente de partida elevada; prever soft-start estrela-triangulo ou inversor de frequencia, alem de verificacao de rede 220 V trifasica, protecoes, cabos, aterramento e painel local. Essa necessidade deve ficar no pacote de instrumentacao/E&I, nao escondida no preco FCA do equipamento.

## 4. CAPEX P500 ate centrifugacao

Escopo: cisalhador, tanques de conversao/separacao, decanter, centrifuga de discos, instrumentacao minima, instalacao, integracao e SAT. Nao inclui secagem, liofilizacao, membranas, obra civil nova ou ampliacao estrutural. Premissa operacional do Rodrigo: P500 alocada junto a P100, na mesma area, sem modificacoes estruturais.

| Bloco | Base de calculo | CAPEX comprado estimado |
|---|---|---:|
| Cisalhadores 500 L | KRB 75/3 cotado Konmix em 06/05/2026: US$ 20.650 + 2 selos mecanicos x US$ 900 = US$ 22.450, FCA Shanghai; cambio de referencia 10/06/2026, dolar comercial compra medio BCB/Ipeadata = R$ 5,1757/US$, consultado em 11/06/2026. Valor convertido: R$ 116k FCA, antes de frete, seguro, desembaraco e tributos. Evidencia primaria: [[MGG3-COT-20260506-01_konmix-inline-homogenizer-krb75-3]]. A estimativa anterior por escala P100 5x com n=0,70 era R$ 115k e fica preservada apenas como sanity check, nao como ancora. | R$ 116k |
| Tanques inox processo 500 L | P100 escalada 5x com n=0,57; sem cotacao Konmix nos documentos de junho/2026. Linha permanece proxy ate RFQ de tanque inox agitado 500 L. | R$ 120k |
| Decanter / primeira separacao | P100 decanter escalado 5x com n=0,67 | R$ 630k |
| Centrifuga de discos / segunda separacao | P100 disco escalada 5x com n=0,49 | R$ 765k |
| Instrumentacao, bombas, inversores e utilidades de interface | 15% sobre principais equipamentos; deve incluir soft-start estrela-triangulo ou inversor para motor 75 kW, conforme alerta tecnico Konmix para modelos grandes | R$ 245k |
| **Subtotal equipamentos comprados** | | **R$ 1,88 MM** |
| Instalacao, E&I, tubulacao, bases, interligacoes e montagem | 25% sobre equipamentos; dentro das faixas de instalacao de mixers/tanques/centrifugas | R$ 470k |
| FAT/SAT, comissionamento frio/quente e performance test | pacote gerencial | R$ 130k |
| Contingencia tecnica preliminar | ~13% sobre subtotal instalado | R$ 320k |
| **CAPEX incremental base P500** | | **R$ 2,80 MM** |

Faixa recomendada: R$ 2,1-4,2 MM. A faixa e deliberadamente larga porque a geometria real da centrifugacao, vazao, RCF, materiais de construcao, automacao e interfaces ainda exigem RFQ. Enquadramento: AACE Classe 4/5. Nao ha base suficiente para Classe 3.

Tratamento de importacao do cisalhador: o valor R$ 116k e preco convertido em condicao FCA Shanghai, portanto comprador assume coleta, frete internacional, seguro, nacionalizacao, impostos, armazenagem/despachante e transporte interno. Para TEA preliminar, usar o preco FCA como ancora de equipamento comprado e uma faixa de nacionalizacao/logistica de 1,4-1,9x ate proposta de freight forwarder e classificacao fiscal: KRB 75/3 landed indicativo de R$ 160-220k. Essa faixa nao substitui RFQ logistica/tributaria; apenas evita tratar FCA como custo posto na planta.

Lacuna de tanque: os quatro documentos Konmix nao contem cotacao de tanque. Eles trazem apenas o requisito operacional de tanque 500 L / >=25 m3/h que dimensiona o cisalhador. A linha "Tanques inox processo 500 L" continua proxy por escalonamento e deve ser substituida por RFQ especifico de tanque inox agitado 500 L, com material, acabamento, agitacao, conexoes, drenagem, resfriamento/encamisamento se aplicavel, instrumentacao e limpeza.

Observacao critica: a planilha KonMix P500 contem linhas de equipamentos 500 L e centrifugas, mas tambem traz valores inconsistentes entre abas e uma depreciacao anual alocada muito baixa na ponte P500. Por isso usei a planilha como fonte de sanidade/ordem de grandeza, nao como CAPEX final.

## 5. OPEX P500 reconciliado

| Categoria | P100 D2 comparavel | P500 KonMix original/ponte | P500 reconciliada base | Ajuste aplicado |
|---|---:|---:|---:|---|
| Equipe direta | R$ 712,8k | R$ 625,2k | R$ 625,2k | mantida KonMix; equipe direta P500 parece plausivel para 1 turno |
| Equipe indireta / overhead | R$ 712,8k | R$ 0 | R$ 712,8k | normalizado ao benchmark P100 D2 |
| Insumos e consumiveis | R$ 371,4k | R$ 561,0k | R$ 1.849k | escalado por massa de grafite: 26.000/5.220 |
| Utilidades | R$ 96,0k | R$ 125,9k | R$ 126k | mantida KonMix; sensibilidade +50% recomendada |
| Manutencao | R$ 216,0k | R$ 3,9k | R$ 140k | 5% do CAPEX instalado aproximado, sem secagem |
| CQ externo e consumiveis CQ | R$ 348,0k | base nao comparavel | R$ 450k | normalizado para release/campanhas P500, abaixo do CQ por lote completo |
| SSMA, residuos e descarte | R$ 24,0k | subestimado no modulo SSMA | R$ 120k | escala com massa e volume de processo |
| **OPEX caixa** | **R$ 2.481k** | **R$ 1.380k na ponte** | **R$ 4.023k** | base comparavel |
| Depreciacao gerencial P500 | nao incluida na D2 | R$ 63,8k na ponte | R$ 280k | 10 anos sobre CAPEX base; gerencial, nao caixa |
| **OPEX tecnico completo** | **R$ 2.481k** | **nao comparavel** | **R$ 4.303k** | caixa + depreciacao |

Nota: mantive depreciacao predial incremental igual a zero na P500 porque a premissa atual e co-localizar a P500 com a P100 sem obra estrutural. Isso nao significa custo predial "inexistente" em um projeto standalone; significa apenas que, para o memorando IFHAN neste desenho, nao ha CAPEX predial incremental a depreciar. Se a P500 virar unidade isolada, somar ocupacao/predial separadamente.

## 6. Custo unitario P100 x P500

Metodo de alocacao: mesmo criterio da P100 v12, pesos por complexidade tecnica GPC:NPG:Nanografite = 4:2:1. Isso evita subalocar custo nas fracoes nobres.

| Produto | P100 D2 R$/kg | P500 base caixa R$/kg | P500 base tecnico R$/kg | Ganho caixa vs P100 |
|---|---:|---:|---:|---:|
| GPC / FLG | R$ 1.790 | R$ 583 | R$ 623 | -67% |
| NPG / GNP | R$ 896 | R$ 291 | R$ 312 | -68% |
| Nanografite | R$ 448 | R$ 146 | R$ 156 | -67% |
| Media fisica simples | R$ 481 | R$ 157 | R$ 168 | -67% |

Ganho real de escala: o ganho defendivel e ~65-68% de reducao de custo unitario, principalmente por diluicao de equipe, overhead e CQ sobre ~5x volume. O ganho maior sugerido pela planilha KonMix original nao deve ser usado sem ressalva porque vem de rendimento P500 mais agressivo e de overhead/manutencao/CQ incompletos.

## 7. Cenarios P500

| Cenario | CAPEX incremental | OPEX caixa | Premissa de rendimento | Custo medio caixa | GPC R$/kg | NPG R$/kg | Nanografite R$/kg | Confianca |
|---|---:|---:|---|---:|---:|---:|---:|---|
| Otimista | R$ 2,1 MM | R$ 3,4 MM/ano | rendimento otimista da P100 v12: 2/16/80,5/1,5 | R$ 133/kg fisico | R$ 434 | R$ 217 | R$ 109 | Baixa-media |
| **Base recomendada** | **R$ 2,8 MM** | **R$ 4,02 MM/ano** | rendimento comum 2021: 0,8/5/93/1,2 | **R$ 157/kg fisico** | **R$ 583** | **R$ 291** | **R$ 146** | Media-baixa |
| Conservador | R$ 4,2 MM | R$ 5,3 MM/ano | rendimento conservador: 0,5/5/93/1,5 + CQ/utilidades/manutencao altos | R$ 207/kg fisico | R$ 777 | R$ 388 | R$ 194 | Media |

Classe AACE: Classe 4/5. A estimativa usa lista de equipamentos e planilhas existentes, mas ainda nao tem RFQ atualizada, layout fechado, curva real de centrifugacao P500, RCF, P&ID, utilidades medidas, contrato de CQ nem SAT. Para due diligence senior, eu apresentaria como estimativa de viabilidade / ordem de grandeza, nao como budget de implantacao.

## 8. Pontos que exigem validacao antes de compromisso com investidor

1. RFQ de cisalhador P500: confirmar potencia, rotor/estator, vazao, material molhado, vedacao, automacao e service factor.
2. RFQ de tanques 500 L: confirmar inox, encamisamento, agitador, conexoes sanitarias/industriais, tampa, drenagem e CIP/limpeza.
3. RFQ de centrifugas: separar decanter e disco; exigir vazao real com dispersao de grafite, RCF, teor de solidos, recuperacao por fracao, limpeza e troca de produto.
4. SAT de separacao: a P100 ja tem pendencia de gargalo em 200 L; a P500 nao pode prometer 43,33 lotes/mes sem cronoanalise de 500 L.
5. CQ: transformar o envelope de R$ 450k/ano em proposta com metodos, frequencia, SLA, preparo de amostras e criterios de liberacao.
6. Insumos: cotar grafite, Triton X-100, NH4OH, embalagens e descarte em volumes P500.
7. Energia/utilidades: medir potencia real e mapear agua, resfriamento, drenagem, efluentes e ventilacao.

## 9. Mensagem recomendada ao IFHAN

A P500 e tecnicamente plausivel e economicamente promissora, mas a versao original KonMix nao deve ser apresentada como custo final. A leitura honesta e mais forte: usando a mesma premissa de rendimento de 2021, normalizando overhead, manutencao e CQ, e escalando os equipamentos por expoentes de engenharia, a P500 ainda reduz o custo unitario em cerca de dois tercos frente a P100 Producao D2. O principal risco tecnico nao e o cisalhamento em si; e confirmar que o modulo de separacao por centrifugacao sustenta 500 L/lote com rendimento, tempo de ciclo e CQ reprodutiveis.
