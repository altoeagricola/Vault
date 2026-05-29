---
titulo: Controle de documentos processo continuo
tipo: controle-documental
produto: MGg3
fase: MGg2
status: extraido
confidencialidade: interno
fonte: Controle de documentos_processo continuo.xlsx
periodo_coberto: 2021-10 a 2022-02
created: 2026-05-20
updated: 2026-05-20
tags:
  - MGg3
  - MGg2
  - custos
  - controle-documental
---

# Controle de documentos processo continuo

## Fonte original

- Arquivo no Vault: `Controle de documentos_processo continuo.xlsx`
- Origem externa: `/Users/okumaaltoe/Documents/MGgrafeno 3.0/EVT-MGg3/Ingestao 20Maio2026/Controle_de_lotes/Controle de documentos_processo continuo.xlsx`
- Estrutura: uma aba (`Planilha1`) com ano, lote, completude de processo, completude de qualidade, status e observações.

## Escopo e periodo coberto

Controle documental da fase de processo contínuo, cobrindo lotes `20211025Pa` a `20220221Pa`. Esta fonte não cobre o lote [[Products/MGg3/MGg2/Custos/Controle operacional de lotes/Processo-Referencia-Levantamento-de-Custos|20210720Pa]], mas ajuda a separar a campanha Duda da etapa posterior de produção contínua.

## Status por lote

| Lote | Processo | Qualidade | Status | Observações |
|---|---|---|---|---|
| 20211025Pa | Completo | Completo | Aprovado | - |
| 20211116Pa | Completo | Completo | Aprovado | - |
| 20211122Pa | Completo | Completo | Aprovado | - |
| 20211124Pa | Incompleto | Completo | Em processo | Verificar OP; indicação de contaminação pelo AFM |
| 20211129Pa | Completo | Completo | Aprovado | - |
| 20211201Pa | Completo | Completo | Aprovado | Baixo rendimento de produção; indicação de contaminante pelo AFM |
| 20211206Pa | Completo | Completo | Aprovado | Indicação de contaminante pelo AFM |
| 20211214Pa | Completo | Completo | Aprovado | - |
| 20220118Pa | Incompleto | Incompleto | Em processo | Falta informações de concentração |
| 20220208Pa | Incompleto | Incompleto | Em processo | Falta informações de concentração e algumas caracterizações |
| 20220214Pa | - | - | - | Sem status preenchido |
| 20220221Pa | - | - | - | Sem status preenchido |

## Metricas economicas identificaveis

- Não há métrica quantitativa de custo.
- O valor econômico do arquivo é de governança: indica quais lotes da produção contínua têm processo e qualidade completos, evitando usar lote incompleto como premissa sem ressalva.
- As observações de baixo rendimento e contaminação são flags de risco para comparativo de representatividade.

## Lacunas

- Não traz volume, concentração, equipamento, tempo de processo, insumos ou rendimento.
- Não há vínculo direto com o lote [[Products/MGg3/MGg2/Custos/Controle operacional de lotes/Processo-Referencia-Levantamento-de-Custos|20210720Pa]].
- Precisa ser usado como filtro documental, não como fonte primária de processo.
