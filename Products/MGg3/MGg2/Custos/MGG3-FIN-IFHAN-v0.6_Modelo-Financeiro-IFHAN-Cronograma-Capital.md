---
codigo_fonte: MGG3-FIN-IFHAN-v0.6
titulo: Modelo financeiro IFHAN v0.6 — cronograma de capital, caixa-ponte e sensibilidade timing x preço
produto: MGgrafeno / MGG3
tipo: modelo financeiro
versao: 0.6
data: 2026-06-11
moeda: R$ milhões, exceto quando indicado
status: entregue_v0.6_registrado_no_vault
autor: Julio
issue_origem: ALT-570
issue_versionamento: ALT-581
fonte_original: ALT-570_modelo_financeiro_IFHAN_v0.6_cronograma_capital.md
audiencia: IFHAN, investidores institucionais, BNDES, FINEP e family offices
---

# ALT-570 - Modelo financeiro IFHAN v0.6

Data-base: 11/06/2026  
Tema da revisao: cronograma de capital, caixa-ponte e sensibilidade timing x preco  
Moeda: R$ milhoes, exceto quando indicado

## 1. Mudanca frente a v0.5

A v0.5 tratava equity, fomento e credito como camadas de capital disponiveis sem defasagem operacional relevante. A v0.6 separa:

1. Equity IFHAN de R$ 5,73 MM como caixa-ponte de arranque.
2. Lead time pre-submissao do fomento, porque FINEP exige o background IP UFMG/CDTN resolvido antes da submissao.
3. Lag de contratacao/desembolso do fomento apos submissao.
4. Credito BNDES/FINEP reembolsavel apenas depois de RFQ/SAT da P500, principalmente centrifugacao.

O guardrail permanece: licenciamento CDTN/UFMG de ~R$ 22,26 MM fica fora do caso operacional e fora do cheque de R$ 5,73 MM.

## 2. Referencias de cronograma

| Fonte | Premissa usada no modelo | Tratamento CFO |
|---|---|---|
| FINEP Mais Inovacao Brasil II - Economia Circular e Cidades Sustentaveis | Submissao aberta ate 31/08/2026; subvenção para PD&I; chamada com recursos FNDCT; desembolso tratado em 2 parcelas conforme chamada/regulamento | Usada como trilha realista/intermediaria; relogio so comeca na submissao |
| EMBRAPII / unidades credenciadas | Fluxo continuo, sem edital; negociacao e contratacao diretamente com a Unidade; recursos nao-reembolsaveis de ate 1/3, podendo chegar a 50% em arranjos colaborativos | Usada como ponta rapida para caixa nao-dilutivo, mas depende de Unidade aderente e contrapartida |
| BNDES Mais Inovacao | Apoia PD&I, plantas pioneiras e difusao tecnologica; exige habilitacao antes do protocolo; prazos e garantias dependem da analise | Timing de 8-11 meses e estimativa, nao SLA bancario; condicionado a RFQ/SAT P500 |

Links de referencia consultados em 11/06/2026:

- FINEP chamada 2026: `https://www.finep.gov.br/e/chamada-publica/222684/755213`
- EMBRAPII/CNPEM modelo de financiamento: `https://pages.cnpem.br/unidadeembrapii/modelo-de-financiamento/`
- BNDES Mais Inovacao: `https://www.bndes.gov.br/wps/portal/site/home/financiamento/produto/programa-bndes-mais-inovacao-investimento`

## 3. Sequenciamento de capital

| Camada | Valor | Timing v0.6 | Uso | Condicao |
|---|---:|---|---|---|
| Equity IFHAN | R$ 5,73 MM | Ano 0/1 | Arranque, P100, equipe, capital de giro e ponte ate fomento | Fecha no investimento 49/51 |
| Fomento nao-dilutivo | R$ 3-5 MM | Recebimento apos pre-submissao + lag de 8/10/12+ meses | Ensaios, validacoes aplicadas, CQ e rotas de mercado | Submissao; IP background resolvido antes no caso FINEP |
| Credito BNDES/FINEP reembolsavel | R$ 2-3 MM | Apos RFQ/SAT P500; caso base m20/m24/m28 | CAPEX P500 e parte do giro industrial | RFQ/SAT centrifugacao; habilitacao e analise financeira |
| Licenciamento CDTN/UFMG | ~R$ 22,26 MM | Transacao separada | IP/licenca | Nao entra no cheque operacional |

