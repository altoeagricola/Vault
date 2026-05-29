---
name: alerta-climatico
description: Consulta INMET e Incaper para identificar alertas meteorológicos, previsões de risco e eventos climáticos com impacto na atividade agrícola (foco conilon no ES). Gera um boletim de risco classificado por severidade. Use quando o usuário disser "alertas climáticos", "previsão do tempo para lavoura", "risco climático para safra", ou por trigger agendado.
---

# Alerta Climático para Agricultura

Skill dedicada ao monitoramento de condições climáticas e emissão de alertas meteorológicos com impacto direto na produção agrícola, com foco especial no conilon no Espírito Santo.

## Workflow

### Step 1: Consulta de Dados Meteorológicos

1. Acessar fontes oficiais:
   - **INMET** (Instituto Nacional de Meteorologia): alertas, previsões, histórico
   - **Incaper** (Instituto Capixaba de Pesquisa): dados locais ES, fenologia do conilon
   - Regional: previsões para municípios produtores (Vitória, Venda Nova do Imigrante, Iúna, etc.)

2. Coletar informações:
   - Alertas meteorológicos em vigência
   - Previsão de temperatura (máxima, mínima, sensação térmica)
   - Previsão de precipitação (volume, horário, probabilidade)
   - Umidade relativa do ar
   - Velocidade e direção do vento
   - Radiação solar UV

### Step 2: Análise de Impacto Fenológico

1. Mapear riscos para o conilon segundo estágio fenológico:
   - **Floração**: risco de geada, chuvas excessivas, umidade baixa
   - **Granação**: risco de veranico, chuvas intensas
   - **Colheita**: risco de chuvas excessivas (impede colheita), estiagem (reduz produtividade)
   - **Pós-colheita**: risco de umidade alta (mofo/fermentação)

2. Classificar severidade:
   - **Atenção** (amarelo): previsão anômala que merece acompanhamento
   - **Aviso** (laranja): risco moderado com possível impacto na produção
   - **Emergência** (vermelho): risco iminente, requer ação imediata

### Step 3: Geração do Boletim

Produzir documento estruturado:

```
## Alerta Climático — [Data/Hora]

### Resumo Executivo
- Região: [municípios monitorados]
- Período coberto: [intervalo de previsão]
- Alertas em vigência: [total]
- Severidade máxima: [cor + descrição]

### Alertas Ativos

#### [Evento 1 — Geada iminente]
- Severidade: Emergência 🔴
- Período: YYYY-MM-DD HH:MM — YYYY-MM-DD HH:MM
- Temperatura mínima prevista: X°C
- Impacto no conilon: [descrição do risco fenológico]
- Recomendação: [ação sugerida]

[idem para outros eventos]

### Previsão Detalhada (próximos 7 dias)

| Data | Temp Min | Temp Max | Chuva | Umidade | Risco |
|------|----------|----------|-------|---------|-------|
| DD/MM | X°C | X°C | Xmm | X% | [status] |

### Contexto de Safra
- Estágio fenológico atual: [fase do conilon]
- Condições de solo: [umidade, compactação, etc.]
- Necessidades hídricas: [em mm por semana]

### Fontes e Confiabilidade
- INMET (acesso: YYYY-MM-DD HH:MM) — confiabilidade: alta
- Incaper (acesso: YYYY-MM-DD HH:MM) — confiabilidade: alta
- Modelo de previsão: [nome, horizonte de confiabilidade]
```

### Step 4: Registro em Log

Manter histórico em `Products/Eloi/alertas-climaticos/` com arquivo por mês. Registrar alertas acionados e respostas tomadas.

## Triggers

- "alertas climáticos"
- "previsão do tempo para lavoura"
- "risco climático para safra"
- "vai gelar?"
- "chuva prevista"
- Automático: agendado (diário, ou antes de fenofases críticas)

## Notas

- Sempre indicar data/hora de acesso aos dados (meteorologia muda rapidamente)
- Relacionar previsão com estágio fenológico do conilon para tornar o alerta acionável
- Em caso de alerta vermelho, considerar sugerir acionamento de especialista agrícola para mitigation
- Manter histórico de alertas emitidos vs. eventos efetivos (aprendizado contínuo)
