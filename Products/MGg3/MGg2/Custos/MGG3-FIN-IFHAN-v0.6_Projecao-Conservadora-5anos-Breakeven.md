---
codigo_fonte: MGG3-FIN-IFHAN-v0.6-PROJ5
titulo: Projecao conservadora de 5 anos, custo da Vertical e ponto de breakeven
produto: MGgrafeno / MGG3
tipo: anexo de modelo financeiro (visao conservadora)
data: 2026-06-11
issue: ALT-566
issue_origem: ALT-570
autor: Carmen
status: rascunho para validacao do CFO (Julio)
---

# Projecao conservadora de 5 anos — custo da Vertical e breakeven

> **Uso.** Complementa o Modelo Financeiro v0.6 (Julio/ALT-570) com duas pecas que faltavam: (A) o **custo anual de uma Vertical de desenvolvimento** com nucleo minimo de 2 pesquisadores e (B) uma **projecao de 5 anos deliberadamente conservadora** com ramp-up por Vertical, para responder **quando ocorre o breakeven**. Postura: pessimista por construcao. A premissa de fundo e que projecoes otimistas no setor de grafeno falham com frequencia — entao aqui o vies e para baixo.

---

## A. Custo anual de uma Vertical de desenvolvimento (nucleo: 1 senior + 1 junior)

**Premissa de equipe.** O nucleo minimo de cada Vertical e de **dois pesquisadores**: um **senior** (PhD, lidera a rota tecnica e a relacao com a ICT ancora) e um **junior** (MSc, execucao de bancada/ensaio). A planta P100/P500 e compartilhada — o custo abaixo e **incremental** por Vertical, nao recria estrutura industrial.

**Base salarial (referencia citavel).** Pesquisador em Quimica CLT, salario.com.br (CBO 203125, levantamento 2025): **senior ~R$ 11.083/mes**; junior ancorado na faixa inicial da mesma CBO (~R$ 6.000/mes). Sobre o salario aplico **encargos CLT de 70%** (mesma premissa dos levantamentos de custo P100/P500), que ja absorve 13o, ferias, FGTS e INSS.

| Componente | Calculo | Custo anual |
|---|---|---:|
| Pesquisador senior (carregado) | R$ 11.083/mes x 12 x 1,70 | R$ 0,226 MM |
| Pesquisador junior (carregado) | R$ 6.000/mes x 12 x 1,70 | R$ 0,122 MM |
| **Subtotal pessoal** | | **R$ 0,348 MM** |
| Bancada, consumiveis e CQ externo | ~30% do pessoal | R$ 0,104 MM |
| Overhead / rateio (espaco, utilidades, coordenacao) | ~20% do pessoal | R$ 0,070 MM |
| **Custo anual da Vertical (nucleo)** | | **~R$ 0,52 MM/ano** |

**Leitura.** Uma Vertical em regime de nucleo custa **~R$ 0,52 MM/ano**. Esse e o "tijolo" replicavel do modelo de plataforma. **Referencia alternativa (fomento):** se o nucleo roda sobre bolsa CNPq DTI (sem encargos CLT, isento), o desembolso efetivo cai — e exatamente essa diferenca que o fomento nao-dilutivo captura. A projecao de 5 anos abaixo usa a base CLT (mais cara/conservadora) e credita o fomento como abatimento parcial.

---

## B. Projecao conservadora de 5 anos

### B.1 Premissas de receita (vies pessimista)

**Preco realizado (tecnico, abaixo do caso-base US$ 96/kg), FX 5,18:**

| | Ano 1 | Ano 2 | Ano 3 | Ano 4 | Ano 5 |
|---|---:|---:|---:|---:|---:|
| Preco realizado (US$/kg) | — | — | 70 | 80 | 90 |
| Preco realizado (R$/kg) | — | — | 362,6 | 414,4 | 466,2 |

**Calendario de entrada das Verticais (definido por Rodrigo):**