## 4. Premissas de timing v0.6

| Cenario de timing | Lead time pre-submissao | Lag apos submissao | 1a parcela fomento | 2a parcela fomento | Credito P500 | Leitura |
|---|---:|---:|---:|---:|---:|---|
| T8 otimista | 2 meses | 8 meses | m10 | m16 | m20 | Requer IP resolvido rapido e rota EMBRAPII/FINEP sem retrabalho |
| T10 realista | 3 meses | 10 meses | m13 | m19 | m24 | Caso-base para memorando |
| T12+ pessimista | 4 meses | 12+ meses | m16 | m22 | m28 | Assume demora em IP/submissao e credito so depois de RFQ/SAT completo |

Premissas financeiras por timing:

- Fomento no caso-base de preco: R$ 4,0 MM, em duas parcelas 60%/40%.
- Credito no caso-base: R$ 2,5 MM, juros referenciais de 16% a.a., amortizacao linear em 5 anos.
- CAPEX P500 base: R$ 2,8 MM, acionado com o credito. No T12+, a defasagem do credito aumenta risco de atraso no ramp-up, mas o modelo abaixo isola primeiro o efeito de caixa.

## 5. Caixa-ponte: equity IFHAN

Resultado: no caso-base de preco (US$ 96/kg), o equity de R$ 5,73 MM cobre a janela ate fomento e credito nos tres timings, desde que o CAPEX P500 nao seja contratado antes do credito/RFQ-SAT.

| Timing | Menor caixa estimado antes/ate m36 | Mes do vale | Folga sobre zero | Diagnostico |
|---|---:|---:|---:|---|
| T8 | R$ 4,39 MM | m9 | R$ 4,39 MM | Equity suficiente |
| T10 | R$ 3,94 MM | m12 | R$ 3,94 MM | Equity suficiente |
| T12+ | R$ 3,94 MM | m12 | R$ 3,94 MM | Equity suficiente, mas com maior risco de atraso da P500 |

No conservador de preco (US$ 50/kg), o caixa fica negativo ate m36 mesmo com fomento e credito:

| Timing | Menor caixa estimado ate m36 | Gap de equity/ponte indicado |
|---|---:|---:|
| T8 | -R$ 2,65 MM | R$ 2,7-3,0 MM |
| T10 | -R$ 2,55 MM | R$ 2,6-3,0 MM |
| T12+ | -R$ 2,44 MM | R$ 2,5-3,0 MM |

Conclusao de caixa-ponte:

- R$ 5,73 MM e adequado para o caso-base se nao houver compromisso antecipado de CAPEX P500.
- Para suportar o caso conservador sem cortes, o cheque total de equity/ponte deveria subir para aproximadamente R$ 8,3-8,7 MM ou o burn precisa ser reduzido ate a chegada de contratos/offtakes.
- O arranque nao deve depender de fomento. O fomento entra como mitigador de risco tecnologico e preservador de caixa, nao como condicao para operar os primeiros 8-12 meses.

## 6. Impacto em VPL, TIR e payback - caso-base de preco

Observacao metodologica: a tabela abaixo e fluxo alavancado/financiado para equity, incluindo fomento como entrada nao-dilutiva e credito como fonte de caixa com servico de divida. Nao comparar diretamente com a TIR operacional unlevered da v0.5 sem esta ressalva.

Preco-base: US$ 96/kg. WACC nominal de referencia: 24% a.a.

| Timing | VPL sem saida | TIR sem saida | Payback | VPL com saida 5,0x EBITDA | TIR com saida | Payback |
|---|---:|---:|---:|---:|---:|---:|
| T8 | R$ 4,01 MM | 41,1% | 3,1 anos | R$ 10,84 MM | 53,3% | 3,1 anos |
| T10 | R$ 3,64 MM | 38,3% | 3,1 anos | R$ 10,46 MM | 50,4% | 3,1 anos |
| T12+ | R$ 3,74 MM | 38,2% | 2,9 anos | R$ 10,46 MM | 49,8% | 2,9 anos |

Leitura: o caso-base continua investivel quando fomento e credito entram em timing realista, mas a TIR melhora porque o fomento e capital nao-dilutivo. O ponto de risco nao e o VPL matematico; e a possibilidade de contratar CAPEX P500 antes de credito aprovado ou de o licenciamento IP atrasar a submissao FINEP.

