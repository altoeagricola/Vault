---
name: pesquisa-mercado
description: Conduz pesquisa externa aprofundada sobre empresas, tecnologias, setores ou players de mercado, produzindo fichas estruturadas com separação explícita entre fato verificado, claim comercial e inferência. Use quando o usuário disser "pesquisar empresa", "inteligência competitiva", "mapeamento de players", "análise de concorrentes", ou quando houver necessidade de research externo antes de registro no Vault.
---

# Pesquisa de Mercado Estruturada

Skill dedicada à pesquisa externa aprofundada sobre empresas, tecnologias, setores ou competitors, com rigor metodológico na separação entre fato, claim e inferência.

## Workflow

### Step 1: Escopo da Pesquisa

1. Definir objeto de pesquisa:
   - **Empresa**: razão social, CNPJ, setor, localização
   - **Tecnologia**: nome, aplicação, players, maturidade
   - **Setor/Segmento**: delimitação geográfica, subsegmentos
   - **Competidor**: empresa específica ou conjunto de concorrentes

2. Definir questões de pesquisa:
   - O que se quer saber? (missão, capacidade, posição de mercado, etc.)
   - Qual o horizonte temporal? (situação atual, evolução, projeção)
   - Qual a profundidade? (overview vs. análise detalhada)

### Step 2: Coleta Estruturada

Pesquisar em fontes oficiais e verificáveis:

1. **Fontes Primárias**
   - Site corporativo (missão, equipe, portfólio)
   - Dados públicos de registro (CNPJ, inscrição estadual, endereço)
   - Documentos regulatórios (CVM, INMETRO, etc.)
   - Patentes (INPI, WIPO)
   - Publicações da própria empresa

2. **Fontes Secundárias Confiáveis**
   - Publicações de imprensa consolidada (jornais, revistas)
   - Relatórios de associações setoriais
   - Análises de consultoria (Gartner, IDC, etc.)
   - Publicações acadêmicas (quando relevante)
   - Bases de dados comerciais (Crunchbase, PitchBook, etc.)

3. **Evitar**
   - Redes sociais como fonte de verdade (apenas para reputação/presença)
   - Claims não verificados
   - Fontes anônimas

### Step 3: Construção da Ficha Estruturada

Registrar cada dado com sua **origem e classificação**:

```
## [Empresa/Tecnologia] — Ficha de Pesquisa

### Identificação Básica

| Campo | Valor | Fonte | Data |
|-------|-------|-------|------|
| Razão Social | | | |
| CNPJ | | | |
| Localização | | | |
| Setor | | | |

### Fatos Verificados (com fonte explícita)

#### Estrutura
- **Fundação:** YYYY (Fonte: registro legal)
- **Sedes:** [endereços] (Fonte: CNPJ, site)
- **Equipe (aprox.):** N pessoas (Fonte: LinkedIn, last check YYYY-MM-DD)
- **Estrutura de governança:** [descrição] (Fonte: site, notícia)

#### Produtos/Serviços
- **Portfólio:** [lista] (Fonte: site)
- **Posicionamento:** [segmento, preço, diferencial] (Fonte: site, material de marketing)
- **Clientes principais:** [lista, se pública] (Fonte: case studies, press releases)

#### Desempenho Financeiro
- **Faturamento:** R$ X [ano] (Fonte: jornal X, publicado YYYY-MM-DD)
- **Investimentos recebidos:** R$ X em [rodada], [investidores] (Fonte: base dados Y, data)
- **Rentabilidade:** [se pública] (Fonte: demonstração contábil, link)

### Claims Comerciais (com marcação)

**CLAIM:** "Somos líderes em [segmento] na região"
- Fonte: site corporativo
- Contexto: página de "Sobre nós"
- Verificação: ✓ parcialmente verificável | ✗ não verificado
- Nota: [comentário crítico, se aplicável]

[idem para outros claims]

### Inferências & Análise

**INFERÊNCIA:** Baseado em [fatos 1, 2, 3], conclui-se que [análise]
- Confiança: [alta | média | baixa]
- Fatores de incerteza: [lista]
- Alternativas: [outras interpretações possíveis]

Exemplo:
**INFERÊNCIA:** A empresa está em expansão geográfica
- Evidência: (1) Abertura de nova sede em [cidade], (2) Recrutamento de 15+ pessoas em [região], (3) Parceria com distribuidor local
- Confiança: alta
- Fonte: press release + LinkedIn + notícia jornal X
- Fatores de incerteza: ritmo de expansão desconhecido

### Matriz Competitiva (se múltiplos players)

| Player | Segmento | Posição | Força | Fraqueza | Tendência |
|--------|----------|---------|-------|----------|-----------|
| A | | | | | |
| B | | | | | |

### Conclusões & Próximos Passos

**Resumo:**
- [síntese dos achados principais]
- [lacunas de informação remanescentes]

**Recomendações:**
- Para decisão estratégica: [sugestão]
- Pesquisa futura: [tópicos não cobertos]

### Cronograma de Pesquisa

- Pesquisa iniciada: YYYY-MM-DD HH:MM
- Pesquisa concluída: YYYY-MM-DD HH:MM
- Próxima atualização recomendada: YYYY-MM-DD (razão)

### Fontes Consultadas

[Lista completa com URLs, datas de acesso, contexto de cada fonte]
```

### Step 4: Ingestão no Vault

1. Salvar ficha em `Sources/Research/Market/[objeto]/`
2. Disparar skill `/ingest` para processar e integrar ao Vault
3. Criar wiki pages para players significativos (reutilizável)
4. Registrar em índice de pesquisas (`Products/Eloi/pesquisas-mercado/Index.md`)

## Triggers

- "pesquisar empresa [X]"
- "inteligência competitiva de [player]"
- "mapeamento de players em [setor]"
- "análise de concorrentes"
- "quem é [empresa]?"
- "fichas de [setor]"

## Notas

- **Rigor é essencial**: a separação fato/claim/inferência permite que o usuário entenda o que é certeza vs. suposição
- **Rastreabilidade**: toda informação deve ter fonte identificada e data de acesso (informação envelhece rapidamente)
- **Atualização**: mercado muda; manter histórico de pesquisas para rastrear evolução
- **Acionabilidade**: conclusões devem levar a decisão ou ação, não apenas informação
- Para pesquisas em empresas privadas (sem dados públicos), ser claro sobre limitações de escopo
