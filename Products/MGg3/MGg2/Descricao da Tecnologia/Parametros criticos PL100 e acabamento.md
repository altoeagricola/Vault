---
titulo: Parametros criticos PL100 e acabamento
tipo: parametros-processo
produto: MGg3
subproduto: MGg2
fonte_base: "[[KNOW-HOW-55.1-2024_Producao-de-Grafeno]]"
status: parcial-controlado
confidencialidade: interno
atualizado: 2026-05-21
---
# Parametros criticos PL100 e acabamento

## Objetivo

Consolidar parametros que podem alimentar levantamento de custo de producao, balanco de massa, plano de negocios e due diligence operacional. Esta nota separa dado aproveitavel, dado a revisar e dado que deve ficar apenas como evidencia.

## Conversao PL100

| Parametro | Valor / descricao | Status |
|---|---|---|
| Escala de referencia | 100 L de agua tipo II | aproveitavel |
| Grafite | 10 kg por batelada; 100 g/L | aproveitavel |
| Aditivo | Triton X-100 a 0,1% m/m | aproveitavel; sanear alias `Titon` em fontes historicas |
| pH | Padrao 10 com NaOH; NH4OH ou ausencia de ajuste aparecem como variacoes testadas | usar como baseline + variantes |
| Cisalhador | Konmix/KonMix KBR/3 inline high shear mixer 3-stage chamber | aproveitavel |
| Rotacao/frequencia | 60 Hz / cerca de 3500 rpm | aproveitavel |
| Tempo de conversao | 5 h no padrao KonMix | aproveitavel |
| Temperatura | 25-30 graus C | aproveitavel |
| Vazao do cisalhador | `4700-5100 L/h` em trechos; `4700 L/min` em outro | conflito de unidade; validar antes de custo final |

## Separacao entre desenvolvimento P25 e baseline produtivo P100

| Escala / equipamento | Papel tecnico | Uso permitido |
|---|---|---|
| P25 Silverson Verso | Desenvolvimento de parametros: vazao, temperatura, geometria de estator, pH/base e configuracao em serie | Evidencia tecnica para hipoteses escalaveis; nao usar como baseline produtivo nem como premissa financeira direta |
| IKA bancada | Exploracao de carga de grafite, aditivo, estabilidade e lavagem de grafite | Evidencia de mecanismo e limites; nao usar para taxa de producao |
| P100 Silverson UHS 275/175 | Transicao de escala e comparacao com KonMix para 75/100 g/L | Evidencia intermediaria; mapear risco de gel e janela segura |
| P100 KonMix | Operacao produtiva escolhida: 100 g/L, 5 h | Baseline para custo, taxa de producao e capacidade |

Registro de controle: [[MGG2-RA2020-2021_Producao-Conversao-Separacao-Acabamento]] confirma que os testes P25/Silverson sao desenvolvimento de parametros, enquanto `P100 KonMix 100 g/L 5 h` continua sendo o padrao produtivo para levantamento de custos e taxas. O ganho KonMix deve ser tratado como tempo/capacidade frente a 50 g/L 24 h, nao como ganho claro de rendimento percentual.

## Separacao

| Etapa | Parametros | Status |
|---|---|---|
| Primeira separacao - decanter | Cerca de 300 g, diferencial 20 rpm, disco de weir 56 mm, alimentacao 75 L/h | aproveitavel, validar por lote/campanha |
| Saidas decanter | `d02` NG/torta umida e `d01` suspensao intermediaria GPC + NPG | canonico inicial |
| Segunda separacao - discos | 60 Hz, 10000 rpm, cerca de 8900 g, vazao 55,2 L/h, pressao 0,5 bar | aproveitavel, validar equipamento/lote |
| Saidas discos | `d03` GPC e `d04` NPG | canonico inicial |

## Acabamento

