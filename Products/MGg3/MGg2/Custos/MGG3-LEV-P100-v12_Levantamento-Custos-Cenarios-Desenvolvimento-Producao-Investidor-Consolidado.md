---
codigo_fonte: MGG3-LEV-P100-v12
titulo: Levantamento de custos da P100 — Cenário real de Desenvolvimento, projeção de Produção e seção do investidor IFHAN — Revisão Carmen-equipe-P&D
produto: MGgrafeno / MGG3
escala: P100 — 2 módulos KonMix de cisalhamento em tanques de 100 L (200 L nominais por lote combinado)
versao: 12
revisao: Plentz-08 + Correção-Carmen-duplicidade-lotes + Ajuste-equipe-P&D-v12
data: 2026-05-31
data_correcao: 2026-06-01
data_revisao_v12: 2026-06-04
status: consolidado_cenario_real_desenvolvimento_com_producao_anexa_e_secao_investidor
base_anterior: MGG3-LEV-P100-v11
issue_revisao_v12: [ALT-539](mention://issue/8dfd745d-8a55-408f-81ec-c2394f430b44)
clientes_destinatarios: Flávio Plentz e Adelina Pinheiro (sócios); IFHAN (grupo investidor, modelo 49/51) como leitor secundário
issue_revisao_6: [ALT-464](mention://issue/e3b93760-b3d1-4468-ab0e-544991700023)
issue_revisao_final: ALT-464
issue_revisao_6a: [ALT-487](mention://issue/6760ed5e-5d9b-4b1b-9c5e-e448f3b85377)
issue_revisao_6b: [ALT-487](mention://issue/6760ed5e-5d9b-4b1b-9c5e-e448f3b85377)
issue_revisao_7: [ALT-488](mention://issue/514e7501-890e-4c1b-864a-11bdecd136bb)
issue_revisao_8: [ALT-491](mention://issue/12a23097-71ce-45a0-913a-b11e25b1d0ac)
subfrentes_rev08: [ALT-492](mention://issue/25873de5-ef7f-4ae9-9e2e-ea14d0acac71), [ALT-493](mention://issue/44de1e29-24a8-47ae-9eaf-f6dbae232738), [ALT-494](mention://issue/cc707c53-96db-4036-b8a3-a9e6aa57ac11), [ALT-495](mention://issue/fdd8dbc3-5dfa-4ebd-b91b-95610c3516ba), [ALT-496](mention://issue/622152af-0851-4330-b1a3-c91732aff0ae), [ALT-497](mention://issue/cacde773-f920-4da7-ada8-1c074261874d), [ALT-498](mention://issue/0d6d34f2-35aa-4770-aa78-44a4b77b46e6)
subfrentes_rev06: [ALT-465](mention://issue/447ac547-6079-4350-92e6-441c91a0e503), [ALT-466](mention://issue/f0520698-b1e9-40a7-85e1-254350010c51), [ALT-467](mention://issue/7e482ee8-564d-4242-8836-2c47d4016c16), [ALT-468](mention://issue/432a64f1-7aa8-40fa-b385-50527c13c985), [ALT-469](mention://issue/98da17bf-f801-43ab-b31f-e3cef93f46af), [ALT-470](mention://issue/44323d04-01c4-476e-848b-b239cc4af1e8), [ALT-471](mention://issue/c4709a22-065d-473c-a080-4447e227c8dd), [ALT-472](mention://issue/cb0eba0b-a456-4a20-af8b-950dd5076d79), [ALT-473](mention://issue/27df4ad9-137a-4121-8d70-09bdee0b4007), [ALT-474](mention://issue/6067b916-e710-41ac-bebe-7ba29472a28b)
audiencia: sócios fundadores (Flávio Plentz, Adelina Pinheiro) e grupo investidor IFHAN — leitura técnico-honesta para avaliação societária e posterior negociação de investimento
---

# Levantamento de custos da P100 — Custo operacional real do Desenvolvimento (base), projeção de Produção em capacidade nominal (Anexo A) e seção do investidor IFHAN

> **O que mudou nesta revisão (v12 — Ajuste de equipe do Cenário P&D, [ALT-539](mention://issue/8dfd745d-8a55-408f-81ec-c2394f430b44)).** Esta é a v12, construída sobre a [[MGG3-LEV-P100-v11_Levantamento-Custos-Cenarios-Desenvolvimento-Producao-Investidor-Consolidado|v11]] (que permanece intocada como base histórica). A pedido dos sócios, a **composição da equipe do Cenário (1) — Desenvolvimento (P&D)** foi redefinida: a equipe passa de 8 para **9 pessoas — um time de operação da planta piloto com 4 pessoas de produção + 2 de controle de qualidade, mais um time de Aplicações com 3 pessoas (desenvolvimento de aplicações e produtos à base de grafeno — GaaS)**, ao **salário médio de R$ 10.000/mês** (base) + 75% de encargos. Isso eleva a mão de obra-base de R$ 1.680.000 para **R$ 1.890.000/ano** (§6) e, no caso-base do cenário real (§8.5, salário 2026-ajustado mantido por convenção da v11 — nota ¹), o OPEX caso-base sobe de R$ 4.624.200 para **R$ 4.891.500/ano**, deslocando o cheque do investidor §2-A de R$ 5,73 MM para **R$ 6,00 MM (caso-base)**. Todos os indicadores derivados foram recalculados; detalhamento em §28. **Nota de premissa:** a v12 mantém a convenção da v11 de modelar o caso-base com salário 2026-ajustado (R$ 12.728/mês = R$ 10.000 + ~27%); se a intenção for fixar R$ 10.000/mês também no caso-base (sem o ajuste 2026), o OPEX caso-base seria de ~R$ 4,38 MM e o cheque ~R$ 5,49 MM — ver §28.

> **Para quem lê este relatório.** Este documento é dirigido, em primeiro lugar, a Flávio Plentz e Adelina Pinheiro, que serão sócios fundadores da empresa a ser criada e investida pelo grupo IFHAN (modelo societário 49/51, controle do IFHAN). Em segundo plano, serve de base técnica para a negociação de investimento com o IFHAN, que pagará o licenciamento da tecnologia MGgrafeno junto ao CDTN e à UFMG. O conteúdo é, por exigência, **técnico e honesto**: nenhum número aqui é promessa comercial, e cada premissa traz a sua fonte e o seu grau de validação.

> **O que mudou nesta revisão (Plentz-08).** Esta é a v11 do levantamento consolidado, construída sobre a [[MGG3-LEV-P100-v10_Levantamento-Custos-Cenarios-Desenvolvimento-Producao-Consolidado|v10]] (que permanece intocada como base histórica). A Plentz-08 acrescenta uma **seção dedicada ao investidor IFHAN** logo após o resultado consolidado (§2-A), respondendo quanto empenhar para a P100 funcionar no Ano 1; incorpora a narrativa de opção estratégica exclusiva, aplicação prioritária cobre-grafeno e licenciamento separado; e atualiza §6.6 para substituir a exclusão genérica de aluguel/ocupação por premissa escalonada: Ano 1 sem locação/condomínio, Ano 2+ com locação de R$ 10 mil/mês, sem dupla contagem com manutenção e utilidades. Briefing: [ALT-491](mention://issue/12a23097-71ce-45a0-913a-b11e25b1d0ac); integração: [ALT-497](mention://issue/cacde773-f920-4da7-ada8-1c074261874d); versionamento: [ALT-498](mention://issue/0d6d34f2-35aa-4770-aa78-44a4b77b46e6).

> **⚠️ Correção aplicada em 2026-06-01 (duplicidade de lotes — [ALT-512](mention://issue/9f60bda6-6e35-4eed-80a1-af850a25fee5)).** Foi corrigida uma **dupla contagem** no Cenário (2) — Produção em capacidade nominal (Anexo A) e nas linhas de referência derivadas dela. A planilha-fonte (CERES 2021, aba `Parâmetros`) conta **lotes por tanque de 100 L / 10 kg** (10/semana → 43,5/mês → 522/ano = operações de módulo). Ao redefinir o lote como batelada combinada de **200 L / 20 kg** (dois módulos em paralelo), a versão Plentz manteve a contagem de 522/ano e multiplicou por 20 kg — contando cada tanque duas vezes. A capacidade nominal correta em 1 turno é de **~21,75 lotes de 200 L/mês (~261/ano)**, ou seja **5.220 kg de grafite e ~5.157 kg de produto/ano** — e não 10.315 kg/ano. Isso reverte exatamente o salto introduzido na v9 (ver §20 e §27). **Impactos:** produção nominal, grafite, custo unitário R$/kg (§9.3, §10) e a cobertura econômica de §7.1 (de ~101% para ~52% do OPEX no piso US$ 50/kg). **Não afeta** o Cenário (1) — Desenvolvimento nem o cheque do investidor §2-A, que são construídos sobre lotes de 100 L / 10 kg (na v12, esses valores são R$ 4,89 MM/ano e R$ 6,00 MM respectivamente, após o ajuste de equipe — mudança independente desta correção de lotes; ver §28). Detalhamento da correção: §27.

> **O que mudou nesta revisão (Plentz-07).** Esta é a v10 do levantamento consolidado, construída sobre a [[MGG3-LEV-P100-v9_Levantamento-Custos-Recomissionamento-Consolidado|v9]] (que permanece intocada como base histórica) e sobre a estrutura de cenários da revisão Plentz-06.b. A Plentz-07 faz três movimentos: (1) **incorpora as revisões conceituais de Flávio Plentz** à fase inicial do relatório — finalidade (§1) e glossário (§3); (2) **adota o Cenário (1) — Desenvolvimento como o cenário real e base desta versão**, na premissa de atividades piloto de **3 lotes-teste de 100 L por semana** (§8), por ser a projeção realista da operação da empresa logo após o investimento; e (3) **reposiciona o Cenário (2) — Produção em capacidade nominal como Anexo A** (§9), tratando-o explicitamente como projeção auxiliar (ferramenta para entender o custo de produção em regime nominal), e **não** como a realidade do Ano 1. Todos os blocos técnico-analíticos da v9 (§4.1–§4.5, §6.1–§6.6, CAPEX por pacotes, glossário, rastreabilidade §12, gates SSMA §11, pendências §22) permanecem reincorporados. Briefing: [ALT-488](mention://issue/514e7501-890e-4c1b-864a-11bdecd136bb).

---

## §1. Finalidade e leitura correta deste relatório

Este relatório apresenta uma estimativa consolidada dos custos para recomissionar e operar a P100, a planta piloto do MGgrafeno composta por sistemas KonMix de cisalhamento em tanques de 100 L. A nomenclatura histórica "reatores KonMix" é preservada como referência documental, mas a leitura técnica desta versão adota a formulação mais precisa de sistemas de cisalhamento. O objetivo não é tratar a P100 como uma fábrica comercial madura, nem como uma bancada de pesquisa pura. A P100 deve ser entendida como uma infraestrutura piloto escalável de uma startup de alta tecnologia que está **buscando investidores para passar a tecnologia a um estágio no qual possa entrar no mercado de grafeno, competitivamente em produtos, processos, serviços e soluções**. Isso significa que a planta precisa produzir uma sequência significativa de lotes de validação, gerar histórico de processo e qualificação do material, apoiar o desenvolvimento de formulações, atender projetos piloto com clientes visando o desenvolvimento de produtos à base de grafeno, e criar evidência técnica para entrar de forma robusta e qualificada nos mercados de tecnologias e produtos à base de grafeno.

Por essa razão, os números deste documento devem ser lidos como projeções técnico-econômicas de uma operação em desenvolvimento. Eles são suficientemente estruturados para orientar decisão, orçamento, priorização e negociação, mas ainda não substituem cotações formais de fornecedores, contratos definitivos de controle de qualidade, validação de desempenho por aplicação e definição completa do regime ideal de uso da planta.

A interpretação central é simples: a P100 é uma **plataforma de validação técnico-comercial com tecnologia de produção já claramente demonstrada em TRL7 e migrando para TRL8**. Seu papel mais importante não é vender grafeno em larga escala, mas fornecer material em uma escala que permita o desenvolvimento de soluções industriais, o desenvolvimento de novos materiais — como, por exemplo, grafenos funcionalizados e em diferentes formulações de entrega —, a validação do material produzido no mercado e a criação de demanda para o escalonamento da produção.

O plano de negócios do MGgrafeno deve buscar valor por solução, formulação, desempenho aplicado e relacionamento técnico com clientes. Ou seja, o modelo de negócios engloba: **(1)** produção e entrega do grafeno como insumo de alto valor agregado em relação ao insumo base, que é o grafite natural; **(2)** produção e entrega de grafenos modificados e personalizados; **(3)** "Grafeno como um Serviço", que se configura como entrega de soluções à base de grafeno por demanda de clientes, por exemplo através de projetos direcionados à introdução de grafeno em linhas de produtos e no portfólio de produtos e serviços de clientes.

**Como esta versão organiza a leitura econômica.** A v10 apresenta dois cenários operacionais distintos e não-misturáveis, mas com pesos deliberadamente diferentes:

- **Cenário (1) — Desenvolvimento (cenário REAL e base desta versão, corpo principal — §8):** é a projeção da realidade que esperamos ter assim que a empresa for investida pelo grupo IFHAN. Modela a P100 operando em atividades piloto de **3 lotes-teste de 100 L por semana** (156 lotes/ano). Os lotes desse cenário são testes de produção ou produções orientadas, sob medida, cujo objetivo é desenvolver tecnologias de processo de produção de grafeno e atender demandas de material (grafenos) para testes de aplicações — isto é, dar suporte ao desenvolvimento de novos produtos. A métrica correta é o custo operacional anual de sustentar essa capacidade técnica.
- **Cenário (2) — Produção em capacidade nominal (projeção auxiliar, Anexo A — §9):** modela a P100 como linha dedicada em 1 turno, operando em máxima capacidade exclusivamente para produzir grafeno (261 lotes de 200 L/ano — corrigido, ver §27). É um cenário **ferramental**, útil para entender o custo de produção em regime nominal, mas que **não** será a realidade do Ano 1 da empresa: a planta não iniciará suas atividades produzindo em capacidade nominal. Por isso este cenário é tratado como anexo e projeção auxiliar, e não como base de planejamento.

Nenhum dos dois cenários invalida o outro. Eles respondem a perguntas diferentes: o Cenário (1) informa quanto custa sustentar a operação real de desenvolvimento; o Cenário (2) informa, como ferramenta de projeção, qual seria o custo unitário de produção caso a planta fosse dedicada à capacidade nominal. Confundi-los produz análise econômica equivocada.

### §1.1 Guia de leitura por audiência

Este relatório tem destinatários definidos e em dois momentos. O **destinatário primário** são os sócios fundadores — **Flávio Plentz e Adelina Pinheiro** — que avaliarão e aprimorarão o documento junto a Rodrigo antes de qualquer passo externo. O **destinatário secundário** é o **grupo investidor IFHAN**, para o qual o relatório servirá, depois, como base sólida de negociação técnico-financeira do investimento (licenciamento da tecnologia junto a CDTN/UFMG e abertura da empresa em modelo 49/51). Use a tabela abaixo para localizar rapidamente as seções de maior relevância.

| Perfil | Seções de entrada | Aprofundamento |
|---|---|---|
| **Sócios fundadores (Flávio Plentz, Adelina Pinheiro)** | §1 (finalidade e posicionamento), §2 (indicadores consolidados), §8 (Cenário real de Desenvolvimento: custo operacional do Ano 1) | §5 (CAPEX de recomissionamento), §7 (referências de preço de mercado), §10 (reconciliação v9↔v10), §13 (sensibilidades), §22 (pendências antes de orçamento executivo) |
| **Grupo investidor (IFHAN)** | §2 (indicadores consolidados), §2-A (cheque do Ano 1 e racional IFHAN), §8 (custo operacional real), §7 (referências de preço de mercado) | §5 (CAPEX detalhado), §9/Anexo A (projeção de produção em capacidade nominal), §10 (reconciliação), §13 (sensibilidades), §22 (pendências) |
| **Parceiros técnicos (UFMG, CDTN)** | §3 (glossário), §4 (base operacional, ciclo, rendimentos, parâmetros por módulo), §11 (gates SSMA e compliance) | §6.1–§6.6 (composição detalhada de custos), §12 (rastreabilidade com fonte documental), §14 (próximos passos técnicos), §22 (pendências técnicas abertas) |

Os indicadores-chave em §2 são a porta de entrada comum. O cenário operacional real (Cenário 1, Desenvolvimento) está em §8; a projeção auxiliar de produção em capacidade nominal está no Anexo A (§9). A rastreabilidade de cada valor crítico está em §12.

---

## §2. Resultado consolidado em linguagem direta

A estimativa separa dois tipos de número que não devem ser confundidos: o dinheiro novo estimado para recolocar a planta existente em operação (CAPEX de recomissionamento) e o custo recorrente de operar (OPEX). O **indicador central desta versão é o OPEX do Cenário (1) — Desenvolvimento**, que é o custo operacional real esperado para a empresa logo após o investimento. A linha do Cenário (2) — Produção é a projeção auxiliar de capacidade nominal (Anexo A).

| Indicador                                                                                    |    Valor consolidado | Como interpretar                                                                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------- | -------------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **★ Cenário (1) — Desenvolvimento (REAL, base): OPEX caso-base**                             | **R$ 4.891.500/ano** | **Custo operacional real do Ano 1.** Premissa: 3 lotes-teste de 100 L/semana (156 lotes/ano); equipe de 9 pessoas (4 produção + 2 CQ + 3 aplicações); CQ por lote-teste. Faixa R$ 4,63–5,20 MM/ano conforme intensidade analítica. Detalhamento: §8                                        |
| CAPEX incremental para recomissionamento                                                     |           R$ 610.000 | Estimativa gerencial preliminar AACE Classe 4/5; faixa indicativa R$ 430–915k; requer vistoria, RFQ e gates documentais                                                                                                                                 |
| Base bruta histórica dos equipamentos da P100                                                |         R$ 1.680.560 | Planilha P100 2021: R$ 1.615.200 (produção) + R$ 65.360 (SSMA); sem depreciação acumulada                                                                                                                                                               |
| OPEX-base do Desenvolvimento (caixa, v12 — equipe 9 pessoas)                                  |     R$ 2.533.444/ano | Base de referência (**261 lotes de 200 L/ano = 5.220 kg grafite**, 20 kg/lote, equipe de 9 pessoas a R$ 10.000/mês, CQ US$5k/mês); sem depreciação. Atualizado da equipe v12 (+R$ 210.000 vs v11) — ver §28; base de lotes corrigida em §27                |
| OPEX-base do Desenvolvimento (técnico completo, v12)                                          |     R$ 2.700.020/ano | OPEX caixa + depreciação gerencial R$ 166.576                                                                                                                                                                                                           |
| Produção técnica de referência (v9, corrigida)                                               |         5.157 kg/ano | Capacidade calculada com 20 kg/lote × **261 lotes/ano** (= 5.220 kg grafite); referência técnica, não garantia de venda. Corrigido da duplicidade — ver §27                                                                                             |
| Cadências alternativas do Cenário (1) por campanhas                                          |  R$ 3,92–5,11 MM/ano | Leituras complementares do mesmo piloto, organizadas por campanhas (8/12/18 campanhas/ano de lotes de 200 L). Atualizado da equipe v12. Detalhamento: §8.2–§8.4                                                                                          |
| **Anexo A — Cenário (2) Produção em capacidade nominal (projeção auxiliar): OPEX caso-base** | **R$ 2.481.000/ano** | **Projeção, não realidade do Ano 1.** Linha dedicada em 1 turno, **261 lotes de 200 L/ano** (corrigido — ver §27), equipe enxuta de 5 pessoas + indiretos de mercado; custo por produto: GPC R$ 1.790/kg, NPG R$ 896/kg, Nanografite R$ 448/kg. Detalhamento: §9/Anexo A; reconciliação: §10 |

A leitura executiva é direta. Para decidir, planejar e negociar o investimento, o número que importa é o **OPEX do Cenário (1) Desenvolvimento (R$ 4,89 MM/ano, faixa R$ 4,63–5,20 MM)** — o custo real de operar a planta como infraestrutura de desenvolvimento de tecnologia e de produtos, com a equipe de 9 pessoas (4 produção + 2 CQ + 3 aplicações) definida na v12. Para o IFHAN, a leitura de funding do Ano 1 está consolidada em §2-A: **R$ 6,00 MM caso-base**, incluindo CAPEX de recomissionamento, OPEX Desenvolvimento e capital de giro, com ocupação CDTN Ano 1 = R$ 0 e licenciamento CDTN/UFMG fora do cheque. O Cenário (2) Produção (R$ 2,48 MM/ano) é uma ferramenta de projeção: mostra qual seria o custo unitário por produto se a planta fosse dedicada à capacidade nominal, mas esse não é o regime do primeiro ano. A diferença entre os dois reflete a estrutura técnica de desenvolvimento (equipe maior, CQ por lote-teste, cadência semanal de testes) que existe no cenário real e não na projeção de produção dedicada. Ver reconciliação completa em §10.

---

## §2-A. Seção do investidor IFHAN — quanto empenhar para a planta funcionar no Ano 1

> **Para quem lê esta seção.** Esta é a porta de entrada do grupo investidor **IFHAN** e o início do plano de negócios da empresa a ser criada. Ela responde, de forma direta e técnico-honesta, à única pergunta que importa para a decisão de investir: **quanto é preciso empenhar para colocar a P100 em operação no Ano 1, e por que isso faz sentido para o IFHAN.** Nenhum número aqui é promessa comercial; cada valor é rastreável às seções técnicas deste relatório (§5 CAPEX, §6/§8 OPEX, §6.6 capital de giro).

### §2-A.1 O racional IFHAN

A oportunidade não deve ser lida como a contratação de uma planta piloto, nem como uma aposta genérica em grafeno. Para o IFHAN, a P100 é uma **opção estratégica exclusiva sobre uma plataforma de materiais avançados para eficiência energética**, com aderência direta ao ecossistema CES (energia, condutividade, armazenamento, redução de perdas). Quatro perguntas guiam a leitura: por que o IFHAN, por que materiais, por que agora, por que exclusividade. A resposta curta: por um cheque de entrada contido para o padrão de uma plataforma industrial, o IFHAN compra **velocidade de implantação, posição em uma rota tecnológica alinhada ao seu campo natural, e exclusividade** sobre o licenciamento antes de a tese amadurecer publicamente.

### §2-A.2 O cheque do Ano 1 e a curva de caixa

O valor a empenhar para a planta funcionar no **Ano 1** é de **R$ 6,00 milhões (caso-base)**, dentro de uma faixa defensável de **R$ 5,46 MM a R$ 6,72 MM**. (Atualizado na v12 com a equipe de 9 pessoas do Cenário Desenvolvimento — ver §28.)

| Cenário | Valor a empenhar (Ano 1) | Composição |
|---|---:|---|
| Otimista / piso técnico | R$ 5,46 MM | CAPEX R$ 430k + OPEX R$ 4,63 MM + giro R$ 400k |
| **Caso-base** | **R$ 6,00 MM** | CAPEX R$ 610k + OPEX R$ 4,89 MM + giro R$ 500k |
| Conservador / teto de funding | R$ 6,72 MM | CAPEX R$ 915k + OPEX R$ 5,20 MM + giro R$ 599k |

**Composição do caso-base:**
- **Arranque (one-time): R$ 1,11 MM** — R$ 610k de CAPEX de recomissionamento (§5) + R$ 500k de capital de giro inicial (§6.6).
- **Operacional (recorrente): R$ 4,89 MM** — OPEX do Cenário Desenvolvimento, o cenário real do Ano 1 (§8.5), com a equipe de 9 pessoas. Já inclui energia.
- **Ocupação CDTN Ano 1: R$ 0** — sem locação e sem condomínio (ver §2-A.6 e §6.6).
- **Licenciamento CDTN/UFMG: fora deste cheque** — pago à parte pelo IFHAN via edital de oferta tecnológica.

**Curva de caixa.** O cheque precisa estar comprometido no início do Ano 1, mas o caixa sai escalonado: o esforço se concentra nos **primeiros 90 dias** (recomissionamento + arranque de giro), estabilizando em torno de **R$ 408 mil/mês** de OPEX a partir do 4º mês. O recomissionamento concentra o risco no início; depois a operação é previsível.

| Período | Desembolso (caso-base) |
|---|---:|
| Mês 1 | R$ 652k (CAPEX R$ 244k + OPEX R$ 408k) |
| Mês 2 | R$ 952k (CAPEX R$ 244k + giro R$ 300k + OPEX R$ 408k) |
| Mês 3 | R$ 730k (CAPEX R$ 122k + giro R$ 200k + OPEX R$ 408k) |
| Meses 4–12 | R$ 408k/mês (OPEX), total R$ 3,67 MM |
| **Total Ano 1** | **R$ 6,00 MM** |

### §2-A.3 O que o IFHAN compra além do custo operacional

O cheque não financia apenas execução; ele trava três ativos de investidor:

1. **Velocidade de implantação** — recolocar uma planta TRL7→TRL8 em operação em meses, não anos, aproveitando ativos existentes (base bruta histórica de R$ 1,68 MM, §5).
2. **Plataforma de materiais para eficiência energética** — acesso a material técnico em régua industrial e capacidade de desenvolver formulações sob medida, alinhadas ao ecossistema CES.
3. **Exclusividade / licenciamento separado (moat)** — o IFHAN paga o licenciamento à parte e **exige exclusividade** (premissa jurídica, §2-A.6). O investimento operacional preserva uma **janela estratégica**: se a tese avançar, a exclusividade reduz o risco de concorrência direta sobre a rota e melhora a posição negocial do grupo.

### §2-A.4 Aplicação prioritária: cobre-grafeno

A primeira tese de upside manifestada pelos investidores é o desenvolvimento de **liga cobre-grafeno**, que conecta a rota tecnológica à linguagem do IFHAN: eficiência energética, condutividade e performance industrial, com potencial de integração ao ecossistema CES. Como referência de mercado, a régua de **US$ 50–200/kg** para NPG/GNP técnico (§7.1) dimensiona o potencial econômico da rota — **como âncora de credibilidade, não como preço realizado**. A captura desse valor depende de validação técnica, especificação de produto, escala, contratos e qualificação junto ao comprador.

### §2-A.5 Por que a tese é assimétrica ("macaco gosta de banana?")

O argumento não é que o resultado esteja garantido — é que a **relação entre custo de entrada, controle estratégico e opção tecnológica é difícil de ignorar** para o IFHAN:

- **Custo de entrada contido** para o padrão de uma plataforma industrial (R$ 5,73 MM no Ano 1, concentrados nos primeiros 90 dias).
- **Risco comercial explicitado**, não escondido: a ocupação entra como R$ 0 no Ano 1 e o caso **não depende de uma curva agressiva de receita** para se sustentar.
- **Upside protegido por exclusividade** se a aplicação prioritária (cobre-grafeno) evoluir.
- **Esforço concentrado na abertura:** no Ano 2, sem repetir CAPEX e giro, o run-rate cai para **R$ 5,01 MM/ano** (R$ 4,89 MM de OPEX + R$ 120k de aluguel CDTN). O maior esforço de caixa está na implantação e estabilização, não em subsídio indefinido.

> Para o IFHAN, a P100 não é uma aposta em receita de Ano 1; é uma opção estratégica exclusiva sobre uma plataforma de materiais avançados para eficiência energética, com cobre-grafeno como primeira aplicação prioritária, financiada por um cheque inicial de R$ 6,00 MM (caso-base) e com o esforço de implantação concentrado nos primeiros 90 dias.

### §2-A.6 Leitura de risco honesta — condições de avanço

A atratividade se sustenta sobre fatos e premissas declaradas, não sobre promessa de venda. As condições para o avanço da tese são: **(1)** validação técnica da aplicação prioritária; **(2)** qualificação do produto junto ao comprador; **(3)** governança do licenciamento e da exclusividade; **(4)** disciplina de OPEX na faixa modelada; **(5)** construção de demanda. As pendências técnicas que condicionam o orçamento executivo (vistoria, RFQs, SAT, gates SSMA) estão em §22 e permanecem válidas: os números desta seção orientam decisão e negociação, mas não substituem orçamento cotado.

> **Atualização de premissa de ocupação (substitui a exclusão de §6.6).** Ano 1: sem locação e sem condomínio — o escopo de "condomínio" (reparos civis/elétricos/mecânicos, marcenaria, soldas, empilhadeira) já está absorvido por manutenção (§6.5) e utilidades (§6.4), e somá-lo seria dupla contagem; energia já está no OPEX (§6.4). A partir do **Ano 2**: locação de **R$ 10 mil/mês (R$ 120k/ano), sem reajuste**, sem condomínio autônomo salvo obrigação contratual distinta comprovada. Ponte: OPEX Ano 2 ≈ R$ 5,01 MM/ano.

## §3. Glossário

Para facilitar a leitura técnica, financeira e editorial do novo v10, os principais códigos e termos usados no relatório ficam organizados abaixo em ordem alfabética, com definição operacional no contexto da P100.

- **AACE**: Association for the Advancement of Cost Engineering. Referência usada neste relatório para classificar estimativas de custo por maturidade de engenharia. A estimativa de CAPEX de recomissionamento deve continuar tratada como AACE Classe 4/5, com faixa de incerteza compatível, até haver RFQs, propostas de fornecedores e engenharia mais fechada.
- **Alocação por complexidade técnica (4:2:1)**: critério econômico da v10 para distribuir o OPEX do Cenário Produção entre os produtos conforme esforço técnico relativo, e não apenas por massa física. Neste relatório, GPC absorve peso 4, NPG peso 2 e Nanografite peso 1. O residual físico não recebe receita nem margem no caso-base.
- **Campanha**: sequência planejada de lotes contíguos dedicada a um objetivo técnico-comercial específico, como desenvolvimento de aplicação, validação de processo, atendimento a parceiro ou produção sob encomenda. No Cenário Desenvolvimento, campanha é unidade de absorção de capacidade técnica; não deve ser confundida com operação contínua de fábrica plena.
- **CAPEX**: investimento de capital. Neste relatório, há duas leituras distintas: o CAPEX incremental de recomissionamento, isto é, dinheiro novo estimado para preparar a planta existente para voltar a operar; e a base bruta histórica dos equipamentos, correspondente aos valores registrados na planilha P100 de 2021 para produção e SSMA, sem depreciação acumulada.
- **Cenário (1) — Desenvolvimento (cenário real e base desta versão)**: leitura operacional em que a P100 funciona como planta piloto de desenvolvimento de tecnologia de produção de grafeno e de novos produtos/aplicações, com formulações, melhoria de processo, suporte a aplicações e produção orientada sob medida. É a projeção da realidade esperada para a empresa após o investimento do IFHAN. O caso-base desta v10 adota o regime de 3 lotes-teste de 100 L por semana (156 lotes/ano). A métrica correta é o custo anual de capacidade técnica; não é R$/kg por ocupação plena.
- **Cenário (2) — Produção em capacidade nominal (projeção auxiliar, Anexo A)**: leitura **ferramental** em que a P100 é hipoteticamente operada como linha dedicada em 1 turno, em máxima capacidade exclusivamente para produzir grafeno (261 lotes de 200 L/ano — corrigido, ver §27), com equipe fixa enxuta, mix produtivo GPC/NPG/Nanografite e custo unitário por produto. Serve para entender o custo de produção em regime nominal; **não** representa a realidade do Ano 1 e por isso é apresentado como anexo. A métrica é R$/kg por produto, por rendimento e alocação por complexidade técnica.
- **Comissionamento frio**: etapa de verificação e teste da planta sem carga real de processo e, quando aplicável, sem produto químico ou grafite. Serve para confirmar montagem, intertravamentos, sentido de rotação, instrumentação, comandos, estanqueidade, utilidades, alarmes, segurança e sequência operacional antes de expor a planta às condições reais de produção.
- **Comissionamento quente**: etapa de teste da planta em condições próximas ou equivalentes à operação real, com água ou meio de processo e, quando previsto no protocolo, carga de grafite ou lote teste. Serve para validar estabilidade operacional, temperatura, vazão, rotação, separação, balanço de massa, qualidade das frações e critérios de aceite antes de tratar a P100 como apta a campanhas regulares.
- **CQ**: controle de qualidade. Na leitura de recomissionamento da v9, CQ é tratado como serviço terceirizado junto à UFMG/CDTN, com orçamento de US$5.000/mês para análises como Raman, AFM, TG, gravimetria e outras. No novo v10, deve ficar separado entre CQ de caracterização por campanha/aplicação no Desenvolvimento e CQ rotineiro por especificação na Produção.
- **DA**: desenvolvimento de aplicações. Designa a frente técnico-comercial que transforma frações de grafeno e nanografite em formulações, protótipos, especificações de uso, propostas de projeto e evidências de desempenho para clientes, CDTN, UFMG e editais de fomento.
- **Depreciação gerencial**: cálculo econômico separado que reconhece o desgaste dos equipamentos ao longo do tempo. Não é pagamento anual a fornecedor e não está abatida no valor bruto histórico de R$1.680.560. No Cenário Produção, depreciação pode não fazer parte do OPEX caso-base dependendo da premissa; em Desenvolvimento é componente do OPEX técnico completo.
- **Editais de fomento**: chamadas públicas ou instrumentos competitivos de subvenção, cooperação ou financiamento à pesquisa, desenvolvimento e inovação. Incluem oportunidades que possam apoiar projetos de aplicação do MGgrafeno em parceria com grupos do CDTN e da UFMG.
- **FAT**: factory acceptance test, ou teste de aceite em fábrica. Aplica-se quando um equipamento ou retrofit for testado antes de instalação em campo.
- **GPC / FLG**: grafeno de poucas camadas, equivalente operacional ao termo internacional few-layer graphene.
- **GPB**: termo legado introduzido sem definição formal. Não deve ser usado como sigla oficial nesta nota. Quando a intenção for falar de grafeno técnico em pó, o texto deve usar GPC, FLG, GNP ou uma descrição técnica explícita.
- **HH**: homem-hora ou mão de obra. No Cenário Desenvolvimento, a equipe é de 9 pessoas (v12): um time de operação da planta piloto com 4 pessoas de produção + 2 de controle de qualidade, mais um time de Aplicações com 3 pessoas (desenvolvimento de aplicações e produtos à base de grafeno — GaaS); no Cenário Produção, a equipe fixa é de 5 pessoas (1 supervisor + 3 técnicos de produção + 1 técnico de CQ).
- **LPE**: liquid phase exfoliation, ou esfoliação em fase líquida. É a família de rotas de produção em que grafite é esfoliado em meio líquido por cisalhamento, sonicação ou mecanismos correlatos.
- **Lote à la carte**: lote sob especificação técnica do parceiro, com formulação e CQ sob medida. O custo inclui abertura de campanha, insumos, ensaios específicos e documentação técnica; não deve ser precificado como pó simples.
- **MC**: módulo de conversão. Cada MC corresponde ao conjunto formado por tanque de 100 L nominal e cisalhador KonMix.
- **MS**: módulo de separação. Corresponde ao conjunto de etapas e equipamentos usados após o cisalhamento para separar frações, incluindo decantação, decanter e/ou centrífuga de discos conforme a rota operacional.
- **Nanografite / NG**: nanoplaca de grafite, correspondente ao grafite finamente esfoliado, que é o produto da conversão **incompleta** de grafite em grafeno (revisão Plentz). Este produto **não pode ser classificado como grafeno**, embora o mercado, de forma frequente, se refira a este tipo de produto como grafeno. É o produto que, de fato, compõe a **maior parte do mercado de grafeno**. No modelo de custos da P100, é a fração de maior volume e menor valor técnico relativo; não é automaticamente GPC nem NPG, deve ser precificado separadamente, e reprocesso é tratado como sensibilidade, não caso-base.
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

A estimativa parte da planta P100, composta por dois módulos de conversão — cada um formado por um tanque de 100 L (volume nominal do equipamento) e um cisalhador KonMix —, operando em regime de um turno. Os dois módulos operam em paralelo dentro do mesmo ciclo de lote, gerando um volume nominal total de 200 L por lote. A referência de capacidade usada no cálculo é de **21,75 lotes de 200 L por mês, ou 261 lotes por ano** (corrigido da duplicidade de lotes — a planilha-fonte conta 43,5/mês de bateladas por tanque de 100 L, que combinadas dois a dois resultam em 21,75 bateladas de 200 L; ver §4.3 e §27). Cada lote parte de 20 kg de grafite como carga de entrada combinada dos dois módulos de conversão — 10 kg por tanque de 100 L, resultando em concentração nominal de 100 g/L (equivalente a 100 g/kg de dispersão líquida) por tanque —, com ciclo técnico de 10,75 horas.

Para garantia de leitura técnica inequívoca: a P100 possui dois módulos de conversão, cada um constituído por um tanque de 100 L (volume nominal) e um cisalhador KonMix, operando em paralelo. A carga de grafite de cada tanque de 100 L é de 10 kg, resultando em concentração nominal de 100 g/L por tanque. Com dois módulos combinados, a carga total por lote é de **20 kg de grafite (10 kg + 10 kg)** e o volume nominal total é de **200 L**. A unidade de referência do modelo é o quilograma (kg): 20,0 kg de entrada, ~19,76 kg de produção técnica por lote.

| Parâmetro operacional         |                                           Valor usado | Leitura no modelo                                             |
| ----------------------------- | ----------------------------------------------------: | ------------------------------------------------------------- |
| Módulos de conversão          | 2 unidades (tanque 100 L nominal + cisalhador KonMix) | Configuração P100                                             |
| Volume nominal total por lote |                                                 200 L | Operação paralela dos dois tanques de 100 L                   |
| Regime operacional            |                                               1 turno | Base de planejamento                                          |
| Lotes por mês (200 L)         |                                                 21,75 | Capacidade nominal econômica (corrigido — ver §4.3 e §27)     |
| Lotes por ano (200 L)         |                                                   261 | Teto nominal — ver §4.3                                       |
| Grafite por lote              |                                               20,0 kg | 10 kg por tanque × 2 tanques; concentração 100 g/L por tanque |
| Tempo técnico de ciclo        |                                          10,75 h/lote | Ciclo otimista do modelo — ver §4.1                           |
| Rendimento GPC/FLG            |                                                 0,80% | 0,160 kg/lote                                                 |
| Rendimento NPG/GNP            |                                                 5,00% | 1,000 kg/lote                                                 |
| Rendimento Nanografite        |                                                93,00% | 18,600 kg/lote                                                |
| Perdas de processo            |                                                 1,20% | 0,240 kg/lote                                                 |
| Produção técnica calculada    |                                        19,760 kg/lote |                                                               |
| Produção técnica anual        |                                       5.157,36 kg/ano | 19,760 × 261 (corrigido — ver §27)                            |

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

### §4.3 Origem da capacidade nominal e ramp-up defensável

A planilha-fonte (`Parâmetros`, CERES 2021) registra **Lotes = 10/semana, 1 turno, 5 dias/semana**, com `Carga de Grafite = 10 kg/lote` e `Volume do Lote = 105,6 L` — ou seja, **a unidade "lote" da fonte é uma batelada de um único tanque de 100 L (10 kg)**. O planilha computa **2 lotes/dia** (a tabela de produtividade usa `g/dia` = 2 × `g/lote`), que correspondem aos **dois módulos de conversão operando em paralelo**. Daí 10 lotes(100 L)/semana → 43,5 lotes(100 L)/mês → 522 operações de módulo/ano.

> **Correção de duplicidade (2026-06-01, [ALT-512](mention://issue/9f60bda6-6e35-4eed-80a1-af850a25fee5)).** Como este relatório define o **lote padrão como a batelada combinada de 200 L / 20 kg** (dois módulos em paralelo no mesmo ciclo — §4.5), a contagem precisa ser convertida: **2 lotes de 100 L em paralelo = 1 lote combinado de 200 L**. Logo, a capacidade nominal correta é **5 lotes de 200 L/semana → 21,75/mês → ~261/ano**, e **não** 522 lotes de 200 L/ano. A versão anterior manteve a contagem de 522 e a multiplicou por 20 kg/lote, contando cada tanque duas vezes (produção nominal aparecia como 10.315 kg/ano em vez de ~5.157 kg/ano). Fisicamente, um ciclo combinado de 200 L leva ~10,75 h — cabe em ~1 ciclo/dia, consistente com ~261 lotes/ano, e não com 522 lotes de 200 L. Detalhamento em §27.

**261 lotes de 200 L/ano deve ser lido como capacidade nominal do modelo econômico**, não como promessa operacional do primeiro ano. Para o primeiro ano pós-recomissionamento, a faixa defensável de ramp-up é **60–80% da capacidade nominal = ~157–209 lotes de 200 L/ano** (base prudente de planejamento: ~180–200 lotes). A evolução para o teto nominal depende de SAT formal, estabilidade de CQ e histórico de campanha reprodutível.

No **Cenário Desenvolvimento**, esse teto de infraestrutura é para campanhas; não é um regime de produção contínua. No **Cenário Produção**, é a capacidade nominal para o regime de 1 turno dedicado.

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

Quando as vazões históricas são extrapoladas para 200 L: decanter a 30–50 L/h exigiria ~4,0–6,7 h; centrífuga de discos a 55 L/h exigiria ~3,6 h. Em sequência: 7,6–10,3 h antes de setup, transições e limpeza — excede os 3,5 h do modelo. Isso é a principal pendência técnica da P100; não invalida o projeto, mas impõe o SAT como gate antes de tratar a capacidade nominal (261 lotes de 200 L/ano) como garantida.

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

O OPEX consolidado foi construído para refletir uma operação piloto realista. O modelo base adota a equipe de 9 pessoas do Cenário Desenvolvimento (v12) e o CQ terceirizado como custos centrais.

| Categoria | Premissa | Custo anual |
|---|---|---:|
| Mão de obra | 9 pessoas (4 produção + 2 CQ + 3 aplicações), salário médio R$ 10.000/mês, encargos 75% | R$ 1.890.000 |
| Controle de qualidade terceirizado | US$ 5.000/mês, câmbio R$ 5/US$ | R$ 300.000 |
| Matérias-primas e consumíveis de processo | Grafite 20 kg/lote × 261 lotes = 5.220 kg/ano (corrigido — ver §27) | R$ 118.713 |
| Utilidades | Energia, água e utilidades de processo | R$ 83.885 |
| Manutenção | 5% dos equipamentos produtivos + SSMA | R$ 81.510 |
| Secretaria | 1 pessoa a R$ 2.500/mês + encargos | R$ 52.500 |
| Consumíveis de SSMA | Base técnica preservada | R$ 6.836 |
| **OPEX caixa recorrente** | | **R$ 2.533.444** |
| Depreciação gerencial | Reconhecimento econômico do uso da infraestrutura | R$ 166.576 |
| **OPEX técnico completo** | | **R$ 2.700.020** |

### §6.1 Composição da equipe de 9 pessoas

A equipe do Cenário Desenvolvimento (v12) é de **9 pessoas**, organizadas em dois times: um **time de operação da planta piloto** com **4 pessoas de produção + 2 pessoas de controle de qualidade**, e um **time de Aplicações** com **3 pessoas** dedicadas ao **desenvolvimento de aplicações e produtos à base de grafeno** — a frente "Grafeno como um Serviço" (GaaS) descrita em §1. O salário médio bruto de R$ 10.000/mês deve ser lido como **média ponderada gerencial**, não como salário uniforme.

| Time | Função | Papel financeiro-operacional | Observação de custo |
|---|---|---|---|
| Operação da planta | Produção 1 — líder de processo | Preparação de lotes, setup de equipamentos, controle operacional, prioridades de campanha e indicadores de processo | Fundamental para repetibilidade; puxa a média salarial para cima (faixa ~R$ 15–20 mil) |
| Operação da planta | Produção 2 | Operação dos módulos de conversão e separação | Base do regime de 1 turno |
| Operação da planta | Produção 3 | Operação de lotes-teste, preparo, pesagem e movimentação | Reduz risco de parada por gargalo humano |
| Operação da planta | Produção 4 | Apoio à operação, limpeza, manutenção simples, utilidades e SSMA operacional | Se manutenção 100% terceirizada, redistribuir função |
| Operação da planta | Controle de qualidade 1 | Amostragem, cadeia de custódia, interface com laboratório externo | Mesmo com CQ terceirizado, alguém interno controla amostras e prazo de laudo |
| Operação da planta | Controle de qualidade 2 | Ensaios internos (gravimetria, dispersão), apoio à caracterização por campanha | Suporta CQ por lote-teste sem sobrecarregar o contrato externo |
| Aplicações (GaaS) | Desenvolvimento de aplicações/produtos 1 | Formulações, protótipos e especificações de uso de grafeno por aplicação | Conecta o material ao desempenho aplicado; motor do GaaS (§1) |
| Aplicações (GaaS) | Desenvolvimento de aplicações/produtos 2 | Projetos de aplicação com clientes/parceiros: desenvolvimento de produtos à base de grafeno e evidência de desempenho | Frente de valor por solução/serviço, não por kg de pó |
| Aplicações (GaaS) | Aplicações e fomento | Parceiros técnicos, propostas CDTN/UFMG, editais de fomento e captação não dilutiva | Cada pessoa-base custa ~R$ 210.000/ano (carregado); conecta operação, validação aplicada e captação não dilutiva (ver sensibilidade §13) |

O salário médio de R$ 10.000/mês é conservador para o líder de processo + os profissionais sêniores de desenvolvimento de aplicações, e elevado se a equipe for composta majoritariamente por operadores juniores. Os encargos de 75% são defensáveis por referência SINAPI 2025 (~71,29%) com margem para benefícios práticos (VT, VA, plano de saúde, seguro de vida, PPR).

> **Nota sobre o time de Aplicações.** Na v11, a frente de desenvolvimento de aplicações era exercida por **1 pessoa** (o "pesquisador de desenvolvimento de aplicações e fomento"). A v12 a **expande para um time de 3 pessoas**, dedicado a projetos de desenvolvimento de aplicações e produtos à base de grafeno no modelo Grafeno como um Serviço (§1). Isso fortalece a tese de valor por solução/serviço, mas concentra mais custo fixo na capacidade técnica antes da geração de receita — ver risco de subutilização em §8.4/§8.5.5 e sensibilidade em §13.

No **Cenário Produção**, a equipe fixa é distinta: **1 supervisor + 3 técnicos de produção + 1 técnico de CQ** (5 pessoas). Não somar com a equipe do Desenvolvimento.

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
| Grafite natural em pó | 20 kg/lote × 261 lotes = 5.220 kg/ano × R$ ~14,07/kg ≈ R$ 73.445 | Parte de R$ 118.713 | Corrigido da duplicidade de lotes (261 lotes de 200 L, não 522); cotação ±30% de incerteza — ver §27 |
| Triton X-100 (surfactante) | Concentração 0,1% na formulação | Parte de R$ 118.713 | Reagente de processo |
| NH4OH (ajuste de pH) | Consumo por lote | Parte de R$ 118.713 | pH-alvo 10,0 |
| Água tratada | Por ciclo de lote | Parte de R$ 118.713 | Utilidade de processo |
| Embalagens e materiais de acondicionamento | Por lote qualificado | Parte de R$ 118.713 | Varia por forma de entrega |
| **Total matérias-primas e consumíveis** | | **R$ 118.713/ano** | Faixa de incerteza ±30% até cotações vigentes |

### §6.4 Base de utilidades

| Utilidade | Base de estimativa | Custo anual | Observação |
|---|---|---:|---|
| Energia elétrica | Potência instalada × tempo × tarifa CEMIG histórica ~R$ 0,857/kWh; KonMix 3,2 kW × 5 h × 522 operações de módulo/ano (= 261 lotes de 200 L × 2 módulos) | Principal componente | Medir potência real em campo. A energia escala com horas-módulo, portanto a base de 522 operações de módulo permanece correta após a correção de lotes |
| Água tratada | Processo e limpeza | Componente menor | Mapear consumo no SAT |
| Ar comprimido | Instrumentação e equipamentos | Se aplicável | Validar se há compressor |
| Resfriamento / chiller | Friotec TFQF 09: 3,8 kW × 2,5 h/lote | Parte do total elétrico | |
| **Total utilidades** | Tarifa histórica CEMIG | **R$ 83.885/ano** | Faixa recomendada até medição: R$ 65–110 mil/ano |

### §6.5 Base da manutenção anual

A taxa de manutenção de **5% da base produtiva + SSMA** (R$ 81.510/ano) é adequada para o estágio de planejamento. Para recomissionamento de planta parada por anos, a taxa real pode ser superior nos dois primeiros anos (5–8%), normalizando após estabilização. Separar preventiva (rotina) de corretiva (incidentes) é crítico para gestão; a taxa atual mistura os dois sem discriminação.

### §6.6 Exclusões e capital de giro

| Item | Tratamento | Valor de referência |
|---|---|---|
| Capital de giro inicial | Exclusão explícita do modelo OPEX/CAPEX | Provisionar separadamente: ~R$ 422–633 mil para 2–3 meses de OPEX caixa mensal médio ~R$ 211.120/mês (equipe v12 de 9 pessoas; base de lotes corrigida — §27). **Nota:** as faixas de giro citadas em §2-A.2 (R$ 400k/500k/599k) são premissas de funding mantidas; o caso-base de R$ 500k permanece válido dentro da nova faixa, mas os limites otimista/conservador devem ser revalidados |
| Aluguel / ocupação | Premissa escalonada: Ano 1 sem locação e sem condomínio; Ano 2+ com locação de R$ 10 mil/mês (R$ 120k/ano), sem reajuste | Ano 1: R$ 0. Ano 2+: somar R$ 120k/ano ao OPEX Desenvolvimento. Não somar condomínio autônomo sem obrigação contratual distinta comprovada, para evitar dupla contagem com §6.4/§6.5 |
| Impostos comerciais, margem e inadimplência | Excluídos do modelo de custo | Incluir no plano de negócios |
| Ponto de equilíbrio operacional pleno | Não fecha sem preço validado, mix comercial e impostos | Declarado como limitação; não forçar número frágil |

| Indicador derivado (nominal, equipe v12; base de lotes corrigida — §27) | Valor |
|---|---:|
| Custo caixa por lote (200 L) | R$ 9.707 |
| Custo técnico completo por lote (200 L) | R$ 10.345 |
| Custo caixa por kg | R$ 491 |
| Custo técnico completo por kg | R$ 524 |
| OPEX caixa mensal de referência | R$ 211.120 |

---

## §7. Referências externas de preço e cobertura econômica

### §7.1 Faixa US$ 50–200/kg para NPG/GNP técnico

A faixa de **US$ 50–200/kg** (câmbio R$ 5,00) para NPG/GNP técnico é restaurada como a régua de mercado defensável para fins de benchmarking econômico e apresentação a investidores. Não é promessa de preço de venda.

Confirmação de cobertura econômica (equipe v12; base de lotes corrigida — ver §27): na P100 com produção nominal de **5.157 kg/ano**, a receita no piso de **US$ 50/kg** (câmbio R$ 5/US$) gera **R$ 1.289.340/ano**, cobrindo **~48% do OPEX Técnico Completo** de R$ 2.700.020/ano, antes de impostos, mix comercial e preço validado. No teto da régua de mercado (**US$ 200/kg**), a mesma produção geraria ~R$ 5,16 MM/ano, cobrindo com folga o OPEX nominal. **A planta não cruza o ponto de equilíbrio no piso da régua** — só o cruza acima de ~US$ 105/kg (NPG/GNP técnico). Esta é a leitura honesta para o investidor.

> **Correção da duplicidade de lotes.** Versões anteriores afirmavam cobertura de **~101%** no piso US$ 50/kg. Esse número decorria da dupla contagem de lotes: a v9 dobrou a carga por lote (10→20 kg) **sem** halvar a contagem de 522 lotes/ano, dobrando artificialmente a produção (de ~5.157 para 10.315 kg/ano) e a receita (de R$ 1,29 para R$ 2,58 MM/ano). Com a produção física correta (~5.157 kg/ano), a cobertura no piso volta a **~52%** sobre a base de equipe de 8 pessoas — exatamente o valor anterior à v9. (A equipe v12 de 9 pessoas eleva o OPEX e reduz essa cobertura para **~48%** — ver §28.) Ver §4.3, §20 e §27.

A mesma receita corrigida de R$ 1.289.340/ano cobre **~52% do OPEX Produção v10** (R$ 2.481.000/ano — Cenário Produção com equipe enxuta de 5 pessoas e indiretos de mercado, sem depreciação gerencial). Os dois denominadores (OPEX Técnico Completo do Desenvolvimento, agora com equipe de 9 pessoas, e OPEX Produção v10) são distintos: a cobertura no piso é de **~48% sobre o OPEX Técnico Completo do Desenvolvimento** e **~52% sobre o OPEX Produção**. Ver reconciliação em §10.

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

## §8. Cenário (1) — P100 Desenvolvimento (cenário REAL e base desta versão)

> **Este é o cenário real e a base desta v10.** Ele projeta o custo operacional da empresa a ser investida pelo grupo IFHAN, no regime que de fato esperamos no Ano 1: a P100 operando como infraestrutura de **desenvolvimento de tecnologia de produção de grafeno e de novos produtos**. O **caso-base** adotado é o regime de **3 lotes-teste de 100 L por semana (156 lotes/ano)** — lotes que são testes de produção ou produções orientadas, sob medida, para desenvolver processos e atender demandas de material para testes de aplicações. A modelagem completa desse caso-base está em **§8.5**, que passa a ser o coração deste cenário. As leituras por campanhas (§8.2–§8.4) são mantidas como **organizações alternativas e complementares** da mesma capacidade técnica de desenvolvimento — úteis para enxergar o custo quando a operação se agrupa em campanhas de 200 L em vez de testes semanais de 100 L —, não como cenários concorrentes.

| Indicador-âncora do cenário real (caso-base §8.5) | Valor |
|---|---:|
| Regime | 3 lotes-teste de 100 L por semana |
| Lotes por ano | 156 |
| Grafite processado | 1.560 kg/ano |
| OPEX caso-base | **R$ 4.891.500/ano** (faixa R$ 4,63–5,20 MM conforme intensidade de CQ; equipe de 9 pessoas — v12) |
| Produção técnica | GPC 12,5 kg · NPG 78,0 kg · Nanografite 1.450,8 kg / ano |

### §8.1 Premissas técnicas

A P100 opera como **planta piloto de desenvolvimento tecnológico**, suporte a aplicações finais, melhoria de processos de produção de grafeno e produção orientada/sob encomenda para parceiros (lotes à la carte). No caso-base real desta versão (§8.5), essa operação assume a forma de **3 lotes-teste de 100 L por semana**; as leituras por campanhas abaixo (§8.2–§8.4) descrevem a mesma planta quando os lotes são agrupados em campanhas de 200 L. Em qualquer das leituras, a operação é por demanda técnica, não por ocupação contínua, e a ociosidade planejada faz parte do custo de P&D.

| Bloco | Premissa |
|---|---|
| Regime | Operação por campanhas com ociosidade planejada; não modelar como fábrica plena |
| Mix | Desenvolvimento próprio, suporte a aplicações, caracterização/formulação e lotes sob encomenda |
| Equipe técnica | 9 pessoas (v12): time de operação da planta (4 produção + 2 CQ) + time de Aplicações (3: desenvolvimento de aplicações e produtos à base de grafeno — GaaS, ver §1 e §6.1) |
| CQ | Caracterização por campanha e aplicação (Raman, granulometria, teor de sólidos, morfologia, estabilidade/funcionalidade); variável e menos repetitivo que Produção |
| Lotes à la carte | Variabilidade deliberada de processo; custo marginal inclui preparação, formulação, setup, retrabalho analítico, amostras e documentação técnica. **Não precificar só por kg** |
| Risco técnico | Separação de 200 L e ciclo real ainda são incertezas de escala |

### §8.2 Leitura alternativa por campanhas — estrutura de custos (12 campanhas/ano, lotes de 200 L)

> *Leitura complementar, não o caso-base.* As tabelas de §8.2 a §8.4 descrevem a mesma capacidade técnica de desenvolvimento organizada em campanhas de lotes de 200 L (dois módulos), em vez do regime semanal de testes de 100 L que é o caso-base real (§8.5). Servem para comparar custo por campanha e custo marginal de lote à la carte.

| Bloco | Natureza | Custo anual | % do total |
|---|---|---:|---:|
| Equipe técnica D1 carregada 2026 — 9 pessoas (¹) | Direto fixo | R$ 2.405.700 | 55,2% |
| CQ externo mínimo e caracterização | Direto fixo | R$ 300.000 | 6,9% |
| Consumíveis fixos de laboratório/aplicações | Direto fixo | R$ 120.000 | 2,8% |
| Manutenção técnica de prontidão | Direto fixo | R$ 240.000 | 5,5% |
| Campanhas de desenvolvimento e à la carte | Direto variável | R$ 960.000 | 22,0% |
| Overhead institucional alocado ao piloto | Indireto fixo | R$ 180.000 | 4,1% |
| SSMA, licenças operacionais e suporte comum | Indireto fixo | R$ 96.000 | 2,2% |
| Administração, TI e apoio compartilhado | Indireto fixo | R$ 60.000 | 1,4% |
| **Total** | | **R$ 4.361.700** | **100,0%** |

Decomposição base: 92,3% direto / 7,7% indireto; 78,0% fixo / 22,0% variável.

> **(¹) Premissa de equipe (v12) e ajuste salarial 2026:** o §6 e §12 adotam a equipe de 9 pessoas (4 produção + 2 CQ + 3 aplicações) a salário médio bruto de R$ 10.000/mês e encargos 75% = R$ 1.890.000/ano (base). O D1 carregado 2026 aplica a essa mesma equipe o salário médio bruto 2026-ajustado de R$ 12.728/mês (R$ 10.000 + ~27%), resultando em R$ 2.405.700/ano. As duas leituras são compatíveis: a base é a referência a R$ 10.000/mês; D1 carregado é a projeção de capacidade técnica para o ano de operação. Não são premissas concorrentes — são horizontes temporais diferentes. Se a intenção dos sócios for fixar R$ 10.000/mês também no caso-base (sem o ajuste 2026), substituir R$ 2.405.700 por R$ 1.890.000 reduz o OPEX caso-base D1.b para ~R$ 4,38 MM (ver §28).*

### §8.3 Modelo por campanha e lote à la carte

Custo variável por campanha base (5 lotes): **R$ 80.000**, composto por insumos produtivos (R$ 17,5k), utilidades (R$ 4,5k), CQ externo incremental e ensaios de aplicação (R$ 35k), manutenção corretiva leve (R$ 7,5k) e setup/formulação/documentação (R$ 15,5k).

Custo marginal de lote à la carte adicional dentro de campanha aberta: **R$ 18.000/lote** (insumos R$ 3,5k, utilidades R$ 0,9k, CQ incremental R$ 4,5k, MO incremental R$ 3k, limpeza/setup/retrabalho R$ 5k, resíduo R$ 1,1k).

**Regra de uso comercial:** proposta à la carte deve separar três camadas: (i) taxa de abertura de campanha (setup/CQ/documentação); (ii) custo marginal por lote adicional; (iii) prêmio técnico por especificação, urgência, confidencialidade, retrabalho ou propriedade intelectual.

### §8.4 Leitura econômica e sensibilidade por cadência

A métrica relevante para Desenvolvimento **não é R$/kg nem OPEX por lote nominal**. A P100 piloto carrega estrutura fixa de capacidade técnica de ~R$ 3,40 MM/ano (equipe v12 carregada); as campanhas apenas absorvem essa capacidade.

| Cadência | OPEX anual | OPEX mensal | Lotes/ano | Uso vs. nominal | Variável anual implícita |
|---|---:|---:|---:|---:|---:|
| Conservador — 8 campanhas (~4 lotes/campanha) | R$ 3.921.700 | R$ 326.808 | 32 | 12,3% | R$ 520.000 |
| Base — 12 campanhas (5 lotes/campanha) | R$ 4.361.700 | R$ 363.475 | 60 | 23,0% | R$ 960.000 |
| Intensivo — 18 campanhas (~6 lotes/campanha + à la carte) | R$ 5.111.700 | R$ 425.975 | 108 | 41,4% | R$ 1.710.000 |

Risco econômico relevante: **subutilização da capacidade técnica**. Poucos lotes não reduzem a maior parte do OPEX; apenas reduzem a absorção do custo fixo.

---

### §8.5 Caso-base do cenário real — 3 lotes-teste/semana (módulo único, 100 L)

> **Este é o caso-base do Cenário (1) e o cenário operacional real desta v10** (briefing [ALT-488](mention://issue/514e7501-890e-4c1b-864a-11bdecd136bb)). É a projeção da operação que esperamos no Ano 1 da empresa investida pelo IFHAN. Os indicadores desta seção são os números de referência do relatório; as leituras por campanhas (§8.2–§8.4) são complementares.

Este caso-base modela a P100 em regime de **testes contínuos semanais**: 3 lotes por semana, cada lote usando um único módulo de conversão (100 L nominal, 10 kg de grafite por lote). Os lotes têm por objetivo desenvolver tecnologias de processo de produção de grafeno e atender demandas de material (grafenos) para testes de aplicações — ou seja, são testes de produção ou produções orientadas, sob medida, que dão suporte ao desenvolvimento de novos produtos. Briefing original do regime: [ALT-487](mention://issue/6760ed5e-5d9b-4b1b-9c5e-e448f3b85377), 2026-05-31.

A qualificação "100 litros" descreve o uso de um único módulo KonMix (100 L nominal), diferenciando-o do lote padrão de 200 L (dois módulos em paralelo) que fundamenta o D1 base e o D2.

#### §8.5.1 Parâmetros técnicos e produção anual

| Parâmetro | D1.b — 3 testes/semana (100L) | D1 base — 12 campanhas (200L) | Observação |
|---|---|---|---|
| Lotes por semana | 3 | ~1,15 | 2,6× mais lotes/semana |
| Volume por lote | 100 L (1 módulo) | 200 L (2 módulos paralelos) | 2º módulo disponível para prep paralela |
| Grafite por lote | 10 kg | 20 kg | Concentração 100 g/L mantida por módulo |
| Lotes por ano | **156** | 60 | D1.b usa 29,9% da capacidade nominal em massa (1.560 kg de 5.220 kg; nominal = 261 lotes de 200 L/ano — corrigido, §27) |
| Volume total anual | 15.600 L | 12.000 L | 30% mais volume que D1 base |
| Grafite anual | **1.560 kg** | 1.200 kg | 30% a mais em carga de processo |
| Uso capacidade nominal | 29,9% | 23,0% | 1,3× mais uso da infraestrutura (corrigido — §27) |
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

Os custos fixos do D1 caso-base (R$ 3.401.700/ano, equipe v12 de 9 pessoas) permanecem integralmente. Os custos variáveis são recalculados para lotes de 100L em regime de testes contínuos, referenciados nos componentes do §8.3.

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
| Custos fixos — idênticos ao D1 caso-base (§8.2) | Fixo | R$ 3.401.700 | 69,5% |
| Insumos (156 lotes × R$ 1.750) | Direto variável | R$ 273.000 | 5,6% |
| Utilidades (156 lotes × R$ 450) | Direto variável | R$ 70.200 | 1,4% |
| CQ incremental (156 lotes × R$ 2.500) | Direto variável | R$ 390.000 | 8,0% |
| MO incremental (156 lotes × R$ 1.800) | Direto variável | R$ 280.800 | 5,7% |
| Limpeza, setup e documentação (156 lotes × R$ 2.500) | Direto variável | R$ 390.000 | 8,0% |
| Resíduo (156 lotes × R$ 550) | Direto variável | R$ 85.800 | 1,8% |
| **Total variável** | | **R$ 1.489.800** | **30,5%** |
| **OPEX total D1.b caso-base** | | **R$ 4.891.500** | **100,0%** |

Decomposição: 93,1% direto / 6,9% indireto; 69,5% fixo / 30,5% variável.

#### §8.5.4 Comparação com D1 base e sensibilidade de CQ

**Comparação do D1.b com os demais cenários D1:**

| Cenário | Lotes/ano | Vol/lote | OPEX anual | OPEX/lote | OPEX/kg grafite | Grafite/ano |
|---|---:|---|---:|---:|---:|---:|
| D1 conservador (8 campanhas × ~4 lotes, 200L) | 32 | 200 L | R$ 3.921.700 | R$ 122.553 | R$ 6.128 | 640 kg |
| D1 base (12 campanhas × 5 lotes, 200L) | 60 | 200 L | R$ 4.361.700 | R$ 72.695 | R$ 3.635 | 1.200 kg |
| **D1.b — 3 testes/semana (100L, este sub-cenário)** | **156** | **100 L** | **R$ 4.891.500** | **R$ 31.356** | **R$ 3.136** | **1.560 kg** |
| D1 intensivo (18 campanhas + à la carte, 200L) | 108 | 200 L | R$ 5.111.700 | R$ 47.331 | R$ 2.366 | 2.160 kg |

O D1.b tem o **menor custo por lote** (R$ 31.356 — melhor diluição do fixo sobre 156 lotes), o **maior número de lotes por ano** e o **maior volume de grafite processado** entre os cenários D1, mas o **maior custo anual** do grupo D1. O custo por kg de grafite processado (R$ 3.136) é levemente superior ao D1 intensivo, mas inferior ao D1 base e conservador.

**Sensibilidade por intensidade de CQ:**

| Premissa CQ/lote | Custo variável total | OPEX total | Leitura operacional |
|---|---:|---:|---|
| Básico — gravimetria interna + Raman bimestral (R$ 800/lote) | R$ 1.224.600 | **R$ 4.626.300** | Monitoramento de processo sem caracterização por lote |
| **Moderado — Raman + gravimetria por lote (R$ 2.500/lote)** | **R$ 1.489.800** | **R$ 4.891.500** | Testes com objetivo técnico por lote (caso-base) |
| Intensivo — caracterização completa por lote-teste (R$ 4.500/lote) | R$ 1.801.800 | **R$ 5.203.500** | Desenvolvimento de aplicação por lote, equivalente a D1 campanha |

**Faixa D1.b: R$ 4.626.000–5.204.000/ano** dependendo da intensidade analítica por lote-teste. (Variáveis recalculadas a partir dos componentes do §8.5.2 com a equipe v12; a faixa varia apenas pela linha de CQ por lote.)

#### §8.5.5 Métricas e leitura econômica

| Indicador | D1.b (3 testes/semana, 100L) | D1 base (12 campanhas, 200L) |
|---|---:|---:|
| OPEX total anual | **R$ 4.891.500** | R$ 4.361.700 |
| Incremento vs D1 base | **+R$ 529.800 (+12%)** | — |
| Lotes por ano | 156 | 60 |
| Grafite processado | 1.560 kg | 1.200 kg |
| GPC produzido | 12,5 kg | 9,6 kg |
| NPG produzido | 78,0 kg | 60,0 kg |
| Nanografite produzida | 1.450,8 kg | 1.116,0 kg |
| Custo por lote (amortizado) | R$ 31.356 | R$ 72.695 |
| Custo por kg grafite | R$ 3.136 | R$ 3.635 |
| Custo por litro processado | R$ 314 | R$ 363 |
| Uso da capacidade nominal em massa (5.220 kg/ano = 261 lotes de 200 L) | 29,9% | 23,0% |
| OPEX mensal de referência | R$ 407.625 | R$ 363.475 |

**Pontos de atenção específicos do D1.b:**

1. **Segundo módulo ocioso:** Durante os 3 lotes/semana de 100L, o segundo KonMix fica disponível. Isso é um recurso — pode ser usado para prep de formulações distintas, testes de condições diferentes de pH ou concentração, ou lotes de outra aplicação em paralelo, sem aumentar o OPEX.

2. **Capacidade de separação favorável:** 100L é metade do volume que impõe o gargalo de separação documentado em §4.5 e §4.3 (7,6–10,3h para 200L). Para 100L, as estimativas de separação caem para ~1,5–3,3h, tornando o ciclo de 100L mais confiável que o de 200L.

3. **Custo por campanha-equivalente:** Se as 3 sessões semanais forem agrupadas em ciclos mensais (13 lotes/mês), o custo por mês de operação é R$ 407.625 — maior que o D1 base (R$ 363.475/mês) mas com 2,6× mais lotes/mês e 30% mais material processado.

4. **Produção superior em volume absoluto:** O D1.b produz mais GPC (12,5 vs 9,6 kg/ano), mais NPG (78,0 vs 60,0 kg/ano) e mais Nanografite (1.450,8 vs 1.116,0 kg/ano) que o D1 base. Para fins de geração de amostras para parceiros UFMG/CDTN ou para qualificação comercial, isso é vantajoso.

5. **Risco econômico:** Igual ao D1 base — a maior parte do OPEX (69,5%) é fixo e não cai com redução de lotes. Se por qualquer motivo a cadência cair de 3 para 1 lote/semana, o OPEX cai apenas ~20% (de R$ 4.891.500 para ~R$ 3.898.300).

> **Conexão com outros cenários e seções:** para comparar com a projeção auxiliar de produção em capacidade nominal (custo por kg de produto em regime dedicado), ver o **Anexo A (§9)**. Para reconciliação dos dois cenários com a base v9, ver §10. Para benchmark de preço e cobertura econômica, ver §7.

---

## §9. Anexo A — Cenário (2): P100 Produção em capacidade nominal (projeção auxiliar)

> **Leia este bloco como anexo e projeção auxiliar, não como o cenário real.** O Cenário (2) é uma **ferramenta** para entender qual seria o custo de produção da P100 caso ela operasse em **regime de capacidade nominal** — 1 turno dedicado exclusivamente a produzir grafeno, 261 lotes de 200 L/ano (corrigido da duplicidade — ver §27). **A planta não iniciará suas atividades produzindo em capacidade nominal**; portanto este cenário **não** é a realidade do Ano 1 da empresa. Ele é útil para projetar o custo unitário por produto em operação nominal e para a negociação futura de escalonamento, mas o cenário operacional real, base de planejamento, é o Cenário (1) — Desenvolvimento (§8). As premissas de equipe seguem o que foi definido na P100 v10 para cada cenário (ver §6.1 e nota ² em §9.2).

### §9.1 Premissas técnicas

A P100 é hipoteticamente operada como **operação dedicada de produção em 1 turno**, com a mesma base física da v9 e três condições de rendimento aplicadas sobre o mesmo OPEX. Trata-se de uma projeção de capacidade nominal, não da operação real do primeiro ano.

| Bloco | Premissa |
|---|---|
| Regime | 1 turno, produção dedicada; capacidade nominal 261 lotes de 200 L/ano como teto (corrigido — ver §27), não caso único |
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

> **(²) Derivação da equipe D2:** 5 pessoas (1 supervisor + 3 técnicos de produção + 1 técnico de CQ), salário médio bruto estimado ~R$ 6.800–7.000/mês por pessoa e encargos efetivos ~78–80% (SINAPI 2025 + VT, VA, plano de saúde) → total ~R$ 59.400/mês. Perfil de equipe enxuta de produção, distinto da equipe D1 com 9 pessoas a salário médio R$ 12.728/mês 2026-ajustado (ver §8.2 nota ¹). Não somar as duas equipes.*

> **(³) Insumos de produção D2 vs matérias-primas v9:** o valor de R$ 30.950/mês (R$ 371.400/ano) é superior ao item correspondente da v9 (R$ 118.713/ano = R$ 9.893/mês, corrigido da duplicidade de lotes — ver §27). A diferença reflete as exigências adicionais do Cenário Produção dedicado em relação ao modelo v9: embalagens específicas por produto (GPC, NPG e Nanografite exigem acondicionamento e rotulagem separados), reagentes de limpeza entre bateladas de produtos distintos, materiais de amostragem por lote para CQ de liberação, e consumíveis de processo com especificação de produção. A faixa de incerteza de ±30% aplicada às matérias-primas da v9 (§6.3) é igualmente válida aqui até cotações formais.*

### §9.3 Custo unitário por produto — três condições

Base de cálculo: **435 kg de grafite seco alimentado por mês (21,75 lotes de 200 L × 20 kg)** — corrigido da duplicidade de lotes (ver §27); o valor anterior de 870 kg/mês contava 43,5 lotes de 200 L em vez de 21,75. O OPEX D2 (R$ 2.481.000/ano) é mantido como estimativa bottom-up; como a massa produzida cai pela metade e o OPEX é mantido, o custo unitário R$/kg **dobra** em relação à versão anterior (ver caveat ao final desta seção). Critério de alocação: **massa ponderada por complexidade técnica** com pesos GPC = 4, NPG = 2, Nanografite = 1. Justificativa: custo por massa pura subaloca GPC/NPG porque as frações nobres concentram esforço de separação, CQ e especificação; alocação por receita exigiria preço de venda ainda não validado.

| Condição | GPC kg/mês | NPG kg/mês | Nanografite kg/mês | Residual kg/mês | GPC R$/kg | NPG R$/kg | Nanografite R$/kg |
|---|---:|---:|---:|---:|---:|---:|---:|
| Conservadora 0,5/5/93/1,5 | 2,18 | 21,75 | 404,55 | 6,53 | **R$ 1.810** | **R$ 906** | **R$ 452** |
| Média histórica v9 0,8/5,0/93,0/1,2 | 3,48 | 21,75 | 404,55 | 5,22 | **R$ 1.790** | **R$ 896** | **R$ 448** |
| Otimista 2/16/80,5/1,5 | 8,70 | 69,60 | 350,18 | 6,53 | **R$ 1.578** | **R$ 788** | **R$ 394** |

O OPEX total não muda entre as condições — o que muda é a massa produzida por produto e, portanto, o custo unitário. As massas/mês acima foram corrigidas para a base de 435 kg de grafite/mês (21,75 lotes de 200 L); os custos R$/kg são ~2× os da versão anterior, que partia da base duplicada de 870 kg/mês.

> **Caveat sobre o OPEX D2 nesta correção.** O custo unitário acima mantém o OPEX D2 caso-base (R$ 2.481.000/ano) inalterado e divide pela massa corrigida. Parte do OPEX D2 é variável (insumos de produção, nota ³ em §9.2, estimados em R$ 371.400/ano para a base antiga); se esses insumos forem reescalonados para o volume corrigido (~metade), o OPEX D2 cairia para ~R$ 2,3 MM/ano e o R$/kg ficaria modestamente abaixo dos valores acima. Recomenda-se revalidar a composição variável do OPEX D2 com cotações antes de uso externo — ver §27.

### §9.4 Leitura econômica

Sensibilidade de indiretos (mercado): R$ 2,18–2,97 MM/ano. Ponto de equilíbrio operacional pleno não fecha sem preço de venda validado, mix comercial por produto e impostos.

> **Conexão com outros cenários e seções:** para comparar com o Cenário Desenvolvimento (custo por campanha e capacidade técnica), ver §8. Para reconciliação dos dois cenários com a base v9, ver §10. Para benchmark de preço e cobertura econômica do piso US$ 50/kg sobre o OPEX D2, ver §7.1.

---

## §10. Reconciliação custo/kg v9↔v10

> Esta reconciliação trata dos custos unitários por produto, que pertencem à **projeção auxiliar de Produção em capacidade nominal (Anexo A, §9)**. O custo operacional do cenário real (Cenário 1 — Desenvolvimento) é o OPEX anual de capacidade técnica de §8 (R$ 4,89 MM/ano caso-base, equipe v12 de 9 pessoas), não um R$/kg por ocupação plena.

A diferença entre o custo técnico médio do Desenvolvimento (R$ 524/kg) e a projeção de Produção R$ 1.790/R$ 896/R$ 448 não é contradição — é mudança de pool e método de alocação. (Valores de Produção corrigidos da duplicidade de lotes — ver §27.)

| Dimensão | Desenvolvimento (base, equipe v12) | v10 Produção (Cenário D2) |
|---|---|---|
| Equipe | 9 pessoas (equipe técnica completa) | 5 pessoas (equipe enxuta de produção) |
| OPEX caixa | R$ 2.533.444/ano (sem depreciação) | R$ 2.481.000/ano (caso-base, inclui indiretos de mercado) |
| OPEX técnico completo | R$ 2.700.020/ano (caixa + depreciação R$ 166.576) | — (depreciação não incluída no caso-base D2) |
| Residual D2 vs base caixa Desenvolvimento | — | −R$ 52.444/ano (D2 é agora *mais barato* que a base caixa do Desenvolvimento; equipe menor compensa indiretos) |
| Residual D2 vs base técnico completo | — | −R$ 219.020/ano (D2 *mais barato* que a base com depreciação; mudança de pool reforça) |
| Custo médio ponderado | R$ 524/kg (OPEX técnico completo / 5.157 kg) | R$ 481/kg físico (OPEX D2 / 5.157 kg — média sem alocação por produto) |
| Produto individual | Custo médio unificado (não desagregado por produto) | GPC R$ 1.790, NPG R$ 896, Nanografite R$ 448 (alocação 4:2:1 por complexidade técnica — ver §9.3) |

**Nota de leitura crítica:** com a equipe v12 de 9 pessoas no Desenvolvimento, o D2 caso-base (R$ 2.481.000/ano) passa a ser *mais barato* que a base de OPEX caixa do Desenvolvimento (R$ 2.533.444/ano) em R$ 52.444/ano. A equipe menor do D2 (5 vs 9 pessoas) gera economia de ~R$ 1.177.200/ano, mas os indiretos empresariais de mercado adicionados (R$ 712.800/ano — benchmark §7.2) e a maior estrutura de insumos de produção e manutenção absorvem a maior parte dessa economia. Frente ao OPEX *técnico completo* do Desenvolvimento (R$ 2.700.020/ano, que inclui R$ 166.576/ano de depreciação gerencial não presente no D2 caso-base), o D2 é mais barato em R$ 219.020/ano.

**Leitura para o investidor:** as duas leituras coexistem e respondem a perguntas diferentes. O custo técnico completo médio do Desenvolvimento, R$ 524/kg, é base de planejamento e cobertura econômica. v10 Produção R$ 1.790/R$ 896/R$ 448 é o custo por produto em regime dedicado com equipe enxuta e indiretos de mercado de EPP. Comparar diretamente os dois sem declarar a diferença de pool e método de alocação gera equívoco analítico.

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
| Resíduos, efluentes e emissões em regime estabilizado | Dimensionar geração mensal em 21,75 lotes de 200 L/mês (43,5 operações de módulo), segregação, armazenamento, transporte, destinação, efluentes de lavagem | Lei 12.305/2010; CONAMA 430/2011; DN COPAM 217/2017 | SSMA/Compliance + Operações | Pendente |
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
| Equipe operacional, CQ e Aplicações | 9 pessoas (4 produção + 2 CQ + 3 aplicações); salário médio R$ 10.000/mês; encargos 75%; R$ 1.890.000/ano | Premissa v12 ([ALT-539](mention://issue/8dfd745d-8a55-408f-81ec-c2394f430b44)) | Estrutura do Cenário Desenvolvimento. Não somar com equipe enxuta de Produção |
| Faixa externa de preço de referência | US$ 50–200/kg para NPG/GNP técnico | Benchmark externo v9; revalidado em §7 | Régua de mercado. A US$ 50/kg e câmbio R$ 5/US$, receita no piso (R$ 1.289.340/ano) cobre ~48% do OPEX Técnico Completo do Desenvolvimento (R$ 2.700.020 — equipe v12, base §7.1) e ~52% do OPEX Produção v10 (R$ 2.481.000 — base §9.2). Equilíbrio só acima de ~US$ 105/kg; ver §7.1 e §10. |
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
| Lotes por mês | 43,5 bateladas de 100 L/mês = 21,75 lotes de 200 L/mês | Aba Parâmetros da planilha P100: 10 lotes/semana, 1 turno, 5 dias/semana (a fonte conta tanques de 100 L) | Capacidade nominal econômica; em lotes de 200 L = 21,75/mês — ver §4.3/§27 |
| Capacidade nominal anual | 261 lotes de 200 L/ano (= 522 operações de módulo de 100 L) | Corrigido: 21,75 × 12; ver §27 | Teto nominal. Não vender como performance do primeiro ano |
| Ramp-up defensável | ~157–209 lotes de 200 L/ano; base prudente ~180–200/ano | Inferência: 60–80% de 261 | Faixa técnica para o primeiro ano |
| Carga de grafite por lote | 20 kg/lote combinado | v9 + confirmação do titular: 10 kg/tanque × 2 tanques | Premissa operacional central. Corrige v8 (10 kg combinado = 5 kg/tanque) |
| Concentração operacional | 100 g/L por tanque | Lote 20210720Pa: 10 kg em tanque de 100 L | Base da rota econômica P100 |
| Matérias-primas e consumíveis | R$ 118.713/ano | Base v9 corrigida; grafite 20 kg/lote × 261 lotes = 5.220 kg + Triton X-100, NH4OH, água, embalagens | OPEX caixa produtivo para 261 lotes de 200 L/ano; incerteza ±30% — ver §27 |
| Utilidades | R$ 83.885/ano | Potência instalada × tempo × tarifa CEMIG histórica ~R$ 0,857/kWh | Ordem de grandeza. Faixa prudente: R$ 65–110 mil/ano |
| OPEX caixa anual (base Desenvolvimento) | R$ 2.533.444/ano | Soma §6 (equipe v12; lotes corrigidos — §27) | Base de custo caixa da P100 piloto com equipe de 9 pessoas |
| OPEX técnico completo (base Desenvolvimento) | R$ 2.700.020/ano | OPEX caixa + depreciação gerencial R$ 166.576 | Base para custo técnico completo de R$ 524/kg |
| Custo técnico médio | R$ 524/kg; R$ 10.345/lote | R$ 2.700.020 / 5.157,36 kg e / 261 lotes | Leitura executiva/banco para custo médio do mix |
| Capital de giro inicial | ~R$ 422–633 mil | 2–3 meses de OPEX caixa mensal médio ~R$ 211.120 (equipe v12) | Exclusão consciente do CAPEX e OPEX; provisionar separadamente. Faixas de §2-A a revalidar (caso-base R$ 500k permanece válido) |
| Desenvolvimento — OPEX anual de capacidade técnica | R$ 4.361.700/ano; faixa R$ 3.921.700–5.111.700/ano | v12 D1 (equipe 9 pessoas); detalhamento [ALT-446](mention://issue/5774ebcb-dcc5-427d-90b6-101a9a603715) | **Linha de cenário.** Aplica ao Cenário Desenvolvimento. Mede capacidade técnica anual, não custo fabril por kg |
| Desenvolvimento — custo por campanha | R$ 80.000 por campanha base de 5 lotes | v10 D1; composição detalhada em §8.3 | **Linha nova v10.** Não dividir por kg vendido |
| Desenvolvimento — custo marginal à la carte | R$ 18.000/lote adicional dentro de campanha aberta | v10 D1; composição detalhada em §8.3 | **Linha nova v10.** Piso de custo, não preço |
| Produção — OPEX mensal/anual caso-base | R$ 206.750/mês; R$ 2.481.000/ano | v10 D2; reconciliado em §10 | **Linha nova v10 reconciliada.** Pool distinto do v9 técnico completo; diferença de R$ 9.020/ano explicada em §10 (corrigido — §27) |
| Produção — custo unitário conservador | GPC R$ 1.810/kg; NPG R$ 906/kg; Nanografite R$ 452/kg | v10 D2; 0,5%/5%/93%/1,5%; alocação 4:2:1 | **Linha nova v10.** Rendimento conservador (corrigido — §27) |
| Produção — custo unitário média histórica | GPC R$ 1.790/kg; NPG R$ 896/kg; Nanografite R$ 448/kg | v10 D2; 0,8%/5,0%/93,0%/1,2%; alocação 4:2:1 | **Linha nova v10.** Caso-base (corrigido — §27) |
| Produção — custo unitário otimista | GPC R$ 1.578/kg; NPG R$ 788/kg; Nanografite R$ 394/kg | v10 D2; 2%/16%/80,5%/1,5%; alocação 4:2:1 | **Linha nova v10.** Sensibilidade otimista; pendente de validação gravimétrica (corrigido — §27) |
| Alocação por complexidade | Pesos GPC=4, NPG=2, Nanografite=1; residual sem receita | Critério CFO v10 D2; reconciliado em §10 | **Linha nova v10.** Para precificação técnica; não é preço de venda |
| Indiretos de mercado — Produção (recomendado) | R$ 59.400/mês; R$ 712.800/ano | Benchmark externo §7.2; faixa R$ 34–100k/mês | **Linha nova v10.** EPP independente. Separar benchmark externo de premissa interna |
| Indiretos compartilhados — Desenvolvimento | R$ 28.000/mês estimado; R$ 336.000/ano na estrutura fixa D1 | v10 D1; uso da infraestrutura ALTOE | **Linha nova v10.** Só no Desenvolvimento; não comparar com EPP sem declarar diferença de perímetro |

---

## §13. Sensibilidades que mais afetam o custo

Os custos são sensíveis principalmente a três fatores: volume anual efetivo, equipe e controle de qualidade.

Na base atual (5,16 t/ano, R$ 524/kg técnico completo — equipe v12, lotes corrigidos §27):
- Se a produção efetiva cair para 3,6 t/ano: R$ 750/kg.
- Se a produção efetiva subir para 7,2 t/ano: R$ 375/kg.
- Para ramp-up de 157–209 lotes de 200 L/ano: R$ 654–870/kg técnico completo.

Cada variação de R$ 50 mil/ano no contrato de CQ altera o custo em ~R$ 9,70/kg. Cada pessoa adicional na equipe de Aplicações (GaaS) — ou em qualquer função, a salário-base de R$ 10.000/mês — custa +R$ 210 mil/ano (+~R$ 41/kg) antes de qualquer receita ou subvenção gerada; a v12 já incorpora um time de Aplicações de 3 pessoas (vs. 1 na v11).

**Para o Cenário Produção:**

| Posição | Variável crítica | Caso baixo | Base | Caso alto | Impacto |
|---:|---|---:|---:|---:|---|
| 1 | Indiretos C2 mensais | R$ 34k | R$ 59,4k | R$ 100k | Nanografite R$ 392–536/kg; OPEX R$ 181,35–247,35k/mês |
| 2 | Rendimento NPG | 5,0% | 5,0% | 16,0% | Nanografite R$ 448 → R$ 410/kg |
| 3 | Rendimento Nanografite | 80,5% | 93,0% | 93,0% | Nanografite R$ 508 → R$ 448/kg |
| 4 | Rendimento GPC | 0,5% | 0,8% | 2,0% | Nanografite R$ 452 → R$ 432/kg |

**Para o Cenário Desenvolvimento:**

| Posição | Variável crítica | Caso baixo | Base | Caso alto | Impacto |
|---:|---|---:|---:|---:|---|
| 1 | Cadência de campanhas | 8 | 12 | 18 campanhas/ano | OPEX R$ 3,92–5,11 MM/ano |

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
| Validação da capacidade do módulo de separação para 200 L | Estimativas de tempo de separação para 200 L (7,6–10,3 h sequencial) excedem os 3,5 h usados no modelo. Principal pendência técnica: valida ou invalida o ciclo de 10,75 h e a produção nominal de 261 lotes de 200 L/ano (5.157 kg/ano). Deve medir vazão, rotação, RCF quando disponível, retirada de sólidos, transições e limpeza. | Alta |
| Vistoria física da planta P100 | Confirma estado real dos ativos, utilidades, itens fora de serviço e escopo de recomissionamento. Fundamento para converter R$ 610 mil de estimativa gerencial em orçamento cotado. | Alta |
| RFQs/cotações formais | Convertem R$ 610 mil de estimativa AACE Cl.4/5 em orçamento contratável. | Alta |
| Protocolo de comissionamento | Define critérios de aceite para comissionamento frio, quente e teste de performance. Inclui cronoanálise formal do ciclo com 200 L, rotação real do KonMix e agitadores, temperatura, pH, vazão e balanço de massa. | Alta |
| Campanha gravimétrica pós-recomissionamento | Valida os rendimentos das três condições (conservadora/média/otimista). Sem ela, o custo por produto no Cenário Produção é premissa, não performance documentada. | Alta (Cenário Produção) |
| SAT com validação de ciclo e rendimentos | Teste de aceite com carga real: cronoanálise, medição de rotações, vazões e balanço de massa. Gate para tratar P100 como apta a campanhas regulares. | Alta |
| Contrato/proposta de CQ externo | Valida a premissa de US$ 5.000/mês com métodos incluídos, volume de amostras, prazo e SLA. | Média |
| Laudos, ARTs e gates SSMA aplicáveis (ver §11) | Liberam ou condicionam operação segura e regular. Lista detalhada em §11. | Média |
| Atualização de cotações de matérias-primas | Grafite, Triton X-100, NH4OH e embalagens devem ser cotados com fornecedores para confirmar premissa de R$ 118.713/ano (faixa ±30%; corrigido da duplicidade de lotes — §27). | Média |
| Medição ou contratação de utilidades | Confirmar tarifa elétrica real e mapear água, ar comprimido, resfriamento e efluentes para refinar o valor de R$ 83.885/ano. | Média |
| Plano de contratação da equipe | Especificar os 9 papéis do Desenvolvimento (4 produção + 2 CQ + 3 aplicações; salários individuais, regime, cronograma) e os 5 do Cenário Produção. | Média |
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

---

## §25. Changelog da Revisão Plentz-06.b para a Revisão Plentz-07

Esta revisão (Plentz-07) incorpora as **revisões conceituais de Flávio Plentz** à fase inicial do relatório e **reestrutura a hierarquia dos cenários** conforme briefing de Rodrigo ([ALT-488](mention://issue/514e7501-890e-4c1b-864a-11bdecd136bb), 2026-05-31). **Nenhum número financeiro existente foi recalculado.** A mudança é de posicionamento, finalidade conceitual e leitura por audiência. Contexto societário registrado: o IFHAN, com outros investidores, pagará o licenciamento da tecnologia MGgrafeno junto a CDTN/UFMG e abrirá a empresa em modelo 49/51 (controle do IFHAN); os destinatários primários do relatório são os sócios Flávio Plentz e Adelina Pinheiro.

| Bloco | Mudança incorporada |
|---|---|
| Frontmatter | `revisao: Plentz-07`; título e `status` reescritos para refletir Desenvolvimento como cenário real e Produção como Anexo A; adicionado `clientes_destinatarios` (Flávio Plentz, Adelina Pinheiro; IFHAN secundário); `audiencia` atualizada; `issue_revisao_7: ALT-488` |
| Cabeçalho do documento | Reescrito o bloco de abertura: novo título, nota "Para quem lê este relatório" (sócios + IFHAN, exigência de conteúdo técnico e honesto) e nota "O que mudou nesta revisão" (três movimentos da Plentz-07) |
| §1 — Finalidade (revisão conceitual Plentz) | Posicionamento atualizado para "startup buscando investidores para passar a tecnologia a um estágio no qual possa entrar no mercado de grafeno, competitivamente em produtos, processos, serviços e soluções"; TRL reescrito para "tecnologia de produção já claramente demonstrada em TRL7 e migrando para TRL8"; modelo de negócios numerado (1) insumo de alto valor, (2) grafenos modificados/personalizados, (3) Grafeno como um Serviço; repositionamento explícito do Cenário (1) Desenvolvimento como real/base e Cenário (2) Produção como projeção auxiliar/anexo |
| §1.1 — Guia de leitura | Reescrito para os destinatários reais: primário sócios fundadores (Flávio Plentz, Adelina Pinheiro), secundário IFHAN; parceiros técnicos UFMG/CDTN mantidos |
| §2 — Resultado consolidado | Tabela reordenada: Cenário (1) Desenvolvimento (R$ 4.624.200/ano, 156 lotes/ano, 3 lotes-teste de 100 L/semana) promovido a indicador central marcado com ★; Cenário (2) Produção rebaixado a Anexo A (projeção auxiliar); leitura executiva reescrita |
| §3 — Glossário (revisão conceitual Plentz) | Verbete **NG/Nanografite** reescrito conforme Plentz: "produto da conversão incompleta de grafite em grafeno, que não pode ser classificado como grafeno embora o mercado frequentemente assim o trate, e que compõe a maior parte do mercado de grafeno"; verbetes de Cenário (1) e Cenário (2) atualizados com a nova hierarquia |
| §8 — Cenário (1) Desenvolvimento | Promovido a cenário real e base da versão; banner de abertura e tabela-âncora; §8.5 (3 lotes-teste/semana, 100 L) reposicionado como **caso-base** (não mais "sub-cenário"); §8.2–§8.4 (campanhas de 200 L) reclassificados como leituras alternativas/complementares da mesma capacidade técnica |
| §9 — Cenário (2) Produção → Anexo A | Retitulado "Anexo A — Cenário (2): P100 Produção em capacidade nominal (projeção auxiliar)"; banner explicitando que é ferramenta de projeção de regime nominal e **não** a realidade do Ano 1; premissas de equipe da v10 preservadas |
| §10 — Reconciliação | Nota de cabeçalho esclarecendo que os custos unitários por produto pertencem à projeção auxiliar (Anexo A); custo do cenário real é o OPEX anual de §8 |
| Premissas de equipe | Preservadas integralmente para ambos os cenários (8 pessoas no Desenvolvimento real; 5 pessoas na projeção de Produção nominal), conforme nota técnica do briefing |

---

## §26. Changelog da Revisão Plentz-07 para a Revisão Plentz-08

Esta revisão (Plentz-08) versiona a v11 como sucessora sequencial da v10 Plentz-07, sem alterar a v10 histórica. A mudança é focal: acrescentar a seção dedicada ao investidor IFHAN e explicitar a premissa de ocupação Ano 1 → Ano 2 sem dupla contagem residual. A seção foi redigida em [ALT-497](mention://issue/cacde773-f920-4da7-ada8-1c074261874d), com insumos de [ALT-492](mention://issue/25873de5-ef7f-4ae9-9e2e-ea14d0acac71) a [ALT-496](mention://issue/622152af-0851-4330-b1a3-c91732aff0ae), e versionada em [ALT-498](mention://issue/0d6d34f2-35aa-4770-aa78-44a4b77b46e6).

| Bloco | Mudança incorporada |
|---|---|
| Frontmatter | `codigo_fonte: MGG3-LEV-P100-v11`; `versao: 11`; `revisao: Plentz-08`; `base_anterior: MGG3-LEV-P100-v10`; adicionado `issue_revisao_8: ALT-491` e `subfrentes_rev08` com ALT-492..ALT-498 |
| Cabeçalho do documento | Adicionada nota "O que mudou nesta revisão (Plentz-08)" com vínculo à issue-mãe ALT-491, integração ALT-497 e versionamento ALT-498 |
| §2-A — Seção do investidor IFHAN | Nova seção inserida logo após §2, respondendo o cheque do Ano 1: R$ 5,73 MM caso-base, faixa R$ 4,99–6,57 MM; composição CAPEX + OPEX Desenvolvimento + capital de giro; ocupação Ano 1 R$ 0; licenciamento CDTN/UFMG fora do cheque |
| §2-A — Narrativa estratégica | Incorporados racional IFHAN, aplicação prioritária cobre-grafeno, exclusividade/licenciamento separado e leitura de risco honesta; números apresentados como premissas rastreáveis, não promessa comercial |
| §6.6 — Exclusões e capital de giro | Substituída a linha "Aluguel / ocupação — Excluído" pela premissa escalonada: Ano 1 sem locação/condomínio; Ano 2+ com locação de R$ 10 mil/mês (R$ 120k/ano), sem condomínio autônomo salvo obrigação contratual distinta comprovada |
| Coerência anti-dupla-contagem | Explicitado que energia já está em §6.4 e reparos/escopo de condomínio já estão absorvidos por manutenção (§6.5) e utilidades (§6.4), portanto não há soma residual cega de condomínio |

---

## §27. Correção da duplicidade de lotes (2026-06-01, [ALT-512](mention://issue/9f60bda6-6e35-4eed-80a1-af850a25fee5))

**Quem solicitou e por quê.** Rodrigo levantou a suspeita de uma "duplicidade semântica" no número de lotes da capacidade nominal: a P100 tem capacidade nominal de pouco mais de 43 lotes/mês, mas esse número se refere a lotes de **100 L** (um tanque), e o relatório o estava tratando como lotes de **200 L** (dois tanques combinados). Verificação e correção em [ALT-512](mention://issue/9f60bda6-6e35-4eed-80a1-af850a25fee5).

**A causa-raiz.** A planilha-fonte (`P100_Custo de Produção - CLT_2021 (CERES)`, aba `Parâmetros`) define o **lote** como uma batelada de **um tanque de 100 L = 10 kg de grafite** (`Carga de Grafite = 10 kg/lote`, `Volume do Lote = 105,6 L`). Os parâmetros `Lotes = 10/semana` e `Lotes/Mês = 43,5` (→ 522/ano) contam **bateladas por tanque de 100 L**; a tabela de produtividade da fonte usa `g/dia` = 2 × `g/lote`, ou seja **2 lotes/dia = os dois módulos operando em paralelo**.

Ao longo das revisões, o relatório passou a definir o lote padrão como a **batelada combinada de 200 L / 20 kg** (dois módulos em paralelo — §4.5), o que é fisicamente correto. O erro foi **manter a contagem de 522 lotes/ano e multiplicá-la por 20 kg/lote**, contando cada tanque duas vezes. Isso é visível no changelog §20 (v8→v9): a v9 "dobrou a carga de 10 para 20 kg/lote" e, com isso, "a produção anual de referência **dobra de 5.157 para 10.315 kg/ano**" — esse salto não foi uma correção física, foi a introdução da dupla contagem. A capacidade física em massa nunca mudou: ~5.220 kg de grafite/ano.

**A correção.** Adotada a definição consistente **lote = batelada combinada de 200 L / 20 kg**, com capacidade nominal em 1 turno de **~21,75 lotes/mês = ~261 lotes/ano** (= 522 operações de módulo de 100 L). Fisicamente: um ciclo combinado de 200 L leva ~10,75 h, cabendo em ~1 ciclo/dia, consistente com ~261 lotes/ano. Os totais corrigidos coincidem exatamente com os valores pré-v9 (v8), conforme registrado no próprio §20.

**Antes → depois (valores corrigidos):**

| Grandeza | Antes (com duplicidade) | Depois (corrigido) |
|---|---:|---:|
| Lotes nominais (200 L) | 43,5/mês · 522/ano | **21,75/mês · 261/ano** |
| Grafite processado nominal | 10.440 kg/ano | **5.220 kg/ano** |
| Produção técnica nominal | 10.314,72 kg/ano | **5.157,36 kg/ano** |
| Matérias-primas (§5/§6.3) | R$ 192.177/ano | **R$ 118.713/ano** |
| OPEX caixa v9 | R$ 2.396.908/ano | **R$ 2.323.444/ano** |
| OPEX técnico completo v9 | R$ 2.563.484/ano | **R$ 2.490.020/ano** |
| Custo técnico médio | R$ 249/kg · R$ 4.912/lote | **R$ 483/kg · R$ 9.540/lote** |
| Receita no piso US$ 50/kg | R$ 2.578.750/ano | **R$ 1.289.340/ano** |
| Cobertura no piso US$ 50/kg | ~101% / ~104% | **~52% / ~52%** |
| Custo unitário média (GPC/NPG/Nanografite) | R$ 895 / R$ 448 / R$ 224 | **R$ 1.790 / R$ 896 / R$ 448** |

**Impacto na leitura econômica.** A planta **não cruza o ponto de equilíbrio no piso da régua de mercado** (US$ 50/kg): cobre ~52% do OPEX nominal. O equilíbrio ocorre acima de **~US$ 96/kg** de NPG/GNP técnico — dentro da régua US$ 50–200/kg, mas não no piso. A afirmação anterior de "~101% — cruza a linha de equilíbrio" era artefato da dupla contagem.

**O que NÃO mudou (por esta correção de lotes).** O Cenário (1) — Desenvolvimento (corpo principal, §8) e o cheque do investidor §2-A são construídos sobre lotes de **100 L / 10 kg** e **não** foram afetados por esta correção de duplicidade: 156 lotes-teste/ano de 100 L = 1.560 kg de grafite/ano permanecem corretos. (Os valores em reais desse cenário — OPEX R$ 4,89 MM/ano e cheque R$ 6,00 MM — foram posteriormente atualizados pela mudança de composição da equipe na v12, mudança **independente** desta correção de lotes; ver §28.) A linha de energia (§6.4) também permanece, pois escala com horas-módulo (522 operações de módulo = 261 lotes × 2 módulos).

**Caveat aberto para revalidação.** O custo unitário R$/kg da Produção (§9.3) foi recalculado mantendo o OPEX D2 (R$ 2.481.000/ano) inalterado e dividindo pela massa corrigida — leitura conservadora. Parte do OPEX D2 é variável (insumos, §9.2 nota ³); se reescalonada ao volume corrigido, o OPEX D2 cairia para ~R$ 2,3 MM/ano e o R$/kg ficaria modestamente abaixo dos valores acima. Recomenda-se revalidar a composição variável do OPEX D2 com cotações antes de uso externo. Os changelogs históricos §15–§26 e §24 (que descrevem a evolução ~101%/~104%) são preservados como registro; ficam superados por esta seção §27.

---

## §28. Changelog da v11 para a v12 (Ajuste de equipe do Cenário P&D, [ALT-539](mention://issue/8dfd745d-8a55-408f-81ec-c2394f430b44))

Esta v12 é sucessora sequencial da v11 (Plentz-08 + correção de lotes), que permanece intocada como base histórica. **A mudança é focal: redefinir a composição da equipe do Cenário (1) — Desenvolvimento (P&D)** a pedido dos sócios. Nenhuma premissa do Cenário (2) — Produção (Anexo A) foi alterada.

**O que mudou.** A equipe do Desenvolvimento passa de **8 para 9 pessoas**, reorganizada em dois times:
- **Time de operação da planta piloto: 6 pessoas** — 4 para atividades de produção (uma como líder de processo) + 2 para controle de qualidade.
- **Time de Aplicações: 3 pessoas** — dedicadas ao desenvolvimento de aplicações e produtos à base de grafeno (modelo "Grafeno como um Serviço" — GaaS, §1): formulações, projetos de aplicação com clientes/parceiros e captação não dilutiva (CDTN/UFMG, editais de fomento). Expande para 3 pessoas a frente que na v11 era exercida por 1 pesquisador de aplicações.
- **Salário médio: R$ 10.000/mês** (base) + 75% de encargos.

**Premissa salarial e convenção da v11 (decisão a confirmar).** A v12 preserva a estrutura de duas leituras da v11: (a) a **base** a R$ 10.000/mês = **R$ 1.890.000/ano** (§6, §12); e (b) o **caso-base do cenário real (§8.5)** com o salário 2026-ajustado de R$ 12.728/mês (R$ 10.000 + ~27%, convenção "carregado 2026" da v11, nota ¹ em §8.2) = **R$ 2.405.700/ano**. **Se a intenção dos sócios for fixar R$ 10.000/mês também no caso-base** (sem o ajuste 2026), substituir R$ 2.405.700 por R$ 1.890.000 resultaria em: OPEX caso-base ~**R$ 4.375.800/ano** (em vez de R$ 4.891.500), faixa ~R$ 4,11–4,69 MM, e cheque §2-A caso-base ~**R$ 5,49 MM** (em vez de R$ 6,00 MM). Esta decisão deve ser confirmada antes de uso externo.

**Antes → depois (caso-base, convenção carregado 2026 mantida):**

| Grandeza | v11 (8 pessoas) | v12 (9 pessoas) |
|---|---:|---:|
| Mão de obra base (§6) | R$ 1.680.000/ano | **R$ 1.890.000/ano** |
| Equipe carregada 2026 (§8) | R$ 2.138.400/ano | **R$ 2.405.700/ano** |
| OPEX caixa base (§6) | R$ 2.323.444/ano | **R$ 2.533.444/ano** |
| OPEX técnico completo base (§6) | R$ 2.490.020/ano | **R$ 2.700.020/ano** |
| Custos fixos D1 (§8) | R$ 3.134.400/ano | **R$ 3.401.700/ano** |
| **OPEX caso-base Desenvolvimento (§8.5)** | **R$ 4.624.200/ano** | **R$ 4.891.500/ano** |
| Faixa caso-base por intensidade de CQ | R$ 4,16–5,06 MM | **R$ 4,63–5,20 MM** |
| Cadência por campanhas (§8.4) | R$ 3,65–4,84 MM | **R$ 3,92–5,11 MM** |
| **Cheque do investidor §2-A (caso-base)** | **R$ 5,73 MM** | **R$ 6,00 MM** |
| Faixa do cheque §2-A | R$ 4,99–6,57 MM | **R$ 5,46–6,72 MM** |
| OPEX mensal de estabilização (§2-A) | R$ 385 mil/mês | **R$ 408 mil/mês** |
| Run-rate Ano 2 (§2-A.5) | R$ 4,74 MM/ano | **R$ 5,01 MM/ano** |
| Custo técnico médio | R$ 483/kg | **R$ 524/kg** |
| Cobertura no piso US$ 50/kg (OPEX téc. completo) | ~52% | **~48%** |
| Ponto de equilíbrio (NPG/GNP técnico) | ~US$ 96/kg | **~US$ 105/kg** |

**Seções recalculadas:** §2 (resultado consolidado), §2-A (cheque do investidor IFHAN, curva de caixa, run-rate Ano 2), §3 (glossário, verbete HH), §6 (tabela de OPEX e §6.1 composição da equipe), §6.6 (capital de giro e indicadores derivados), §7.1 (cobertura econômica), §8 (tabela-âncora, §8.2 campanhas e nota ¹, §8.4 cadências, §8.5.2/3/4/5 caso-base D1.b), §10 (reconciliação), §12 (rastreabilidade), §13 (sensibilidades), §22 (plano de contratação).

**O que NÃO mudou:** a base física e operacional (§4, lotes, rendimentos, ciclo), o CAPEX (§5, R$ 610k), o Cenário (2) — Produção / Anexo A (§9) e sua equipe enxuta de 5 pessoas, os gates SSMA (§11) e a correção de duplicidade de lotes (§27). Os demais custos do OPEX (CQ terceirizado, matérias-primas, utilidades, manutenção, secretaria) permanecem inalterados; apenas a mão de obra do Desenvolvimento foi alterada.
