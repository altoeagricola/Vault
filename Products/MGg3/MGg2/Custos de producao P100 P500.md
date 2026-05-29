---
titulo: Custos de producao P100 P500
tipo: sintese-tematica
produto: MGg3
fonte_base: "[[MGG2-BASE01_Catalogo-MGg3-contexto-historico]]"
status: extraido_parcial
atualizado: 2026-05-07
confidencialidade: interno
---
# Custos de producao P100 P500

## Sintese

O catalogo identifica dois documentos economicos centrais para MGg3: uma planilha P100, baseada em dois reatores de 100 L, e uma planilha P500, baseada em dois reatores de 500 L. A P100 teria sido produzida em 2021 durante o projeto MGgrafeno; a P500 foi projetada em janeiro de 2026 com base nos dados da P100.

## Fontes citadas

| Documento | Leitura inicial |
|---|---|
| `P100_Custo de Producao - CLT_2021 - 9 de agosto de 2021 (CERES).xlsx` | Custos de planta com dois reatores de 100 L; pode superestimar controle de qualidade por incluir equipamentos caros de caracterizacao |
| `P500_Custo de Producao - 1 turno - KonMix - MGg 3.0.xlsx` | Projecao para dois reatores de 500 L; substitui parte de CQ interno por compra de analises em terceiros |
| `Resumo de custos de producao P500.xlsx` | Resumo economico da projecao P500 |

## Uso para MGg3

- Criar registros proprios para cada planilha antes de usar os numeros.
- Separar CAPEX, OPEX, controle de qualidade, pessoal, materias-primas e terceiros.
- Comparar P100 com P500 para entender economias de escala e premissas alteradas.
- Manter rastreabilidade de unidades, turno, capacidade e premissas de rendimento.
- Usar [[Custos/Saneamento custos P100 P500]] como registro operacional para separar valores extraidos, reconciliados, estimados, pendentes e nao comparaveis.

## Leitura de saneamento

A comparacao P100/P500 nao deve ser usada como custo unitario final sem reconciliação. A P100 carrega depreciação predial, equipe indireta e maior estrutura de caracterização interna; a P500 zera depreciação predial/equipe indireta e embute rendimento mais agressivo para Grafeno A e B do que a premissa comum do Lote 2021.

Registro detalhado: [[Custos/Saneamento custos P100 P500]].

## Complemento de insumos

A planilha [[Fornecedores/MGG3-FORN02_Fornecedores-insumos-grafeno-startup]] acrescenta valores de insumos, utilidades e HH que podem alimentar a leitura econômica: esferas de zirconia, N2, CO2, PET micronizado, aditivo BT Sulfonol, energia, agua/esgoto e HH operador/tecnico/analista. Esses valores devem ser incorporados ao saneamento como `extraido`, `estimado`, `defasado`, `pendente` ou `nao comparavel`, sem substituir automaticamente os custos das planilhas P100/P500.

## Perguntas abertas

- Quais premissas de preco, produtividade e perdas sustentam P500?
- Qual nivel minimo de controle de qualidade e tecnicamente aceitavel para venda?
- O custo por kg permite competir com fornecedores globais ou o valor esta na integracao aplicada?
