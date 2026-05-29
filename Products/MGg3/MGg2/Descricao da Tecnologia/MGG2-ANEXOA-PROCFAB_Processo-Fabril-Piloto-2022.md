---
titulo: Anexo A - Processo Fabril Piloto RA OR 10 03 2022
tipo: registro-documento
produto: MGg3
fase: MGg2
codigo_fonte: MGG2-ANEXOA-PROCFAB
fonte_arquivo: Anexo A_Processo Fabril Piloto_RA_OR_10_03_2022_rev.pdf
caminho_fonte: /Users/okumaaltoe/Documents/MGgrafeno 3.0/EVT-MGg3/Ingestao 20Maio2026/VAI/Anexo A - foi/Anexo A_Processo Fabril Piloto_RA_OR_10_03_2022_rev.pdf
nome_original: Anexo A_Processo Fabril Piloto_RA_OR_10_03_2022_rev.pdf
organizacao: MGgrafeno / MGg2
tipo_documento: processo fabril piloto
data_documento: 2022-03-10
confidencialidade: interno
status_extracao: extraido-controlado
confianca_extracao: media
temas:
  - processo fabril
  - P100
  - KonMix
  - decanter
  - custos
metricas_chave:
  - decanter 75 L/h
  - 500 L/dia conservador
  - 600 L/turno declarado
riscos_uso:
  - cenarios P500/P2000 sao projecoes, nao dado observado de performance industrial
  - claims de triplicar producao e reducao 24x exigem ressalva
links_relacionados:
  - "[[Parametros criticos PL100 e acabamento]]"
  - "[[../Custos/MGG2-CUSTO-P100_Modelo-custo-planta-piloto]]"
  - "[[../Custos/Controle operacional de lotes/Processo-Referencia-Levantamento-de-Custos]]"
atualizado: 2026-05-21
---
# Anexo A - Processo Fabril Piloto RA OR 10 03 2022

## Resumo executivo

Registro documental do processo fabril piloto MGgrafeno em marco de 2022. O documento e relevante porque conecta rota P100, operacao KonMix, gargalo de primeira separacao, capacidade declarada de decanter e cenarios de custo/producao. Deve ser usado como fonte de leitura operacional e de limites de escala, nao como prova isolada de capacidade industrial validada.

## Identificacao

| Campo | Valor |
|---|---|
| Arquivo preservado | `Descricao da Tecnologia/Anexos/Anexo A_Processo Fabril Piloto_RA_OR_10_03_2022_rev.pdf` |
| Caminho externo usado | `/Users/okumaaltoe/Documents/MGgrafeno 3.0/EVT-MGg3/Ingestao 20Maio2026/VAI/Anexo A - foi/` |
| Documento | Processo Fabril Piloto RA OR 10 03 2022 |
| Data | 2022-03-10 |
| Status | Registro documental controlado |
| Confianca | Media para parametros operacionais; baixa para extrapolacao economica final |

## Dados operacionais rastreados

| Tema | Marcacao | Fonte / pagina | Leitura |
|---|---|---|---|
| Gargalo de separacao | Dado observado | Processo Fabril, p. 14 e p. 24 | A primeira separacao e tratada como gargalo historico e motivou condicoes de decanter. |
| Decanter | Dado observado | Processo Fabril, p. 14 e p. 24 | Parametros reportados incluem 75 L/h e campo centrifugo de 300 g. |
| Capacidade diaria | Premissa tecnica | Processo Fabril, p. 17 | 600 L/turno declarado e 500 L/dia usado como premissa conservadora; nao confundir com performance industrial auditada. |
| Cenario P&D | Premissa tecnica | Processo Fabril, p. 35 | 2 lotes/semana, 8 h/turno, 1 turno/dia e 5 dias/semana aparecem como cenario de custo P&D. |
| Expansao 2 turnos/decanters | Inferencia / cenario | Processo Fabril, p. 36 | Potencial de escala depende de configuracao operacional; nao e dado observado de planta validada. |

## Marcacao tecnica obrigatoria

| Categoria | Registro |
|---|---|
| Dado observado | O documento descreve processo P100 com conversao, primeira separacao, segunda separacao, acabamento, formularios e controles operacionais. |
| Premissa tecnica | Decanter 75 L/h e 300 g pode alimentar TEA preliminar somente como premissa rastreada e sensivel. |
| Inferencia | O ganho de capacidade depende mais da remocao do gargalo de separacao e da reducao de tempo/ciclo do que de aumento percentual de rendimento. |
| Lacuna | Nao fecha energia real, HH por lote, consumos efetivos de agua/lavagem, descarte, CQ e setup/limpeza. |
| Conflito | Claims de triplicar producao e reducao 24x aparecem como potencial/cenario; nao podem virar premissa final sem validacao operacional. |

## Ressalvas de claim

- `Triplicar producao`: registrar apenas como potencial condicionado a configuracao de separacao, surfactante, turnos e validação de qualidade.
- `Reducao 24x`: registrar apenas com ressalva; depende de cenario P&D e nao substitui demonstracao de OPEX real.
- `Nanografite como produto final`: tratar como fracao/intermediario/reprocessavel ate haver especificacao, mercado e custo de acabamento/reprocesso.

## Links relacionados

- [[Parametros criticos PL100 e acabamento]]
- [[../Custos/MGG2-CUSTO-P100_Modelo-custo-planta-piloto]]
- [[../Custos/Controle operacional de lotes/Processo-Referencia-Levantamento-de-Custos]]
