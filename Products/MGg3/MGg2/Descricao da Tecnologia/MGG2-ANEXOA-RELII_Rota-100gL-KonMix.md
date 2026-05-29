---
titulo: Anexo A - Relatorio Ano II Projeto MGgrafeno - rota 100 g/L KonMix
tipo: registro-documento
produto: MGg3
fase: MGg2
codigo_fonte: MGG2-ANEXOA-RELII
fonte_arquivo: Anexo A_Relatório ano II Projeto MGgrafeno - out-20  [478-481].pdf
caminho_fonte: /Users/okumaaltoe/Documents/MGgrafeno 3.0/EVT-MGg3/Ingestao 20Maio2026/VAI/Anexo A - foi/Anexo A_Relatório ano II Projeto MGgrafeno - out-20  [478-481].pdf
nome_original: Anexo A_Relatório ano II Projeto MGgrafeno - out-20  [478-481].pdf
organizacao: MGgrafeno / MGg2
tipo_documento: relatorio tecnico parcial
data_documento: 2020-10
confidencialidade: interno
status_extracao: extraido-controlado
confianca_extracao: media-alta
temas:
  - 100 g/L
  - KonMix
  - Silverson
  - tempo de conversao
  - Campanha Duda
metricas_chave:
  - KonMix 100 g/L 5 h
  - comparador 50 g/L 24 h
  - media 0,365 g/L
riscos_uso:
  - ganho defensavel e de tempo/capacidade, nao de rendimento percentual
  - nao usar reducao 24x ou triplicar producao sem ressalva
links_relacionados:
  - "[[Parametros criticos PL100 e acabamento]]"
  - "[[../Custos/Controle operacional de lotes/Processo-Referencia-Levantamento-de-Custos]]"
  - "[[../Custos/Controle operacional de lotes/MGG2-ANEXOA-BMG_Balanco-Massa-Global-PDF]]"
atualizado: 2026-05-21
---
# Anexo A - Relatorio Ano II Projeto MGgrafeno - rota 100 g/L KonMix

## Resumo executivo

Registro documental das paginas 478-481 do Relatorio Ano II, usado como fonte interpretativa da rota de aumento de carga. O ponto central e a evolucao de 50 g/L para 75/100 g/L no Silverson e depois para 100 g/L no KonMix, com justificativa tecnica para 5 h de conversao. A leitura aceita nesta ingestao: o ganho defensavel e tempo/capacidade de conversao frente ao cenario 50 g/L 24 h, nao aumento de rendimento percentual.

## Identificacao

| Campo | Valor |
|---|---|
| Arquivo preservado | `Descricao da Tecnologia/Anexos/Anexo A_Relatório ano II Projeto MGgrafeno - out-20  [478-481].pdf` |
| Caminho externo usado | `/Users/okumaaltoe/Documents/MGgrafeno 3.0/EVT-MGg3/Ingestao 20Maio2026/VAI/Anexo A - foi/` |
| Paginas | 478-481 |
| Status | Registro documental controlado |
| Confianca | Media-alta para narrativa tecnica; media para comparacao quantitativa agregada |

## Evidencias tecnicas

| Condicao | Marcacao | Fonte / pagina | Leitura |
|---|---|---|---|
| 75 g/L Silverson | Dado observado | Relatorio Ano II, p. 479 | Elevar de 50 para 75 g/L aumentou concentracao ao longo da curva, mas nao consolidou ganho final material em 24 h. |
| 100 g/L Silverson | Dado observado | Relatorio Ano II, p. 479-480 | A curva desacelera perto de 12 h e ha risco de queda de solidos/gel; 10 h aparece como ponto operacional mais seguro. |
| 100 g/L KonMix | Dado observado | Relatorio Ano II, p. 481 | Desaceleracao entre 4 e 6 h; 5 h e adotado como tempo operacional. |
| Comparador 50 g/L 24 h | Dado observado | Relatorio Ano II, p. 481 | Media reportada de 100 g/L KonMix superior a 50 g/L em concentracao final, mas sem diferenca numerica relevante de rendimento percentual. |
| Ganho operacional | Inferencia defensavel | Relatorio Ano II, p. 481 + ALT-299 | Reducao de 24 h para 5 h gera ganho de capacidade/tempo de conversao; fator temporal 4,8x. |

## Marcacao tecnica obrigatoria

| Categoria | Registro |
|---|---|
| Dado observado | KonMix 100 g/L com desaceleracao entre 4 e 6 h e escolha operacional de 5 h. |
| Premissa tecnica | Usar `100 g/L KonMix 5 h` como rotulo operacional rastreado ao lote [[../Custos/Controle operacional de lotes/Processo-Referencia-Levantamento-de-Custos|20210720Pa]]. |
| Inferencia | O beneficio principal e produtividade horaria/capacidade de conversao, nao rendimento percentual superior por kg de grafite. |
| Lacuna | O recorte nao fecha energia, custo de separacao/acabamento nem qualidade comercial dos produtos. |
| Conflito | Claims de reducao 24x, triplicar producao e nanografite como produto final precisam permanecer como ressalva, nao premissa. |

## Regra de uso

- Vincular esta nota ao lote `20210720Pa` como justificativa tecnica da rota, mas manter o balanco de massa no registro [[../Custos/Controle operacional de lotes/MGG2-ANEXOA-BMG_Balanco-Massa-Global-PDF]].
- Nao apresentar `100 g/L` como ganho de rendimento percentual.
- Nao transformar nanografite/NPG majoritario em produto final sem especificacao de qualidade, rota de acabamento e OPEX.

## Links relacionados

- [[Parametros criticos PL100 e acabamento]]
- [[../Custos/Controle operacional de lotes/Processo-Referencia-Levantamento-de-Custos]]
- [[../Custos/Controle operacional de lotes/MGG2-ANEXOA-BMG_Balanco-Massa-Global-PDF]]
