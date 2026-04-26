---
title: Technical Summary — High-Efficiency Coffee Dryer
tipo: Memorial Descritivo Técnico
projeto: "[[Overview]]"
status: Rascunho — levantamento de viabilidade técnica
audience: Engenheiros eletricistas e de automação
updated: 2026-04-26
---

# Technical Summary — High-Efficiency Coffee Dryer

Quadro técnico consolidado para avaliação de viabilidade por engenheiros eletricistas e de automação. Organizado em dois blocos: dados levantados diretamente por [[Beto Parteli]] + parâmetros típicos de secadores da região de Marilândia/ES.

---

## Quadro 1 — Informações Técnicas de Beto Parteli

Extraídas das conversas de Beto com fornecedores de resistências elétricas (jun/2023) e com o solicitante (abr/2026).

### 1.1 Dados do Equipamento e Processo

| Parâmetro | Informação de Beto | Observação |
|-----------|-------------------|-----------|
| **Tipo de secador** | Rotativo de tambor (igual ao da foto da patente) | Secadores de "caixa" para gourmet existem, mas não são a realidade de Marilândia |
| **Posição do termômetro principal** | Na entrada do secador | Mede temperatura do ar entrante |
| **Distribuição interna do ar** | Via "carambola" — tubo perfurado dentro do tambor | Distribui o ar aquecido pela massa de grãos |
| **Segundo termômetro** | No meio do secador | Mede temperatura real no processo |
| **Temperatura de processo — início** | < 90°C | Temperatura no interior do tambor, início do ciclo |
| **Temperatura de processo — ponto do conilon** | ~120°C | Temperatura no meio do tambor quando o café está "no ponto" |
| **Temperatura de referência citada (400°C)** | Temperatura da queima de lenha na fornalha | **Não é a temperatura de processo** — é a temperatura do fogo. Beto confirmou: "Quando eu digo 400°C, porque é a temperatura que usamos com a queima de lenha" |
| **Temperatura-alvo proposta (sistema elétrico)** | 70–80°C | Faixa de trabalho do equipamento que Beto já fornece; considerada segura e eficiente |
| **Café arábica vs. conilon** | Arábica: temperaturas baixas. Conilon: "o fogo como solto" | Conilon é historicamente seco em altas temperaturas para maior velocidade |

### 1.2 Vazão de Ar — Dado Usado nas Consultas

| Parâmetro | Valor |
|-----------|-------|
| **Vazão de ar (consulta a fornecedores)** | **220 m³/min = 13.200 m³/h** |
| Temperatura de entrada do ar (ambiente, safra ES) | ~20–25°C |
| Temperatura-alvo do ar aquecido (revisão proposta) | 70°C (ΔT ≈ 50°C) |

### 1.3 Cálculos de Potência — Compilação das Consultas a Fornecedores

Beto consultou ao menos duas empresas de fabricação de resistências elétricas industriais. Os resultados foram divergentes e levaram a uma análise de qual temperatura é realmente necessária no processo:

| Fornecedor | Vazão | ΔT (entrada → saída) | Potência calculada | Status |
|-----------|-------|---------------------|-------------------|--------|
| **Corel Resistencia Elétrica** | ~220 m³/min | 20°C → 400°C (ref. lenha) | **~2.100 kW** | Inviável — "ele não tem isso, pede para reavaliar" |
| **Segunda empresa (anônima)** | 200 m³/min | 10°C → 150°C | 670 kW | — |
| **Segunda empresa (anônima)** | 200 m³/min | 10°C → 250°C | 1.150 kW | — |
| **Segunda empresa (anônima)** | 200 m³/min | 10°C → 300°C | 1.400 kW | Beto consultou se era possível ir a 350°C |
| **Revisão técnica — fornecedor** | 220 m³/min | 20°C → 70°C | **265 kW** | **"Mais realista"** — temperatura de processo correta |

> **Insight crítico de Beto:** *"Os dados obtidos através de fornalhas normalmente possuem um valor muito alto para a temperatura, porque não se controla a temperatura do fogo, apenas do processo."*
>
> A divergência entre 2.100 kW e 265 kW explica-se inteiramente pela diferença entre temperatura de combustão (400°C) e temperatura real de processo (70°C).

### 1.4 Recirculação Parcial — Proposta de Eficiência de Beto

Observação técnica levantada por Beto ao comparar o secador rotativo com um secador de minério industrial (75% similar ao da foto da patente):

