---
title: Technical Summary — Secador 15000L
tipo: Especificação Técnica — Secador Rotativo
projeto: "[[Overview]]"
status: Proposta
audience: Engenheiros eletricistas, fornecedores de equipamento
updated: 2026-05-04
---

# Technical Summary — Secador 15000L

Parâmetros técnicos consolidados para secador rotativo de café conilon, capacidade 15.000 litros, baseados em equipamentos típicos de Marilândia/ES com validação e recomendações de Beto Parteli.

---

## 2.1 — Características Gerais do Equipamento

Especificações do equipamento de referência: secador rotativo de batelada, com tambor metálico cilíndrico inclinado e aletas internas.

| Parâmetro | Valor Típico | Validação com Beto Parteli |
|-----------|-------------|---------------------------|
| **Tipo** | Rotativo de batelada, tambor metálico cilíndrico inclinado, aletas internas | ✅ Compatível |
| **Capacidade nominal** | 15.000 litros | A confirmar com Beto o porte-alvo |
| **Capacidade em sacas** | ~100 a 130 sacas de café em coco por ciclo | — |
| **Tempo médio de secagem** | 12 a 18 horas por ciclo | ✅ Compatível |
| **Motor do tambor (motoredutor)** | 3 a 7 cv (~2,2 a 5,2 kW) | — |
| **Sistema de ventilação** | Forçada — conduz ar aquecido pela massa de grãos | ✅ Confirmado |
| **Dimensões** | Ø 2,0 – 2,5 m × 5 – 7 m de comprimento | — |
| **Combustível convencional** | Biomassa (lenha, palha de café) ou gás | ✅ Beto confirma uso de palha |
| **Umidade inicial do produto** | 35 – 45 % b.u. (café colhido mecanicamente) | — |
| **Umidade final desejada** | 11 – 12 % b.u. | ✅ Compatível |

---

## 2.2 — Parâmetros Térmicos e Fluxo de Ar

Análise comparativa entre especificações típicas de mercado e os dados levantados com Beto Parteli para este projeto.

| Parâmetro | Valor Típico (15.000 L) | Dado de Beto Parteli | Reconciliação |
|-----------|------------------------|---------------------|---------------|
| **Vazão de ar** | 10.000 – 20.000 m³/h | 220 m³/min = 13.200 m³/h | ✅ Dentro da faixa típica |
| **Temperatura do ar na entrada (fornalha a biomassa)** | Até 200 – 220 °C | < 90 °C medido no processo; 120 °C no ponto do conilon | ✅ Consistente: fornalha gera >200 °C, que se mistura e resfria antes do tambor |
| **Temperatura de processo alvo (sistema elétrico)** | A definir | 70 – 80 °C (proposta de Beto) | ⚠️ Redução para 70 °C viabiliza o dimensionamento de 265 kW |
| **Temperatura de combustão (ref. lenha)** | Não controlada na fornalha | ~400 °C (temperatura do fogo) | ⚠️ NÃO usar como base para dimensionar o sistema elétrico |

---

## 2.3 — Demanda de Potência Elétrica

Estimativa de demanda por componente, com dois cenários: sem recirculação parcial (base conservadora) e com recirculação parcial (base otimista com redução de ~20–30% na potência de aquecimento).

| Componente | Potência Estimada | Base / Observação |
|-----------|-----------------|------------------|
| **Resistências de aquecimento (sem recirculação)** | 265 kW | Cálculo do fornecedor: 220 m³/min, ΔT 20 → 70 °C |
| **Resistências de aquecimento (com recirculação parcial)** | ~185 – 220 kW | Redução estimada de 20 – 30 % |
| **Motor do tambor (motoredutor)** | 2,2 – 5,2 kW | Faixa do porte (3 – 7 cv) |
| **Ventilação forçada** | 3 – 7 kW | Proporcional à vazão de 13.200 m³/h |
| **Painel / PLC / sensores** | < 1 kW | — |
| **TOTAL — sem recirculação parcial** | **~275 – 280 kW** | Base conservadora |
| **TOTAL — com recirculação parcial** | **~195 – 235 kW** | Base otimista |

> **Verificação matemática:** P = Q × ρ × Cp × ΔT → Q = 3,67 m³/s; ρ ≈ 1,11 kg/m³; Cp = 1,005 kJ/kg·K; ΔT = 50 °C → **P ≈ 205 kW teórico**. Os 265 kW do fornecedor incluem perdas e margem de segurança (~30 %). ✅ Valor coerente.

---

## Conexões

- [[Overview]]
- [[Beto Parteli]]
- [[Technical Summary — High-Efficiency Coffee Dryer]]
