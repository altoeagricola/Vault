# Technical Summary — High-Efficiency Coffee Dryer

**Projeto:** High-Efficiency Coffee Dryer (Secador Elétrico Solar Off-Grid)  
**Tipo:** Memorial Descritivo Técnico — Viabilidade  
**Audiência:** Engenheiros eletricistas e de automação  
**Status:** Rascunho — levantamento de viabilidade técnica  
**Atualização:** 2026-04-26  
**Solicitante:** Beto Parteli

---

## Números-Chave

| Parâmetro | Sem Recirculação | Com Recirculação Parcial | Observação |
|---|---|---|---|
| **Potência — aquecimento** | 265 kW | ~185–220 kW | Redução 20–30% com recirculação |
| **Potência total instalada** | ~275–280 kW | ~195–235 kW | Inclui motor, ventilação, automação |
| **Verificação teórica (Q×ρ×Cp×ΔT)** | ~205 kW | — | Fornecedor inclui perdas + margem 30% |
| **Vazão de ar (Beto)** | 13.200 m³/h | 13.200 m³/h | 220 m³/min — dado dos fornecedores |
| **Temperatura de processo alvo** | 70–80°C | 70–80°C | Temperatura real no tambor (≠ 400°C da fornalha) |
| **Energia diária necessária** | ~3.920 kWh/dia | ~2.730 kWh/dia | Base: 14 h/dia de operação |
| **Sistema FV estimado** | ~890 kWp | ~620 kWp | Inclui perdas 20%; 5,5 h/dia sol pleno |
| **Banco de baterias (8 h noturno)** | ~2.240 kWh | ~1.570 kWh | Grande porte — avaliar PCM térmico |

---

## 1. Dados do Equipamento e Processo

### 1.1 Características do Secador

| Parâmetro | Informação de Beto | Observação |
|---|---|---|
| Tipo de secador | Rotativo de tambor (igual ao da foto da patente) | Secadores de 'caixa' para gourmet existem, mas não são a realidade de Marilândia |
| Posição do termômetro principal | Na entrada do secador | Mede temperatura do ar entrante |
| Distribuição interna do ar | Via 'carambola' — tubo perfurado dentro do tambor | Distribui o ar aquecido pela massa de grãos |
| Segundo termômetro | No meio do secador | Mede temperatura real no processo |
| Temperatura de processo — início | < 90°C | Temperatura no interior do tambor, início do ciclo |
| Temperatura de processo — ponto conilon | ~120°C | Temperatura no meio do tambor quando café está 'no ponto' |
| Temperatura 400°C (ref. lenha) | Temperatura da queima de lenha na fornalha | ⚠ NÃO é temperatura de processo — é a temperatura do fogo |
| Temperatura-alvo proposta (elétrico) | 70–80°C | Faixa de trabalho do equipamento que Beto já fornece; segura e eficiente |
| Arábica vs. Conilon | Arábica: baixas temps. Conilon: 'fogo como solto' | Conilon historicamente seco em altas temperaturas p/ maior velocidade |

### 1.2 Vazão de Ar — Dado Usado nas Consultas

| Parâmetro | Valor |
|---|---|
| Vazão de ar (consulta a fornecedores) | 220 m³/min = 13.200 m³/h |
| Temperatura de entrada do ar (ambiente, safra ES) | ~20–25°C |
| Temperatura-alvo do ar aquecido (revisão proposta) | 70°C (ΔT ≈ 50°C) |

### 1.3 Cálculos de Potência — Compilação das Consultas a Fornecedores

| Fornecedor / Cenário | ΔT (entrada → saída) · Vazão | Potência calculada |
|---|---|---|
| Corel Resistência Elétrica | 20°C → 400°C · ~220 m³/min | ~2.100 kW  ⚠ Inviável — temperatura errada (ref. lenha) |
| Segunda empresa (anônima) — cenário A | 10°C → 150°C · 200 m³/min | 670 kW |
| Segunda empresa (anônima) — cenário B | 10°C → 250°C · 200 m³/min | 1.150 kW |
| Segunda empresa (anônima) — cenário C | 10°C → 300°C · 200 m³/min | 1.400 kW |
| **Revisão técnica — temperatura correta** | **20°C → 70°C · 220 m³/min** | **265 kW  ✅ "Mais realista"** |

### 1.4 Recirculação Parcial — Proposta de Eficiência de Beto

