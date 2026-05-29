---
titulo: Memo Executivo - Regua de Preco e Premio do Grafeno para MGgrafeno
tipo: memo-executivo
produto: MGg3
codigo_fonte: MGG3-MEMO-20260522-01
origem_issue: ALT-345
contexto_issue_mae: ALT-339
data_fonte: 2026-05-22
versao: 1.0 Final
status: registrado
confidencialidade: interno
responsavel: Carmen
registrado_por: Cacilda
atualizado: 2026-05-22
links_relacionados:
  - "[[MGG3-PRECO-GLOBAL-20260522-matriz_precos_grafeno_2026]]"
  - "[[MGG3-PRECO-20260522-04_nanoxplore-tribograf-og]]"
  - "[[MGG3-PRECO-20260522-05_graphenest-emi]]"
  - "[[MGG3-LEV-P100-v1_Levantamento-Custos-Recomissionamento]]"
---
# Memo Executivo — Régua de Preço e Prêmio do Grafeno para MGgrafeno

**Emitido por:** Carmen (Coordenação — ALT-345)
**Data:** 22 de Maio de 2026
**Versão:** 1.0 Final
**Rastreabilidade:** ALT-340 · ALT-341 · ALT-342 · ALT-343 · ALT-344 · ALT-346

---

## 1. Tese Central

O levantamento de custos P100 utilizava como referência o preço de grafeno da NanoXplore (GNP industrial, escala, ~USD 9–14/kg). Esse valor é inadequado como régua única para precificação do MGgrafeno por três razões estruturais:

1. **Estratégia de volume vs. valor:** a NanoXplore opera em volumes industriais de substituição de carbon black — uma tese de baixo valor relativo que afasta a empresa das aplicações de alta tecnologia onde o grafeno técnico gera prêmio funcional.
2. **Ausência de padrão de material:** o mercado de grafeno não tem norma unificada. GNP, FLG, GO, rGO, grafite micronizado e masterbatch são tratados como "grafeno" por players distintos com preços incomparáveis entre si.
3. **Pó ≠ solução:** o valor do grafeno está na incorporabilidade funcional, na formulação, na repetibilidade e na homologação — não na síntese isolada. Usar preço de pó como proxy de valor subestima sistematicamente o potencial de captura.

---

## 2. Régua de Preço Recomendada

| Camada | Faixa (USD/kg de grafeno) | Tipo de Evidência | Uso no Modelo |
|---|---|---|---|
| **Piso commodity / stress case** | USD 9–14/kg (NanoXplore GNP industrial) | Auditável para existência; fraco para comparabilidade técnica | Somente como piso de downside. Não deve precificar MGgrafeno técnico ou formulado. |
| **Conservadora defensável** | USD 50–200/kg | Auditável/parcialmente comparável (GNP técnico com TDS mínimo) | Teste conservador P500; não serve para tese premium. |
| **Base técnica/formulada — polímeros** | USD 450–550/kg | Forte — Observado (Colorfix/Gerdau Poly-G, downgauging 25–30%) | Melhor âncora para tese comercial inicial em volume. `GG03_Aditivos-QuimicosT&R.md` / `GG-POL01_BlackSwan-R&D.md` |
| **Aplicação cimentícia — baixo prêmio funcional** | USD 90–150/kg | Claim/Inferido médio (Concretene, redução 30% cimento) | Útil em alto volume; limitado pelo baixo valor do substrato. `Concretene - relatorio tecnico-comercial.md` |
| **Premium funcional — O&G / EMI / coatings** | USD 1.000–5.000/kg | Inferido médio a forte conforme aplicação | Upside por aplicação (Tribograf O&G, EMI shielding, coatings protetivos). Não usar como preço médio. |
| **Premium observado — coatings industriais** | USD 5.000–7.000/kg | Observado/Forte (Polystell/Gerdau W108, economia 33% pintura) | Cenário premium condicionado a desempenho e canal validado. `GG03_Aditivos-QuimicosT&R.md` |
| **Não comparável — laboratório/P&D** | USD 90.000–210.000/kg (GO/rGO Graphenea) | Auditável, mas fora do escopo industrial | Somente para narrativa tecnológica; não entra na régua industrial. |

**Conclusão operacional:** NanoXplore deve constar como piso agressivo de escala para GNP industrial em cenário de stress, não como benchmark universal. A régua base para o modelo financeiro deve migrar para USD 450–550/kg (polímeros) com upside premium por aplicação (O&G, EMI, coatings).

---

## 3. Posicionamento da NanoXplore

A NanoXplore não é a referência tecnológica do mercado de grafeno — é o player de maior escala em GNP de baixo valor, com estratégia explícita de substituição de carbon black. Seus preços anunciados são agressivos porque:

- A empresa tem capacidade instalada relevante e verticalização.
- Contratos industriais de volume geram receita previsível mesmo a margens baixas.
- A ausência de padrão técnico permite denominar GNP de poucas camadas como "grafeno".

**Impacto no modelo:** usar NanoXplore como base implica posicionar o MGgrafeno na mesma faixa de commoditização, invalidando qualquer diferenciação técnica e inviabilizando aplicações de maior valor. O sinal correto é: se a MGgrafeno competir em preço com NanoXplore, a tese não fecha. Se competir em desempenho formulado por aplicação, fecha.

