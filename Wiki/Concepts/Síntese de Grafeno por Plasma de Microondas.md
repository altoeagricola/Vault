---
title: Síntese de Grafeno por Plasma de Microondas
type: Concept
sources:
  - "[[Levidian - Patente EP3167694B1]]"
related:
  - "[[Levidian]]"
  - "[[NanoXplore]]"
created: 2026-05-21
updated: 2026-05-21
confidence: medio
---

# Síntese de Grafeno por Plasma de Microondas

Técnica "bottom-up" para produção de grafeno em escala a partir do craqueamento de feedstock carbonáceo por plasma de microondas em pressão atmosférica, com recombinação das espécies de carbono em grafeno sólido no afterglow do plasma.

## Princípio

A síntese ocorre em duas etapas no interior do reator:

1. **Cracking:** feedstock carbonáceo (ex: CH₄) é introduzido no bocal de plasma, onde radiação de microondas (2,45 GHz) excita o gás e cria um plasma que quebra as moléculas de carbono em espécies atômicas/radicais
2. **Recombinação:** as espécies de carbono craquedas passam para a câmara de afterglow, onde se resfriamm e recombinamo, formando folhas de grafeno (single-layer e multi-layer)

A temperatura ideal de formação de grafeno é 900–1.000°C (temperatura no ponto de formação na saída do bocal).

## Vantagens sobre outros métodos de síntese

| Método | Escala | Substrato | Vácuo | Continuidade | Custo feedstock | Pureza |
|---|---|---|---|---|---|---|
| Exfoliação mecânica | Muito baixa | Não | Não | Batch | Baixo | Alta |
| CVD | Média | Sim (metálico) | Parcial | Batch | Médio | Alta |
| Exfoliação líquida | Média | Não | Não | Batch | Médio | Média |
| Plasma arco/ICP | Baixa | Não | **Sim** | Batch | Alto (Ar/He) | Alta |
| **Plasma microondas (Levidian)** | **Alta** | **Não** | **Não** | **Contínuo** | **Baixo (CH₄ + N₂)** | **>99,5% C** |

## Design de bocal de triplo vórtice (inovação Levidian)

O bocal de plasma com 3 vórtices concêntricos é a inovação central que possibilita operação em pressão atmosférica com feedstock barato e cracking de ~99%:

- **Vórtice 1:** formado pelas injeções tangenciais do gás de processo
- **Vórtice 2:** criado por efeito Coanda no reflector (espaço vazio no fundo do bocal)
- **Vórtice 3:** reflexão do vórtice 2 → tripla exposição ao campo de microondas

O design aumenta o tempo de residência do gás no campo de microondas, eleva a eficiência de cracking (CH₄: ~30% convencional → ~99% neste design) e permite plasma estável em pressão atmosférica com fluxos elevados de feedstock.

## Parâmetros típicos de processo

| Parâmetro | Faixa / Valor típico |
|---|---|
| Frequência de microondas | 2,45 GHz (padrão); 896 MHz (testado) |
| Potência | 2–6 kW (piloto); escalável |
| Temperatura afterglow | <3.500°C; ideal <1.000°C; possível a 300°C |
| Temperatura de formação | 900–1.000°C (ponto de máxima qualidade) |
| Feedstock C : tampão | ≤ 50:50; ideal ≤ 20:80 |
| Feedstocks testados | CH₄, gás natural, C₂H₆, C₂H₄, C₃H₈, C₄H₁₀, CO₂, tolueno |
| Gases tampão | N₂, Ar, He |

## Resultados de produção (Levidian, piloto 5 kW)

- Produtividade: **100 g grafeno/hora**
- Eficiência energética: **15–20 g/kWh**
- Pureza: **>99,5% em carbono**
- Qualidade: comparável à exfoliação líquida (Raman, TEM validados)

## Proteção intelectual

A patente EP 3 167 694 B1 (Levidian/FGV Cambridge Nanosystems) cobre o aparelho e método descritos acima, com 20 reivindicações (9 de aparelho + 11 de método), em 27 estados europeus + UK. É referência de IP defensável em um setor onde a maioria dos players (ex: [[NanoXplore]]) opera com trade secrets não patenteados.

## Relevância para MGgrafeno

A rota de síntese por plasma é **alternativa/complementar** à rota de exfoliação líquida do MGgrafeno. A análise desta patente é relevante para due diligence tecnológica, FTO (Freedom to Operate) e avaliação de parceiros estratégicos no contexto do EVT-MGg3.
