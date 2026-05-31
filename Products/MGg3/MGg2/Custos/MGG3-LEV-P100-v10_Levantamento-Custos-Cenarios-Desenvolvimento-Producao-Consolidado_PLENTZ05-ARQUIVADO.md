---
codigo_fonte: MGG3-LEV-P100-v10
titulo: Levantamento de custos da P100 — Cenários Desenvolvimento e Produção
produto: MGgrafeno / MGG3
escala: P100 — 2 módulos KonMix de cisalhamento em tanques de 100 L (200 L nominais por lote combinado)
versao: 10
data: 2026-05-28
status: remodelado_cenarios_desenvolvimento_producao
base_anterior: MGG3-LEV-P100-v9
issue_mae: ALT-440
subfrentes: ALT-442, ALT-443, ALT-444, ALT-445, ALT-446, ALT-447, ALT-448, ALT-449, ALT-450
audiencia: investidor (revisão técnico-econômica)
---

# Levantamento de custos da P100 — Cenários Desenvolvimento e Produção

> Esta é a v10 do levantamento consolidado. A [[MGG3-LEV-P100-v9_Levantamento-Custos-Recomissionamento-Consolidado|v9]] permanece intocada como base histórica imediata. A v10 reorganiza a leitura econômica da P100 em **dois cenários operacionais distintos e não-misturáveis**, conforme briefing ALT-440 (item 7).

Fontes integradas: briefing operacional Fase A (ALT-440), inventário técnico B1 (ALT-442), inventário documental B2 (ALT-443), premissas técnicas C1 (ALT-444), benchmark de indiretos C2 (ALT-445), modelo D1 — Cenário Desenvolvimento (ALT-446), modelo D2 — Cenário Produção (ALT-447), análise financeira E (ALT-448), reescrita F (ALT-449), revisão final e Vault G (ALT-450).

---

## Sumário Executivo

A P100, planta consolidada na v9 do levantamento de custos de recomissionamento, é apresentada agora sob **dois cenários operacionais distintos e não-misturáveis**, cada qual com a métrica econômica que faz sentido para sua natureza.

**Cenário (1) — P100 Desenvolvimento.** A planta opera como piloto de desenvolvimento tecnológico, melhoria de processo, suporte a aplicações e produção sob encomenda à la carte. A métrica relevante é o **custo anual de capacidade técnica** mais o **custo por campanha** e o **custo marginal de lote sob medida**. Não é fábrica plena: dividir o OPEX por 522 lotes nominais subestima o que efetivamente carrega a estrutura.

- OPEX base: **R$ 4,094 MM/ano** (R$ 341,2k/mês), faixa **R$ 3,65–4,84 MM/ano** dependendo de 8 a 18 campanhas/ano.
- Custo por campanha base: **R$ 80k**.
- Custo marginal de lote à la carte: **R$ 18k/lote** (piso de custo, não preço).
- Composição: 91,8% direto / 8,2% indireto na base; 76,6% fixo / 23,4% variável.

**Cenário (2) — P100 Produção.** A planta opera como linha dedicada em 1 turno, com equipe fixa de 1 supervisor + 3 técnicos de produção + 1 técnico de CQ. A métrica relevante é o **custo unitário por produto** (GPC, NPG, Nanografite) em três condições de rendimento.

- OPEX caso-base: **R$ 2,481 MM/ano** (R$ 206,75k/mês), igual nas três condições — o que muda é a alocação de massa entre produtos.
- Sensibilidade de indiretos (mercado): R$ 2,18–2,97 MM/ano.
- Custo unitário média histórica: **GPC R$ 895/kg, NPG R$ 448/kg, Nanografite R$ 224/kg**.
- Alocação entre produtos: massa ponderada por complexidade técnica (GPC=4, NPG=2, Nanografite=1).

**Comparação para investidor.** Os dois cenários respondem a perguntas distintas: Desenvolvimento informa o volume de recursos para sustentar a tese tecnológica; Produção informa a viabilidade econômica como linha dedicada. Em base anual, a P100 carrega ~R$ 4 MM/ano operando como piloto técnico ou ~R$ 2,5 MM/ano operando como produção dedicada — a diferença reflete a estrutura técnica de desenvolvimento (equipe v9 de 8 pessoas, CQ caracterização por aplicação, campanhas variáveis) que não está presente em Produção.