| Aspecto | Passagem única (atual) | Com recirculação parcial |
|---|---|---|
| Aproveitamento do ar aquecido | Parcial — ar descartado antes de saturar | Alto — ar recircula até maior saturação |
| Potência instalada necessária | Maior (todo calor vem das resistências) | Menor (reutiliza energia do ar recirculado) |
| Temperatura de trabalho possível | Limitada pela potência instalada | Pode ser maior com mesma potência |
| Complexidade adicional | — | Tubulação de retorno + damper motorizado |
| Base da patente | Patente BR 10 2012 019091-5 A2 — sem recirculação | Melhoria direta sobre a patente — não prevista no original |

---

## 2. Secador Rotativo Típico — 15.000 L

### 2.1 Características Gerais

| Parâmetro | Valor típico | Validação com Beto |
|---|---|---|
| Tipo | Rotativo de batelada, tambor metálico cilíndrico inclinado, aletas internas | ✅ Compatível |
| Capacidade nominal | 15.000 litros | A confirmar com Beto o porte do equipamento-alvo |
| Capacidade em sacas | ~100 a 130 sacas de café em coco por ciclo | — |
| Tempo médio de secagem | 12 a 18 horas por ciclo | ✅ Compatível |
| Motor do tambor | 3 a 7 cv (~2,2 a 5,2 kW) | — |
| Sistema de ventilação | Forçada — conduz ar aquecido pela massa de grãos | ✅ Confirmado |
| Dimensões | Ø 2,0–2,5 m × 5–7 m de comprimento | — |
| Combustível convencional | Biomassa (lenha, palha de café) ou gás | ✅ Beto confirma palha |
| Umidade inicial do produto | 35–45% b.u. (café colhido mecanicamente) | — |
| Umidade final desejada | 11–12% b.u. | ✅ Compatível |

### 2.2 Parâmetros Térmicos e Fluxo de Ar

| Parâmetro | Valor típico (15.000 L) | Dado de Beto | Reconciliação |
|---|---|---|---|
| Vazão de ar | 10.000–20.000 m³/h | 220 m³/min = 13.200 m³/h | ✅ Dentro da faixa típica |
| Temperatura do ar na entrada — fornalha | Até 200–220°C | < 90°C no processo; 120°C no ponto | ✅ Consistente: fornalha >200°C, ar mistura e resfria antes do tambor |
| Temperatura de processo alvo — elétrico | A definir | 70–80°C (Beto) | ⚠ Redução p/ 70°C viabiliza dimensionamento de 265 kW |
| Temperatura da combustão — ref. lenha | Não controlada | ~400°C (temperatura do fogo) | ⚠ NÃO usar como base para dimensionar o sistema elétrico |

### 2.3 Demanda de Potência Elétrica — Consolidado

| Componente | Potência estimada | Base |
|---|---|---|
| Resistências de aquecimento | 265 kW | Cálculo do fornecedor: 220 m³/min, ΔT 20→70°C |
|   → Com recirculação parcial | ~185–220 kW | Redução estimada de 20–30% |
| Motor do tambor (motoredutor) | 2,2–5,2 kW | Faixa do porte |
| Ventilação forçada | 3–7 kW | Proporcional à vazão de 13.200 m³/h |
| Painel / PLC / sensores | < 1 kW | — |
| **TOTAL — sem recirculação** | **~275–280 kW** | **Base conservadora** |
| **TOTAL — com recirculação parcial** | **~195–235 kW** | **Base otimista** |
| **Verificação matemática (Q×ρ×Cp×ΔT)** | **~205 kW teórico** | **Q=3,67 m³/s; ρ=1,11 kg/m³; Cp=1,005 kJ/kg·K; ΔT=50°C → ✅ Coerente** |

---

## 3. Sistema Fotovoltaico Off-Grid

| Parâmetro | Valor / Requisito |
|---|---|
| Tipo de sistema | Off-grid — sem conexão à rede da ELFSM |
| Carga de aquecimento — sem recirculação | 265 kW |
| Carga de aquecimento — com recirculação | ~200 kW |
| Carga total instalada | ~280 kW |
| Horas de operação diária (safra) | 12–16 h/dia |
| Energia diária necessária | 280 kW × 14 h = ~3.920 kWh/dia |
| Pleno sol equivalente (maio–set, ES) | ~5–6 h/dia |
| Geração solar necessária | ~3.920 ÷ 5,5 ÷ 0,80 ≈ ~890 kWp instalados (estimativa, inclui perdas 20%) |
| Armazenamento — baterias (operação noturna 8h) | 280 kW × 8 h = ~2.240 kWh — banco de grande porte |
| Alternativa: PCM (armazenamento térmico) | Armazena calor, não eletricidade — eficaz para 2–6 h pós-pôr do sol; reduz tamanho do banco de baterias |
| Fonte auxiliar obrigatória | Gerador diesel ou conexão ELFSM (backup) — períodos de baixa irradiância |
| ⚠ Observação estratégica | ~890 kWp é sistema industrial de grande porte — viabilidade econômica é etapa crítica antes do projeto detalhado; avaliar escala coletiva (consórcio de produtores) |