| Vertical | Ano 1 | Ano 2 | Ano 3 | Ano 4 | Ano 5 |
|---|:---:|:---:|:---:|:---:|:---:|
| Cimenticios | — | dev | entra | ramp | ramp |
| Tintas | — | dev | entra | ramp | ramp |
| Polimeros | — | dev | entra | ramp | ramp |
| Ligas (cobre-grafeno) | — | dev | dev | entra | ramp |
| Supercapacitores | — | dev | dev | dev | entra |

**Volume vendido (kg/ano), ramp conservador.** Vertical entrante vende ~800 kg no 1o ano, +50%/ano. Tudo muito abaixo da capacidade P500 (25.688 kg/ano) — utilizacao de **9% / 17% / 29%** nos anos 3/4/5.

| | Ano 1 | Ano 2 | Ano 3 | Ano 4 | Ano 5 |
|---|---:|---:|---:|---:|---:|
| Volume vendido (kg) | 0 | 200 | 2.400 | 4.400 | 7.400 |
| **Receita (R$ MM)** | **0** | **0,07** | **0,87** | **1,82** | **3,45** |

- **Ano 1:** receita zero — produtos em desenvolvimento; caixa e equity.
- **Ano 2:** vendas pouco significativas (amostras/validacao), ~R$ 0,07 MM.
- **Ano 3:** Cimenticios + Tintas + Polimeros entram com volume baixo.
- **Anos 4-5:** ramp dessas tres + Ligas (Ano 4) e Supercapacitores (Ano 5).

### B.2 Premissas de custo

| Linha | Ano 1 | Ano 2 | Ano 3 | Ano 4 | Ano 5 | Base |
|---|---:|---:|---:|---:|---:|---|
| Verticais ativas (n) | 1 | 3 | 4 | 5 | 5 | calendario B.1 |
| Custo Verticais — bruto (R$ MM) | 0,52 | 1,56 | 2,08 | 2,60 | 2,60 | n x R$ 0,52 MM (item A) |
| Cobertura por fomento (%) | 0% | 40% | 70% | 70% | 70% | lag do fomento (8/10/12+ m) |
| **Custo Verticais — liquido (R$ MM)** | **0,52** | **0,94** | **0,62** | **0,78** | **0,78** | bruto x (1 - cobertura) |
| OPEX producao caixa (R$ MM) | 0,80 | 1,00 | 1,83 | 2,01 | 2,30 | P100 piloto -> P500 (fixo R$ 1,6 MM + R$ 94/kg) |

### B.3 EBITDA-caixa e breakeven

| EBITDA-caixa (R$ MM) | Ano 1 | Ano 2 | Ano 3 | Ano 4 | Ano 5 |
|---|---:|---:|---:|---:|---:|
| **Com fomento (cenario do modelo)** | −1,32 | −1,87 | −1,58 | −0,97 | **+0,37** |
| Sem fomento (estresse) | −1,32 | −2,49 | −3,04 | −2,79 | −1,45 |

> **Breakeven operacional: Ano 5** — e **somente** com o fomento nao-dilutivo carregando ~70% do custo das Verticais. **Sem fomento, nao ha breakeven dentro dos 5 anos** (o Ano 5 ainda fecha em −R$ 1,45 MM). Isso quantifica, em caixa, por que o fomento e estrutural e nao um "bonus": ele e a diferenca entre cruzar o zero no Ano 5 ou nao cruzar.

### B.4 Caixa acumulado e demanda de investimento

CAPEX faseado (base R$ 2,80 MM P500 + P100): Ano 1 R$ 1,5 MM, Ano 2 R$ 1,3 MM, Ano 3 R$ 0,3 MM.

| Fluxo livre (R$ MM) | Ano 1 | Ano 2 | Ano 3 | Ano 4 | Ano 5 |
|---|---:|---:|---:|---:|---:|
| EBITDA-caixa (com fomento) | −1,32 | −1,87 | −1,58 | −0,97 | +0,37 |
| CAPEX | −1,50 | −1,30 | −0,30 | 0 | 0 |
| **Fluxo livre do ano** | **−2,82** | **−3,17** | **−1,88** | **−0,97** | **+0,37** |
| **Caixa acumulado** | **−2,82** | **−5,99** | **−7,87** | **−8,84** | **−8,47** |

