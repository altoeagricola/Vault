---
titulo: Saneamento de custos P100 P500
tipo: saneamento-custos
produto: MGg3
status: preliminar
confidencialidade: interno
fontes:
  - "[[MGG2-CUSTO-P100_Modelo-custo-planta-piloto]]"
  - "[[MGG3-CUSTO-P500_Projecao-KonMix]]"
  - "[[MGG3-FORN02_Fornecedores-insumos-grafeno-startup]]"
  - "[[Custos de producao P100 P500]]"
atualizado: 2026-06-11
---
# Saneamento de custos P100 P500

## Resultado executivo

As planilhas P100 e P500 possuem dados suficientes para entender equipamentos, custos, depreciações, energia, equipe, insumos e custos por módulo. O problema principal não é ausência de informação; é comparabilidade.

A P100 está mais completa como visão de planta piloto: inclui obra civil/depreciação predial, equipe indireta, caracterização interna e base de equipamentos mais carregada. A P500 está modelada como projeção enxuta: zera depreciação predial e equipe indireta, reduz manutenção/caracterização e usa rendimento embutido mais agressivo que a premissa comum informada pelo usuário.

Portanto, os custos unitários atuais devem ser lidos em três camadas:

| Camada | Uso | Status |
|---|---|---|
| Planilha original | Preserva os números como foram calculados nos arquivos | extraído |
| Comparável P100/P500 | Requer harmonizar rendimento, overhead, depreciação predial e alocação de CQ | pendente de reconciliação |
| Investidor conservador | Deve incluir rendimento 2021, overhead mínimo, CQ/terceiros e contingência operacional | pendente |

## Premissas operacionais extraídas

| Campo | P100 | P500 | Status |
|---|---:|---:|---|
| Reatores / MC | 2 | 2 | extraído |
| Volume/carga de referência | 105,6 L/lote | 449,5 kg na célula de volume; 50.000 g grafite/lote | extraído, unidade P500 exige cuidado |
| Grafite por lote | 10.000 g | 50.000 g | extraído |
| Lotes/mês | 43,5 | 43,33 | extraído |
| Tempo de lote total | 10,75 h | 15,25 h | extraído |
| Obra civil | R$ 15.000.000 | R$ 0 | extraído; não comparável |
| Depreciação predial anual | R$ 600.000 | R$ 0 | extraído; não comparável |

## Premissa de rendimento comum

Premissa informada pelo usuário para o Lote 2021, a ser usada tanto para P100 quanto para P500 quando o objetivo for comparação limpa.

| Material | Rendimento comum | P100 comum, 10 kg/lote | P500 comum, 50 kg/lote | P500 embutido na planilha | Status |
|---|---:|---:|---:|---:|---|
| Grafeno A | 0,80% | 80 g/lote | 400 g/lote | 750 g/lote | P500 divergente |
| Grafeno B | 5,00% | 500 g/lote | 2.500 g/lote | 3.750 g/lote | P500 divergente |
| A+B | 5,80% | 580 g/lote | 2.900 g/lote | 4.500 g/lote | P500 divergente |
| Nanoplaca | 93,00% | 9.300 g/lote | 46.500 g/lote | 45.000 g/lote | P500 divergente |
| Perdas | 1,20% | 120 g/lote | 600 g/lote | 500 g/lote implícito | P500 divergente |

Leitura: P100 está alinhada à premissa comum. P500 mistura escala maior com rendimento melhor para Grafeno A e B. Se o custo total P500 permanecer igual e apenas o rendimento for harmonizado, o custo unitário do Grafeno A tende a subir por fator de 1,875 e o do Grafeno B por fator de 1,5.

## Ponte de custos anuais

Tabela extraída da aba `Comparação P500xP100`. Ela é útil como ponte gerencial, mas não deve ser tratada como custo final canônico sem reconciliar as divergências com `Dashboard` e `Custo Final`.

| Categoria | P100 anual | P500 anual | Leitura de saneamento |
|---|---:|---:|---|
| Equipe direta | R$ 227.011,80 | R$ 625.200,00 | P500 aumenta por salários/equipe projetada; conferir base de encargos |
| Equipe indireta | R$ 2.160.216,24 | R$ 0,00 | principal quebra de comparabilidade |
| Depreciação de equipamentos | R$ 607.457,14 | R$ 63.768,71 | P500 usa carga muito menor de depreciação alocada |
| Depreciação predial | R$ 600.000,00 | R$ 0,00 | P100 carrega obra civil, P500 não |
| Manutenção | R$ 122.842,61 | R$ 3.893,66 | P500 provavelmente subestima manutenção normalizada |
| Energia | R$ 188.187,28 | R$ 125.885,79 | redução plausível, mas conferir por kWh/lote |
| Insumos e consumíveis | R$ 743.403,92 | R$ 561.015,52 | P500 menor apesar da escala; verificar quantidades e preços |
| **Total da ponte** | **R$ 4.649.118,98** | **R$ 1.379.763,69** | comparação enviesada sem ajustes |

## Equipamentos e ativos

Resumo por bloco de equipamento, extraído das abas de equipamentos. Estes valores ajudam a montar o cadastro saneado de ativos, mas ainda precisam ser normalizados item a item.

| Bloco | P100 CAPEX | P100 kW | P100 deprec. anual | P100 manut. anual | P500 CAPEX | P500 kW | P500 deprec. anual | P500 manut. anual | Status |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Produção | R$ 1.615.200,33 | 47,20 | R$ 160.017,87 | R$ 0,00 | R$ 1.615.200,33 | 47,20 | R$ 160.017,87 | R$ 0,00 | extraído; manutenção zerada exige revisão |
| Caracterização | R$ 6.642.339,51 | 25,50 | R$ 537.715,24 | R$ 93.123,07 | R$ 6.522.655,47 | 25,50 | R$ 529.270,17 | R$ 5.840,00 | extraído; P500 parece trocar CQ interno por terceiros |
| SSMA | R$ 65.360,00 | 0,77 | R$ 6.558,00 | R$ 750,00 | R$ 65.360,00 | 0,77 | R$ 6.558,00 | R$ 2.660,00 | extraído |