---

## 4. Sistema de Automação e Controle

| Parâmetro | Requisito |
|---|---|
| Controlador principal | PLC (CLP) com IHM touchscreen |
| Sensores de temperatura | Termopares tipo K ou PT100 — mínimo 3 pontos: entrada do ar, meio do tambor (carambola), saída |
| Sensor de umidade do produto | Sonda de umidade inline (microondas ou capacitivo) — controle por resultado |
| Controle de temperatura | PID com setpoint programável — perfis distintos: commodity (~120°C) e gourmet (70°C) |
| Controle de recirculação | Damper motorizado + atuador controlado pelo PLC — proporção de recirculação ajustável |
| Controle de velocidade do tambor | Inversor de frequência — ajuste de tempo de residência dos grãos |
| Monitoramento de energia | Medidor de energia integrado — rastreamento kWh/saca |
| Alarmes | Alta temperatura, falha de resistência, falha de comunicação, nível baixo de bateria, falha de damper |
| Conectividade | Protocolo Modbus ou CAN — integração com supervisório |
| Registro de dados | Log temperatura × tempo × umidade por lote — rastreabilidade para certificação de café gourmet |

---

## 5. Módulo de Aquecimento Elétrico

**Base:** Patente BR 10 2012 019091-5 A2 + recirculação

| Componente | Especificação |
|---|---|
| Elemento aquecedor | Resistências elétricas blindadas tubulares (níquel-cromo) — potência total ~265 kW |
| Câmara de aquecimento | Carcaça metálica (aço inox) com isolamento térmico — design monobloco |
| Acoplamento ao secador | Peça de transição flangeada — customizada por modelo de secador |
| Suporte | Regulável — retrofit em secadores de qualquer marca e porte |
| Alimentação | Trifásico 380V ou 440V — a confirmar com especificação dos inversores off-grid |
| Proteções elétricas | Disjuntores termomagnéticos por bancada de resistências + DR |
| ✅ Melhoria sobre a patente | Tubulação de retorno com damper motorizado para recirculação parcial — NÃO prevista na patente original |

---

## 6. Pontos de Decisão para Engenharia

| Ponto de Decisão | Detalhamento | Status |
|---|---|---|
| Capacidade exata do secador-alvo | Volume do tambor, vazão do ventilador existente (m³/h), potência do motor | ⬜ Pendente |
| Temperatura-alvo de processo | Commodity (~120°C no ponto) ou gourmet (70–80°C) ou perfis duplos com troca de setpoint | ⬜ Pendente |
| Incluir recirculação parcial? | Reduz potência instalada ~20–30%; adiciona damper + tubulação de retorno | ⬜ Pendente |
| Regime de operação noturna | Proporção entre baterias, PCM e gerador auxiliar | ⬜ Pendente |
| Escala de implantação | Único produtor ou consórcio/associação (compartilhamento reduz custo per capita do sistema solar) | ⬜ Pendente |
| Retrofit vs. equipamento novo | Custo de adequação mecânica do secador existente para acoplamento da câmara elétrica | ⬜ Pendente |
| Orçamento por subsistema | Resistências + câmara + painéis FV + baterias + inversores off-grid + automação | ⬜ Pendente |

---

## Notas Importantes

- A temperatura-alvo de **70–80°C** é crítica para viabilidade — reduz a potência necessária de ~2.100 kW (baseado em temperatura errada de 400°C) para **265 kW** realista.
- **Recirculação parcial** oferece redução de 20–30% na potência instalada, justificando a adição de damper e tubulação de retorno.
- Sistema FV de **~890 kWp** é de escala industrial — recomenda-se avaliar **escala coletiva** (consórcio de produtores) para viabilidade econômica.
- **Backup obrigatório**: gerador diesel ou conexão ELFSM para períodos de baixa irradiância.
- A patente original (BR 10 2012 019091-5 A2) serve como base, mas a proposta de recirculação é uma **melhoria não prevista**.

---

**Arquivo original (XLSX):** Technical Summary — High-Efficiency Coffee Dryer.xlsx  
**Gerado em:** 2026-05-04  
**Para consultas:** Beto Parteli