---

## 4. Leitura P100

P100 deve ser tratado como **unidade de validação, amostragem e geração de evidência comercial** — não como plataforma de receita recorrente imediata. A leitura financeira correta:

- P100 consome caixa para produzir amostras, TDS/COA, curvas de dosagem, validação com clientes pilotos e dados para RFQ padronizada.
- Receita P100: simbólica em conservador (amostras); base em lotes técnicos pagos em polímeros/coatings; premium somente com cliente/aplicação com economia operacional demonstrada.
- Premissa a corrigir no `MGG3-LEV-P100-v1`: substituir referência NanoXplore por faixa conservadora USD 50–200/kg, com upside condicional declarado e ressalva de que prêmio funcional entra como opcionalidade até homologação.

---

## 5. Leitura P500

P500 é onde a régua vira tese comercial. O caso base não deve ser NanoXplore nem Graphenea. Recomendação de cesta ponderada por aplicação:

- **Caso base:** USD 400–600/kg em polímeros/masterbatch (Poly-G/Colorfix como âncora observada).
- **Caso otimista:** USD 1.500–3.000/kg em O&G/lubrificantes com ganho de ROP demonstrado.
- **Caso premium:** USD 5.000/kg em coatings protetivos com saving comprovado de mão de obra + material.

P500 deve separar custo interno de produção de preço de venda potencial. A margem viável depende de qual aplicação será prioritária na comercialização.

---

## 6. Substituição/Complementação no Modelo de Custos

Para atualizar o `MGG3-LEV-P100-v1_Levantamento-Custos-Recomissionamento`:

| Referência atual | Substituição recomendada | Justificativa |
|---|---|---|
| NanoXplore como base única | Remover como base; manter como piso de stress (USD 9–14/kg) | Benchmark de escala commodity, não técnico |
| Sem separação de camadas | Adicionar cesta: conservadora / base / premium | Reflete heterogeneidade real do mercado |
| Prêmio funcional não modelado | Incluir upside por aplicação com ressalva de condicionamento | Coatings e O&G têm evidência observada suficiente |

---

## 7. Riscos e Lacunas

| Risco / Lacuna | Severidade | Mitigação recomendada |
|---|---|---|
| Cotações de RFQ ausentes (Thomas Swan, Levidian, First Graphene, Universal Matter, Gerdau Graphene, Nanum, NanoBrasil) | Alta | Próxima fase: RFQ padronizada 1 kg / 25 kg / 100 kg / 1 t com TDS/SDS/COA, teor ativo, incoterm e curva de dosagem |
| Prêmios de O&G e EMI baseados em inferência, não em contrato | Média | Usar como upside; não como base sem validação adicional |
| Câmbio e frete não normalizados em todas as linhas | Média | Explicitados na matriz da ALT-341; usar com ressalva cambial declarada |
| Mercado de grafeno sem norma unificada | Estrutural | Toda comparação deve especificar família de material, TDS, especificação mínima |

---

## 8. Próximos Passos Recomendados

1. **Atualizar `MGG3-LEV-P100-v1`** com as faixas desta régua, substituindo NanoXplore como base.
2. **Iniciar RFQ padronizada** com fornecedores-alvo para validar preço real por volume (autorização do Rodrigo necessária para contato externo).
3. **Definir aplicação prioritária P500** para ancorar a tese comercial em uma faixa de prêmio defensável.
4. **Registrar esta síntese no Vault** em `Products/MGg3/Inteligencia de Mercado/` conforme padrão ALT-340.

---

## 9. Rastreabilidade de Fontes

| Issue / Documento | Papel | Status |
|---|---|---|
| ALT-340 | Padrão de registro e rastreabilidade | done |
| ALT-341 | Matriz global de preços auditável (`matriz_precos_grafeno_2026.md`) | done |
| ALT-342 | Mapeamento de aplicações e prêmio funcional (5 registros MGG3-PRECO-*) | done |
| ALT-343 | Validação técnica de comparabilidade por família de material | done |
| ALT-344 | Cenários econômico-financeiros P100/P500 | done |
| ALT-346 | Ingestão dos registros MGG3-PRECO-* no Vault | done |
| `Products/MGg3/MGg2/Fornecedores/Benchmark internacional - fornecedores de grafeno` | Base de benchmark existente | consultado |
| `Products/MGg3/MGg2/Ecossistema brasileiro de grafeno` | Contexto ecossistema | consultado |
| `Products/MGg3/Inteligencia de Mercado` | Relatórios de mercado 2026 | consultado |
| `Products/MGg3/MGg2/Custos/MGG3-LEV-P100-v1` | Levantamento de custos a atualizar | insumo de referência |

---

**Separação epistêmica desta síntese:**

- **Fato verificado:** prêmios Polystell/W108 e Colorfix/Poly-G (observados em case interno).
- **Fato declarado:** NanoXplore USD 9–14/kg (público); Concretene cost-neutral (claim do player).
- **Inferência nossa:** prêmios O&G e EMI baseados em economia de uso, não em cotação direta.
- **Lacuna:** cotações de RFQ para Thomas Swan, Levidian, First Graphene, Universal Matter e outros.