| Frente | Dados aproveitaveis | Tratamento |
|---|---|---|
| Spray dryer | Bico 0,7-1,0 mm; entrada 100-150 graus C; saida 70-90 graus C; ar de secagem 1,65-1,75 m3/min; ar de atomizacao 35-45 L/min; alimentacao 0,4-0,7 L/h | Usar para GPC seco; confirmar por relatorio tecnico antes de custo final. |
| Liofilizacao | Aplicavel a NG, NPG e GPC | Manter como rota de secagem, mas nao copiar POP inteiro. |
| Filtracao tangencial | Concentracao 2-3x em piloto; diafiltracao reduziu surfactante em cerca de 52-56% em bancada, com perda/aglomeracao | Tratar como tecnologia demonstrada com lacunas de otimizacao. |
| Troca de aditivo | BYK-2013 testado como substituto/estabilizante | Rota de produto aplicado; nao tratar como processo padrao maduro sem validacao. |

## Tratamento de residuos

| Criterio | Valor | Uso |
|---|---|---|
| Fluxo liquido principal | ~18.000 L de residuo liquido tipo 1 tratados ate julho de 2019 | dado observado do [[MGG2-RTF-VOLV_SSMA-Tratamento-Residuos]]; nao extrapolar para operacao posterior |
| Filtrado pos-filtro prensa | turbidez abaixo de 5 NTU | criterio de processo SSMA; se nao atingir, o residuo e repassado |
| Pretratamento alternativo | coagulacao/floculacao com sulfato de aluminio; testes em 80 L e espessador de 200 L | usar para residuos dificeis, nao como rota obrigatoria de todo lote |
| Filtros de seguranca | membranas 0,45 um e 0,22 um | retencao de solidos/microrganismos remanescentes antes de carvao/resina |
| Remocao de surfactante | carvao ativado GAC400; 750 g, 340 mL/min, ~500 L/dia; troca preventiva a cada 1.000 L | premissa historica de consumivel/OPEX; validar em escala |
| Surfactante final | 0,18 ppm por HPLC, abaixo do limite ambiental citado de 2 ppm | dado observado de eficiencia do tratamento |
| Deionizacao | resina mista com meta de condutividade abaixo de 100 uS | criterio interno de reuso; entrada de osmose aceita CE abaixo de 250 uS/cm |
| Controle microbiologico | hipoclorito 11%, UV e recirculacao; regra pratica de 80 mL/600 L quando cloro livre abaixo de 0,2 ppm | parametro operacional de agua estocada |
| Agua final para reuso | adequada para osmose reversa, pias do processo e irrigacao de jardins; nao consumo humano ou irrigacao de hortalicas | DBO/DQO elevados exigem ressalva |

## Lacunas para custo de producao

| Lacuna | Por que importa |
|---|---|
| Vazao real do cisalhador | Afeta energia, tempo de residencia, escala e comparabilidade P100/P500. |
| Representatividade de lotes | Lotes historicos tem rendimentos e perdas diferentes; custo nao pode usar lote isolado sem justificativa. |
| CQ/caracterizacao | Precisa separar analise interna, terceirizada e requisito minimo por lote. |
| Acabamento por produto | GPC, NPG e NG nao carregam o mesmo custo de secagem/concentracao. |
| Tratamento de residuos | Agua/reuso e perdas precisam entrar como custo operacional, nao como nota ambiental solta. |

## Validacao Volume V SSMA - residuos e agua

| Categoria | Registro controlado |
|---|---|
| Dado observado | [[MGG2-RTF-VOLV_SSMA-Tratamento-Residuos]] registra quatro fluxos de residuos: liquido tipo 1 (~18.000 L), liquido tipo 2 (246 L), solido tipo 1 (40 kg) e solido tipo 2 (86 kg). |
| Dado observado | O filtro prensa retem solidos com maior teor de Grafeno B e nanoplaca de grafite; batelada de bancada gerou cerca de 250 g de solido retido. |
| Premissa tecnica | Para OPEX preliminar, 750 g de carvao por 1.000 L tratados pode ser usado como regra historica, com sensibilidade obrigatoria. |
| Inferencia | SSMA/residuos e modulo de custo e compliance do processo, conectado a conversao, separacao, acabamento e caracterizacao. |
| Lacuna | Faltam balanco de massa ambiental, vida util de membranas/resina, destino de consumiveis exauridos, HH, energia, custo de analises e certificados regulatorios. |
| Conflito | Claim de `reuso 100% da agua` fica restrito ao historico da planta piloto/CDTN; nao vira claim industrial MGg3 sem validacao atual. |

