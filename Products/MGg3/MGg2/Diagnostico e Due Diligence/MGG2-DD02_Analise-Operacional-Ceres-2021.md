---
titulo: Análise Operacional e Maturidade Tecnológica — Ceres 2021
codigo: MGG2-DD02
tipo: diagnostico-due-diligence
produto: MGg2
data_base: 2021-07
origem: "Ceres Inteligência Financeira — Relatório R0, Seção 3"
contratante: CODEMGE
status: referencia_historica
nao_usar_como_dado_atual: true
notas_relacionadas:
  - "[[MGG2-DD01_Visao-Geral-Ceres-2021]]"
  - "[[MGG2-DD05_Inventario-Equipamentos-MGg1.0]]"
---

# Análise Operacional e Maturidade Tecnológica — Ceres 2021

> **Ressalva temporal:** estado do projeto em julho de 2021. TRL e avaliações de capacidade refletem a perspectiva Ceres naquele momento.

## Objetivos tecnológicos do projeto (conforme Ceres)

1. Desenvolver processo de produção de grafeno por esfoliação química
2. Desenvolver tecnologia de caracterização do grafeno
3. Desenvolver aplicações para o grafeno consistentes com o processo selecionado

## Estratégia de desenvolvimento

Desenvolvimento gradual da esfoliação química em meio aquoso: escala laboratorial → escala piloto → escala industrial. O processo foi dividido em 4 etapas: (i) Dispersão, (ii) Cisalhamento, (iii) Separação, (iv) Acabamento.

Até julho de 2021, as Etapas 1 e 2 (laboratorial e piloto) estavam concluídas.

## Avaliação de maturidade tecnológica (TRL inferido por módulo)

| Módulo | TRL inferido | Base da avaliação Ceres |
|---|---|---|
| Processo P100 (planta piloto 100 L/batelada) | ~TRL 6 | Planta operando há mais de 2 anos, rendimentos documentados, lote-padrão definido |
| Escalonamento para P500+ (300 L+) | ~TRL 4–5 | Know-how acumulado, sem execução formal do escalonamento |
| G-Scan / caracterização automatizada | ~TRL 4–5 | Sistema funcional, uso de IA para processamento de imagens, sem padronização externa |
| Funcionalização e aplicações | ~TRL 1–3 | Estudos iniciais em múltiplos vetores; nenhuma aplicação implementada comercialmente |

## Competências mapeadas

| Competência | Infraestrutura necessária | Serviços/produtos potenciais |
|---|---|---|
| Desenvolvimento do processo de esfoliação química | Bancada + piloto + caracterização + equipe | Parametrização de plantas piloto até 500 t/batelada; melhorias de processo |
| Produção de grafeno | Piloto + caracterização simplificada + equipe | Venda de GPC/NPG/NG dentro das capacidades documentadas |
| Caracterização de grafeno | Caracterização + equipe | Serviço de caracterização para empresas compradoras |
| Know-how do processo | Bancada + caracterização + equipe | Conceitualização de planta, definição de equipamentos, comissionamento, operação |
| Know-how em grafeno | Equipe | Consultoria sobre produto e processo; suporte na aquisição de grafeno |
| Funcionalização e desenvolvimento de aplicações | Bancada + piloto + caracterização + equipe | Desenvolvimento de aplicações de grafeno |

## Lacunas identificadas pela Ceres

- **Reprodutibilidade quantitativa:** grande quantidade de bateladas caracterizadas, mas faltava estudo comparativo formal de múltiplos lotes para demonstrar variabilidade de processo
- **Metrologia e padronização externa:** técnicas de caracterização disponíveis e estado-da-arte, mas comparação com padrões NPL/ISO não documentada formalmente
- **Nenhuma aplicação implementada comercialmente** até julho de 2021
- **Necessidade de parceiro industrial** para implantação de plantas em escala
- **Estruturação societária** necessária para seguir ao mercado
- **Equipamentos dentro de centros de pesquisa** — requerem processo de transição para desenvolvimento externo

## Progresso de rendimentos da planta piloto

| Produto | Rendimento (%) jul/2018 | Rendimento (%) jul/2019 |
|---|---|---|
| NG (Nanoplaca de Grafite) | 81,7% | 88,4% |
| NPG (Grafeno B / Nanoplaca de Grafeno) | 8,0% | 9,4% |
| GPC (Grafeno A / Grafeno de Poucas Camadas) | 2,4% | 1,1% |
| Perdas | 7,9% | 1,1% |

*Nomenclatura canônica aplicada; Ceres usava Grafeno A/B/Nanoplaca.*

## Custo de produção P100 (referência histórica jul/2021)

| Produto | Custo P100 (R$/g) | Custo P500 projetado (R$/g) | Referência de mercado (R$/g) |
|---|---|---|---|
| GPC (Grafeno A) | 2,15 | 2,00 | — |
| NPG (Grafeno B) | 2,17 | n/d | — |
| NG (Nanoplaca) | 1,01 | 1,12 | 0,53 (IDTechEx) |
| GPC conc. | 12,67 | 9,28 | — |
| GPC conc.+liof | 23,55 | 24,09 | — |

> **Cautela:** estes são valores históricos de 2021. Os valores de P500 assumem premissas de escalonamento de rendimento que foram revisadas. Para referência de custo atual usar as planilhas de saneamento em [[Custos]].

## Ativos operacionais totais (valores de compra)

- Produção + desenvolvimento (Planta Piloto + Bancada): **~R$ 5,43 milhões**
- Caracterização: **~R$ 5,19 milhões**
- **Total:** ~R$ 10,62 milhões

Detalhamento por equipamento em [[MGG2-DD05_Inventario-Equipamentos-MGg1.0]].

## Benchmarking contra NPL/ISO

A Ceres registrou avaliação das técnicas de caracterização disponíveis no projeto contra os padrões do NPL (National Physical Laboratory, UK) e ISO. O projeto atendia os principais requisitos, com destaque para: espectroscopia Raman (Witec), AFM (Park Systems), DLS (Anton Paar), reometria (TA Instruments) e técnicas de tamanho de partícula (Microtrac). A avaliação formal de conformidade NPL/ISO não estava documentada como procedimento sistemático.
