---
codigo_fonte: MGG3-LEV-P100-v10
titulo: Levantamento de custos da P100 — Cenários Desenvolvimento e Produção (Revisão Plentz-06.b)
produto: MGgrafeno / MGG3
escala: P100 — 2 módulos KonMix de cisalhamento em tanques de 100 L (200 L nominais por lote combinado)
versao: 10
revisao: Plentz-06.b
data: 2026-05-31
status: consolidado_cenarios_desenvolvimento_producao
base_anterior: MGG3-LEV-P100-v9
issue_revisao_6: [ALT-464](mention://issue/e3b93760-b3d1-4468-ab0e-544991700023)
issue_revisao_final: ALT-464
issue_revisao_6a: [ALT-487](mention://issue/6760ed5e-5d9b-4b1b-9c5e-e448f3b85377)
issue_revisao_6b: [ALT-487](mention://issue/6760ed5e-5d9b-4b1b-9c5e-e448f3b85377)
subfrentes_rev06: [ALT-465](mention://issue/447ac547-6079-4350-92e6-441c91a0e503), [ALT-466](mention://issue/f0520698-b1e9-40a7-85e1-254350010c51), [ALT-467](mention://issue/7e482ee8-564d-4242-8836-2c47d4016c16), [ALT-468](mention://issue/432a64f1-7aa8-40fa-b385-50527c13c985), [ALT-469](mention://issue/98da17bf-f801-43ab-b31f-e3cef93f46af), [ALT-470](mention://issue/44323d04-01c4-476e-848b-b239cc4af1e8), [ALT-471](mention://issue/c4709a22-065d-473c-a080-4447e227c8dd), [ALT-472](mention://issue/cb0eba0b-a456-4a20-af8b-950dd5076d79), [ALT-473](mention://issue/27df4ad9-137a-4121-8d70-09bdee0b4007), [ALT-474](mention://issue/6067b916-e710-41ac-bebe-7ba29472a28b)
audiencia: técnico-acadêmico-financeira (rigor v9 + leitura de cenários para investidor e pesquisador)
---

# Levantamento de custos da P100 — Cenários Desenvolvimento e Produção (Revisão Plentz-06)

> Esta é a v10 do levantamento consolidado. A [[MGG3-LEV-P100-v9_Levantamento-Custos-Recomissionamento-Consolidado|v9]] permanece intocada como base histórica imediata. A v10 é **sucessora sequencial da v9**: reincorpora todos os blocos analíticos da v9 (§4.1–§4.5, §6.1–§6.6, CAPEX por pacotes, glossário 26 termos, rastreabilidade §12, gates SSMA §11, pendências §22) e acrescenta a estrutura de dois cenários operacionais distintos (Desenvolvimento e Produção) conforme briefing [ALT-464](mention://issue/e3b93760-b3d1-4468-ab0e-544991700023) Revisão Plentz-06.

---

## §1. Finalidade e leitura correta deste relatório

Este relatório apresenta uma estimativa consolidada dos custos para recomissionar e operar a P100, a planta piloto do MGgrafeno composta por sistemas KonMix de cisalhamento em tanques de 100 L. A nomenclatura histórica "reatores KonMix" é preservada como referência documental, mas a leitura técnica desta versão adota a formulação mais precisa de sistemas de cisalhamento. O objetivo não é tratar a P100 como uma fábrica comercial madura, nem como uma bancada de pesquisa pura. A P100 deve ser entendida como uma infraestrutura piloto escalável de uma startup de alta tecnologia que está passando da tecnologia para o mercado.

Por essa razão, os números deste documento devem ser lidos como projeções técnico-econômicas de uma operação em desenvolvimento. Eles são suficientemente estruturados para orientar decisão, orçamento, priorização e negociação, mas ainda não substituem cotações formais de fornecedores, contratos definitivos de controle de qualidade, validação de desempenho por aplicação e definição completa do regime de uso da planta.

A P100 pode produzir material, mas seu papel mais importante no primeiro ciclo não é vender grafeno em pó como commodity. O plano de negócios do MGgrafeno deve buscar valor por solução, formulação, desempenho aplicado e relacionamento técnico com clientes. Isso inclui três frentes: entrega de grafeno como insumo de alto valor agregado em relação ao grafite natural, desenvolvimento de grafenos modificados ou personalizados, e prestação de serviços técnicos por demanda ("Grafeno como Serviço").

Esta v10 organiza a leitura econômica em **dois cenários operacionais distintos e não-misturáveis** conforme o propósito predominante da planta:

- **Cenário Desenvolvimento:** P100 como piloto técnico. Métrica correta: custo anual de capacidade técnica, custo por campanha, custo marginal por lote à la carte.
- **Cenário Produção:** P100 como linha dedicada em 1 turno. Métrica correta: custo unitário por produto (GPC, NPG, Nanografite) em três condições de rendimento.

Nenhum dos dois cenários invalida o outro. São leituras de finalidades distintas; a confusão entre elas produz análise econômica equivocada.

### §1.1 Guia de leitura por audiência

Este relatório atende simultaneamente a duas audiências com necessidades distintas. Use a tabela abaixo para localizar rapidamente as seções de maior relevância para seu perfil.

| Perfil | Seções de entrada | Aprofundamento |
|---|---|---|
| **Investidores e parceiros financeiros (IFHAN)** | §2 (indicadores consolidados), §7 (referências de preço de mercado), §13 (sensibilidades) | §5 (CAPEX detalhado), §8 (Cenário Desenvolvimento: OPEX, custo por campanha), §9 (Cenário Produção: custo por produto), §10 (reconciliação v9↔v10), §22 (pendências antes de orçamento executivo) |
| **Pesquisadores e parceiros técnicos (UFMG, CDTN)** | §3 (glossário de 26 termos), §4 (base operacional, ciclo, rendimentos, parâmetros por módulo), §11 (gates SSMA e compliance) | §6.1–§6.6 (composição detalhada de custos), §12 (rastreabilidade de valores críticos com fonte documental), §14 (próximos passos técnicos), §22 (pendências técnicas abertas) |
| **Ambas as audiências** | §1 (finalidade e posicionamento da P100), §2 (indicadores-chave) | §10 (reconciliação dos dois cenários com base v9), §14 (próximos passos), §15–§21 (changelogs da v3 à v10) |

Os indicadores-chave em §2 são a porta de entrada comum. Investidores seguem para §7–§9; pesquisadores seguem para §4 e §11. A rastreabilidade de cada valor crítico está em §12.

---

## §2. Resultado consolidado em linguagem direta

A estimativa atual separa dois tipos de número que não devem ser confundidos: o dinheiro novo estimado para recolocar a planta existente em operação e o custo recorrente de operar.

| Indicador                                     |    Valor consolidado | Como interpretar                                                                                                        |
| --------------------------------------------- | -------------------: | ----------------------------------------------------------------------------------------------------------------------- |
| CAPEX incremental para recomissionamento      |           R$ 610.000 | Estimativa gerencial preliminar AACE Classe 4/5; faixa indicativa R$ 430–915k; requer vistoria, RFQ e gates documentais |
| Base bruta histórica dos equipamentos da P100 |         R$ 1.680.560 | Planilha P100 2021: R$ 1.615.200 (produção) + R$ 65.360 (SSMA); sem depreciação acumulada                               |
| OPEX caixa recorrente (base v9)               |     R$ 2.396.908/ano | Gastos operacionais anuais sem depreciação; equipe 8 pessoas, CQ US$5k/mês, matérias-primas, utilidades, manutenção     |
| OPEX técnico completo (base v9)               |     R$ 2.563.484/ano | OPEX caixa + depreciação gerencial R$ 166.576                                                                           |
| Produção técnica de referência                |        10.315 kg/ano | Capacidade calculada com 20 kg/lote, 522 lotes/ano; não é garantia de venda integral                                    |
| Custo técnico completo médio (base v9)        |            R$ 249/kg | OPEX completo / produção técnica; base comparativa com preços de mercado                                                |
| **Cenário Desenvolvimento — OPEX caso-base**  | **R$ 4.094.400/ano** | Equipe v9 8 pessoas + frentes técnicas; faixa R$ 3,65–4,84 MM/ano por cadência de campanhas. Detalhamento: §8                     |
| **Cenário Produção — OPEX caso-base**         | **R$ 2.481.000/ano** | Equipe enxuta 5 pessoas + indiretos de mercado; custo por produto: GPC R$ 895/kg, NPG R$ 448/kg, Nanografite R$ 224/kg. Detalhamento: §9; reconciliação v9↔v10: §10 |

Os dois cenários respondem a perguntas distintas. Desenvolvimento informa o volume de recursos para sustentar a tese tecnológica. Produção informa a viabilidade econômica como linha dedicada. A diferença de ~R$ 1,6 MM/ano entre os cenários reflete a estrutura técnica de desenvolvimento (equipe v9 de 8 pessoas, CQ por aplicação, campanhas variáveis) que não está presente em Produção. Ver reconciliação completa em §10.

---

## §3. Glossário

Para facilitar a leitura técnica, financeira e editorial do novo v10, os principais códigos e termos usados no relatório ficam organizados abaixo em ordem alfabética, com definição operacional no contexto da P100.

- **AACE**: Association for the Advancement of Cost Engineering. Referência usada neste relatório para classificar estimativas de custo por maturidade de engenharia. A estimativa de CAPEX de recomissionamento deve continuar tratada como AACE Classe 4/5, com faixa de incerteza compatível, até haver RFQs, propostas de fornecedores e engenharia mais fechada.
- **Alocação por complexidade técnica (4:2:1)**: critério econômico da v10 para distribuir o OPEX do Cenário Produção entre os produtos conforme esforço técnico relativo, e não apenas por massa física. Neste relatório, GPC absorve peso 4, NPG peso 2 e Nanografite peso 1. O residual físico não recebe receita nem margem no caso-base.
- **Campanha**: sequência planejada de lotes contíguos dedicada a um objetivo técnico-comercial específico, como desenvolvimento de aplicação, validação de processo, atendimento a parceiro ou produção sob encomenda. No Cenário Desenvolvimento, campanha é unidade de absorção de capacidade técnica; não deve ser confundida com operação contínua de fábrica plena.
- **CAPEX**: investimento de capital. Neste relatório, há duas leituras distintas: o CAPEX incremental de recomissionamento, isto é, dinheiro novo estimado para preparar a planta existente para voltar a operar; e a base bruta histórica dos equipamentos, correspondente aos valores registrados na planilha P100 de 2021 para produção e SSMA, sem depreciação acumulada.
- **Cenário Desenvolvimento**: leitura operacional em que a P100 funciona como planta piloto de desenvolvimento tecnológico, formulações, melhoria de processo, suporte a aplicações e produção sob encomenda. A métrica correta é custo anual de capacidade técnica, custo por campanha e custo marginal de lote à la carte; não é R$/kg por ocupação plena.
- **Cenário Produção**: leitura operacional em que a P100 funciona como linha dedicada em 1 turno, com equipe fixa enxuta, mix produtivo GPC/NPG/Nanografite e custo unitário por produto. A métrica correta é R$/kg por produto, calculado por rendimento e alocação por complexidade técnica.
- **Comissionamento frio**: etapa de verificação e teste da planta sem carga real de processo e, quando aplicável, sem produto químico ou grafite. Serve para confirmar montagem, intertravamentos, sentido de rotação, instrumentação, comandos, estanqueidade, utilidades, alarmes, segurança e sequência operacional antes de expor a planta às condições reais de produção.
- **Comissionamento quente**: etapa de teste da planta em condições próximas ou equivalentes à operação real, com água ou meio de processo e, quando previsto no protocolo, carga de grafite ou lote teste. Serve para validar estabilidade operacional, temperatura, vazão, rotação, separação, balanço de massa, qualidade das frações e critérios de aceite antes de tratar a P100 como apta a campanhas regulares.
- **CQ**: controle de qualidade. Na leitura de recomissionamento da v9, CQ é tratado como serviço terceirizado junto à UFMG/CDTN, com orçamento de US$5.000/mês para análises como Raman, AFM, TG, gravimetria e outras. No novo v10, deve ficar separado entre CQ de caracterização por campanha/aplicação no Desenvolvimento e CQ rotineiro por especificação na Produção.
- **DA**: desenvolvimento de aplicações. Designa a frente técnico-comercial que transforma frações de grafeno e nanografite em formulações, protótipos, especificações de uso, propostas de projeto e evidências de desempenho para clientes, CDTN, UFMG e editais de fomento.
- **Depreciação gerencial**: cálculo econômico separado que reconhece o desgaste dos equipamentos ao longo do tempo. Não é pagamento anual a fornecedor e não está abatida no valor bruto histórico de R$1.680.560. No Cenário Produção, depreciação pode não fazer parte do OPEX caso-base dependendo da premissa; em Desenvolvimento é componente do OPEX técnico completo.
- **Editais de fomento**: chamadas públicas ou instrumentos competitivos de subvenção, cooperação ou financiamento à pesquisa, desenvolvimento e inovação. Incluem oportunidades que possam apoiar projetos de aplicação do MGgrafeno em parceria com grupos do CDTN e da UFMG.
- **FAT**: factory acceptance test, ou teste de aceite em fábrica. Aplica-se quando um equipamento ou retrofit for testado antes de instalação em campo.
- **GPC / FLG**: grafeno de poucas camadas, equivalente operacional ao termo internacional few-layer graphene.
- **GPB**: termo legado introduzido sem definição formal. Não deve ser usado como sigla oficial nesta nota. Quando a intenção for falar de grafeno técnico em pó, o texto deve usar GPC, FLG, GNP ou uma descrição técnica explícita.
- **HH**: homem-hora ou mão de obra. No Cenário Desenvolvimento, a equipe operacional, de CQ e de desenvolvimento de aplicações é de 8 pessoas (equipe v9); no Cenário Produção, a equipe fixa é de 5 pessoas (1 supervisor + 3 técnicos de produção + 1 técnico de CQ).
- **LPE**: liquid phase exfoliation, ou esfoliação em fase líquida. É a família de rotas de produção em que grafite é esfoliado em meio líquido por cisalhamento, sonicação ou mecanismos correlatos.
- **Lote à la carte**: lote sob especificação técnica do parceiro, com formulação e CQ sob medida. O custo inclui abertura de campanha, insumos, ensaios específicos e documentação técnica; não deve ser precificado como pó simples.
- **MC**: módulo de conversão. Cada MC corresponde ao conjunto formado por tanque de 100 L nominal e cisalhador KonMix.
- **MS**: módulo de separação. Corresponde ao conjunto de etapas e equipamentos usados após o cisalhamento para separar frações, incluindo decantação, decanter e/ou centrífuga de discos conforme a rota operacional.
- **Nanografite / NG**: grafite em escala nanométrica (n-graphite), fração de maior volume e menor valor técnico relativo; não é automaticamente GPC nem NPG. Deve ser precificado separadamente; reprocesso é sensibilidade, não caso-base.
- **NPG / GNP**: nanoplaquetas de grafeno, equivalente operacional ao termo internacional graphene nanoplatelets.
- **OPEX**: despesa operacional total (diretos + indiretos). Leituras distintas por cenário: em Desenvolvimento mede capacidade técnica anual; em Produção mede custo fabril dedicado por produto.
- **OPEX caixa**: parcela do OPEX que representa desembolso operacional recorrente. Inclui equipe, CQ terceirizado, materiais, utilidades, manutenção e consumíveis de SSMA.
- **OPEX técnico completo**: OPEX caixa somado à depreciação gerencial. Serve para enxergar o custo econômico total de usar a infraestrutura.
- **P100**: planta piloto com sistemas KonMix de cisalhamento em tanques de 100 L, usada para transição tecnologia-mercado, produção de lotes qualificados, desenvolvimento de formulações e validação técnico-comercial.
- **PIO**: procedimento interno operacional. Nos documentos históricos da P100, os PIOs registram rotas e instruções de operação para etapas como cisalhamento, decanter e centrífuga de discos.
- **RCF**: relative centrifugal force, ou força centrífuga relativa. Expressa em múltiplos da gravidade (g) e é mais adequada que rpm isolado para comparar capacidade de separação centrífuga entre equipamentos de geometrias diferentes.
- **Retrofit mecânico**: conjunto de intervenções físicas em equipamentos e interfaces mecânicas existentes para recuperar condição operacional, segurança e repetibilidade sem substituir integralmente a planta.
- **rpm**: rotações por minuto.
- **SAT**: site acceptance test, ou teste de aceite em campo. Gate recomendado para validar volume real por lote, vazões, rotações, capacidade de separação, tempo de limpeza e balanço de massa com a P100 instalada.
- **SSMA**: saúde, segurança e meio ambiente.

---

## §4. Base operacional da P100

A estimativa parte da planta P100, composta por dois módulos de conversão — cada um formado por um tanque de 100 L (volume nominal do equipamento) e um cisalhador KonMix —, operando em regime de um turno. Os dois módulos operam em paralelo dentro do mesmo ciclo de lote, gerando um volume nominal total de 200 L por lote. A referência de capacidade usada no cálculo é de 43,5 lotes por mês, ou 522 lotes por ano. Cada lote parte de 20 kg de grafite como carga de entrada combinada dos dois módulos de conversão — 10 kg por tanque de 100 L, resultando em concentração nominal de 100 g/L (equivalente a 100 g/kg de dispersão líquida) por tanque —, com ciclo técnico de 10,75 horas.

Para garantia de leitura técnica inequívoca: a P100 possui dois módulos de conversão, cada um constituído por um tanque de 100 L (volume nominal) e um cisalhador KonMix, operando em paralelo. A carga de grafite de cada tanque de 100 L é de 10 kg, resultando em concentração nominal de 100 g/L por tanque. Com dois módulos combinados, a carga total por lote é de **20 kg de grafite (10 kg + 10 kg)** e o volume nominal total é de **200 L**. A unidade de referência do modelo é o quilograma (kg): 20,0 kg de entrada, ~19,76 kg de produção técnica por lote.

| Parâmetro operacional | Valor usado | Leitura no modelo |
|---|---:|---|
| Módulos de conversão | 2 unidades (tanque 100 L nominal + cisalhador KonMix) | Configuração P100 |
| Volume nominal total por lote | 200 L | Operação paralela dos dois tanques de 100 L |
| Regime operacional | 1 turno | Base de planejamento |
| Lotes por mês | 43,5 | Capacidade nominal econômica |
| Lotes por ano | 522 | Teto nominal — ver §4.3 |
| Grafite por lote | 20,0 kg | 10 kg por tanque × 2 tanques; concentração 100 g/L por tanque |
| Tempo técnico de ciclo | 10,75 h/lote | Ciclo otimista do modelo — ver §4.1 |
| Rendimento GPC/FLG | 0,80% | 0,160 kg/lote |
| Rendimento NPG/GNP | 5,00% | 1,000 kg/lote |
| Rendimento Nanografite | 93,00% | 18,600 kg/lote |
| Perdas de processo | 1,20% | 0,240 kg/lote |
| Produção técnica calculada | 19,760 kg/lote | |
| Produção técnica anual | 10.314,72 kg/ano | 19,760 × 522 |

A composição estimada preserva os rendimentos de caso-base da v9. A regra de convenção é invariável: **todos os percentuais de rendimento são em massa, relativos à massa inicial de grafite seco alimentado na corrente de entrada do módulo de conversão** — não sobre a formulação líquida, água, surfactante, NH4OH ou massa úmida.

### §4.1 Origem e decomposição do ciclo de 10,75 h/lote

O ciclo de **10,75 h/lote** deve entrar no novo v10 como **ciclo técnico otimista de modelo**, não como cronoanálise de campo. A origem documental é a aba `Parâmetros` da planilha histórica `P100_Custo de Produção - CLT_2021 - 9 de agosto de 2021 (CERES).xlsx` e a planilha externa `Levantamento de custos de Producao P100x2.xlsx`.

| Etapa do ciclo | Tempo | Natureza da fonte | Leitura no novo v10 | Aplicabilidade por cenário |
|---|---:|---|---|---|
| Carga e preparo do módulo de conversão | 1,50 h | Dado documentado em planilha CERES / P100x2 | Parâmetro de modelo; requer confirmação em cronoanálise SAT | Ambos |
| Operação de cisalhamento KonMix | 5,00 h | Dado documentado no lote 20210720Pa e planilhas econômicas | Tempo base da rota econômica 100 g/L; não confundir com PIO 50 g/L/24 h | Ambos |
| Descarga do módulo de conversão | 0,75 h | Dado documentado em planilha | Parâmetro de modelo; validar tempo real de drenagem/transferência | Ambos |
| **Subtotal módulo de conversão** | **7,25 h** | Soma documentada | Base de conversão antes da separação | Ambos |
| 1ª separação | 2,00 h | Dado documentado em planilha econômica | Parâmetro histórico otimista; depende de volume e rota de separação | Gate crítico para Produção |
| 2ª separação | 1,50 h | Dado documentado em planilha econômica | Parâmetro histórico otimista | Gate crítico para Produção |
| **Subtotal módulo de separação** | **3,50 h** | Soma documentada | Não incorpora integralmente limpeza do MS | Ambos |
| **Total do ciclo no modelo** | **10,75 h** | Planilha CERES / P100x2 | Capacidade nominal, não performance garantida | Ambos |
| Limpeza MS | 2,50 h/lote | Dado documentado em planilha | **Pendência preservada:** limpeza não está integralmente embutida no 10,75 h | Produção: regra operacional fixa; Desenvolvimento: por campanha |
| Faixa defensável com limpeza | 10,75–13,25 h/lote | Inferência: 10,75 h + limpeza MS 2,50 h | Usar em sensibilidade e gate de performance test | Ambos |

Duas advertências devem permanecer no texto:
1. O ciclo de **10,75 h/lote** é defensável para capacidade nominal, mas o intervalo **10,75–13,25 h/lote** é mais honesto para planejamento enquanto a limpeza do MS não for cronometrada e incorporada ao fluxo real.
2. A divergência entre **105,6 L** no lote histórico de separação e **200 L** no volume nominal atual deve permanecer explícita. A v9 registra que as vazões históricas de separação foram observadas em lotes de ~105 L; extrapolar para 200 L indica separação sequencial de 7,6–10,3 h antes de setup e limpeza. Isso é pendência técnica, não detalhe editorial.

### §4.2 Origem dos rendimentos (yields) e convenção de balanço de massa

Os rendimentos do caso-base técnico permanecem: **0,80% GPC/FLG, 5,00% NPG/GNP, 93,00% NG/Nanografite e 1,20% perdas**, sempre relativos à massa inicial de **grafite seco alimentado**, não à formulação líquida, água, NH4OH, surfactante ou massa úmida.

O lote de referência mais próximo é o `20210720Pa`, registrado no `Balanço Global.pptx` com: 0,52% GPC/FLG, 4,85% NPG/GNP, 93,66% nanoplaca (NG) e 0,96% de perdas. O modelo arredonda levemente as frações de valor (GPC 0,52→0,80%, NPG 4,85→5,00%), leitura gerencializada defensável como margem de melhoria pós-recomissionamento.

| Lote | GPC/FLG | NPG/GNP | NG | Perdas |
|---|---:|---:|---:|---:|
| 20210720Pa (referência) | 0,52% | 4,85% | 93,66% | 0,96% |
| 20210729Pa | 0,54% | 5,19% | 79,83% | 14,4% |
| 20210810Pa | 0,45% | 4,08% | 80,44% | 15,0% |
| 20210816Pa | 0,49% | 3,83% | 87,82% | 7,86% |
| **Premissa do modelo** | **0,80%** | **5,00%** | **93,00%** | **1,20%** |

Faixa de variação defensável para sensibilidade: GPC 0,45–0,80%, NPG 3,8–5,2%, NG 80–94%, perdas 1–15%.

**Balanço de massa fechado — base 100 kg de grafite alimentado:**

| Condição | GPC | NPG | Nanografite | Residual físico | Soma |
|---|---:|---:|---:|---:|---:|
| Conservadora | 0,5 kg | 5,0 kg | 93,0 kg | 1,5 kg | 100,0 kg |
| Média histórica v9 | 0,8 kg | 5,0 kg | 93,0 kg | 1,2 kg | 100,0 kg |
| Otimista | 2,0 kg | 16,0 kg | 80,5 kg | 1,5 kg | 100,0 kg |

**Destino físico do residual:** fração de grafite/carbono não recuperada como GPC, NPG ou Nanografite com especificação. Não recebe receita no caso-base.

### §4.3 Origem da capacidade de 43,5 lotes/mês e ramp-up defensável

O valor de 43,5 lotes/mês é extraído da aba `Parâmetros` da planilha P100: Lotes = 10/semana, 1 turno, 5 dias/semana. O anual de 522 resulta de 43,5 × 12 meses.

522 lotes/ano deve ser lido como capacidade nominal do modelo econômico, não como promessa operacional do primeiro ano. Para o primeiro ano pós-recomissionamento, a faixa defensável de ramp-up é **60–80% da capacidade nominal = 313–418 lotes/ano** (base prudente de planejamento: 365–400 lotes). A evolução para 500+ lotes depende de SAT formal, estabilidade de CQ e histórico de campanha reprodutível.

No **Cenário Desenvolvimento**, 43,5 lotes/mês é o teto de infraestrutura para campanhas; não é um regime de produção contínua. No **Cenário Produção**, é a capacidade nominal para o regime de 1 turno dedicado.

### §4.4 Gate de formulações antes dos módulos de conversão

A P100 não deve ser lida apenas como uma sequência física de tanque, cisalhamento e separação. A formulação é o elo que transforma material particulado em solução aplicada. A definição prévia de matriz, dispersante, concentração, rota de incorporação, especificação de desempenho e critério analítico altera como cada lote deve ser preparado, amostrado, qualificado e eventualmente precificado. Por isso, a formulação é tratada como **gate técnico-comercial anterior à conversão**.

O gate de formulações deve organizar a finalidade de cada campanha antes que o grafite entre nos módulos de conversão. Um lote para polímeros, cimento, coatings, agricultura ou EMI não necessariamente exige a mesma distribuição de frações, teor de sólidos, estabilidade coloidal ou pacote analítico.

No **Cenário Desenvolvimento**, cada campanha deve ter ficha técnico-financeira registrada: aplicação-alvo, fração pretendida, forma de entrega, ensaios necessários, custo analítico, hipótese de preço, risco técnico e parceiro potencial.

### §4.5 Premissas e parâmetros de operação por módulo

A planta deve ser compreendida como sequência técnica: gate de formulações → módulos de conversão (paralelo) → módulo de separação. Os parâmetros que governam formulação, conversão e separação são distintos e não intercambiáveis.

**Módulos de conversão:**

| Parâmetro | Valor ou faixa rastreável | Natureza da fonte | Leitura para o relatório | Aplicabilidade por cenário |
|---|---:|---|---|---|
| Volume nominal por módulo | 100 L | Documentado na configuração P100 | Volume nominal do equipamento | Ambos |
| Volume nominal combinado | 200 L/lote | Inferido da operação paralela | Premissa consolidada desde v5 | Ambos |
| Carga de grafite | 20 kg/lote combinado | 10 kg/tanque × 2 tanques, 100 g/L | Corrige v8 que registrava 10 kg combinado | Ambos |
| Concentração operacional | 100 g/L por tanque (100 g/kg) | Lote 20210720Pa | Rota econômica documentada | Ambos |
| Tempo de cisalhamento | 5 h | Documentado no lote de referência | Base econômica da rota 2021 | Ambos |
| Rotação do KonMix | 3.468–3.550 rpm | PIO-MGG-019 + lote 20210720Pa | Parâmetro forte; confirmar por inversor/tacômetro no SAT | Ambos; Produção deve congelar protocolo validado |
| Agitação do tanque | 100–150 rpm | PIO-MGG-019 (rota 50 g/L) | Benchmark interno; confirmar para rota 100 g/L/5 h | Ambos |
| pH de processo | 10,0 | PIO-MGG-019 | Parâmetro de rota; registrar por lote | Ambos |
| Temperatura de processamento | 25–30 °C | PIO-MGG-019 | Controlar por datalogger/enjaquetamento no SAT | Ambos |

**Módulo de separação:**

| Parâmetro | Valor ou faixa rastreável | Natureza da fonte | Leitura para o relatório |
|---|---:|---|---|
| Tempo de 1ª separação no modelo | 2,0 h | Planilha econômica | Parâmetro histórico otimista; requer cronoanálise com 200 L |
| Tempo de 2ª separação no modelo | 1,5 h | Planilha econômica | Parâmetro histórico otimista |
| Limpeza do MS | 2,5 h/lote | Planilha econômica | Documentado; não claramente incorporado ao ciclo de 10,75 h |
| Vazão decanter | 30–50 L/h | Registros de lotes históricos | Parâmetro rastreável; extrapolação para 200 L indica gargalo |
| Vazão centrífuga de discos | 55–65 L/h | Lotes 20210720Pa (~55) e 20210816Pa (~65) | Parâmetro rastreável; testar com 200 L |
| Rotação centrífuga de discos | 3.600 rpm | Lote 20210720Pa | Documentado; RCF não localizado |
| RCF de separação | Não localizado | Pendência técnica | Não converter rpm em RCF sem raio/geometria; validar no SAT |

Quando as vazões históricas são extrapoladas para 200 L: decanter a 30–50 L/h exigiria ~4,0–6,7 h; centrífuga de discos a 55 L/h exigiria ~3,6 h. Em sequência: 7,6–10,3 h antes de setup, transições e limpeza — excede os 3,5 h do modelo. Isso é a principal pendência técnica da P100; não invalida o projeto, mas impõe o SAT como gate antes de tratar 522 lotes/ano como capacidade garantida.

---

## §5. CAPEX: investimento de recomissionamento e base histórica

O CAPEX incremental de recomissionamento da P100 é de **R$ 610.000**, como estimativa gerencial preliminar por pacotes de trabalho. Enquadra-se como **AACE Classe 4/5**, com faixa de acurácia esperada de **−30%/+50%**, portanto intervalo indicativo de **R$ 430.000 a R$ 915.000** até vistoria, RFQs, escopo fechado, laudos/ARTs e critérios de aceite.

A base bruta histórica de equipamentos é outra métrica: **R$ 1.680.560**, composta por R$ 1.615.200 (equipamentos produtivos) + R$ 65.360 (SSMA), extraída da planilha P100/CERES 2021. Não é valor atual de reposição nem valor líquido depreciado.

| Pacote de recomissionamento | Estimativa | Metodologia | Confiança | Validação necessária |
|---|---:|---|---|---|
| Inspeção técnica, calibração e instrumentação | R$ 90.000 | HH técnico + calibração balanças, sensores pH/condutividade/vazão/temperatura/pressão; laudos e lista de pendências | Média-baixa | Inventário de instrumentos, certificados, malhas de controle, proposta de calibração, ART quando aplicável |
| Retrofit mecânico, elétrico e automação essencial | R$ 160.000 | Analogia com recuperação parcial de planta piloto; painéis, inversores, sensores, proteções, aterramento, vedações, bombas, mangotes | Média | Vistoria elétrica/mecânica, sobressalentes, unifilar, P&ID, RFQ de integrador e mecânica industrial |
| Adequações SSMA e intertravamentos mínimos | R$ 85.000 | NR-12/NR-10, emergências, LOTO, sinalização, controle de pós/nanomateriais, rotas e intertravamentos | Média-baixa | Matriz de risco, laudos NR-12/NR-10, inspeção elétrica, emergência, enquadramento de químicos/resíduos |
| Reinstalação, utilidades, conexões e integração | R$ 110.000 | Montagem, reposicionamento, linhas hidráulicas/elétricas, ar, água, resfriamento, drenagem, integração | Média | Layout, pontos de utilidade, lista de conexões, pressões/diâmetros, proposta de montagem |
| Comissionamento frio, quente e teste de performance | R$ 65.000 | HH de equipe técnica, consumíveis, lotes de validação, CQ de aceite, relatório | Média | Protocolo frio/quente/com carga real, critérios de sucesso, plano de amostragem |
| Contingência técnica preliminar | R$ 100.000 | 19,6% sobre subtotal de R$ 510.000 | Adequada ao estágio | Substituir por contingência por risco após vistoria e RFQs; não reduzir antes |
| **Total incremental estimado** | **R$ 610.000** | AACE Classe 4/5 | Planejamento | Orçamento executivo só após RFQ/SAT/SSMA |

**Benchmark de plausibilidade:** R$ 610.000 / R$ 1.680.560 = 36,3%. Teste de sanidade — não é metodologia primária. Não significa reposição de 36% dos ativos; significa que o dinheiro novo está em ordem de grandeza defensável para reativar infraestrutura existente.

---

## §6. OPEX: custo de operação anual

O OPEX consolidado foi construído para refletir uma operação piloto realista. O modelo base preserva a equipe v9 de 8 pessoas e o CQ terceirizado como custos centrais.

| Categoria | Premissa | Custo anual |
|---|---|---:|
| Mão de obra | 8 pessoas, salário médio R$ 10.000/mês, encargos 75% | R$ 1.680.000 |
| Controle de qualidade terceirizado | US$ 5.000/mês, câmbio R$ 5/US$ | R$ 300.000 |
| Matérias-primas e consumíveis de processo | Grafite corrigido para 20 kg/lote | R$ 192.177 |
| Utilidades | Energia, água e utilidades de processo | R$ 83.885 |
| Manutenção | 5% dos equipamentos produtivos + SSMA | R$ 81.510 |
| Secretaria | 1 pessoa a R$ 2.500/mês + encargos | R$ 52.500 |
| Consumíveis de SSMA | Base técnica preservada | R$ 6.836 |
| **OPEX caixa recorrente** | | **R$ 2.396.908** |
| Depreciação gerencial | Reconhecimento econômico do uso da infraestrutura | R$ 166.576 |
| **OPEX técnico completo** | | **R$ 2.563.484** |

### §6.1 Composição da equipe de 8 pessoas

A premissa de 8 pessoas a salário médio bruto de R$ 10.000/mês deve ser lida como **média ponderada gerencial**, não como salário uniforme.

| Função | Papel financeiro-operacional | Observação de custo |
|---|---|---|
| Coordenador de planta / operação piloto | Rotina operacional, prioridades de campanha, indicadores de processo | Puxa a média salarial para cima; faixa ~R$ 15–20 mil |
| Engenheiro ou especialista de processo | Ajuste de processo, troubleshooting, documentação técnica | Pode ser alocado full-time no primeiro ano ou parcialmente |
| Técnico líder de processo | Preparação de lotes, setup de equipamentos, controle operacional | Fundamental para repetibilidade |
| Operador de produção 1 | Operação módulos de conversão e separação | Base do regime de 1 turno |
| Operador de produção 2 | Apoio à operação, limpeza, pesagem, movimentação | Reduz risco de parada por gargalo humano |
| Analista ou técnico de CQ interno | Amostragem, cadeia de custódia, interface com laboratório externo | Mesmo com CQ terceirizado, alguém interno controla amostras e prazo de laudo |
| Técnico de manutenção, utilidades e SSMA operacional | Preventiva simples, LOTO, inspeções de utilidades | Se manutenção 100% terceirizada, redistribuir função |
| Pesquisador de desenvolvimento de aplicações e fomento | Formulações, parceiros, propostas CDTN/UFMG, editais de fomento | +R$ 210.000/ano; conecta operação, validação aplicada e captação não dilutiva |

O salário médio de R$ 10.000/mês é conservador para coordenador sênior + especialista de processo + pesquisador de aplicações, e elevado se a equipe for composta majoritariamente por operadores juniores. Os encargos de 75% são defensáveis por referência SINAPI 2025 (~71,29%) com margem para benefícios práticos (VT, VA, plano de saúde, seguro de vida, PPR).

No **Cenário Produção**, a equipe fixa é distinta: **1 supervisor + 3 técnicos de produção + 1 técnico de CQ** (5 pessoas). Não somar com a equipe v9 do Desenvolvimento.

### §6.2 Escopo do controle de qualidade terceirizado

A premissa de US$ 5.000/mês (R$ 25.000/mês ao câmbio R$ 5/US$) é o envelope gerencial para contrato recorrente de caracterização de materiais com análises limitadas e relatório técnico. O escopo típico inclui:

| Técnica ou atividade | Uso operacional | Frequência plausível |
|---|---|---|
| Espectroscopia Raman | Confirmação de GPC/NPG/NG, número de camadas, defeitos | Por campanha ou a cada N lotes |
| Microscopia AFM/MEV | Morfologia, tamanho de plaqueta, contaminações | Seletiva por campanha ou especificação |
| TG/TGA | Pureza, resíduos inorgânicos, conteúdo de carbono | Por especificação de produto |
| Granulometria (DLS/laser) | Distribuição de tamanho das frações | Por campanha; pode ser internalizado com equipamento simples |
| Análises wet-chemistry | pH, condutividade, teor de sólidos, estabilidade de dispersão | Pode ser internalizado |
| Cadeia de custódia e relatório | Rastreabilidade amostral e evidência técnica auditável | Por lote/campanha conforme contrato |

No **Cenário Desenvolvimento**, CQ é principalmente de caracterização por campanha e aplicação (intensidade variável). No **Cenário Produção**, CQ vira rotina por especificação/lote com frequência fixa.

### §6.3 Base de matérias-primas e consumíveis

| Insumo | Base de cálculo | Custo anual | Observação |
|---|---|---:|---|
| Grafite natural em pó | 20 kg/lote × 522 lotes × R$ ~14,07/kg | Parte de R$ 192.177 | Corrigido de 10 para 20 kg/lote na v9; cotação ±30% de incerteza |
| Triton X-100 (surfactante) | Concentração 0,1% na formulação | Parte de R$ 192.177 | Reagente de processo |
| NH4OH (ajuste de pH) | Consumo por lote | Parte de R$ 192.177 | pH-alvo 10,0 |
| Água tratada | Por ciclo de lote | Parte de R$ 192.177 | Utilidade de processo |
| Embalagens e materiais de acondicionamento | Por lote qualificado | Parte de R$ 192.177 | Varia por forma de entrega |
| **Total matérias-primas e consumíveis** | | **R$ 192.177/ano** | Faixa de incerteza ±30% até cotações vigentes |

### §6.4 Base de utilidades

| Utilidade | Base de estimativa | Custo anual | Observação |
|---|---|---:|---|
| Energia elétrica | Potência instalada × tempo × tarifa CEMIG histórica ~R$ 0,857/kWh; KonMix 3,2 kW × 5 h/lote × 522 lotes/ano | Principal componente | Medir potência real em campo |
| Água tratada | Processo e limpeza | Componente menor | Mapear consumo no SAT |
| Ar comprimido | Instrumentação e equipamentos | Se aplicável | Validar se há compressor |
| Resfriamento / chiller | Friotec TFQF 09: 3,8 kW × 2,5 h/lote | Parte do total elétrico | |
| **Total utilidades** | Tarifa histórica CEMIG | **R$ 83.885/ano** | Faixa recomendada até medição: R$ 65–110 mil/ano |

### §6.5 Base da manutenção anual

A taxa de manutenção de **5% da base produtiva + SSMA** (R$ 81.510/ano) é adequada para o estágio de planejamento. Para recomissionamento de planta parada por anos, a taxa real pode ser superior nos dois primeiros anos (5–8%), normalizando após estabilização. Separar preventiva (rotina) de corretiva (incidentes) é crítico para gestão; a taxa atual mistura os dois sem discriminação.

### §6.6 Exclusões e capital de giro

| Item | Tratamento | Valor de referência |
|---|---|---|
| Capital de giro inicial | Exclusão explícita do modelo OPEX/CAPEX | Provisionar separadamente: R$ 400–599 mil para 2–3 meses de OPEX caixa mensal médio ~R$ 199.742/mês |
| Aluguel / ocupação | Excluído no primeiro ciclo (uso/locação operacional sem aluguel) | Se mudar, atualizar OPEX |
| Impostos comerciais, margem e inadimplência | Excluídos do modelo de custo | Incluir no plano de negócios |
| Ponto de equilíbrio operacional pleno | Não fecha sem preço validado, mix comercial e impostos | Declarado como limitação; não forçar número frágil |

| Indicador derivado | Valor |
|---|---:|
| Custo caixa por lote | R$ 4.592 |
| Custo técnico completo por lote | R$ 4.912 |
| Custo caixa por kg (base v9) | R$ 232 |
| Custo técnico completo por kg (base v9) | R$ 249 |
| OPEX caixa mensal de referência | R$ 199.742 |

---

## §7. Referências externas de preço e cobertura econômica

### §7.1 Faixa US$ 50–200/kg para NPG/GNP técnico

A faixa de **US$ 50–200/kg** (câmbio R$ 5,00) para NPG/GNP técnico é restaurada como a régua de mercado defensável para fins de benchmarking econômico e apresentação a investidores. Não é promessa de preço de venda.

Confirmação de cobertura econômica: na P100 com produção de **10.315 kg/ano**, a receita no piso de **US$ 50/kg** gera **R$ 2.578.750/ano**, cobrindo **~101% do OPEX Técnico Completo** de R$ 2.563.484/ano, antes de impostos, mix comercial e preço validado. Essa cobertura mínima só é possível com a carga correta de **20 kg/lote** — na v8 e versões anteriores com 10 kg/lote combinado, a cobertura ficava em ~52%.

**Evolução histórica da cobertura no piso US$ 50/kg (base: OPEX Técnico Completo v9 — R$ 2.563.484/ano):**
- v8 (10 kg/lote combinado): ~52% do OPEX técnico completo
- v9+ (20 kg/lote correto): **~101%** do OPEX Técnico Completo v9 — cruza a linha de equilíbrio econômico

A mesma receita de R$ 2.578.750/ano cobre **~104% do OPEX Produção v10** (R$ 2.481.000/ano — Cenário Produção com equipe enxuta de 5 pessoas e indiretos de mercado, sem depreciação gerencial). Os dois percentuais são denominadores distintos e complementares: ~101% reflete o custo técnico completo incluindo depreciação da v9; ~104% reflete o custo caixa operacional do Cenário Produção dedicado com pool de equipe distinto. Ver reconciliação em §10.

### §7.2 Benchmark de indiretos de mercado (Cenário Produção como EPP independente)

Esta seção fundamenta os custos indiretos e as referências de preço de mercado para a P100 no Cenário Produção operando como EPP (Empresa de Pequeno Porte) independente.

| Categoria | Mínimo (mês) | Médio (recom.) | Máximo (mês) | Fonte / Benchmark |
|---|---:|---:|---:|---|
| Adm. Geral & Apoio (1 Ger. + 1 Assis., TI/ERP) | R$ 18.200 | **R$ 32.800** | R$ 54.000 | C2 — salários + TI/sistemas/ERP SaaS + despesas gerais |
| Seguros (Patrimonial, Ambiental, RC) | R$ 1.500 | **R$ 3.500** | R$ 7.000 | Consultorias de seguros ambientais 2026; base anual R$ 18–84k |
| Jurídico & Compliance | R$ 1.500 | **R$ 2.500** | R$ 4.500 | Retainer para contratos e compliance ambiental/trabalhista |
| RH, Benefícios & NRs | R$ 8.500 | **R$ 12.500** | R$ 18.500 | VR/VT/Saúde p/ 7 pessoas + Treinamentos NRs Mandatórias |
| Contabilidade & Fiscal | R$ 1.800 | **R$ 3.000** | R$ 5.500 | Outsourcing Fenacon 2025 (Lucro Presumido/Real) |
| Segurança & Manutenção Adm. | R$ 1.800 | **R$ 3.600** | R$ 8.000 | Monitoramento 24h + Limpeza/Conservação Predial |
| Utilidades Indiretas | R$ 700 | **R$ 1.500** | R$ 2.500 | Energia/Água/Internet área administrativa |
| **TOTAL MENSAL** | **R$ 34.000** | **R$ 59.400** | **R$ 100.000** | ~28,7% do OPEX mensal total no Caso-Base |
| **TOTAL ANUAL** | **R$ 408.000** | **R$ 712.800** | **R$ 1.200.000** | Benchmark saudável: 10–18% do faturamento projetado |

**Distinção fundamental:**
- **Benchmark externo (auditável):** Contabilidade, Seguros, Jurídico e Utilidades Indiretas derivam de tabelas de associações (Fenacon), consultorias e tarifas públicas. São custos "impostos" pelo mercado.
- **Premissa interna (editorial):** A decisão de ter equipe de apoio de 2 pessoas (Gerente + Assistente) e seus salários é premissa de projeto da ALTOE. No Cenário Desenvolvimento, esse indireto é R$ 28k/mês (suporte compartilhado/alocado, aproveitando infraestrutura institucional). No Cenário Produção, assume-se independência total (EPP), elevando o custo mas aumentando a credibilidade para o investidor (planta autossustentável).

**Fontes consultáveis (Vault: `Sources/`):**

| Fonte | Tipo | Data | Conteúdo |
|---|---|:---:|---|
| NanoXplore Presentation | Relatório | Jun/2020 | Benchmark industrial de escala e faixa US$ 50–200/kg |
| Graphene-Info (Market) | Dashboard | 2025/2026 | Monitoramento de tendências e preços reportados de pó |
| Fenacon/Sescap | Estudo | 2025 | Honorários contábeis para empresas Lucro Real/Presumido |
| SEBRAE / CNI | Relatório | 2025 | Custos regulatórios e administrativos para EPP Industrial |
| Cheap Tubes / USA Graphene | Catálogo | Maio/2026 | Referências comerciais vigentes para NPG/GNP |
| Consultorias Seguros | Dashboard | 2026 | Tendências de prêmio para risco ambiental/químico |

---

## §8. Cenário (1) — P100 Desenvolvimento

### §8.1 Premissas técnicas

A P100 opera como **planta piloto de desenvolvimento tecnológico**, suporte a aplicações finais, melhoria de processos de produção de grafeno e produção sob encomenda para parceiros (lotes à la carte). Operação por campanhas, não por ocupação contínua. A ociosidade planejada faz parte do custo de P&D.

| Bloco | Premissa |
|---|---|
| Regime | Operação por campanhas com ociosidade planejada; não modelar como fábrica plena |
| Mix | Desenvolvimento próprio, suporte a aplicações, caracterização/formulação e lotes sob encomenda |
| Equipe técnica | 8 pessoas (estrutura v9): coordenação, especialista, técnico líder, 2 operadores, CQ interno, manutenção/SSMA, pesquisador de aplicações/fomento |
| CQ | Caracterização por campanha e aplicação (Raman, granulometria, teor de sólidos, morfologia, estabilidade/funcionalidade); variável e menos repetitivo que Produção |
| Lotes à la carte | Variabilidade deliberada de processo; custo marginal inclui preparação, formulação, setup, retrabalho analítico, amostras e documentação técnica. **Não precificar só por kg** |
| Risco técnico | Separação de 200 L e ciclo real ainda são incertezas de escala |

### §8.2 Estrutura de custos (caso-base 12 campanhas/ano)

| Bloco | Natureza | Custo anual | % do total |
|---|---|---:|---:|
| Equipe técnica D1 carregada 2026 — 8 pessoas (¹) | Direto fixo | R$ 2.138.400 | 52,2% |
| CQ externo mínimo e caracterização | Direto fixo | R$ 300.000 | 7,3% |
| Consumíveis fixos de laboratório/aplicações | Direto fixo | R$ 120.000 | 2,9% |
| Manutenção técnica de prontidão | Direto fixo | R$ 240.000 | 5,9% |
| Campanhas de desenvolvimento e à la carte | Direto variável | R$ 960.000 | 23,4% |
| Overhead institucional alocado ao piloto | Indireto fixo | R$ 180.000 | 4,4% |
| SSMA, licenças operacionais e suporte comum | Indireto fixo | R$ 96.000 | 2,3% |
| Administração, TI e apoio compartilhado | Indireto fixo | R$ 60.000 | 1,5% |
| **Total** | | **R$ 4.094.400** | **100,0%** |

Decomposição base: 91,8% direto / 8,2% indireto; 76,6% fixo / 23,4% variável.

> **(¹) Reconciliação com premissa v9:** o §6 e §12 preservam a premissa v9 de equipe com salário médio bruto de R$ 10.000/mês e encargos 75% = R$ 1.680.000/ano. O D1 carregado 2026 usa salário médio bruto de R$ 12.728/mês (mesmos 8 papéis, ajuste salarial 2026 estimado em ~27%), resultando em R$ 2.138.400/ano. As duas premissas são compatíveis: a v9 é a base de referência histórica; D1 carregado é a projeção de capacidade técnica para o ano de operação. Não são premissas concorrentes — são horizontes temporais diferentes.*

### §8.3 Modelo por campanha e lote à la carte

Custo variável por campanha base (5 lotes): **R$ 80.000**, composto por insumos produtivos (R$ 17,5k), utilidades (R$ 4,5k), CQ externo incremental e ensaios de aplicação (R$ 35k), manutenção corretiva leve (R$ 7,5k) e setup/formulação/documentação (R$ 15,5k).

Custo marginal de lote à la carte adicional dentro de campanha aberta: **R$ 18.000/lote** (insumos R$ 3,5k, utilidades R$ 0,9k, CQ incremental R$ 4,5k, MO incremental R$ 3k, limpeza/setup/retrabalho R$ 5k, resíduo R$ 1,1k).

**Regra de uso comercial:** proposta à la carte deve separar três camadas: (i) taxa de abertura de campanha (setup/CQ/documentação); (ii) custo marginal por lote adicional; (iii) prêmio técnico por especificação, urgência, confidencialidade, retrabalho ou propriedade intelectual.

### §8.4 Leitura econômica e sensibilidade por cadência

A métrica relevante para Desenvolvimento **não é R$/kg nem OPEX/522 lotes**. A P100 piloto carrega estrutura fixa de capacidade técnica de ~R$ 3,13 MM/ano; as campanhas apenas absorvem essa capacidade.

| Cadência | OPEX anual | OPEX mensal | Lotes/ano | Uso vs. nominal | Variável anual implícita |
|---|---:|---:|---:|---:|---:|
| Conservador — 8 campanhas (~4 lotes/campanha) | R$ 3.654.400 | R$ 304.500 | 32 | 6,1% | R$ 520.000 |
| Base — 12 campanhas (5 lotes/campanha) | R$ 4.094.400 | R$ 341.200 | 60 | 11,5% | R$ 960.000 |
| Intensivo — 18 campanhas (~6 lotes/campanha + à la carte) | R$ 4.844.400 | R$ 403.700 | 108 | 20,7% | R$ 1.710.000 |

Risco econômico relevante: **subutilização da capacidade técnica**. Poucos lotes não reduzem a maior parte do OPEX; apenas reduzem a absorção do custo fixo.

---

### §8.5 Sub-cenário D1.b — 3 Lotes Testes/Semana (Módulo Único, 100L)

Este sub-cenário modela a P100 em regime de **testes contínuos semanais**: 3 lotes por semana, cada lote usando um único módulo de conversão (100 L nominal, 10 kg de grafite por lote), sem a estrutura de campanhas formais do D1 caso-base. Briefing: [ALT-487](mention://issue/6760ed5e-5d9b-4b1b-9c5e-e448f3b85377), 2026-05-31.

A qualificação "100 litros" descreve o uso de um único módulo KonMix (100 L nominal), diferenciando-o do lote padrão de 200 L (dois módulos em paralelo) que fundamenta o D1 base e o D2.

#### §8.5.1 Parâmetros técnicos e produção anual

| Parâmetro | D1.b — 3 testes/semana (100L) | D1 base — 12 campanhas (200L) | Observação |
|---|---|---|---|
| Lotes por semana | 3 | ~1,15 | 2,6× mais lotes/semana |
| Volume por lote | 100 L (1 módulo) | 200 L (2 módulos paralelos) | 2º módulo disponível para prep paralela |
| Grafite por lote | 10 kg | 20 kg | Concentração 100 g/L mantida por módulo |
| Lotes por ano | **156** | 60 | 29,9% da capacidade nominal (522 lotes/ano) |
| Volume total anual | 15.600 L | 12.000 L | 30% mais volume que D1 base |
| Grafite anual | **1.560 kg** | 1.200 kg | 30% a mais em carga de processo |
| Uso capacidade nominal | 29,9% | 11,5% | 2,6× mais uso da infraestrutura |
| Ciclo por lote 100L | ~8,75–9,25 h | ~10,75–13,25 h (200L) | Separação 100L mais rápida (~1,5–2,0 h vs ~3,5 h nominal 200L) |
| Regime de trabalho | 3 dias/semana (~27 h planta/semana) | Por campanha (~2–3 dias/campanha) | Operação cadenciada, sustentável sem hora extra |

**Produção técnica anual (yields caso-base §4.2):**

| Fração | % rendimento | kg/lote (10 kg grafite) | kg/ano (156 lotes) | Comparativo D1 base |
|---|---:|---:|---:|---:|
| GPC/FLG | 0,80% | 0,080 | **12,5** | 9,6 kg |
| NPG/GNP | 5,00% | 0,500 | **78,0** | 60,0 kg |
| Nanografite | 93,00% | 9,300 | **1.450,8** | 1.116,0 kg |
| Residual | 1,20% | 0,120 | 18,7 | 14,4 kg |
| **Total** | **100%** | **10,000** | **1.560,0** | **1.200,0 kg** |

O D1.b produz **30% mais material** que o D1 base por processar mais lotes (156 vs 60), apesar do volume menor por lote. O segundo módulo KonMix permanece ocioso durante a operação D1.b — pode ser dedicado a prep de formulações, testes paralelos de reagentes ou atividades de desenvolvimento de aplicação.

#### §8.5.2 Estrutura de custos variáveis por lote 100L

Os custos fixos do D1 caso-base (R$ 3.134.400/ano) permanecem integralmente. Os custos variáveis são recalculados para lotes de 100L em regime de testes contínuos, referenciados nos componentes do §8.3.

| Item variável | R$/lote (100L, D1.b) | Base de cálculo | Comparativo lote 200L §8.3 |
|---|---:|---|---:|
| Insumos (grafite 10 kg + Triton X-100, NH4OH, água, embalagem) | R$ 1.750 | 50% do lote 200L R$ 3.500 — volume e carga proporcionais | R$ 3.500 |
| Utilidades (1 KonMix 5h + separação 100L ~1,75h) | R$ 450 | 50% do lote 200L R$ 900 — 1 cisalhador + separação mais curta | R$ 900 |
| CQ incremental por lote teste (Raman + gravimetria) | R$ 2.500 | Raman externo (R$ 500–800/análise) + gravimetria interna; a cada lote-teste com objetivo técnico definido | R$ 4.500 |
| MO incremental de operação | R$ 1.800 | 60% do lote 200L R$ 3.000 — 1 módulo, ciclo mais curto | R$ 3.000 |
| Limpeza, setup e documentação por lote | R$ 2.500 | 50% do lote 200L R$ 5.000 — 1 módulo, limpeza mais rápida | R$ 5.000 |
| Resíduo e descarte | R$ 550 | 50% do lote 200L R$ 1.100 — metade da massa de processo | R$ 1.100 |
| **Total variável por lote 100L (caso-base)** | **R$ 9.550** | | **R$ 18.000** |

> **Nota sobre CQ do D1.b:** O CQ de R$ 2.500/lote-teste é adequado para testes com objetivo técnico por lote — Raman para confirmar GPC/NPG, gravimetria de yield, análise de dispersão quando relevante. É inferior ao CQ de campanha D1 base (R$ 7.000/lote médio para campanhas de desenvolvimento de aplicação com Raman, AFM, TGA e ensaios de cliente). Se o D1.b for usado exclusivamente como monitoramento de processo sem caracterização por lote, o CQ cai para R$ 700–800/lote (Raman bimestral + gravimetria interna). Ver sensibilidade §8.5.4.

#### §8.5.3 OPEX total D1.b

| Bloco | Natureza | Custo anual | % do total |
|---|---|---:|---:|
| Custos fixos — idênticos ao D1 caso-base (§8.2) | Fixo | R$ 3.134.400 | 67,8% |
| Insumos (156 lotes × R$ 1.750) | Direto variável | R$ 273.000 | 5,9% |
| Utilidades (156 lotes × R$ 450) | Direto variável | R$ 70.200 | 1,5% |
| CQ incremental (156 lotes × R$ 2.500) | Direto variável | R$ 390.000 | 8,4% |
| MO incremental (156 lotes × R$ 1.800) | Direto variável | R$ 280.800 | 6,1% |
| Limpeza, setup e documentação (156 lotes × R$ 2.500) | Direto variável | R$ 390.000 | 8,4% |
| Resíduo (156 lotes × R$ 550) | Direto variável | R$ 85.800 | 1,9% |
| **Total variável** | | **R$ 1.489.800** | **32,2%** |
| **OPEX total D1.b caso-base** | | **R$ 4.624.200** | **100,0%** |

Decomposição: 90,4% direto / 9,6% indireto; 67,8% fixo / 32,2% variável.

#### §8.5.4 Comparação com D1 base e sensibilidade de CQ

**Comparação do D1.b com os demais cenários D1:**

| Cenário | Lotes/ano | Vol/lote | OPEX anual | OPEX/lote | OPEX/kg grafite | Grafite/ano |
|---|---:|---|---:|---:|---:|---:|
| D1 conservador (8 campanhas × ~4 lotes, 200L) | 32 | 200 L | R$ 3.654.400 | R$ 114.200 | R$ 4.568 | 640 kg |
| D1 base (12 campanhas × 5 lotes, 200L) | 60 | 200 L | R$ 4.094.400 | R$ 68.240 | R$ 3.412 | 1.200 kg |
| **D1.b — 3 testes/semana (100L, este sub-cenário)** | **156** | **100 L** | **R$ 4.624.200** | **R$ 29.642** | **R$ 2.964** | **1.560 kg** |
| D1 intensivo (18 campanhas + à la carte, 200L) | 108 | 200 L | R$ 4.844.400 | R$ 44.856 | R$ 2.243 | 2.160 kg |

O D1.b tem o **menor custo por lote** (R$ 29.642 — melhor diluição do fixo sobre 156 lotes), o **maior número de lotes por ano** e o **maior volume de grafite processado** entre os cenários D1, mas o **maior custo anual** do grupo D1. O custo por kg de grafite processado (R$ 2.964) é levemente superior ao D1 intensivo, mas inferior ao D1 base e conservador.

**Sensibilidade por intensidade de CQ:**

| Premissa CQ/lote | Custo variável total | OPEX total | Leitura operacional |
|---|---:|---:|---|
| Básico — gravimetria interna + Raman bimestral (R$ 800/lote) | R$ 1.021.800 | **R$ 4.156.200** | Monitoramento de processo sem caracterização por lote |
| **Moderado — Raman + gravimetria por lote (R$ 2.500/lote)** | **R$ 1.489.800** | **R$ 4.624.200** | Testes com objetivo técnico por lote (caso-base) |
| Intensivo — caracterização completa por lote-teste (R$ 4.500/lote) | R$ 1.927.800 | **R$ 5.062.200** | Desenvolvimento de aplicação por lote, equivalente a D1 campanha |

**Faixa D1.b: R$ 4.156.000–5.062.000/ano** dependendo da intensidade analítica por lote-teste.

#### §8.5.5 Métricas e leitura econômica

| Indicador | D1.b (3 testes/semana, 100L) | D1 base (12 campanhas, 200L) |
|---|---:|---:|
| OPEX total anual | **R$ 4.624.200** | R$ 4.094.400 |
| Incremento vs D1 base | **+R$ 529.800 (+13%)** | — |
| Lotes por ano | 156 | 60 |
| Grafite processado | 1.560 kg | 1.200 kg |
| GPC produzido | 12,5 kg | 9,6 kg |
| NPG produzido | 78,0 kg | 60,0 kg |
| Nanografite produzida | 1.450,8 kg | 1.116,0 kg |
| Custo por lote (amortizado) | R$ 29.642 | R$ 68.240 |
| Custo por kg grafite | R$ 2.964 | R$ 3.412 |
| Custo por litro processado | R$ 296 | R$ 341 |
| Uso da capacidade nominal (522 lotes/ano) | 29,9% | 11,5% |
| OPEX mensal de referência | R$ 385.350 | R$ 341.200 |

**Pontos de atenção específicos do D1.b:**

1. **Segundo módulo ocioso:** Durante os 3 lotes/semana de 100L, o segundo KonMix fica disponível. Isso é um recurso — pode ser usado para prep de formulações distintas, testes de condições diferentes de pH ou concentração, ou lotes de outra aplicação em paralelo, sem aumentar o OPEX.

2. **Capacidade de separação favorável:** 100L é metade do volume que impõe o gargalo de separação documentado em §4.5 e §4.3 (7,6–10,3h para 200L). Para 100L, as estimativas de separação caem para ~1,5–3,3h, tornando o ciclo de 100L mais confiável que o de 200L.

3. **Custo por campanha-equivalente:** Se as 3 sessões semanais forem agrupadas em ciclos mensais (13 lotes/mês), o custo por mês de operação é R$ 385.350 — maior que o D1 base (R$ 341.200/mês) mas com 2,6× mais lotes/mês e 30% mais material processado.

4. **Produção superior em volume absoluto:** O D1.b produz mais GPC (12,5 vs 9,6 kg/ano), mais NPG (78,0 vs 60,0 kg/ano) e mais Nanografite (1.450,8 vs 1.116,0 kg/ano) que o D1 base. Para fins de geração de amostras para parceiros UFMG/CDTN ou para qualificação comercial, isso é vantajoso.

5. **Risco econômico:** Igual ao D1 base — a maior parte do OPEX (67,8%) é fixo e não cai com redução de lotes. Se por qualquer motivo a cadência cair de 3 para 1 lote/semana, o OPEX cai apenas ~22% (de R$ 4.624.200 para ~R$ 3.621.400).

> **Conexão com outros cenários e seções:** para comparar com o Cenário Produção (custo por kg de produto em regime dedicado), ver §9. Para reconciliação dos dois cenários com a base v9, ver §10. Para benchmark de preço e cobertura econômica, ver §7.

---

## §9. Cenário (2) — P100 Produção

### §9.1 Premissas técnicas

A P100 opera como **operação dedicada de produção em 1 turno**, com a mesma base física da v9 e três condições de rendimento aplicadas sobre o mesmo OPEX.

| Bloco | Premissa |
|---|---|
| Regime | 1 turno, produção dedicada; capacidade nominal 522 lotes/ano como teto, não caso único |
| Equipe fixa | 1 supervisor + 3 técnicos de produção + 1 técnico de CQ (substitui equipe v9 de 8) |
| Mix de produto | GPC, NPG e Nanografite como frações produtivas; residual como perda/resíduo |
| CQ | Controle rotineiro por especificação/lote; técnico CQ fixo + ensaios externos por frequência |
| Manutenção | Preventiva/corretiva; faixa 3–5% estabilizada ou 5–8% se estado da planta exigir |

### §9.2 Estrutura mensal de custos (caso-base, faixa média de indiretos)

| Bloco | R$/mês |
|---|---:|
| Equipe fixa de produção (²) | 59.400 |
| Insumos de produção (³) | 30.950 |
| Utilidades produtivas | 8.000 |
| Manutenção preventiva/corretiva | 18.000 |
| CQ externo rotineiro | 25.000 |
| Consumíveis de CQ | 4.000 |
| Resíduo/reprocesso | 2.000 |
| Indiretos empresariais médios (benchmark C2 — ver §7.2) | 59.400 |
| **Total mensal caso-base** | **206.750** |
| **Total anual caso-base** | **2.481.000** |

Decomposição: 71,3% direto / 28,7% indireto; 86,1% fixo / 13,9% variável.

> **(²) Derivação da equipe D2:** 5 pessoas (1 supervisor + 3 técnicos de produção + 1 técnico de CQ), salário médio bruto estimado ~R$ 6.800–7.000/mês por pessoa e encargos efetivos ~78–80% (SINAPI 2025 + VT, VA, plano de saúde) → total ~R$ 59.400/mês. Perfil de equipe enxuta de produção, distinto da equipe D1 com 8 pessoas a salário médio R$ 12.728/mês 2026-ajustado (ver §8.2 nota ¹). Não somar as duas equipes.*

> **(³) Insumos de produção D2 vs matérias-primas v9:** o valor de R$ 30.950/mês (R$ 371.400/ano) é superior ao item correspondente da v9 (R$ 192.177/ano = R$ 16.015/mês). A diferença reflete as exigências adicionais do Cenário Produção dedicado em relação ao modelo v9: embalagens específicas por produto (GPC, NPG e Nanografite exigem acondicionamento e rotulagem separados), reagentes de limpeza entre bateladas de produtos distintos, materiais de amostragem por lote para CQ de liberação, e consumíveis de processo com especificação de produção. A faixa de incerteza de ±30% aplicada às matérias-primas da v9 (§6.3) é igualmente válida aqui até cotações formais.*

### §9.3 Custo unitário por produto — três condições

Base de cálculo: 870 kg de grafite seco alimentado por mês (43,5 lotes × 20 kg). Critério de alocação: **massa ponderada por complexidade técnica** com pesos GPC = 4, NPG = 2, Nanografite = 1. Justificativa: custo por massa pura subaloca GPC/NPG porque as frações nobres concentram esforço de separação, CQ e especificação; alocação por receita exigiria preço de venda ainda não validado.

| Condição | GPC kg/mês | NPG kg/mês | Nanografite kg/mês | Residual kg/mês | GPC R$/kg | NPG R$/kg | Nanografite R$/kg |
|---|---:|---:|---:|---:|---:|---:|---:|
| Conservadora 0,5/5/93/1,5 | 4,35 | 43,50 | 809,10 | 13,05 | **R$ 905** | **R$ 453** | **R$ 226** |
| Média histórica v9 0,8/5,0/93,0/1,2 | 6,96 | 43,50 | 809,10 | 10,44 | **R$ 895** | **R$ 448** | **R$ 224** |
| Otimista 2/16/80,5/1,5 | 17,40 | 139,20 | 700,35 | 13,05 | **R$ 789** | **R$ 394** | **R$ 197** |

O OPEX total não muda entre as condições — o que muda é a massa produzida por produto e, portanto, o custo unitário.

### §9.4 Leitura econômica

Sensibilidade de indiretos (mercado): R$ 2,18–2,97 MM/ano. Ponto de equilíbrio operacional pleno não fecha sem preço de venda validado, mix comercial por produto e impostos.

> **Conexão com outros cenários e seções:** para comparar com o Cenário Desenvolvimento (custo por campanha e capacidade técnica), ver §8. Para reconciliação dos dois cenários com a base v9, ver §10. Para benchmark de preço e cobertura econômica do piso US$ 50/kg sobre o OPEX D2, ver §7.1.

---

## §10. Reconciliação custo/kg v9↔v10

A diferença entre v9 R$ 249/kg e v10 Produção R$ 895/R$ 448/R$ 224 não é contradição — é mudança de pool e método de alocação.

| Dimensão | v9 (referência histórica) | v10 Produção (Cenário D2) |
|---|---|---|
| Equipe | 8 pessoas (equipe técnica completa) | 5 pessoas (equipe enxuta de produção) |
| OPEX caixa | R$ 2.396.908/ano (sem depreciação) | R$ 2.481.000/ano (caso-base, inclui indiretos de mercado) |
| OPEX técnico completo | R$ 2.563.484/ano (caixa + depreciação R$ 166.576) | — (depreciação não incluída no caso-base D2) |
| Residual D2 vs v9 caixa | — | +R$ 84.092/ano (D2 é *mais caro* que v9 caixa; equipe menor mas indiretos empresariais adicionados) |
| Residual D2 vs v9 técnico completo | — | −R$ 82.484/ano (D2 é *mais barato* que v9 com depreciação; mudança de pool compensa) |
| Custo médio ponderado | R$ 249/kg (OPEX técnico completo / 10.315 kg) | R$ 241/kg físico (OPEX D2 / 10.315 kg — média sem alocação por produto) |
| Produto individual | Custo médio unificado (não desagregado por produto) | GPC R$ 895, NPG R$ 448, Nanografite R$ 224 (alocação 4:2:1 por complexidade técnica — ver §9.3) |

**Nota de leitura crítica:** o D2 caso-base (R$ 2.481.000/ano) é levemente *mais caro* que o v9 OPEX caixa (R$ 2.396.908/ano), não mais barato. A equipe menor (5 vs 8 pessoas) gera economia de ~R$ 967.200/ano, mas os indiretos empresariais de mercado adicionados (R$ 712.800/ano — benchmark §7.2) e a maior estrutura de insumos de produção e manutenção absorvem parte dessa economia. O D2 é mais barato apenas quando comparado ao v9 OPEX *técnico completo* (que inclui R$ 166.576/ano de depreciação gerencial não presente no D2 caso-base).

**Leitura para o investidor:** as duas leituras coexistem e respondem a perguntas diferentes. v9 R$ 249/kg é o custo técnico completo médio — base de planejamento e cobertura econômica histórica. v10 Produção R$ 895/R$ 448/R$ 224 é o custo por produto em regime dedicado com equipe enxuta e indiretos de mercado de EPP. Comparar diretamente os dois sem declarar a diferença de pool e método de alocação gera equívoco analítico.

**Leitura para pesquisadores:** a alocação 4:2:1 (GPC:NPG:Nanografite) não é divisão por massa — é ponderação por esforço técnico relativo. GPC concentra maior CQ analítico, maior separação e maior especificação; Nanografite concentra maior volume físico mas menor valor técnico unitário. O custo unitário por produto só faz sentido no Cenário Produção dedicado; no Cenário Desenvolvimento o custo por campanha (R$ 80.000 base de 5 lotes — ver §8.3) é a métrica correta.

---

## §11. Riscos, controles e gates SSMA

**Até a conclusão desses gates, a P100 deve ser descrita como infraestrutura piloto com potencial de recomissionamento, e não como unidade liberada para operação segura, repetível ou comercial.**

### §11.1 Gates universais — aplicáveis a qualquer uso da P100

| Gate | Descrição | Fundamento legal/normativo | Aplicabilidade | Responsável | Status atual |
|---|---|---|---|---|---|
| Vistoria física da planta e dos ativos P100 | Inspecionar estado real dos módulos KonMix, tanques, separação, utilidades, painéis, instrumentos, proteções, itens fora de serviço e lacunas de recomissionamento. Relatório fotográfico e lista de não conformidades. | Boa prática de recomissionamento; base para RFQ e SAT | Ambos | Engenharia/Operações + SSMA | Pendente. Gate obrigatório antes de orçamento executivo |
| Conformidade de máquinas, proteções e intertravamentos | Verificar proteções físicas, zonas de risco, emergência, parada, intertravamentos, acesso a partes móveis, procedimentos e documentação mínima de segurança. | NR-12; ABNT aplicável quando especificada | Ambos | Engenharia + SSMA + prestador habilitado | Pendente |
| Inspeção elétrica, aterramento, automação e LOTO | Validar painéis, aterramento, proteção elétrica, inversores, sensores, automação, bloqueio/etiquetagem, prontuário/diagramas e condições para manutenção segura. | NR-10; NR-12 para interface máquina/comando | Ambos | Engenharia elétrica + SSMA | Pendente. Deve entrar no escopo de RFQ/SAT |
| Enquadramento de vasos, tanques, linhas pressurizadas | Confirmar se há vasos de pressão, linhas pressurizadas, ar comprimido, tanques metálicos enquadráveis; registrar dispensa quando não aplicável. | NR-13 quando aplicável | Ambos | Engenharia mecânica + responsável técnico | Pendente. Aplicabilidade deve ser formalmente verificada |
| Validação de utilidades e integração | Confirmar água, energia, ar comprimido, exaustão/ventilação, drenagem, resfriamento, efluentes, potência instalada e interfaces com a planta. | NR-10 para energia; requisitos ambientais conforme processo real | Ambos | Engenharia + Utilidades + SSMA | Pendente. Alimenta OPEX de utilidades e SAT |
| Atualização de PGR/GRO e matriz de riscos | Atualizar inventário de riscos por tarefa, máquina, agente químico/físico e regime; medidas de controle, EPIs/EPCs, treinamento, permissões de trabalho. | NR-1 (GRO/PGR); NR-9 para exposições ocupacionais | Ambos | SSMA | Pendente. Gate documental antes de qualquer operação assistida |
| Controles de exposição ocupacional | Controles para grafite, grafeno/nanomateriais, pós, NH4OH, Triton X-100, ruído, calor, névoas/aerossóis, limpeza e descarte. | NR-9; NR-15 e anexos; NR-6 para EPI; FISPQ/GHS e NR-26 | Ambos | SSMA + CQ + Operações | Pendente. Deve gerar matriz de exposição e plano de monitoramento |
| Incêndio, emergência e sinalização | Verificar cenário de incêndio, rotas, extintores, sinalização, brigada, compatibilidade de materiais e procedimentos de emergência. | NR-23; NR-26; normas Corpo de Bombeiros local; FISPQs | Ambos | SSMA + Brigada/Facilities | Pendente. Se houver inflamáveis, cruzar com gate NR-20 |
| Protocolo de comissionamento frio, quente e SAT | Critérios de aceite: rotação KonMix, agitadores, temperatura, pH, vazões, RCF quando disponível, limpeza, potência, balanço de massa e cronoanálise do ciclo. | Boa prática SAT/FAT; NR-10/12/13 conforme equipamento; ART quando houver responsável técnico (Lei 6.496/1977) | Ambos | Engenharia + Operações + CQ + SSMA | Pendente. Gate técnico central |
| RFQs com escopo técnico e ARTs | Converter CAPEX gerencial em escopos contratáveis com fotos, lista de equipamentos, responsabilidade, critérios de aceite, cronograma e ARTs quando aplicável. | Lei 6.496/1977 (CONFEA/CREA) para ART; NR-10/12/13 conforme escopo | Ambos | Engenharia + Compras + Jurídico/Compliance | Pendente. Sem RFQ, R$610 mil segue AACE Classe 4/5 |
| Formalização de CQ terceirizado | Proposta/contrato com métodos, volume de amostras, SLA, preparo/envio, interpretação técnica, guarda de laudos e critérios de aceite. | Requisitos contratuais; ISO/IEC 17025 desejável quando laboratório declarar ensaio acreditado | Ambos | CQ + Jurídico/Compliance | Pendente. Escopo diferente para D1 (caracterização) e D2 (liberação) |
| Licença, dispensa, resíduos, efluentes e emissões | Confirmar enquadramento ambiental da atividade real: licença, dispensa ou não incidência; mapear resíduos, efluentes, emissões, armazenamento e transporte. | DN COPAM 217/2017 em MG; CONAMA 237/1997; Lei 12.305/2010; CONAMA 430/2011; normas locais | Ambos | Compliance/SSMA + consultoria ambiental | Pendente. Precisa decisão documental, não nota genérica |

### §11.2 Gates adicionais — Cenário Produção

| Gate | Descrição | Fundamento | Responsável | Status |
|---|---|---|---|---|
| SAT com cronoanálise de ciclo e validação de separação em 200 L | Validar volume real por lote, vazões, rotações, balanço de massa, tempo de ciclo e rendimentos com 200 L reais | Boa prática de qualificação de processo | Engenharia + Operações + CQ | Pendente. Condiciona confiabilidade do custo unitário por produto |
| Campanha gravimétrica para validação dos rendimentos | Pelo menos 3 campanhas consecutivas com medição formal de rendimento por fração | Boa prática estatística de processo | CQ + Operações | Pendente. Sem isso, condições conservadora/média/otimista não têm base estatística |
| Validação de especificações de produto por cliente/aplicação | Confirmar especificação e critérios de aceite por produto antes de operar como linha dedicada | Requisito comercial/contratual | Comercial + CQ | Pendente |
| Validação de regime dedicado e equipe enxuta (1+3+1) | Confirmar se equipe enxuta D2 cobre operação, manutenção, SSMA, limpeza, amostragem e contingências sem degradar segurança | NR-1/PGR; NR-12; treinamentos internos | Operações + RH + SSMA | Pendente. Premissa D2 válida apenas para Cenário Produção |
| CQ rotineiro por especificação de produto | Transformar CQ de caracterização em CQ de liberação rotineira: amostragem, retenção, laudos, critérios de rejeição/reprocesso | Contrato CQ; ISO/IEC 17025 quando aplicável | CQ + Operações | Pendente. Necessário para promessa comercial |
| Enquadramento de inflamáveis e NR-20 | Verificar se solventes, líquidos auxiliares ou formulações geram enquadramento; se não, registrar dispensa técnica | NR-20; FISPQs; Corpo de Bombeiros | SSMA + Operações | Pendente condicionado ao processo real |
| Resíduos, efluentes e emissões em regime estabilizado | Dimensionar geração mensal em 43,5 lotes/mês, segregação, armazenamento, transporte, destinação, efluentes de lavagem | Lei 12.305/2010; CONAMA 430/2011; DN COPAM 217/2017 | SSMA/Compliance + Operações | Pendente |
| Licenciamento/dispensa para operação comercial | Formalizar se atividade dedicada é licenciável, dispensada ou coberta por licença existente; registrar CNAE, porte/potencial poluidor | CONAMA 237/1997; DN COPAM 217/2017; normas municipais | Compliance + consultoria ambiental | Pendente. Gate bloqueante para narrativa comercial |
| Treinamento, rotina operacional e registros de produção | Formalizar POPs, permissões de trabalho, treinamento, registros de batelada, manutenção, desvios, limpeza e rastreabilidade de lote | NR-1; NR-9; NR-10; NR-12; boas práticas internas | Operações + SSMA + CQ | Pendente. Necessário para operação repetível |

### §11.3 Gates específicos — Cenário Desenvolvimento

| Gate | Descrição | Fundamento | Responsável | Status |
|---|---|---|---|---|
| Plano de campanhas técnicas e aplicações | Vincular cada campanha a hipótese técnica, cliente/aplicação, formulação, volume, amostras, ensaios, descarte e critérios de aprendizado | Governança técnica do projeto; requisitos contratuais se houver parceiro/cliente | P&D/Aplicações + Operações + CQ | Pendente. Reduz risco de tratar D1 como fábrica mal ocupada |
| CQ de caracterização por aplicação | Diferenciar ensaios exploratórios de P&D dos ensaios de liberação rotineira; definir métodos por aplicação e laudos que sustentem TRL/cliente | Contrato CQ; ISO/IEC 17025 desejável; rastreabilidade técnica | CQ + P&D/Aplicações | Pendente. Conecta custo de CQ ao valor técnico do D1 |
| Controle de amostras, pilotos e remessas | Definir rótulos, FISPQ quando cabível, embalagem, transporte, autorização de envio, rastreabilidade de amostras e responsabilidade por uso em cliente/parceiro | NR-26/GHS; regras de transporte; contrato/NDA com parceiro | Compliance + CQ + Comercial técnico | Pendente. Importante para reputação com parceiro e investidor |
| Gate de formulações antes da conversão comercial | Preservar lógica da v9: formulação e aplicação são anteriores à promessa de conversão econômica; campanha deve gerar evidência de desempenho, não só massa | Governança técnica/comercial do projeto | P&D/Aplicações + Comercial técnico | Pendente. Vincular ao §4.4 |
---

## §12. Rastreabilidade dos valores críticos

A revisão desta nota separa valores extraídos de fonte documental, valores informados como premissa do projeto e valores estimados gerencialmente. Valores marcados como **Linha nova v10** são próprios dos cenários e não existiam na v9.

| Informação crítica | Valor usado | Natureza da fonte | Como deve ser lida |
|---|---:|---|---|
| Base bruta histórica de equipamentos produtivos | R$ 1.615.200 | Planilha P100/CERES 2021; saneamento de custos | Base histórica bruta. Não é CAPEX incremental, valor de reposição nem valor líquido contábil |
| Base bruta histórica de SSMA | R$ 65.360 | Planilha P100/CERES 2021; saneamento de custos | Complemento SSMA da base histórica |
| Base bruta histórica total | R$ 1.680.560 | Soma: R$ 1.615.200 + R$ 65.360 | Base para benchmark de recomissionamento e manutenção |
| Depreciação gerencial anual | R$ 166.576/ano | Cálculo a partir da vida útil dos ativos | Custo econômico anual; não é desembolso caixa |
| CAPEX incremental de recomissionamento | R$ 610.000 | Estimativa gerencial por pacotes; AACE Classe 4/5 | Investimento novo para reativar P100. Faixa indicativa R$ 430–915k até RFQs, vistoria, ARTs e SAT |
| Benchmark CAPEX / base histórica | 36,3% | R$ 610.000 / R$ 1.680.560 | Teste de plausibilidade, não metodologia primária |
| Manutenção anual | R$ 81.510/ano | Premissa v9: ~5% da base histórica produção + SSMA | Planejamento. Separar preventiva/corretiva; falhas pré-partida pertencem ao CAPEX |
| Controle de qualidade terceirizado | US$ 5.000/mês; câmbio R$ 5/US$; R$ 300.000/ano | Premissa v9 preservada | Envelope recorrente para Raman, AFM/MEV/MET, TG/TGA, relatórios e cadeia de custódia |
| Equipe operacional, CQ e aplicações | 8 pessoas; salário médio R$ 10.000/mês; encargos 75%; R$ 1.680.000/ano | Premissa v9 preservada | Estrutura do Cenário Desenvolvimento. Não somar com equipe enxuta de Produção |
| Faixa externa de preço de referência | US$ 50–200/kg para NPG/GNP técnico | Benchmark externo v9; revalidado em §7 | Régua de mercado. A US$ 50/kg e câmbio R$ 5/US$, receita no piso (R$ 2.578.750/ano) cobre: ~101% do OPEX Técnico Completo v9 (R$ 2.563.484 — base §7.1) e ~104% do OPEX Produção v10 (R$ 2.481.000 — base §9.2). Os percentuais referem-se a denominadores distintos; ver reconciliação em §10. |
| Tempo de ciclo nominal | 10,75 h/lote | Planilha CERES / P100x2 | Capacidade nominal econômica, não cronoanálise garantida |
| Faixa defensável de ciclo com limpeza | 10,75–13,25 h/lote | Inferência técnica: ciclo nominal + limpeza MS 2,50 h | Usar em sensibilidade até cronoanálise SAT |
| Rotação KonMix | 3.468–3.550 rpm | PIO-MGG-019 + lote 20210720Pa | Parâmetro interno forte. Confirmar por inversor/tacômetro no SAT |
| Agitação do tanque | 100–150 rpm | PIO-MGG-019 | Referência operacional. Confirmar para rota 100 g/L/5 h |
| pH de processo | pH 10,0 | PIO-MGG-019 | Parâmetro de rota; registrar por lote |
| Temperatura de processamento | 25–30 °C | PIO-MGG-019 | Controlar por datalogger/enjaquetamento. Afeta repetibilidade |
| Vazão de separação por decanter | 30–50 L/h | Registros de lotes históricos | Parâmetro rastreável. A 30–50 L/h, 200 L exigem 4,0–6,7 h |
| Vazão de separação por centrífuga de discos | 55–65 L/h | Lotes 20210720Pa (~55) e 20210816Pa (~65) | A 55 L/h, 200 L exigem ~3,6 h antes de setup/limpeza |
| Rotação da centrífuga de discos | 3.600 rpm | Lote 20210720Pa | Documentado. RCF não localizado |
| RCF de separação | Não localizado | Pendência técnica | Não converter rpm em RCF sem raio/geometria. Lacuna para SAT |
| Rendimentos do caso-base técnico | GPC 0,80%; NPG 5,00%; Nanografite 93,00%; perdas 1,20% | Premissa gerencial; lote 20210720Pa e planilha P100 | Caso-base técnico. Relativo à massa de grafite seco alimentado |
| Faixa histórica de rendimentos | GPC 0,45–0,80%; NPG 3,8–5,2%; NG 80–94%; perdas 1–15% | Campanha 2021 | Usar em sensibilidade até campanha pós-recomissionamento |
| Lotes por mês | 43,5 lotes/mês | Aba Parâmetros da planilha P100: 10 lotes/semana, 1 turno, 5 dias/semana | Capacidade nominal econômica |
| Capacidade nominal anual | 522 lotes/ano | Inferência: 43,5 × 12 | Teto nominal. Não vender como performance do primeiro ano |
| Ramp-up defensável | 313–418 lotes/ano; base prudente 365–400/ano | Inferência v9: 60–80% de 522 | Faixa técnica para o primeiro ano |
| Carga de grafite por lote | 20 kg/lote combinado | v9 + confirmação do titular: 10 kg/tanque × 2 tanques | Premissa operacional central. Corrige v8 (10 kg combinado = 5 kg/tanque) |
| Concentração operacional | 100 g/L por tanque | Lote 20210720Pa: 10 kg em tanque de 100 L | Base da rota econômica P100 |
| Matérias-primas e consumíveis | R$ 192.177/ano | Base v9; grafite 20 kg/lote + Triton X-100, NH4OH, água, embalagens | OPEX caixa produtivo para 522 lotes/ano; incerteza ±30% |
| Utilidades | R$ 83.885/ano | Potência instalada × tempo × tarifa CEMIG histórica ~R$ 0,857/kWh | Ordem de grandeza. Faixa prudente: R$ 65–110 mil/ano |
| OPEX caixa anual v9 | R$ 2.396.908/ano | Soma v9 §6 | Base de custo caixa da P100 piloto com equipe de 8 pessoas |
| OPEX técnico completo v9 | R$ 2.563.484/ano | OPEX caixa + depreciação gerencial R$ 166.576 | Base para custo técnico completo de R$ 249/kg |
| Custo técnico médio v9 | R$ 249/kg; R$ 4.912/lote | R$ 2.563.484 / 10.314,72 kg e / 522 lotes | Leitura executiva/banco para custo médio do mix |
| Capital de giro inicial | R$ 400–599 mil | 2–3 meses de OPEX caixa mensal médio ~R$ 199.742 | Exclusão consciente do CAPEX e OPEX; provisionar separadamente |
| Desenvolvimento — OPEX anual de capacidade técnica | R$ 4.094.400/ano; faixa R$ 3.654.400–4.844.400/ano | v10 D1; detalhamento [ALT-446](mention://issue/5774ebcb-dcc5-427d-90b6-101a9a603715) | **Linha nova v10.** Aplica ao Cenário Desenvolvimento. Mede capacidade técnica anual, não custo fabril por kg |
| Desenvolvimento — custo por campanha | R$ 80.000 por campanha base de 5 lotes | v10 D1; composição detalhada em §8.3 | **Linha nova v10.** Não dividir por kg vendido |
| Desenvolvimento — custo marginal à la carte | R$ 18.000/lote adicional dentro de campanha aberta | v10 D1; composição detalhada em §8.3 | **Linha nova v10.** Piso de custo, não preço |
| Produção — OPEX mensal/anual caso-base | R$ 206.750/mês; R$ 2.481.000/ano | v10 D2; reconciliado em §10 | **Linha nova v10 reconciliada.** Pool distinto do v9 técnico completo; diferença de R$ 82.484/ano explicada em §10 |
| Produção — custo unitário conservador | GPC R$ 905/kg; NPG R$ 453/kg; Nanografite R$ 226/kg | v10 D2; 0,5%/5%/93%/1,5%; alocação 4:2:1 | **Linha nova v10.** Rendimento conservador |
| Produção — custo unitário média histórica | GPC R$ 895/kg; NPG R$ 448/kg; Nanografite R$ 224/kg | v10 D2; 0,8%/5,0%/93,0%/1,2%; alocação 4:2:1 | **Linha nova v10.** Caso-base |
| Produção — custo unitário otimista | GPC R$ 789/kg; NPG R$ 394/kg; Nanografite R$ 197/kg | v10 D2; 2%/16%/80,5%/1,5%; alocação 4:2:1 | **Linha nova v10.** Sensibilidade otimista; pendente de validação gravimétrica |
| Alocação por complexidade | Pesos GPC=4, NPG=2, Nanografite=1; residual sem receita | Critério CFO v10 D2; reconciliado em §10 | **Linha nova v10.** Para precificação técnica; não é preço de venda |
| Indiretos de mercado — Produção (recomendado) | R$ 59.400/mês; R$ 712.800/ano | Benchmark externo §7.2; faixa R$ 34–100k/mês | **Linha nova v10.** EPP independente. Separar benchmark externo de premissa interna |
| Indiretos compartilhados — Desenvolvimento | R$ 28.000/mês estimado; R$ 336.000/ano na estrutura fixa D1 | v10 D1; uso da infraestrutura ALTOE | **Linha nova v10.** Só no Desenvolvimento; não comparar com EPP sem declarar diferença de perímetro |

---

## §13. Sensibilidades que mais afetam o custo

Os custos são sensíveis principalmente a três fatores: volume anual efetivo, equipe e controle de qualidade.

Na base atual (10,31 t/ano, R$ 249/kg técnico completo):
- Se a produção efetiva cair para 7,2 t/ano: R$ 355/kg.
- Se a produção efetiva subir para 14,4 t/ano: R$ 178/kg.
- Para ramp-up de 313–418 lotes/ano: R$ 310–414/kg técnico completo.

Cada variação de R$ 50 mil/ano no contrato de CQ altera o custo em ~R$ 4,85/kg. O pesquisador adicional de aplicações e fomento: +R$ 210 mil/ano (+~R$ 20/kg) antes de qualquer receita ou subvenção gerada.

**Para o Cenário Produção:**

| Posição | Variável crítica | Caso baixo | Base | Caso alto | Impacto |
|---:|---|---:|---:|---:|---|
| 1 | Indiretos C2 mensais | R$ 34k | R$ 59,4k | R$ 100k | Nanografite R$ 196–268/kg; OPEX R$ 181,35–247,35k/mês |
| 2 | Rendimento NPG | 5,0% | 5,0% | 16,0% | Nanografite R$ 224 → R$ 205/kg |
| 3 | Rendimento Nanografite | 80,5% | 93,0% | 93,0% | Nanografite R$ 254 → R$ 224/kg |
| 4 | Rendimento GPC | 0,5% | 0,8% | 2,0% | Nanografite R$ 226 → R$ 216/kg |

**Para o Cenário Desenvolvimento:**

| Posição | Variável crítica | Caso baixo | Base | Caso alto | Impacto |
|---:|---|---:|---:|---:|---|
| 1 | Cadência de campanhas | 8 | 12 | 18 campanhas/ano | OPEX R$ 3,65–4,84 MM/ano |

---

## §14. Próximos passos

O próximo passo técnico imediato é validar a capacidade do módulo de separação para processar 200 L por lote dentro do ciclo operacional. Esse teste deve ocorrer em SAT ou no primeiro comissionamento com carga real, com cronoanálise formal, medição de vazão por etapa, rotação, RCF quando disponível, balanço de massa e identificação do tempo de limpeza.

A estimativa de R$ 610.000 deve ser transformada em pacote de cotação: escopo, fotos, lista de equipamentos, critérios de aceite, matriz de responsabilidade e prazos. O contrato de CQ também deve ser formalizado com UFMG/CDTN ou equivalente.

Em paralelo, a frente de formulações e aplicações deve ser estruturada antes da retomada regular das campanhas (ver §4.4). O pesquisador responsável deve mapear contatos históricos do MGgrafeno, selecionar aplicações prioritárias, preparar fichas de formulação e articular propostas com grupos do CDTN e da UFMG.

Para o Cenário Produção, as condições de rendimento (conservadora/média/otimista) precisam ser validadas por campanha de balanço gravimétrico pós-recomissionamento. Sem isso, o custo unitário por produto é defensável como estimativa, mas não como performance documentada.

---

## §15. Changelog da v3 para a v4

Esta v4 incorpora a revisão de Flavio Plentz sem alterar os números financeiros centrais do relatório. As mudanças são principalmente conceituais, terminológicas e de controle de risco.

| Bloco | Mudança incorporada |
|---|---|
| Posicionamento | P100 reposicionada como plataforma piloto de validação técnico-comercial para grafenos de performance, formulações e serviços técnicos aplicados |
| TRL | Removida leitura categórica de TRL7 → TRL8; adotada redação de objetivo de demonstração TRL7 pós-recomissionamento e TRL8 condicionado a qualificação formal |
| Nomenclatura | Mantida rastreabilidade GPC/FLG e NPG/GNP na primeira ocorrência; NG tratado como fração nanografítica de menor valor; GPB mantido como termo legado |
| CAPEX | R$ 610 mil preservados como estimativa gerencial preliminar, não orçamento executivo |
| OPEX | R$ 2,113 MM/ano de OPEX caixa e R$ 2,280 MM/ano de OPEX técnico completo preservados |
| Mercado | Faixa US$ 50–200/kg mantida como régua externa para NPG/GNP técnico, sem virar promessa de preço |
| Comercial | Tese deslocada de venda indiferenciada de pó para valor por solução, formulação, aplicação e "Grafeno como Serviço" |
| SSMA/compliance | Inseridos gates documentais mínimos antes de transformar a estimativa em orçamento executivo ou operação liberada |

## §16. Changelog da v4 para a v5

> **Nota histórica (v9):** os valores de carga de grafite e produção registrados nos changelogs v5 a v7 abaixo foram superados pela correção aplicada na v9. A carga de 10 kg/lote combinados (≈5 kg/tanque) mencionada nesses changelogs estava incorreta; o valor correto é 20 kg/lote (10 kg/tanque). Leia esses blocos como histórico documental, não como premissas concorrentes.

Esta v5 incorpora a validação da condição operacional da P100 solicitada em [ALT-413](mention://issue/79196bc8-6c3a-4844-870b-7de5afa5552d). Não há alteração nos números financeiros ou nas premissas de cálculo.

| Bloco | Mudança incorporada |
|---|---|
| Base operacional — §4 (texto e tabela) | Reescrito para explicitar que a P100 é composta por dois módulos de conversão operando em paralelo, gerando 200 L de volume nominal por lote |
| Base operacional — §4 (nota de validação) | Confirmados: (a) 10 kg/lote = carga combinada dos dois módulos; (b) volume nominal total = 200 L; (c) toda a massa dos dois módulos é transferida ao módulo de separação; (d) unidade do lote é kg; (e) "tanques de 100 L" descreve volume nominal dos equipamentos, não massa |

## §17. Changelog da v5 para a v6

Esta v6 documenta a base metodológica das premissas técnicas e financeiras do modelo, preenchendo os gaps de rastreabilidade identificados em [ALT-414](mention://issue/413c4f5f-1189-4afd-88f5-71a7ae2b35c3). Não há alteração nos números financeiros.

| Bloco | Mudança incorporada |
|---|---|
| Glossário | Adicionado verbete AACE com definição de classificação Classe 1–5 |
| §4.1 (nova) | Decomposição do ciclo de 10,75 h em etapas; documentada inconsistência da limpeza do MS; divergência 105,6 L vs. 200 L |
| §4.2 (nova) | Origem dos yields: lote de referência 20210720Pa; variação histórica entre lotes da campanha 2021 |
| §4.3 (nova) | Origem de 43,5 lotes/mês; ramp-up defensável 313–418 lotes/ano |
| §5 — CAPEX | Inserida classificação AACE Cl.4/5; faixa −30%/+50%; tabela de pacotes com base metodológica e grau de confiança |
| §6.1–§6.6 (novas) | Tabela de equipe com funções; escopo CQ terceirizado; base de matérias-primas e utilidades; qualificação da taxa de manutenção; exclusões e capital de giro |
| §12 — Rastreabilidade | Adicionadas entradas para ciclo 10,75 h, rendimentos, lotes/mês, matérias-primas, utilidades e capital de giro |

## §18. Changelog da v6 para a v7

Esta v7 incorpora a revisão operacional solicitada em [ALT-417](mention://issue/9ed494f6-7d14-4964-b5ff-479ad44f5ddf). Não há alteração nos números financeiros. As mudanças são de explicitação técnica.

| Bloco | Mudança incorporada |
|---|---|
| Glossário | Adicionados MC, MS, rpm, RCF, SAT, FAT, PIO, LPE, retrofit mecânico, comissionamento frio e comissionamento quente |
| §4.4 (nova) | Premissas e parâmetros de operação por módulo: conversão, separação, benchmarks internos e externos, lacunas de validação |
| Módulos de conversão | Documentados 100 L/MC, 200 L nominais combinados, 10 kg/lote, 100 g/L nominal, 5 h de cisalhamento, rotação KonMix 3.468–3.550 rpm, agitador 100–150 rpm, pH 10,0 e 25–30 °C |
| Módulo de separação | Documentadas vazões históricas decanter (30–50 L/h), centrífuga de discos (55–65 L/h), rotação de discos 3.600 rpm, limpeza MS 2,5 h/lote, lacuna de RCF |
| §12 — Rastreabilidade | Adicionadas entradas para rotação KonMix, agitação do tanque, pH/temperatura, vazões de separação e rotação/RCF |

## §19. Changelog da v7 para a v8

Esta v8 incorpora a revisão solicitada em [ALT-420](mention://issue/2d734bd1-e5f2-4796-b472-6d31a6a66fb6). A alteração central é a criação de §4.4 dedicada a formulações antes dos módulos de conversão e a inclusão do pesquisador adicional de desenvolvimento de aplicações. **Esta revisão altera os números de OPEX e todos os indicadores derivados.**

| Bloco | Mudança incorporada |
|---|---|
| Glossário | Adicionados DA e editais de fomento |
| §4.4 (nova) | Formulações antes dos módulos de conversão como gate técnico-comercial |
| §4.5 | Renumerada a antiga §4.4 |
| §6 | Equipe atualizada de 7 para 8 pessoas; mão de obra de R$ 1.470.000 → R$ 1.680.000/ano |
| OPEX consolidado | OPEX caixa de R$ 2.323.444 → R$ 2.396.908/ano; OPEX técnico completo de R$ 2.490.020 → R$ 2.563.484/ano |
| Indicadores unitários | Custo caixa: R$ 4.451/lote, R$ 451/kg → R$ 4.592/lote, R$ 232/kg; custo técnico completo: R$ 4.770/lote, R$ 483/kg → R$ 4.912/lote, R$ 249/kg |
| Capital de giro | R$ 390–580 mil → R$ 400–599 mil |

## §20. Changelog da v8 para a v9

Esta v9 incorpora a correção da carga de grafite por lote, confirmada pelo titular do projeto ([ALT-420](mention://issue/2d734bd1-e5f2-4796-b472-6d31a6a66fb6)). **A alteração central é a mudança de 10 kg combinados (5 kg/tanque) para 20 kg combinados (10 kg/tanque).** A produção anual de referência dobra de 5.157 kg/ano para 10.315 kg/ano, e o custo por kg cai de R$ 483/kg para R$ 249/kg (técnico completo).

| Bloco | Mudança incorporada |
|---|---|
| Base operacional — §4 | Carga de grafite corrigida para 20 kg/lote (10 kg/tanque × 2 tanques); rendimentos por lote dobrados; produção técnica anual: 5.157,36 → 10.314,72 kg/ano |
| §4.5 | Linha "Carga de grafite" corrigida; linha "Concentração operacional" atualizada para 100 g/L por tanque com rastreabilidade ao lote 20210720Pa |
| §6 e tabela | Matérias-primas: R$ 118.713 → R$ 192.177/ano (grafite 10→20 kg/lote); OPEX caixa: R$ 2.323.444 → R$ 2.396.908/ano; OPEX técnico completo: R$ 2.490.020 → R$ 2.563.484/ano |
| §6.6 | Custo caixa/kg: R$ 451 → R$ 232; custo técnico/kg: R$ 483 → R$ 249; capital de giro: R$ 390–580 → R$ 400–599 mil |
| §8 — Cenários econômicos | Receitas e coberturas recalculadas com 10.315 kg/ano; cobertura mínima (US$ 50/kg) passa de 52% para ~101% do OPEX Técnico Completo v9 |
| §9 — Preço de equilíbrio | Produção por fração atualizada (GPC: 41,76 → 83,52 kg/ano; NPG: 261,00 → 522,00 kg/ano; NG: 4.854,60 → 9.709,20 kg/ano) |
| §10 — Sensibilidades | Base atualizada para 10,31 t/ano a R$ 249/kg; custo no ramp-up 60–80%: R$ 603–805 → R$ 310–414/kg |
| §12 — Rastreabilidade | Adicionada linha "Carga de grafite por lote" corrigida; linha "Matérias-primas" atualizada |
| §20 — Pendências | Linha de matérias-primas atualizada para R$ 192.177/ano |

## §21. Changelog da v9 para a v10 (Revisão Plentz-06)

Esta v10 é **sucessora sequencial da v9**: reincorpora todos os blocos analíticos da v9 que foram omitidos na primeira versão v10 (revisão Plentz-05, [ALT-440](mention://issue/4edaa80f-47b0-4309-b732-3e99ca5f9d68)) e acrescenta a estrutura de dois cenários operacionais distintos (Desenvolvimento e Produção). A primeira versão v10 havia sido estruturada exclusivamente para o investidor (cenários), perdendo 9 blocos técnico-analíticos da v9. Esta revisão elimina essa descontinuidade.

**Blocos reincorporados da v9 (por subfrente de F2, [ALT-464](mention://issue/e3b93760-b3d1-4468-ab0e-544991700023)):**

| Bloco reincorporado | Referência v9 | Subfrente | Nota de reconciliação |
|---|---|---|---|
| §4.1 — Decomposição do ciclo de 10,75 h com contexto por cenário | §4.1, linhas 106–123 | F2.1 ([ALT-468](mention://issue/432a64f1-7aa8-40fa-b385-50527c13c985)) — Valdemiro | Ciclo preservado; adicionada coluna de aplicabilidade Desenvolvimento/Produção |
| §4.2 — Origem dos rendimentos e convenção de balanço de massa | §4.2, linhas 125–141 | F2.1 ([ALT-468](mention://issue/432a64f1-7aa8-40fa-b385-50527c13c985)) — Valdemiro | Tabela histórica de lotes preservada; balanço de massa por cenário adicionado |
| §4.3 — Origem da capacidade de 43,5 lotes/mês e ramp-up | §4.3, linhas 143–149 | F2.1 ([ALT-468](mention://issue/432a64f1-7aa8-40fa-b385-50527c13c985)) — Valdemiro | Leitura de ramp-up por cenário diferenciada |
| §4.4 — Gate de formulações antes dos módulos de conversão | §4.4, linhas 151–161 | F2.1 ([ALT-468](mention://issue/432a64f1-7aa8-40fa-b385-50527c13c985)) — Valdemiro | Preservado; contexto de campanha aprofundado para D1 |
| §4.5 — Premissas e parâmetros de operação por módulo | §4.5, linhas 163–208 | F2.1 ([ALT-468](mention://issue/432a64f1-7aa8-40fa-b385-50527c13c985)) — Valdemiro | Tabelas de parâmetros ampliadas com coluna de aplicabilidade por cenário |
| §5 — CAPEX por pacotes com AACE Cl.4/5 | §5, linhas 210–253 | F2.2 ([ALT-469](mention://issue/98da17bf-f801-43ab-b31f-e3cef93f46af)) — Julio | Tabela de pacotes restaurada; formatação harmonizada com §6 |
| §6.1 — Composição da equipe de 8 pessoas | §6.1, linhas 274–293 | F2.2 ([ALT-469](mention://issue/98da17bf-f801-43ab-b31f-e3cef93f46af)) — Julio | Nota de distinção entre equipe D1 (8) e D2 (5) adicionada |
| §6.2 — Escopo do CQ terceirizado | §6.2, linhas 295–307 | F2.2 ([ALT-469](mention://issue/98da17bf-f801-43ab-b31f-e3cef93f46af)) — Julio | Tabela ampliada; leitura D1/D2 diferenciada |
| §6.3 — Base de matérias-primas | §6.3, linhas 308+ | F2.2 ([ALT-469](mention://issue/98da17bf-f801-43ab-b31f-e3cef93f46af)) — Julio | Formato tabular; faixa de incerteza ±30% preservada |
| §6.4 — Base de utilidades | §6.4 | F2.2 ([ALT-469](mention://issue/98da17bf-f801-43ab-b31f-e3cef93f46af)) — Julio | Formato tabular; faixa R$ 65–110 mil/ano preservada |
| §6.5 — Qualificação da manutenção | §6.5 | F2.2 ([ALT-469](mention://issue/98da17bf-f801-43ab-b31f-e3cef93f46af)) — Julio | Taxa 5% preservada; nota sobre primeiro ciclo 5–8% adicionada |
| §6.6 — Exclusões e capital de giro | §6.6 | F2.2 ([ALT-469](mention://issue/98da17bf-f801-43ab-b31f-e3cef93f46af)) — Julio | R$ 400–599 mil preservados; tabela de indicadores derivados adicionada |
| §7 — Referências externas e benchmark de indiretos | Apenas US$ 50–200/kg em §7 da v9 | F2.3 ([ALT-470](mention://issue/44323d04-01c4-476e-848b-b239cc4af1e8)) — Eloi | Ampliado com tabela de indiretos de mercado (min/médio/máx), benchmark 2026, fontes auditáveis |
| §3 — Glossário (26 termos) | §3, linhas 51–81 v9 | F2.4 ([ALT-471](mention://issue/c4709a22-065d-473c-a080-4447e227c8dd)) — Cacilda | 26 termos da v9 restaurados + novos termos próprios da v10 (alocação 4:2:1, campanha, cenários); ambiguidades terminológicas explicitadas |
| §11 — Gates SSMA e compliance | §11, linhas 459–471 v9 | F2.5 ([ALT-472](mention://issue/cb0eba0b-a456-4a20-af8b-950dd5076d79)) — Tereza | Gates organizados em tabela com NRs; linha de bloqueio operacional literal da v9 preservada; gates adicionais de Produção |
| §12 — Rastreabilidade (19 linhas v9) | §12, linhas 473–500 v9 | F2.6 ([ALT-473](mention://issue/27df4ad9-137a-4121-8d70-09bdee0b4007)) — Julio + Valdemiro | Restauradas as 19 linhas da v9 + 24 linhas novas dos cenários; total 43 linhas |
| §22 — Pendências controladas | §20, linhas 618–635 v9 | F2.5 ([ALT-472](mention://issue/cb0eba0b-a456-4a20-af8b-950dd5076d79)) — Tereza | Tabela v9 restaurada; pendências específicas de Produção adicionadas |

**Estrutura acrescentada nesta v10 (própria dos cenários — mantida da revisão Plentz-05):**

| Bloco novo | Seção | Origem |
|---|---|---|
| Cenário (1) — P100 Desenvolvimento | §8 | v10 Plentz-05; harmonizado com bases reincorporadas |
| Cenário (2) — P100 Produção | §9 | v10 Plentz-05; reconciliado com OPEX v9 em §10 |
| Reconciliação custo/kg v9↔v10 | §10 | F2.2 ([ALT-469](mention://issue/98da17bf-f801-43ab-b31f-e3cef93f46af)) — Julio; novo nesta v10 |
| Análise comparativa e sensibilidade por cenário | §13 | v10 §4 + v9 §10; consolidado |
| Changelog v9→v10 | §21 | F3 ([ALT-474](mention://issue/6067b916-e710-41ac-bebe-7ba29472a28b)) — Carmen |

**Divergências reconciliadas:**
- v9 R$ 249/kg vs. v10 Produção R$ 895/R$ 448/R$ 224: não é contradição — é mudança de pool (equipe 8→5 pessoas) e método de alocação (média vs. 4:2:1 por produto). Tratado em §10.
- Indiretos de mercado: a v10 Plentz-05 listava apenas a faixa R$ 59,4k/mês como premissa sem benchmark externo. Esta v10 restaura e fundamenta a tabela min/médio/máx com fontes auditáveis (F2.3/Eloi).
- "Premissas CFO ainda pendentes de reconciliação com a planilha v9" declaradas na v10 Plentz-05 como risco: reconciliação realizada em F2.2 (Julio) e documentada em §10 e §12.

---

## §22. Pendências controladas

As pendências abaixo não impedem o uso desta v10 como relatório de planejamento, mas impedem tratar seus números como orçamento executivo ou promessa comercial.

| Pendência | Por que importa | Prioridade |
|---|---|---|
| Validação da capacidade do módulo de separação para 200 L | Estimativas de tempo de separação para 200 L (7,6–10,3 h sequencial) excedem os 3,5 h usados no modelo. Principal pendência técnica: valida ou invalida o ciclo de 10,75 h e a produção nominal de 522 lotes/ano. Deve medir vazão, rotação, RCF quando disponível, retirada de sólidos, transições e limpeza. | Alta |
| Vistoria física da planta P100 | Confirma estado real dos ativos, utilidades, itens fora de serviço e escopo de recomissionamento. Fundamento para converter R$ 610 mil de estimativa gerencial em orçamento cotado. | Alta |
| RFQs/cotações formais | Convertem R$ 610 mil de estimativa AACE Cl.4/5 em orçamento contratável. | Alta |
| Protocolo de comissionamento | Define critérios de aceite para comissionamento frio, quente e teste de performance. Inclui cronoanálise formal do ciclo com 200 L, rotação real do KonMix e agitadores, temperatura, pH, vazão e balanço de massa. | Alta |
| Campanha gravimétrica pós-recomissionamento | Valida os rendimentos das três condições (conservadora/média/otimista). Sem ela, o custo por produto no Cenário Produção é premissa, não performance documentada. | Alta (Cenário Produção) |
| SAT com validação de ciclo e rendimentos | Teste de aceite com carga real: cronoanálise, medição de rotações, vazões e balanço de massa. Gate para tratar P100 como apta a campanhas regulares. | Alta |
| Contrato/proposta de CQ externo | Valida a premissa de US$ 5.000/mês com métodos incluídos, volume de amostras, prazo e SLA. | Média |
| Laudos, ARTs e gates SSMA aplicáveis (ver §11) | Liberam ou condicionam operação segura e regular. Lista detalhada em §11. | Média |
| Atualização de cotações de matérias-primas | Grafite, Triton X-100, NH4OH e embalagens devem ser cotados com fornecedores para confirmar premissa de R$ 192.177/ano (faixa ±30%). | Média |
| Medição ou contratação de utilidades | Confirmar tarifa elétrica real e mapear água, ar comprimido, resfriamento e efluentes para refinar o valor de R$ 83.885/ano. | Média |
| Plano de contratação da equipe | Especificar os 8 papéis do Desenvolvimento (salários individuais, regime, cronograma) e os 5 do Cenário Produção. | Média |
| Plano de trabalho do pesquisador de aplicações e fomento | Define escopo, metas, contatos prioritários, aplicações-alvo, grupos CDTN/UFMG, editais elegíveis e entregáveis de formulação. Sem esse plano, a função adicional vira custo fixo sem mecanismo de captura de valor. | Média |
| Campanhas reprodutíveis pós-recomissionamento | Sustentam eventual demonstração TRL7 e futura qualificação TRL8. Geram balanço de massa real para substituir premissas históricas de yield. | Média |
| Estratégia comercial por aplicação | Separa massa técnica, massa qualificada, fração vendável, amostras, pilotos e formulações. | Média |
| Decisão sobre estrutura societária e regime tributário | Afeta tabela de indiretos de mercado (Lucro Presumido vs. Real) e custo administrativo do Cenário Produção. | Média |
| Matriz NR-12/SSMA por equipamento | Sair de menção genérica e criar matriz por equipamento (2 × KonMix, tanques, separação, painéis), risco, proteção, intertravamento e evidência. Bloqueia operação sem this gate. | Alta |
| Licença/dispensa ambiental e enquadramento de resíduos/efluentes | Definir se atividade piloto ou dedicada é licenciável, dispensada ou de não incidência ambiental. Afeta risco regulatório e reputacional. DN COPAM 217/2017 (MG), CONAMA 237/1997, Lei 12.305/2010. | Alta |
| POPs, treinamento e registros de produção | Formalizar procedimentos operacionais, permissões de trabalho, registros de batelada, manutenção e desvios. Necessário para operação repetível e auditável. | Média |
| Controle de amostras, pilotos e remessas | Definir rótulos, FISPQ quando aplicável, rastreabilidade de amostras enviadas a parceiros/clientes. Requisito reputacional e contratual. | Média |
| Enquadramento inflamáveis/NR-20 e FISPQs do processo | Verificar solventes, auxiliares de formulação e reagentes quanto à NR-20; FISPQ atualizada para grafite, NH4OH, Triton X-100. Se não aplicável, registrar dispensa técnica. | Média |
| Reconciliação final com a planilha-fonte P100/CERES 2021 | Planilha `P100_Custo de Produção - CLT_2021 - 9 de agosto de 2021 (CERES).xlsx` e `Levantamento de custos de Producao P100x2.xlsx` devem ser conferidas contra os valores desta v10. | Média |
| Ingestão no Vault das fontes externas | `Levantamento de custos de Producao P100x2.xlsx`, `PIO-MGG-019` e `PIO-MGG-039`, hoje fora da pasta `Custos/`. | Baixa |

---

## §23. Changelog da Revisão Plentz-06 para a Revisão Plentz-06.a

Esta revisão (06.a) é uma revisão editorial e de coerência analítica sobre a v10 Plentz-06 ([ALT-487](mention://issue/6760ed5e-5d9b-4b1b-9c5e-e448f3b85377)). **Não há alteração nos números financeiros centrais.** As mudanças são de clareza analítica, rastreabilidade e acessibilidade para as audiências técnico-acadêmica e financeira.

| Bloco | Mudança incorporada |
|---|---|
| Frontmatter | Adicionado campo `revisao: Plentz-06.a`, `issue_revisao_6a: ALT-487`, atualização de `data` para 2026-05-31 e atualização do campo `audiencia` para técnico-acadêmico-financeira |
| §1.1 — Guia de leitura por audiência (novo) | Tabela de navegação por perfil: Investidores/IFHAN (entrada por §2, §7–§9), Pesquisadores UFMG/CDTN (entrada por §3, §4, §11) e ambas as audiências (§1, §2, §10, §14). Reduz o tempo de localização para leitores com diferentes formações |
| §2 — Resultado consolidado | Adicionadas referências cruzadas nas linhas dos Cenários Desenvolvimento e Produção: "Detalhamento: §8" e "Detalhamento: §9; reconciliação §10", permitindo navegação direta para os leitores orientados pelos indicadores-chave |
| §7.1 — Cobertura econômica | Clarificada a ambiguidade entre os percentuais ~101% e ~104%: o ~101% refere-se ao OPEX Técnico Completo v9 (R$ 2.563.484, inclui depreciação); o ~104% refere-se ao OPEX Produção v10 (R$ 2.481.000, pool distinto sem depreciação). Os dois são complementares, não contraditórios. Adicionada referência a §10 |
| §8 — Cenário Desenvolvimento (fim de seção) | Adicionada nota de conexão explicitando relação com §9, §10 e §7 |
| §9.2 — Estrutura de custos D2 | Adicionada nota (²) derivando o custo de equipe D2: 5 pessoas, salário médio bruto ~R$ 6.800–7.000/mês, encargos ~78–80%. Adicionada nota (³) explicando por que os Insumos D2 (R$ 30.950/mês) são superiores às matérias-primas v9 (R$ 16.015/mês): embalagens por produto, reagentes de limpeza entre bateladas de produtos distintos, materiais de amostragem e consumíveis de CQ de liberação |
| §9 — Cenário Produção (fim de seção) | Adicionada nota de conexão explicitando relação com §8, §10 e §7.1 |
| §10 — Reconciliação v9↔v10 | Tabela expandida com coluna OPEX caixa v9 separada de OPEX técnico completo v9; adicionada linha "Residual D2 vs v9 caixa" explicando que D2 é levemente mais caro que v9 caixa (+R$ 84.092/ano) apesar da equipe menor, por causa dos indiretos empresariais adicionados. Adicionadas notas de leitura para investidor e para pesquisador |
| §12 — Rastreabilidade | Entrada "Faixa externa de preço" atualizada: explicitados os dois denominadores de cobertura (~101% sobre OPEX Técnico Completo v9, ~104% sobre OPEX Produção v10) com referência cruzada a §7.1, §9.2 e §10 |

---

## §24. Changelog da Revisão Plentz-06.a para a Revisão Plentz-06.b

Esta revisão (06.b) acrescenta o Sub-cenário D1.b ao Cenário Desenvolvimento ([ALT-487](mention://issue/6760ed5e-5d9b-4b1b-9c5e-e448f3b85377), briefing 2026-05-31). **Nenhum número existente foi alterado.** O acréscimo é exclusivamente um novo bloco analítico dentro do §8.

| Bloco | Mudança incorporada |
|---|---|
| Frontmatter | `revisao: Plentz-06.b`, `issue_revisao_6b: ALT-487` |
| **§8.5 — Sub-cenário D1.b (novo)** | Modelagem completa do regime de 3 lotes testes/semana a 100L (módulo único): §8.5.1 parâmetros técnicos e produção anual (156 lotes, 1.560 kg grafite, GPC 12,5 kg / NPG 78,0 kg / Nanografite 1.450,8 kg); §8.5.2 estrutura de custos variáveis por lote 100L (R$ 9.550/lote caso-base); §8.5.3 OPEX total D1.b caso-base R$ 4.624.200/ano; §8.5.4 comparação com D1 base e sensibilidade de CQ (faixa R$ 4.156.000–5.062.000/ano); §8.5.5 métricas derivadas e pontos de atenção operacionais |
