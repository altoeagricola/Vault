---
name: sintese-tendencia
description: Consolida dados de preços, clima, movimentos de mercado e políticas públicas recentes em uma síntese executiva de tendências para suporte à decisão estratégica. Use quando o usuário disser "síntese de tendências", "relatório de inteligência de mercado", "briefing estratégico", "quadro geral do setor", ou quando dados de múltiplas fontes precisam ser integrados.
---

# Síntese de Tendências Estratégicas

Skill que integra dados de múltiplas fontes (preços, clima, mercado, políticas) em uma síntese executiva estruturada para suporte à decisão estratégica da organização.

## Workflow

### Step 1: Coleta de Dados Multidimensionais

Consolidar informações de:

1. **Preços & Mercado**
   - Últimas cotações de conilon, café, grãos (via monitor-precos-agricolas)
   - Variações recentes (últimas 2 semanas, mês, trimestre)
   - Comparação com histórico (média de 5 anos)
   - Posição relativa no ciclo de preços

2. **Clima & Safra**
   - Alertas climáticos vigentes (via alerta-climatico)
   - Previsão de clima para próximas semanas
   - Estágio fenológico do conilon no ES
   - Estimativas de produtividade (se disponíveis)

3. **Mercado Global**
   - Preços de commodities correlatas (café, cacau, açúcar)
   - Câmbio (impacto em exportações)
   - Volumes de negociação (liquidez)

4. **Políticas & Regulação**
   - Medidas governamentais recentes (subsídios, tarifas)
   - Legislação ambiental/trabalhista
   - Programas de fomento disponíveis

### Step 2: Análise de Convergência

1. Identificar concordâncias:
   - Tendências que se reforçam mutuamente (ex: preços em alta + clima favorável)
   - Desalinhamentos que criam risco (ex: preços baixos + safra reduzida)

2. Projetar horizonte:
   - Curto prazo (próximas 2-4 semanas): recomendações operacionais
   - Médio prazo (próximos 3-6 meses): decisões de plantio/investimento
   - Longo prazo (semestral+): reposicionamento estratégico

### Step 3: Geração da Síntese Executiva

Produzir documento estruturado:

```
## Síntese de Tendências — [Data]

### Situação Atual

**Resumo executivo de 3 parágrafos** integrado:
- Dinâmica de preços no contexto global
- Condição climática e perspectiva de safra
- Oportunidades e riscos principais

### Dimensão 1: Preços & Mercado

#### Movimento Recente
- [variação últimas 2 semanas]
- Posição no ciclo: [alta, baixa, normal]
- Comparação histórica: [acima/abaixo média de 5 anos]

#### Fatores de Pressão
- [forças de alta] vs. [forças de baixa]
- Liquidez: [comentário sobre volumes]

#### Perspectiva (próximos 30-90 dias)
- [projeção de tendência]
- [fatores críticos a monitorar]

### Dimensão 2: Clima & Safra

#### Estado Atual
- Estágio fenológico: [fase]
- Condições de umidade de solo: [situação]
- Alertas climáticos: [lista]

#### Perspectiva (próximas 4-8 semanas)
- [previsão de produtividade]
- [riscos climáticos a acompanhar]

### Dimensão 3: Contexto Global & Macro

#### Câmbio & Exportações
- Dólar: [valor + tendência]
- Impacto em competitividade: [análise]

#### Políticas & Programas
- [medidas governamentais relevantes]
- [oportunidades de fomento]

### Recomendações Estratégicas

**Curto prazo (2-4 semanas):**
- [ação 1]
- [ação 2]

**Médio prazo (3-6 meses):**
- [decisão de investimento/plantio]
- [ajustes operacionais]

**Monitoramento contínuo:**
- [indicador crítico 1]
- [indicador crítico 2]

### Incertezas & Cenários Alternativos

- **Cenário otimista:** [descrição + probabilidade]
- **Cenário base:** [descrição + probabilidade]
- **Cenário pessimista:** [descrição + probabilidade]

### Fontes & Metodologia
- Data de referência: YYYY-MM-DD
- Dados integrados de: [listar skills/fontes consultadas]
- Próxima síntese: [data prevista]
```

### Step 4: Registro em Vault

Arquivar síntese em `Products/Eloi/tendencias-estrategicas/` com versionamento por data. Manter histórico para rastrear acertos e aprendizado.

## Triggers

- "síntese de tendências"
- "relatório de inteligência de mercado"
- "briefing estratégico"
- "quadro geral do setor"
- "como está a situação geral?"
- Automático: semanal ou sob demanda

## Notas

- A síntese é executiva: não detalha metodologias, aponta decisões
- Sempre indicar incertezas e cenários alternativos (decisão é sempre sob risco)
- Integra outputs de outras skills (monitor-precos-agricolas, alerta-climatico, pesquisa-mercado)
- Deve ser acionável: cada seção termina com recomendação concreta