**Riscos econômicos relevantes:** subutilização de capacidade técnica em D1, dispersão dos rendimentos reais em D2 (especialmente NPG e Nanografite), faixa de indiretos de mercado em C2 (Adm Geral, Seguros, Jurídico/Compliance), e premissas CFO ainda pendentes de reconciliação com a planilha v9.

---

## 1. Bases comuns

### 1.1 Escopo da P100

A P100 é a planta consolidada na [[MGG3-LEV-P100-v9_Levantamento-Custos-Recomissionamento-Consolidado|v9]] do MGG3-LEV-P100, com 2 módulos de conversão, cada um composto por tanque de 100 L e KonMix, totalizando 200 L de volume nominal por lote combinado. Cada lote consome **20 kg de grafite seco** alimentado à corrente de entrada do módulo de conversão. O ciclo nominal é de 10,75 h/lote, com capacidade nominal de **43,5 lotes/mês ou 522 lotes/ano**. A capacidade nominal é teto técnico de regime estabilizado, não promessa de primeiro ano; ramp-up defensável fica em 313–418 lotes/ano (faixa prudente 365–400).

### 1.2 Convenção de rendimento

**Todos os percentuais de rendimento neste relatório são em massa, relativos à massa inicial de grafite seco alimentado na corrente de entrada do módulo de conversão.** Não são percentuais sobre a massa total da formulação líquida, água, surfactante, NH4OH ou massa úmida separada.

### 1.3 Balanço de massa fechado — base 100 kg de grafite alimentado

| Condição | GPC | NPG | Nanografite | Residual físico | Soma |
|---|---:|---:|---:|---:|---:|
| Conservadora | 0,5 kg | 5,0 kg | 93,0 kg | 1,5 kg | 100,0 kg |
| Média histórica v9 | 0,8 kg | 5,0 kg | 93,0 kg | 1,2 kg | 100,0 kg |
| Otimista | 2,0 kg | 16,0 kg | 80,5 kg | 1,5 kg | 100,0 kg |

**Destino físico do residual:** fração de grafite/carbono alimentado não recuperada como GPC, NPG ou Nanografite com especificação. Tratado tecnicamente como mistura de finos fora de especificação, material retido em linhas/tanques/filtros, perdas por amostragem e limpeza, lodo/torta úmida de separação contendo carbono e massa carbonácea descartada ou reprocessável ainda sem especificação comercial. O residual **não é** evaporação de água, perda de NH4OH/surfactante, efluente líquido total ou diferença de massa da formulação inteira. **Não recebe receita no caso-base**; reprocesso entra apenas como sensibilidade.

### 1.4 Glossário

- **GPC** — Grafeno em poucas camadas (few-layer).
- **NPG** — Nanoplaquetas de grafeno.
- **Nanografite** — Grafite em escala nanométrica (n-graphite).
- **OPEX** — Despesa operacional total (diretos + indiretos).
- **Campanha** — Sequência de lotes contígua dedicada a um objetivo (desenvolvimento, aplicação, parceiro).
- **Lote à la carte** — Lote sob especificação técnica do parceiro, com formulação e CQ sob medida.

---

## 2. Cenário (1) — P100 Desenvolvimento

### 2.1 Premissas técnicas

A P100 opera como **planta piloto de desenvolvimento tecnológico**, suporte a aplicações finais, melhoria de processos de produção de grafeno e produção sob encomenda para parceiros (lotes à la carte). Operação por campanhas, não por ocupação contínua. A ociosidade planejada faz parte do custo de P&D.

| Bloco | Premissa |
|---|---|
| Regime | Operação por campanhas com ociosidade planejada; não modelar como fábrica plena. |
| Mix | Desenvolvimento próprio, suporte a aplicações, caracterização/formulação e lotes sob encomenda. |
| Equipe técnica | 8 pessoas (estrutura v9): coordenação, especialista, técnico líder, 2 operadores, CQ interno, manutenção/SSMA, pesquisador de aplicações/fomento. Coerente com piloto. |
| CQ | Caracterização por campanha e aplicação (Raman, granulometria, teor de sólidos, morfologia, estabilidade/funcionalidade). Variável e menos repetitivo que Produção. |
| Lotes à la carte | Variabilidade deliberada de processo; custo marginal inclui preparação, formulação, setup, retrabalho analítico, amostras e documentação técnica. **Não precificar só por kg.** |
| Risco técnico | Separação de 200 L e ciclo real ainda são incertezas de escala. |

### 2.2 Estrutura de custos (caso-base 12 campanhas/ano)

