---
titulo: Relatorio Anual 2020-2021 - Producao MGgrafeno
tipo: registro-documento
produto: MGg3
fase: MGg2
codigo_fonte: MGG2-RA2020-2021-PROD
fonte_arquivo: MGG2-RA2020-2021_Producao_OC_SR_JT_RA_2021-11-23.docx
caminho_fonte: "/Users/okumaaltoe/Documents/MGgrafeno 3.0/EVT-MGg3/Ingestao 20Maio2026/VAI/Relatório Anual 2020-2021 - Produção_OC_SR_JT_RA_23_11_2021.docx.v1637669862 (1).docx"
nome_original: "Relatório Anual 2020-2021 - Produção_OC_SR_JT_RA_23_11_2021.docx.v1637669862 (1).docx"
organizacao: MGgrafeno / UFMG / CDTN / CODEMGE
tipo_documento: relatorio anual tecnico de producao
data_documento: 2021-11-23
confidencialidade: interno
status_extracao: extraido-controlado
confianca_extracao: alta
temas:
  - conversao
  - P25 Silverson Verso
  - P100 KonMix
  - separacao
  - acabamento
  - custo de producao
metricas_chave:
  - Superfine P25 0,134 g/L e 0,243% rendimento medio
  - KonMix P100 100 g/L 5 h
  - KonMix P100 0,365 g/L em 5 h
  - ganho temporal 4,8x frente a 50 g/L 24 h
  - Tabela 26 premissas 2 MC e 42 lotes/semana em 3 turnos
riscos_uso:
  - P25 Silverson e desenvolvimento de parametros, nao baseline produtivo
  - 100 g/L KonMix 5 h e baseline de produtividade/custo, nao ganho claro de rendimento percentual
  - nanografite e fracao relevante, mas nao produto final comercial sem especificacao propria
links_relacionados:
  - "[[Parametros criticos PL100 e acabamento]]"
  - "[[Mapa de processo e correntes MGgrafeno]]"
  - "[[MGG2-ANEXOA-RELII_Rota-100gL-KonMix]]"
  - "[[MGG2-ANEXOA-PROCFAB_Processo-Fabril-Piloto-2022]]"
  - "[[../Custos/Controle operacional de lotes/MGG2-ANEXOA-BMG_Balanco-Massa-Global-PDF]]"
  - "[[../Custos/MGG2-CUSTO-P100_Modelo-custo-planta-piloto]]"
atualizado: 2026-05-21
---
# Relatorio Anual 2020-2021 - Producao MGgrafeno

## Resumo executivo

Registro documental controlado do Relatorio Anual 2020-2021 da frente de producao MGgrafeno. O documento cobre conversao, separacao, acabamento, entrega de materiais, patentes, levantamento de custos e engenharia basica. Para o Vault, a leitura principal e separar com rigor o bloco P25/Silverson Verso como desenvolvimento de parametros do bloco P100/KonMix como operacao produtiva usada para custo, capacidade e taxa de producao.

O relatorio confirma a trilha tecnica ja internalizada em [[MGG2-ANEXOA-RELII_Rota-100gL-KonMix]] e [[MGG2-ANEXOA-PROCFAB_Processo-Fabril-Piloto-2022]]: a configuracao `P100 KonMix 100 g/L 5 h` e o baseline operacional de produtividade. O ganho defensavel e de tempo/capacidade frente ao comparador 50 g/L 24 h; nao deve ser convertido em ganho percentual de rendimento sem rastreabilidade adicional.

## Identificacao

| Campo | Valor |
|---|---|
| Arquivo preservado | `Descricao da Tecnologia/Anexos/MGG2-RA2020-2021_Producao_OC_SR_JT_RA_2021-11-23.docx` |
| Caminho externo usado | `/Users/okumaaltoe/Documents/MGgrafeno 3.0/EVT-MGg3/Ingestao 20Maio2026/VAI/` |
| Data do documento | 2021-11-23 |
| Status | Registro documental controlado |
| Confianca | Alta para parametros transcritos; media para numeros obtidos apenas de figuras/curvas |

## Separacao entre desenvolvimento e operacao produtiva