## 7. Sensibilidade cruzada timing x preco

Tabela com saida estrategica incluida, porque e a leitura adequada para investidor IFHAN.

| Preco realizado | T8: VPL / TIR | T10: VPL / TIR | T12+: VPL / TIR | Leitura |
|---|---:|---:|---:|---|
| US$ 50/kg | -R$ 13,24 MM / n.m. | -R$ 13,61 MM / n.m. | -R$ 13,62 MM / n.m. | Preco baixo inviabiliza; timing nao salva |
| US$ 96/kg | R$ 10,84 MM / 53,3% | R$ 10,46 MM / 50,4% | R$ 10,46 MM / 49,8% | Investivel com fomento, credito e disciplina de CAPEX |
| US$ 140/kg | R$ 35,63 MM / 110,2% | R$ 35,25 MM / 102,9% | R$ 35,25 MM / 101,1% | Forte, mas nao deve ser narrado como base |

Tabela sem saida estrategica:

| Preco realizado | T8: VPL / TIR | T10: VPL / TIR | T12+: VPL / TIR |
|---|---:|---:|---:|
| US$ 50/kg | -R$ 13,24 MM / n.m. | -R$ 13,61 MM / n.m. | -R$ 13,51 MM / n.m. |
| US$ 96/kg | R$ 4,01 MM / 41,1% | R$ 3,64 MM / 38,3% | R$ 3,74 MM / 38,2% |
| US$ 140/kg | R$ 21,90 MM / 105,1% | R$ 21,52 MM / 97,3% | R$ 21,63 MM / 95,5% |

## 8. Guardrails para o memorando

1. FINEP nao deve ser modelado como caixa de Ano 0. O relogio comeca na submissao, e a submissao depende de IP background resolvido.
2. EMBRAPII pode ser a rota rapida, mas nao substitui o pacote FINEP se o projeto precisar de R$ 3-5 MM. O limite de ate 1/3, ou ate 50% colaborativo, exige contrapartida e Unidade aderente.
3. BNDES Mais Inovacao nao tem SLA no modelo. O prazo de 8-11 meses e estimativa de tramitacao, nao compromisso do banco.
4. CAPEX P500 nao deve ser assinado antes de RFQ/SAT da centrifugacao e antes de fonte reembolsavel estar encaminhada.
5. Licenciamento CDTN/UFMG continua separado. Se R$ 22,26 MM entrar no closing, o equity de R$ 5,73 MM deixa de ser suficiente e o valuation precisa ser reaberto.

## 9. Premissas que ainda precisam fechar

| Premissa | Status | Acao |
|---|---|---|
| Lead time pre-submissao IP | Provisorio: 2/3/4 meses | Validar com juridico e CDTN/UFMG |
| Elegibilidade FINEP da frente MGgrafeno | Provavel para materiais/circularidade, mas nao confirmado | Mapear linha tematica e TRL exato |
| Unidade EMBRAPII aderente | Em aberto | Identificar Unidade e faixa de contrapartida |
| Cronograma BNDES/FINEP reembolsavel | Indicativo, nao SLA | Simular com agente financeiro/BNDES apos RFQ/SAT |
| Parcelamento real do fomento | Modelo usa 60%/40% | Ajustar ao edital/termo de outorga efetivo |
| CAPEX P500 | Base AACE 4/5 | RFQ/SAT centrifugacao antes de compromisso financeiro |

## 10. Conclusao CFO v0.6

O cheque IFHAN de R$ 5,73 MM funciona como caixa-ponte no caso-base de US$ 96/kg, desde que:

- o fomento seja tratado como entrada com lag, nao como caixa inicial;
- o CAPEX P500 espere RFQ/SAT e fonte reembolsavel;
- a questao IP UFMG/CDTN seja resolvida antes da submissao FINEP;
- o licenciamento de R$ 22,26 MM permaneca fora do cheque operacional.

Se Rodrigo quiser estressar a tese para comite, o ponto de corte e simples: a US$ 50/kg o projeto precisa de R$ 2,5-3,0 MM adicionais de ponte ou reducao de burn; a US$ 96/kg, o modelo fecha com folga; acima de US$ 140/kg, a tese fica muito forte, mas deve ser mantida como upside.