| Bloco | Natureza | Custo anual | % do total |
|---|---|---:|---:|
| Equipe técnica v9 de 8 pessoas | Direto fixo | R$ 2.138.400 | 52,2% |
| CQ externo mínimo e caracterização | Direto fixo | R$ 300.000 | 7,3% |
| Consumíveis fixos de laboratório/aplicações | Direto fixo | R$ 120.000 | 2,9% |
| Manutenção técnica de prontidão | Direto fixo | R$ 240.000 | 5,9% |
| Campanhas de desenvolvimento e à la carte | Direto variável | R$ 960.000 | 23,4% |
| Overhead institucional alocado ao piloto | Indireto fixo | R$ 180.000 | 4,4% |
| SSMA, licenças operacionais e suporte comum | Indireto fixo | R$ 96.000 | 2,3% |
| Administração, TI e apoio compartilhado | Indireto fixo | R$ 60.000 | 1,5% |
| **Total** |  | **R$ 4.094.400** | **100,0%** |

Decomposição base: 91,8% direto / 8,2% indireto; 76,6% fixo / 23,4% variável.

### 2.3 Modelo por campanha e lote à la carte

Custo variável por campanha base (5 lotes): **R$ 80.000**, composto por insumos produtivos (R$ 17,5k), utilidades (R$ 4,5k), CQ externo incremental e ensaios de aplicação (R$ 35k), manutenção corretiva leve (R$ 7,5k) e setup/formulação/documentação (R$ 15,5k).

Custo marginal de lote à la carte adicional dentro de campanha aberta: **R$ 18.000/lote** (insumos R$ 3,5k, utilidades R$ 0,9k, CQ incremental R$ 4,5k, mão de obra incremental R$ 3k, limpeza/setup/retrabalho R$ 5k, resíduo R$ 1,1k).

**Regra de uso comercial:** proposta à la carte deve separar três camadas: (i) taxa de abertura de campanha (cobre setup/CQ/documentação); (ii) custo marginal por lote adicional; (iii) prêmio técnico por especificação, urgência, confidencialidade, retrabalho ou propriedade intelectual.

### 2.4 Leitura econômica

A métrica relevante para Desenvolvimento **não é R$/kg nem OPEX/522 lotes**. A P100 piloto carrega uma estrutura fixa de capacidade técnica de ~R$ 3,13 MM/ano (equipe + CQ mínimo + consumíveis fixos + manutenção de prontidão + indiretos); as campanhas apenas absorvem essa capacidade. O risco econômico relevante é **subutilização da capacidade técnica**: poucos lotes não reduzem a maior parte do OPEX, apenas reduzem absorção do custo fixo.

| Cadência | OPEX anual | OPEX mensal | Lotes/ano | Uso vs. nominal | Variável anual implícita |
|---|---:|---:|---:|---:|---:|
| Conservador — 8 campanhas (≈4 lotes/campanha) | R$ 3.654.400 | R$ 304.500 | 32 | 6,1% | R$ 520.000 |
| Base — 12 campanhas (5 lotes/campanha) | R$ 4.094.400 | R$ 341.200 | 60 | 11,5% | R$ 960.000 |
| Intensivo — 18 campanhas (≈6 lotes/campanha + à la carte) | R$ 4.844.400 | R$ 403.700 | 108 | 20,7% | R$ 1.710.000 |

Nota de rastreabilidade: a estrutura fixa total (R$ 3.134.400/ano: diretos fixos R$ 2.798.400 + indiretos R$ 336.000) é constante entre cadências; a variável anual decorre da combinação cadência × tamanho médio de campanha × intensidade à la carte, conforme detalhado em ALT-446 (D1).

---

## 3. Cenário (2) — P100 Produção

### 3.1 Premissas técnicas

A P100 opera como **operação dedicada de produção em 1 turno**, com a mesma base física da v9 e três condições de rendimento aplicadas sobre o mesmo OPEX.

| Bloco | Premissa |
|---|---|
| Regime | 1 turno, produção dedicada, mesma base física da v9; capacidade nominal 522 lotes/ano como teto, não como caso único. |
| Equipe fixa | 1 supervisor + 3 técnicos de produção + 1 técnico de CQ (substitui a equipe v9 de 8). |
| Mix de produto | GPC, NPG e Nanografite como frações produtivas; residual como perda/resíduo de processo, sem receita no caso-base. |
| CQ | Controle rotineiro por especificação/lote, com amostragem e liberação; técnico CQ fixo + ensaios externos por frequência. |
| Insumos/utilidades | Mesma família da v9, consumo variável por lote; custos unitários por produto recalculados em cada condição de rendimento. |
| Manutenção | Preventiva/corretiva da operação dedicada. Faixa: 3–5% estabilizada ou 5–8% se estado da planta exigir. |