| Escala | Equipamento | Papel na arquitetura | Uso no Vault |
|---|---|---|---|
| P25 | Silverson Verso | Desenvolvimento de parametros e telas/estatores | Evidencia tecnica para hipoteses escalaveis, nao baseline produtivo |
| Bancada | IKA | Teste exploratorio de carga, aditivo, estabilidade e lavagem de grafite | Evidencia de mecanismo e limites; nao usar para custo de producao |
| P100 | Silverson UHS 275/175 | Transicao de escala e comparacao com KonMix | Evidencia intermediaria; mapeia 75/100 g/L e risco de gel |
| P100 | KonMix | Operacao produtiva escolhida: 100 g/L, 5 h | Baseline para custo, taxa de producao e capacidade |

## Evidencias de conversao

| Categoria | Dado observado | Fonte no relatorio | Leitura controlada |
|---|---|---|---|
| P25 preliminar | 25 L; 50 g/L grafite; aditivo 0,1% m/v; 10.000 rpm; 6 h; estator de furos quadrados 2 estagios | Tabela 1 | Base de desenvolvimento para estudar vazao, temperatura e geometria do estator |
| DOE P25 | Temperatura 17/30 graus C; vazao 12/44 L/min; 8 lotes com replicas | Tabelas 2-3 | Vazao e numero de ciclos foram os fatores mais informativos; temperatura nao fechou como fator principal |
| Modelo por vazao | R = 0,17658 + 0,03992V; R2 91,89%; R2aj 90,20%; R2pred 85,55 | Eq. 1 / Tabela 4 | Dado observado do DOE; nao extrapolar diretamente para P100 |
| Estatores P25 | SF: 0,134 +/- 0,02 g/L e 0,243%; FQ: 0,103 +/- 0,01 g/L e 0,223%; RV: 0,092 +/- 0,01 g/L e 0,183% | Tabela 7 | Superfine foi o melhor design observado no P25/Silverson Verso |
| Sistema em serie | Estator Superfine em serie reportou rendimento medio 0,504% | Figuras 28-30 / texto | Rota de intensificacao promissora; nao entra em OPEX sem energia especifica |
| pH/base P25 | NH4OH e sem ajuste reduziram residuo frente a NaOH; AFM indicou >90% de flocos entre 1 e 10 camadas para NaOH/NH4OH | Figuras 31-33 / Tabela 8 | Desenvolvimento de parametro escalavel, nao troca automatica do baseline |
| P100 Silverson | 75 e 100 g/L; pH 10 NaOH; Triton X-100 0,1% m/m; 100 g/L supera 50 g/L em 24 h ja em 10 h | Figuras 44-45 | Transicao de escala; risco de gel/desestabilizacao apos janela segura |
| P100 KonMix | 100 g/L; desaceleracao entre 4 e 6 h; tempo operacional adotado de 5 h | Figuras 46-48 | Baseline produtivo para capacidade/custo |
| P100 KonMix vs 50 g/L | Media 0,365 g/L em 5 h contra 0,29 g/L em 24 h para 50 g/L; fator temporal 4,8x | Figuras 47-48 / texto | Ganho de tempo/capacidade, nao diferenca numerica clara de rendimento percentual |
| Aditivo P100 | KonMix, 10 kg grafite, 100 kg agua, 5 h, pH 10 NaOH; lotes 20210914Pa, 20210920Pa e 20210927Pb | Secao acrescimo de aditivo | Rota de intensificacao; lote 20210920Pa chegou a alta concentracao antes de desestabilizacao |
| NH4OH P100 | Lotes 20210719Pa, 20210720Pa, 20210729Pa, 20210810Pa e 20210816Pa reduziram residuos; planta retomou NaOH por estabilidade | Secao mudanca de base | Desenvolvimento para novos parametros, mas baseline operacional voltou para NaOH |

## Separacao, acabamento e correntes