> *"Em uma passagem só, o ar não atinge saturação de umidade; despejar este ar não saturado e aquecido na atmosfera é desperdício de energia. Podemos utilizar uma tubulação com damper para uma recirculação parcial — traz economia de energia e menor potência total instalada ou maior temperatura de trabalho."*

| Aspecto | Passagem única (atual) | Com recirculação parcial |
|---------|----------------------|------------------------|
| Aproveitamento do ar aquecido | Parcial — ar descartado antes de saturar | Alto — ar recircula até maior saturação |
| Potência instalada necessária | Maior (todo calor vem das resistências) | Menor (reutiliza energia do ar recirculado) |
| Temperatura de trabalho possível | Limitada pela potência instalada | Pode ser maior com mesma potência |
| Complexidade adicional | — | Tubulação de retorno + damper motorizado |

> O sistema de recirculação parcial com damper controlado por PLC é uma **melhoria direta sobre a patente BR 10 2012 019091-5 A2**, que não contempla recirculação.

---

## Quadro 2 — Parâmetros Típicos: Secador Rotativo de Café Conilon 15.000 L (Marilândia/ES)

Baseado no memorial descritivo fornecido pelo solicitante, validado contra os dados de Beto Parteli.

### 2.1 Características Gerais do Equipamento

| Parâmetro | Valor típico | Validação com Beto |
|-----------|-------------|-------------------|
| **Tipo** | Rotativo de batelada, tambor metálico cilíndrico inclinado, aletas internas | ✅ Compatível |
| **Capacidade nominal** | 15.000 litros | A confirmar com Beto o porte do equipamento-alvo |
| **Capacidade em sacas** | ~100 a 130 sacas de café em coco por ciclo | — |
| **Tempo médio de secagem** | 12 a 18 horas por ciclo | ✅ Compatível |
| **Motor do tambor (motoredutor)** | 3 a 7 cv (~2,2 a 5,2 kW) | — |
| **Sistema de ventilação** | Forçada — conduz ar aquecido pela massa de grãos | ✅ Confirmado |
| **Dimensões** | Ø 2,0–2,5 m × 5–7 m de comprimento | — |
| **Combustível convencional** | Biomassa (lenha, palha de café) ou gás | ✅ Beto confirma palha |
| **Umidade inicial do produto** | 35–45% b.u. (café colhido mecanicamente) | — |
| **Umidade final desejada** | 11–12% b.u. | ✅ Compatível |

### 2.2 Parâmetros Térmicos e Fluxo de Ar

| Parâmetro | Valor típico (15.000 L) | Dado de Beto | Reconciliação |
|-----------|------------------------|-------------|--------------|
| **Vazão de ar** | **10.000–20.000 m³/h** | **220 m³/min = 13.200 m³/h** | ✅ Dentro da faixa típica |
| **Temperatura do ar na entrada — fornalha** | Até 200–220°C | < 90°C medido no processo; 120°C no ponto | ✅ Consistente: a fornalha gera ar >200°C, que se mistura e resfria antes do tambor |
| **Temperatura de processo alvo — elétrico** | A definir | 70–80°C (Beto) | ⚠️ Redução para 70°C viabiliza o dimensionamento de 265 kW |
| **Temperatura da combustão — ref. lenha** | Não controlada | ~400°C (temperatura do fogo) | ⚠️ Não usar como base para dimensionar o sistema elétrico |

### 2.3 Demanda de Potência Elétrica — Consolidado

| Componente | Potência estimada | Base |
|-----------|-----------------|------|
| **Resistências de aquecimento** | **265 kW** | Cálculo do fornecedor: 220 m³/min, ΔT 20→70°C |
| **Com recirculação parcial** | ~185–220 kW | Redução estimada de 20–30% |
| Motor do tambor (motoredutor) | 2,2–5,2 kW | Faixa do porte |
| Ventilação forçada | 3–7 kW | Proporcional à vazão de 13.200 m³/h |
| Painel / PLC / sensores | < 1 kW | — |
| **Total estimado — sem recirculação** | **~275–280 kW** | Base conservadora |
| **Total estimado — com recirculação parcial** | **~195–235 kW** | Base otimista |

> **Verificação matemática:** P = Q × ρ × Cp × ΔT → Q = 3,67 m³/s; ρ ≈ 1,11 kg/m³; Cp = 1,005 kJ/kg·K; ΔT = 50°C → **P ≈ 205 kW teórico**. Os 265 kW do fornecedor incluem perdas e margem de segurança (~30%). ✅ Coerente.

---

## 3. Sistema Fotovoltaico Off-Grid