### 3.2 Estrutura mensal de custos (caso-base, faixa média de indiretos)

| Bloco | R$/mês |
|---|---:|
| Equipe fixa de produção | 59.400 |
| Insumos de produção | 30.950 |
| Utilidades produtivas | 8.000 |
| Manutenção preventiva/corretiva | 18.000 |
| CQ externo rotineiro | 25.000 |
| Consumíveis de CQ | 4.000 |
| Resíduo/reprocesso | 2.000 |
| Indiretos empresariais médios (C2) | 59.400 |
| **Total mensal caso-base** | **206.750** |
| **Total anual caso-base** | **2.481.000** |

Decomposição base: 71,3% direto / 28,7% indireto; 86,1% fixo / 13,9% variável. Para esta classificação, **fixo** é a parcela mantida no regime mensal de 43,5 lotes/mês; **variável** é a parcela que escala com lotes efetivamente processados no mês. Insumos produtivos ficam tratados como semi-fixos no regime de referência, não como variação livre lote-a-lote.

### 3.3 Custo unitário por produto — três condições

Base de cálculo: 870 kg de grafite seco alimentado por mês (43,5 lotes × 20 kg). Critério de alocação entre produtos: **massa ponderada por complexidade técnica** com pesos GPC = 4, NPG = 2, Nanografite = 1. Justificativa: custo por massa pura subaloca GPC/NPG porque as frações nobres concentram esforço de separação, CQ e especificação; alocação por receita exigiria preço de venda ainda não validado e misturaria custo com hipótese comercial. O critério ponderado é defensável para investidor porque preserva causalidade operacional sem depender de preço futuro. Residual não recebe receita nem absorve margem.

| Condição | GPC kg/mês | NPG kg/mês | Nanografite kg/mês | Residual kg/mês | GPC R$/kg | NPG R$/kg | Nanografite R$/kg |
|---|---:|---:|---:|---:|---:|---:|---:|
| Conservadora 0,5/5/93/1,5 | 4,35 | 43,50 | 809,10 | 13,05 | **R$ 905** | **R$ 453** | **R$ 226** |
| Média histórica v9 0,8/5,0/93,0/1,2 | 6,96 | 43,50 | 809,10 | 10,44 | **R$ 895** | **R$ 448** | **R$ 224** |
| Otimista 2/16/80,5/1,5 | 17,40 | 139,20 | 700,35 | 13,05 | **R$ 789** | **R$ 394** | **R$ 197** |

### 3.4 Leitura econômica

O OPEX total não muda entre as condições — o que muda é a massa produzida por produto e, portanto, o custo unitário. A operação precisa gerar contribuição suficiente para cobrir **R$ 206,75k/mês** no caso-base, ou **R$ 181,35k–247,35k/mês** considerando apenas a faixa de indiretos C2. Ponto de equilíbrio operacional pleno não fecha sem preço de venda validado, mix comercial por produto e impostos comerciais.

---

## 4. Análise comparativa e sensibilidade

### 4.1 Quadro comparativo simétrico

Os dois cenários respondem a perguntas distintas e exigem métricas distintas. O quadro abaixo respeita essa assimetria.

| Cenário | Condição | OPEX mensal | OPEX anual | Diretos / indiretos | Fixos / variáveis | Métrica correta |
|---|---:|---:|---:|---:|---:|---|
| Desenvolvimento | 8 campanhas/ano | R$ 304,5k | R$ 3,654 MM | 90,8% / 9,2% | 85,8% / 14,2% | capacidade técnica anual + custo por campanha |
| Desenvolvimento | 12 campanhas/ano | R$ 341,2k | R$ 4,094 MM | 91,8% / 8,2% | 76,6% / 23,4% | R$ 80k/campanha + R$ 18k/lote marginal à la carte |
| Desenvolvimento | 18 campanhas/ano | R$ 403,7k | R$ 4,844 MM | 93,1% / 6,9% | 64,7% / 35,3% | absorção de capacidade, não custo fabril pleno |
| Produção | Conservadora | R$ 206,75k | R$ 2,481 MM | 71,3% / 28,7% | 86,1% / 13,9% | custo unitário por produto |
| Produção | Média histórica v9 | R$ 206,75k | R$ 2,481 MM | 71,3% / 28,7% | 86,1% / 13,9% | custo unitário por produto |
| Produção | Otimista | R$ 206,75k | R$ 2,481 MM | 71,3% / 28,7% | 86,1% / 13,9% | custo unitário por produto |