Observação: a soma de depreciação por equipamentos nas abas de equipamentos não fecha diretamente com a alocação resumida da aba `Comparação P500xP100`. Isso reforça que deve haver uma camada intermediária de reconciliação antes de publicar custo unitário saneado.

## Custos por módulo/lote

Extraído da aba `Custo Final`.

| Módulo | P100 total/lote | P500 total/lote | Leitura |
|---|---:|---:|---|
| Conversão | R$ 197,24 | R$ 1.037,80 | P500 cresce por carga de insumos/energia de conversão |
| Primeira separação | R$ 137,13 | R$ 168,81 | aumento moderado |
| Segunda separação | R$ 117,11 | R$ 105,41 | P500 levemente menor |
| Secagem | R$ 117,65 | R$ 111,45 | semelhante |
| SSMA / resíduos | R$ 453,75 | R$ 40,00 | P500 possivelmente subestima resíduo/SSMA |
| CQ / caracterização | R$ 2.017,68 somando técnicas internas principais | R$ 3.950,00 em análises terceirizadas/modeladas | bases diferentes; não comparar sem separar CQ interno vs terceiro |

## Estrutura saneada recomendada

Criar uma visão limpa com sete tabelas, sem sobrescrever as planilhas originais:

| Tabela | Finalidade | Campos mínimos | Status inicial |
|---|---|---|---|
| Cadastro de ativos/equipamentos | Normalizar cada equipamento | planta, módulo, descrição, quantidade, valor unitário, valor total, potência, fonte, status | extraído parcial |
| Depreciação e manutenção | Separar ativo, prédio e manutenção | base depreciável, vida útil, taxa, depreciação anual/mês/lote, manutenção anual/mês/lote | pendente reconciliação |
| Energia por equipamento/módulo | Fechar kWh por lote | potência, horas/lote, kWh/lote, tarifa, custo/lote, módulo | pendente |
| Insumos e consumíveis | Validar preços e quantidades | item, unidade, preço, quantidade P100, quantidade P500, custo/lote, data, fonte, status | extraído parcial |
| Equipe e overhead | Separar direto/indireto | função, quantidade, salário, encargos, turno, direto/indireto, custo anual | pendente reconciliação |
| Produção e rendimento | Harmonizar capacidade e produtos | carga/lote, lotes/mês, rendimento, g/lote, kg/ano, cenário | reconciliado para premissa 2021 |
| Ponte de custo final | Unificar leitura executiva | categoria, custo anual, custo/lote, custo por produto, cenário, fonte | pendente |

## Campos de controle

Cada valor saneado deve receber um status:

| Status | Significado |
|---|---|
| extraído | Valor lido diretamente da planilha |
| reconciliado | Valor conferido entre abas ou ajustado para base comum |
| estimado | Valor calculado por premissa explícita |
| pendente | Valor existe, mas exige confirmação antes de uso |
| não comparável | Valor não deve ser comparado entre P100/P500 sem ajuste |

## Complemento MGG3-FORN02

A planilha [[MGG3-FORN02_Fornecedores-insumos-grafeno-startup]] deve alimentar principalmente as tabelas saneadas de `Insumos e consumíveis`, `Energia por equipamento/módulo` e `Equipe e overhead`.

| Categoria | Exemplos | Tratamento |
|---|---|---|
| Consumíveis de processo | esferas de zircônia, N2, CO2 | extrair custo unitário e estimar taxa de consumo por lote |
| Insumos de aplicação | PET micronizado, BT Sulfonol | manter separado de custo de produção de grafeno acabado |
| Utilidades | energia ENEL/Ouro Branco, água/esgoto SABESP | atualizar tarifa e localização antes de usar como premissa final |
| HH | operador, técnico, analista, pesquisador | reconciliar salário, encargos e base mensal com equipe P100/P500 |

## Conclusão operacional

A proposta de saneamento deve começar pela criação de uma matriz única P100/P500 com os valores originais e uma coluna `status_comparabilidade`. O primeiro ajuste obrigatório é separar o que é ganho de escala real do que é efeito de premissa: rendimento P500 mais agressivo, overhead zerado, depreciação predial zerada e CQ modelado em base diferente.

Até essa reconciliação, a melhor mensagem executiva é: P500 indica potencial de redução de custo por escala, mas a projeção atual não deve ser usada como custo unitário final sem harmonização de rendimento, overhead, depreciação e CQ.

## Atualizacao Konmix 2026

Para a selecao do cisalhador P500 e o CAPEX reconciliado, a referencia canonica passa a ser [[MGG3-CUSTO-P500-v2_Escalonamento-Engenharia-P100-P500]]. As evidencias de cotacao ficam em [[MGG3-COT-20260506-01_konmix-inline-homogenizer-krb75-3]] e [[MGG3-COT-20260505-01_konmix-inline-homogenizer-krb15-3]], com ficha do fornecedor em [[KONMIX-FORN01_Ficha-fornecedor-equipamentos]].

A estimativa antiga de cisalhador por escalonamento deve ser lida apenas como sanity check historico. A ancora de CAPEX do cisalhador P500 e a cotacao formal do KRB 75/3 registrada no documento v2; o KRB 15/3 permanece evidenciado como descarte tecnico por vazao insuficiente.