> **Vale de caixa: ~−R$ 8,8 MM no fim do Ano 4.** A demanda total de financiamento (equity R$ 5,73 MM + fomento + credito) precisa cobrir esse vale. O envelope **~R$ 8,2-8,8 MM** e consistente com o estresse de preco conservador da v0.6 (ponte total ~R$ 8,3-8,7 MM, secao 5 do modelo de Julio) — checagem de sanidade independente, por outra rota de calculo.

### B.5 Conclusao — tres leituras de breakeven (todas conservadoras)

1. **Breakeven operacional (EBITDA-caixa >= 0): Ano 5**, condicionado a fomento. Sem fomento, fora da janela de 5 anos.
2. **Vale de caixa / pico de demanda de capital:** ~−R$ 8,8 MM no fim do Ano 4 — define o tamanho do funding total (equity + fomento + credito).
3. **Recuperacao do cheque de equity (R$ 5,73 MM):** **nao** ocorre pela geracao operacional dentro dos 5 anos. O retorno ao investidor depende da **saida estrategica (5x EBITDA)**, com o EBITDA construido a partir do Ano 5.

**Contraste com a leitura anterior.** O memorando trazia "payback ~3,1 a 4,4 anos". Essa leitura assume capital disponivel e regime de venda ja estabelecido. A visao conservadora acima — receita zero no Ano 1, ramp lento, fomento com lag — **empurra o breakeven operacional para o Ano 5 e condiciona-o ao fomento**. E a leitura que se sustenta diante de um comite ceptico.

---

## C. Premissas a validar (CFO)

| Premissa | Valor usado | Acao |
|---|---|---|
| Salario senior/junior | R$ 11.083 / R$ 6.000 (CLT, CBO 203125) | Confirmar faixa junior; avaliar uso de bolsa CNPq DTI |
| Encargos CLT | 70% | Alinhar com levantamento P100/P500 |
| Volume entrante por Vertical | 800 kg, +50%/ano | Validar contra capacidade de absorcao dos parceiros |
| Preco realizado conservador | US$ 70 -> 90/kg | Confirmar abaixo do caso-base US$ 96/kg |
| Cobertura de fomento sobre Verticais | 70% em regime | Alinhar a matriz A4 e ao lag real |
| Decomposicao OPEX (fixo/variavel) | R$ 1,6 MM + R$ 94/kg | Validar com o modelo P500 (Valdemiro) |

> **Proximo passo:** validacao por Julio (CFO, ALT-570) e integracao formal ao modelo v0.6 -> v0.7, antes da entrega ao IFHAN. Os numeros acima sao de Carmen, com vies conservador deliberado; pendem do aval financeiro.

---

## D. Serviços de Inovação — duas linhas de receita originadas em Inovação & Novos Negócios

> **Origem.** Sugestao de Rodrigo (a partir de Eduardo): monetizar a area Inovacao & Novos Negocios como **fonte de renda**, no modelo do **GEIC — Graphene Engineering Innovation Centre (Univ. de Manchester)**. E GaaS no sentido mais literal: vende-se o **serviço** (expertise + equipamento + rede academica), nao so o material.

### D.1 Modelo de referencia GEIC (pesquisado)

O GEIC e um centro industry-led que vende acesso a equipamento de escala-piloto, engenheiros de aplicacao e rede academica, em camadas:

| Camada GEIC | Preco (ref. Manchester) | Conteudo |
|---|---|---|
| **Pathfinder** (viabilidade rapida) | £10k–£25k | Estudo curto de viabilidade; porta de entrada |
| **Tier 2** (1 area de aplicacao, ate 12 meses) | a partir de £45k/ano (>=50% em projeto) | Framework, acesso a equipamento e areas, preco preferencial, hot desk/lab |
| **Tier 1** (multi-aplicacao, min. 3 anos) | £225k+/ano (>=50% em projeto) | Lab dedicado, equipamento, parceiros academicos, assento no conselho tecnico |
| **Affiliate** | — | Servicos habilitadores (juridico, contabil, PI, engenharia) |

### D.2 Adaptacao Grafex (escala BR, conservador)

**Produto 1 — Suporte tecnico / desenvolvimento assistido (GaaS-Serviço).** Camadas adaptadas: Viabilidade ~R$ 50–150k; Parceiro de Aplicacao (Tier 2) ~R$ 200–400k/ano; Parceiro Estrategico (Tier 1) ~R$ 1,0–1,5 MM/ano. Vende tempo de pesquisador/tecnico, acesso a P100/P500 e a rede de ICTs (CTNano/UFMG, LNNano/CNPEM).

**Produto 2 — Suporte + success fee de fomento.** Estrutura e desrisca a submissao de fomento de um parceiro (playbook Alberico), com **success fee de 5–10%** sobre o valor nao-dilutivo aprovado. Receita **contingente e com lag** (aprovacao 8–12 meses) — descontada com peso.

### D.3 Receita conservadora de Serviços de Inovação (corrigida por Rodrigo)

**Correcao de rota (Rodrigo):** o GaaS **tambem nao gera receita no Ano 1** — o Ano 1 e de **formacao dos grupos**. As duas linhas arrancam devagar:

- **Acesso a lab (Tier 2):** **1 unico cliente no Ano 2** e mais **1 no Ano 3** (ambos Tier 2), acelerando **lentamente** so a partir do Ano 4. Preco ~R$ 250k/cliente/ano. Clientes ativos (acumulado): 0 / 1 / 2 / 3 / 4.
- **Success fee de fomento:** **alguns (poucos) no Ano 2**, acelerando **singelamente** no Ano 3 e adiante. 5–10% sobre o valor aprovado.

| R$ MM | Ano 1 | Ano 2 | Ano 3 | Ano 4 | Ano 5 |
|---|---:|---:|---:|---:|---:|
| Receita acesso a lab (Tier 2) | 0 | 0,25 | 0,50 | 0,75 | 1,00 |
| Receita success fee (fomento) | 0 | 0,15 | 0,30 | 0,45 | 0,60 |
| **Receita de serviços (bruta)** | **0** | **0,40** | **0,80** | **1,20** | **1,60** |
| Contribuicao (lab 50% / success fee 70%) | 0 | 0,23 | 0,46 | 0,69 | 0,92 |

### D.4 Efeito no breakeven

| EBITDA-caixa (R$ MM) | Ano 1 | Ano 2 | Ano 3 | Ano 4 | Ano 5 |
|---|---:|---:|---:|---:|---:|
| Base (so material, com fomento) | −1,32 | −1,87 | −1,58 | −0,97 | +0,37 |
| (+) contribuicao de serviços | 0 | +0,23 | +0,46 | +0,69 | +0,92 |
| **Com Serviços de Inovação** | **−1,32** | **−1,64** | **−1,12** | **−0,28** | **+1,29** |

> **Breakeven operacional permanece no Ano 5** sob a hipotese corrigida (mais conservadora). Os serviços **nao antecipam o breakeven** para o Ano 4 — mas **suavizam todo o caminho** (o Ano 4 chega quase ao zero, −R$ 0,28 MM) e **deixam o Ano 5 ~3,5x mais forte** (+R$ 1,29 MM vs. +R$ 0,37 MM so com material). Como o GaaS so arranca no Ano 2, o Ano 1 segue integralmente bancado por equity.

### D.5 Pedida de recursos ampliada (preservar potencial de PI)

Mesmo com o breakeven melhor, Rodrigo pediu **ampliar a pedida** para preservar a geracao de PI. Proposta de estrutura (a calibrar com Julio):