### 4.2 Sensibilidade — ranking financeiro

| Posição | Variável crítica | Caso baixo | Base | Caso alto | Impacto |
|---:|---|---:|---:|---:|---|
| 1 | Indiretos C2 mensais (P100 Produção) | R$ 34k | R$ 59,4k | R$ 100k | Nanografite R$ 196–268/kg; OPEX R$ 181,35k–247,35k/mês |
| 2 | Rendimento NPG (P100 Produção) | 5,0% | 5,0% | 16,0% | Nanografite R$ 224 → R$ 205/kg (variação isolada com Nano rebaseado em 80,5%) |
| 3 | Rendimento Nanografite (P100 Produção) | 80,5% | 93,0% | 93,0% | Nanografite R$ 254 → R$ 224/kg |
| 4 | Cadência D1 (P100 Desenvolvimento) | 8 | 12 | 18 campanhas/ano | OPEX D1 R$ 3,65–4,84 MM/ano |
| 5 | Rendimento GPC (P100 Produção) | 0,5% | 0,8% | 2,0% | Nanografite R$ 226 → R$ 216/kg (GPC alto com Nano rebaseado em 91,8%) |

**Leitura para investidor:** D2 é sensível à estrutura administrativa e aos rendimentos reais; D1 é sensível à ocupação da capacidade técnica.

---

## 5. Riscos e premissas frágeis

1. **Cadência D1 — subutilização de capacidade técnica.** Se a planta piloto tiver baixa ocupação, o OPEX não cai proporcionalmente. A estrutura fixa de ~R$ 3,13 MM/ano continua carregada mesmo com 8 campanhas/ano.
2. **Rendimentos reais D2.** O custo unitário depende do rendimento por produto; NPG e Nanografite movem mais a absorção econômica que GPC em massa. Os três cenários de rendimento (conservadora, média histórica, otimista) precisam ser validados por campanha de balanço gravimétrico pós-recomissionamento.
3. **Dispersão de indiretos C2.** Adm. Geral, Seguros e Jurídico/Compliance têm dispersão suficiente para mover o OPEX mensal de Produção em ~R$ 66k entre mínimo e máximo. Decisão sobre estrutura societária e regime tributário (Lucro Presumido vs. Real) afeta a tabela.
4. **Premissas CFO não reconciliadas com planilha v9.** Folha carregada, CQ externo, manutenção, insumos, utilidades e custo marginal à la carte precisam de reconciliação final com v9/RFQs antes de virarem número de banco.
5. **Risco de precificação.** Sem preço de venda validado por produto, o custo unitário é defensável, mas a tese de margem ainda não está fechada. Recomenda-se contratar offtake ou pré-venda antes de comprometer ramp-up de produção dedicada.
6. **Gargalo técnico de separação em 200 L.** Identificado no inventário B1 como incerteza alta. Pode reduzir lotes efetivos/ano e elevar ciclo real para ~13,25 h/lote, comprimindo capacidade nominal.

---

## 6. Recomendações para apresentação ao investidor

1. **Apresentar os dois cenários como respostas a perguntas distintas, não como alternativas excludentes.** Desenvolvimento informa o custo de manter a tese tecnológica viva; Produção informa o custo unitário se a planta for dedicada. Combinações mistas (parte do ano em desenvolvimento, parte em produção dedicada) são tecnicamente possíveis e devem aparecer como variante de planejamento, não como cenário-base.
2. **Não dividir D1 por 522 lotes nominais nem comparar diretamente R$/kg entre D1 e D2.** A métrica de Desenvolvimento é capacidade técnica anual; a métrica de Produção é R$/kg por produto.
3. **Tratar os três rendimentos de D2 como banda de defesa, não como casos isolados.** A média histórica v9 (0,8/5,0/93,0/1,2) é o caso-base; conservadora e otimista delimitam a defesa frente à variabilidade real.
4. **Apresentar a faixa de indiretos C2 (mín/médio/máx) com a fonte de cada linha.** O investidor sofisticado vai questionar a base de seguros ambientais e a estrutura administrativa (Diretor sócio vs. Gerente contratado).
5. **Explicitar o residual de processo como custo, não como receita.** Reprocesso pode aparecer como sensibilidade, mas não pode entrar no caso-base sem evidência experimental.
6. **Recomendar campanha de balanço gravimétrico pós-recomissionamento** como condição para fechar as três condições de rendimento com rigor estatístico.