## Validacao Anexo A - rota 100 g/L KonMix

| Categoria | Registro controlado |
|---|---|
| Dado observado | [[MGG2-ANEXOA-RELII_Rota-100gL-KonMix]] registra desaceleracao do KonMix 100 g/L entre 4 e 6 h e escolha operacional de 5 h. |
| Dado observado | [[../Custos/Controle operacional de lotes/MGG2-ANEXOA-BMG_Balanco-Massa-Global-PDF]] rastreia o lote `20210720Pa` como Campanha Duda, 100 g/L KonMix 5 h, com NH4OH, decantacao estatica e discos. |
| Premissa tecnica | `100 g/L KonMix 5 h` pode ser usado como rotulo operacional nominal rastreado ao lote `20210720Pa`; a concentracao calculada proxima de 95,502 g/L deve ficar separada quando a fonte estruturada for usada. |
| Inferencia | O ganho tecnicamente defensavel e tempo/capacidade de conversao frente ao comparador `50 g/L 24 h`, nao aumento percentual de rendimento por kg de grafite. |
| Lacuna | Energia por lote, HH, agua de lavagem, consumo real de base/aditivo, custo de separacao/acabamento e CQ ainda nao estao fechados como premissa TEA/OPEX. |
| Conflito | `Triplicar producao`, `reducao 24x` e nanografite como produto final permanecem claims condicionados; nao viram premissa final sem validacao operacional e comercial. |

## Validacao Relatorio Anual 2020-2021

| Categoria | Registro controlado |
|---|---|
| Dado observado | [[MGG2-RA2020-2021_Producao-Conversao-Separacao-Acabamento]] registra Superfine como melhor estator observado no P25/Silverson Verso: 0,134 +/- 0,02 g/L e 0,243% de rendimento medio. |
| Dado observado | O relatorio anual registra KonMix P100 100 g/L com media 0,365 g/L em 5 h contra 0,29 g/L em 24 h para 50 g/L, sem diferenca numerica clara de rendimento percentual. |
| Premissa tecnica | Tabela 26 entra como premissa historica de custo/capacidade: 2 MC, 105,6 L/lote, 10 kg grafite/lote, 100 g aditivo/lote, 5 h operacao MC, 7,25 h/lote MC, 10,75 h/lote total e 42 lotes/semana em 3 turnos. |
| Premissa tecnica | Tabela 28 entra como cenario de rendimento de custo da operacao P100, nao como substituicao automatica do lote canonico `20210720Pa`. |
| Inferencia | NH4OH deve ser classificado como teste de desenvolvimento para novos parametros escalaveis a P100; reduziu residuos, mas a baixa estabilidade levou a retomada operacional de NaOH. |
| Lacuna | Estatores P25 nao foram replicados como baseline P100/KonMix; energia especifica, potencia, perdas por gel, custo de aditivo e qualidade comercial por produto seguem abertos. |

## Valores criticos do lote 20210720Pa

Fonte: [[../Custos/Controle operacional de lotes/MGG2-ANEXOA-BMG_Balanco-Massa-Global-PDF]], p. 15-16 do PDF original.

| Parametro | Valor | Uso |
|---|---:|---|
| Agua | 100 kg | Dado observado |
| Grafite | 10,01 kg | Dado observado |
| Aditivo | 0,1 kg | Dado observado |
| Base | NH4OH | Dado observado por lote; nao substituir o baseline NaOH sem recorte |
| Tempo | 5 h | Dado observado |
| GPC / Grafeno A | 0,051 kg solidos; RP 0,52% | Dado observado |
| GPB / Grafeno B | 0,4805 kg solidos; RP 4,85% | Dado observado |
| Nanografite | 9,2728 kg solidos; RP 93,66% | Dado observado; tratar como fracao/intermediario salvo especificacao |
| Perda | 0,10 kg; 0,96% | Dado observado; representatividade limitada |