| Camada | v0.6 | Proposta |
|---|---:|---:|
| Core operacional (equity) | R$ 5,73 MM | R$ 5,73 MM |
| **Reserva ring-fenced de Inovacao & PI** | — | **R$ 2,3–3,3 MM** |
| **Pedida total de equity** | **R$ 5,73 MM** | **~R$ 8,0–9,0 MM** |

A reserva blindada banca o motor de PI (equipe, equipamento para a linha de serviços, relacoes com ICTs), sob governanca por portoes de TRL. Cobre tambem o vale de caixa conservador (~−R$ 8,8 MM), eliminando o gap de ponte da v0.6.

### D.6 Ressalvas honestas (vies conservador)

- **Tensao de capacidade:** vender tempo de pesquisador compete com o desenvolvimento interno das Verticais — exige regra de teto (% do tempo vendavel).
- **Equipamento limitado cedo:** acesso real a equipamento depende da P500 (~Ano 3); Anos 1–2 sao mais consultoria/viabilidade/brokering academico do que lab GEIC completo.
- **Firewall de PI:** ajudar terceiros a desenvolver grafeno pode competir com nossas proprias Verticais — definir fronteira de PI (background/foreground) e non-compete nas Verticais prioritarias.
- **Success fee e contingente e com lag** — nao bancar nos primeiros anos.
- **Profundidade de mercado BR:** quantas empresas pagam tarifas tipo GEIC no Brasil? Precos/volumes acima sao deliberadamente baixos.

### D.7 Valor de PI gerado (ativo intangivel), Ano 3 -> Ano 5

**Pedido de Rodrigo:** projetar valor de PI a partir do Ano 3, com ramp-up ate o Ano 5. Aqui esta a peca que justifica a pedida ampliada: a area Inovacao & Novos Negocios **constroi patrimonio**, nao so queima caixa.

**Natureza (importante).** Estes valores **NAO sao caixa** — sao **ativo intangivel** (patentes, know-how, dados proprietarios) reconhecivel sob **IAS 38** quando o desenvolvimento cumpre os criterios (viabilidade tecnica, intencao e beneficio futuro mensuravel). Entram no **valuation e na tese de saida**, nao na linha de EBITDA-caixa. Sao **foreground IP** gerado pela operacao — distinto do background IP licenciado do CDTN/UFMG (~R$ 22,26 MM), que e transacao separada.

| R$ MM | Ano 3 | Ano 4 | Ano 5 |
|---|---:|---:|---:|
| Valor de PI criado no ano (incremento) | 1,0 | 1,5 | 2,5 |
| **Valor de PI acumulado (ativo intangivel)** | **1,0** | **2,5** | **5,0** |

- **Ano 3:** primeiras patentes/know-how das Verticais entrantes (Cimenticios, Tintas, Polimeros) + dados de co-desenvolvimento dos primeiros clientes de serviço.
- **Ano 4:** novos depositos + resultados de Ligas (cobre-grafeno) — tese proprietaria de maior valor.
- **Ano 5:** portfolio nas 5 Verticais + PI co-desenvolvida na linha de serviços; base de R$ 5,0 MM em ativo intangivel proprio.

> **Por que isso sustenta a pedida ampliada.** O retorno da tese tem duas pernas: (1) **EBITDA** (saida a 5x), construido a partir do Ano 5; e (2) **valor de PI** (~R$ 5,0 MM acumulados ate o Ano 5), que adiciona valor de empresa **independentemente** do breakeven operacional. Preservar a geracao de PI — o que Rodrigo pediu — e exatamente o que a reserva ring-fenced de R$ 2,3–3,3 MM protege. Numeros deliberadamente conservadores; sao valores-semente, a refinar com avaliacao de PI dedicada.

---

> **Status:** numeros ilustrativos de Carmen, vies conservador. Pendem de validacao do Julio e da definicao de Rodrigo sobre (a) tamanho do carve-out de PI e (b) se o veiculo e area dentro da GRAFEX ou entidade separada.