---

## 7. Pendências antes da entrega ao investidor

Itens herdados do v9 e das frentes B1–E que permanecem como pendências documentais controladas — não bloqueiam a leitura econômica, mas devem ser fechados antes de uso contratual:

- RFQs formais para equipe, CQ externo, manutenção, insumos e utilidades.
- Vistoria de campo, laudos/ARTs aplicáveis e protocolo de comissionamento (SAT) com critérios de aceite.
- Matriz NR-12/SSMA atualizada para a configuração 2 × KonMix em 100 L.
- Reconciliação final com a planilha-fonte [[P100_Custo de Produção - CLT_2021  - 9 de agosto de 2021 (CERES)]] (CERES 2021) e com o relatório revisado por Plentz.
- Ingestão no Vault das fontes externas `Levantamento de custos de Producao P100x2.xlsx`, `PIO-MGG-019` e `PIO-MGG-039`, hoje fora da pasta `Custos/` (ver B2, ALT-443).

---

## Anexos

### A. Premissas com fonte, data e incerteza

Todas as premissas numéricas estão consolidadas em planilhas anexas às issues filhas (C1, C2, D1, D2, E). A tabela canônica de premissas com fonte, data de validade e faixa de incerteza está em E (ALT-448), aba `Premissas` da planilha entregue por Julio.

### B. Modelos econômicos detalhados

- Modelo D1 — Cenário Desenvolvimento: tabela 2.2 e seção 2.3 deste relatório; detalhamento integral em ALT-446.
- Modelo D2 — Cenário Produção: tabela 3.2 e seção 3.3 deste relatório; detalhamento integral e planilha em ALT-447.
- Análise comparativa e sensibilidade: planilha `ALT-448_analise_financeira_comparativa_sensibilidade.xlsx` anexa em ALT-448.

### C. Documentos vizinhos no Vault

- [[MGG3-LEV-P100-v9_Levantamento-Custos-Recomissionamento-Consolidado|MGG3-LEV-P100-v9]] — base imediata desta versão, preservada para rastreabilidade.
- [[MGG2-CUSTO-P100_Modelo-custo-planta-piloto|MGG2-CUSTO-P100 — Modelo de custo da planta piloto]] — registro documental da planilha P100 2021.
- [[Saneamento custos P100 P500|Saneamento de custos P100/P500]] — nota operacional de ponte de premissas.
- [[MGG3-CUSTO-P500_Projecao-KonMix|MGG3-CUSTO-P500 — Projeção KonMix P500]] — relatório irmão para contexto comparativo.
- `Controle operacional de lotes/` — subpasta com fontes primárias de balanço de massa (lote `20210720Pa`), volumes processados e controle de processos.

### D. Decisões editoriais não-óbvias (mantidas após revisão G)

1. **Equipe v9 de 8 pessoas em Desenvolvimento, não a equipe fixa do briefing.** A equipe fixa (1 supervisor + 3 técnicos + 1 CQ) é específica de Produção, conforme C1. Misturar as duas comprometeria a tese de Desenvolvimento como piloto técnico.
2. **OPEX igual nas três condições de Produção.** A estrutura operacional é a mesma; o que muda entre conservadora/média/otimista é a massa produzida por produto e, portanto, o R$/kg. Mantido explícito em 3.4 e 4.1 para evitar leitura financeira equivocada.
3. **Critério de alocação GPC=4, NPG=2, Nanografite=1.** Vem de D2 e foi mantido. Justificativa de causalidade operacional está em 3.3.
4. **Ponto de equilíbrio operacional pleno não fecha** sem preço validado. Declarado como limitação em vez de forçar um número frágil — postura defensável diante de investidor sofisticado.
5. **Recomendação 1 (cenários mistos) mantida no corpo.** Decorre da leitura combinada e ajuda o framing do investidor; não é um número, é guidance de uso.

---

*Versão consolidada na Fase G por Carmen (ALT-450), com base na reescrita de F (ALT-449) e nas frentes B1–E. Para a história completa de revisões e o caminho até v10, consultar a issue-mãe ALT-440.*
