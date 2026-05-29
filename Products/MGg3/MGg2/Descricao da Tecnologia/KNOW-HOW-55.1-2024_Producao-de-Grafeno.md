---
titulo: KNOW-HOW 55.1-2024 - Producao de Grafeno
tipo: registro-documento
produto: MGg3
subproduto: MGg2
fonte_arquivo: "KNOW HOW 55.1-2024 - Producao de Grafeno - Final.docx"
caminho_fonte: "Products/MGg3/MGg2/Descricao da Tecnologia/KNOW HOW 55.1-2024 - Producao de Grafeno - Final.docx"
organizacao:
  - UFMG
  - CDTN
tipo_documento: know-how tecnico
data_documento: 2025-01-14
confidencialidade: interno
status_extracao: parcial-controlado
confianca_extracao: media
temas:
  - producao de grafeno
  - planta piloto
  - PL100
  - correntes de processo
  - caracterizacao
links_relacionados:
  - "[[Descricao da Tecnologia]]"
  - "[[Mapa de processo e correntes MGgrafeno]]"
  - "[[Parametros criticos PL100 e acabamento]]"
  - "[[Matriz de anexos e evidencias - KNOW-HOW-55.1-2024]]"
atualizado: 2026-05-20
---
# KNOW-HOW 55.1-2024 - Producao de Grafeno

## Resumo executivo

Documento central da descricao oficial da tecnologia MGgrafeno. Descreve uma rota de producao de uma familia de materiais de grafeno a partir de grafite natural comercial por esfoliacao/delaminacao em fase liquida mecanicamente assistida por cisalhamento, com separacao, acabamento, caracterizacao e tratamento de residuos.

O documento deve ser usado como fonte-mae para taxonomia tecnica do processo. Ele nao deve ser copiado integralmente para notas operacionais; deve alimentar mapas controlados de processo, correntes, parametros e evidencias.

## Escopo tecnico extraido

| Bloco | Conteudo aproveitavel | Uso no Vault |
|---|---|---|
| Problema e aplicacoes | Grafeno como nanocarga para polimeros, cimenticios, tintas, revestimentos, sensores, membranas e energia | Contexto tecnico; nao duplicar inteligencia de mercado ja existente. |
| Produtos | GPC, NPG e NG/Nanografite/Nanoplacas de Grafite | Taxonomia canonica de produtos. |
| Processo | Modulos de conversao, separacao, acabamento e residuos | Base do mapa de processo. |
| Correntes | `c31`, `d01`, `d02`, `d03`, `d04`, aliases `s02/s03/s04` | Base para custos, balanco de massa e plano de negocios. |
| Parametros | PL100, cisalhamento, decanter, centrifuga de discos, secagem, filtracao tangencial | Base para parametros criticos e lacunas. |
| Anexos | PIOs, relatorio tecnico de spray dryer, filtracao tangencial, UV-Vis, liofilizador | Rastreabilidade por codigo/titulo. |

## Definicoes controladas

| Termo | Definicao operacional |
|---|---|
| GPC | Grafeno de Poucas Camadas; tambem denominado Grafeno A; associado a `d03` ou `s03`. |
| NPG | NanoPlaca de Grafeno; tambem denominada Grafeno B; associada a `d04` ou `s04`. |
| NG | Nanoplaca de Grafite ou Nanografite; tambem pode aparecer como Nanoplacas de Grafite; associada a `d02` ou `s02`. |
| `c31` | Suspensao mae formada apos conversao de grafite + agua + aditivo no modulo de conversao. Alimenta a primeira separacao. |
| Prefixo `d` | Corrente/produto associado a separacao com centrifuga decanter. |
| Prefixo `s` | Corrente/produto associado a separacao na centrifuga de discos, conforme orientacao tecnica recebida. Quando o DOCX associar `s` a rota alternativa/decantacao estatica, tratar como conflito documental a validar. |

## Restricoes de uso

- O documento contem dados pessoais de responsaveis pelo know-how. Esses dados nao devem ser transcritos para notas tecnicas.
- Dados quantitativos devem manter unidade, condicao experimental e origem. Sem isso, ficam como pendencia, nao como parametro canonico.
- Trechos de POP/checklist so devem ser internalizados quando alterarem custo, risco operacional, parametro critico, qualidade ou rastreabilidade.
- A numeracao de anexos e instavel; usar codigo/titulo/revisao como chave.

## Lacunas e conflitos

| Tema | Situacao | Tratamento |
|---|---|---|
| Vazao do cisalhador | Ha referencia a `4700 L/min` e tambem a `4700-5100 L/h`. | Sinalizar como conflito de unidade; usar `L/h` como hipotese tecnica ate validacao. |
| NPG | Ha variacao entre centro 5-6 camadas/ate 10 camadas e outra descricao abaixo de 20/centro 10. | Manter definicao validada pelo responsavel tecnico e registrar variacao como conflito documental. |
| Anexos | Numero do anexo no arquivo nao coincide sempre com remissao interna do DOCX. | Usar matriz de anexos e evidencias. |
| Correntes `s`/`d` | Mistura de nomenclatura em fontes historicas e no DOCX. | Usar `d` = decanter e `s` = centrifuga de discos como regra controlada; preservar aliases e marcar divergencias. |