| Modulo | Dado observado | Uso controlado |
|---|---|---|
| Decanter | Mapeamento para material de 100 g/L; alvo de corrente solida de nanografite e corrente liquida com GPC + NPG | Conecta a [[Mapa de processo e correntes MGgrafeno]] e aos controles de lote |
| Recuperacao de GPC/NPG em nanografite | Lavagens sucessivas deslocam a fracao de interesse e alteram tamanho/temperatura de queima | Tratar nanografite como fracao relevante e economicamente sensivel, nao como produto final pronto |
| Filtracao tangencial | Concentracao e diafiltracao reduzem volume/aditivo, mas podem gerar aglomeracao e perda de solidos | Usar como tecnologia demonstrada com lacuna de estabilidade e perda |
| Diafiltracao | Reducao de aditivo de 55-73% veio acompanhada de perdas de solidos de 42-78% nos testes citados | Nao transformar remocao de surfactante em etapa madura sem custo/perda |
| Troca de aditivo | BYK-2013 foi testado como substituto do Triton | Registrar como rota de acabamento/formulacao, nao processo padrao |
| Spray drying e liofilizacao | Secagem aparece como acabamento para materiais grafenicos | Manter separacao de custo por produto e rota de secagem |

## Premissas de custo rastreadas

| Item | Valor / descricao | Fonte | Tratamento |
|---|---|---|---|
| Configuracao de linha | 2 MC | Tabela 26 | Premissa de custo historica |
| Batelada MC | 105,6 L/lote; 10 kg grafite/lote; 100 g aditivo/lote | Tabela 26 | Usar com recorte P100/KonMix |
| Tempo MC | 5 h operacao MC; 7,25 h/lote MC; 10,75 h/lote total | Tabela 26 | Base para taxa/capacidade |
| Capacidade semanal | 42 lotes/semana em 3 turnos | Tabela 26 | Premissa de capacidade, nao validacao economica final |
| Rendimentos de custo | GPC umido 0,78%; NG 4,99%; GPC+NG 5,77%; nanografite 91,19%; GPC concentrado 0,58%; GPC liofilizado 0,57%; NG liofilizado 4,87% | Tabela 28 | Cenario/premissa de custo da operacao P100; nao substituir automaticamente o lote canonico 20210720Pa |

## Marcacao de uso

| Categoria | Registro |
|---|---|
| Dado observado | Valores das Tabelas 1, 4, 7, 26 e 28; media KonMix P100 0,365 g/L; comparador 50 g/L 0,29 g/L; lotes NH4OH incluindo `20210720Pa`; retomada de NaOH por estabilidade. |
| Premissa rastreada | `P100 KonMix 100 g/L 5 h` e baseline produtivo para custo, taxa de producao e capacidade, com Tabela 26 para tempos/capacidade e Tabela 28 para cenario de rendimento de custo. |
| Inferencia defensavel | Superfine e melhor estator observado no P25/Silverson Verso; sistema em serie pode intensificar rendimento, mas exige energia especifica antes de OPEX; NH4OH e alternativa de desenvolvimento com restricao de estabilidade. |
| Lacuna | Shear rate calculado, torque, potencia absorvida, energia especifica kWh/kg, temperatura real por campanha, dados brutos UV-Vis/AFM/TEM, replicacao P100 dos estatores e custo de perdas por gel/aditivo nao estao fechados. |

## Riscos de claim exagerado

- Nao afirmar que Superfine e o melhor estator industrial. O dado forte e: melhor design observado no P25/Silverson Verso dentro das telas testadas.
- Nao tratar 4,8x como ganho de rendimento. O texto sustenta ganho de tempo/capacidade.
- Nao trocar o baseline produtivo para NH4OH sem recorte: NH4OH reduziu residuos, mas a baixa estabilidade levou a planta a retomar NaOH.
- Nao substituir o lote canonico `20210720Pa` pela Tabela 28. A Tabela 28 e cenario/premissa de custo; o lote segue como rastreio operacional.
- Manter nanografite como fracao relevante e economicamente importante, mas sem status de produto final comercial sem especificacao, rota de acabamento/reprocesso e custo.

## Links relacionados

- [[Parametros criticos PL100 e acabamento]]
- [[Mapa de processo e correntes MGgrafeno]]
- [[MGG2-ANEXOA-RELII_Rota-100gL-KonMix]]
- [[MGG2-ANEXOA-PROCFAB_Processo-Fabril-Piloto-2022]]
- [[../Custos/Controle operacional de lotes/MGG2-ANEXOA-BMG_Balanco-Massa-Global-PDF]]
- [[../Custos/MGG2-CUSTO-P100_Modelo-custo-planta-piloto]]