| Parâmetro | Valor / Requisito |
|-----------|-----------------|
| Tipo de sistema | Off-grid — sem conexão à rede da ELFSM |
| Carga de aquecimento | 265 kW (sem recirculação) / ~200 kW (com recirculação) |
| Carga total instalada | ~280 kW |
| Horas de operação diária (safra) | 12–16 h/dia |
| Energia diária necessária | 280 kW × 14 h = **~3.920 kWh/dia** |
| Pleno sol equivalente (maio–set, ES) | ~5–6 h/dia |
| Geração solar necessária | ~3.920 ÷ 5,5 ÷ 0,80 ≈ **~890 kWp instalados** (estimativa, inclui perdas) |
| Armazenamento — baterias (operação noturna) | 280 kW × 8 h = **~2.240 kWh** — banco de grande porte |
| Alternativa: PCM (armazenamento térmico) | Armazena calor, não eletricidade — eficaz para 2–6 h pós-pôr do sol; reduz tamanho do banco de baterias |
| Fonte auxiliar obrigatória | Gerador diesel ou conexão ELFSM (backup) — períodos de baixa irradiância |
| **Observação estratégica** | ~890 kWp é um sistema industrial de grande porte — viabilidade econômica é etapa crítica antes do projeto detalhado; avaliar escala coletiva (consórcio de produtores) |

---

## 4. Sistema de Automação e Controle

| Parâmetro | Requisito |
|-----------|----------|
| Controlador principal | PLC (CLP) com IHM touchscreen |
| Sensores de temperatura | Termopares tipo K ou PT100 — mínimo 3 pontos: entrada do ar, meio do tambor (carambola), saída |
| Sensor de umidade do produto | Sonda de umidade inline (microondas ou capacitivo) — controle por resultado |
| Controle de temperatura | PID com setpoint programável — perfis distintos: commodity (120°C ponto) e gourmet (70°C) |
| Controle de recirculação | Damper motorizado + atuador controlado pelo PLC — proporção de recirculação ajustável |
| Controle de velocidade do tambor | Inversor de frequência — ajuste de tempo de residência dos grãos |
| Monitoramento de energia | Medidor de energia integrado — rastreamento kWh/saca |
| Alarmes | Alta temperatura, falha de resistência, falha de comunicação, nível baixo de bateria, falha de damper |
| Conectividade | Protocolo Modbus ou CAN — integração com supervisório |
| Registro de dados | Log temperatura × tempo × umidade por lote — rastreabilidade para certificação de café gourmet |

---

## 5. Módulo de Aquecimento Elétrico

Baseado na patente BR 10 2012 019091-5 A2 (domínio público desde 2016) com adição de recirculação parcial.

| Componente | Especificação |
|-----------|--------------|
| Elemento aquecedor | Resistências elétricas blindadas tubulares (níquel-cromo) — potência total ~265 kW |
| Câmara de aquecimento | Carcaça metálica (aço inox) com isolamento térmico — design monobloco |
| Acoplamento ao secador | Peça de transição flangeada — customizada por modelo de secador |
| Suporte | Regulável — retrofit em secadores de qualquer marca e porte |
| Alimentação | Trifásico 380V ou 440V — a confirmar com especificação dos inversores off-grid |
| Proteções elétricas | Disjuntores termomagnéticos por bancada de resistências + DR |
| **Melhoria sobre a patente** | Tubulação de retorno com damper motorizado para recirculação parcial — não prevista na patente original |

---

## 6. Pontos de Decisão para Engenharia

- [ ] **Capacidade exata do secador-alvo** — volume do tambor, vazão do ventilador existente (m³/h), potência do motor
- [ ] **Temperatura-alvo de processo** — commodity (~120°C no ponto) ou gourmet (70–80°C) ou perfis duplos com troca de setpoint
- [ ] **Incluir recirculação parcial?** — reduz potência instalada ~20–30%; adiciona damper + tubulação de retorno
- [ ] **Regime de operação noturna** — proporção entre baterias, PCM e gerador auxiliar
- [ ] **Escala de implantação** — único produtor ou consórcio/associação (compartilhamento reduz custo per capita do sistema solar)
- [ ] **Retrofit vs. equipamento novo** — custo de adequação mecânica do secador existente para acoplamento da câmara elétrica
- [ ] **Orçamento por subsistema** — resistências + câmara + painéis FV + baterias + inversores off-grid + automação

---

## Conexões

- [[Overview]]
- [[Beto Parteli]]
