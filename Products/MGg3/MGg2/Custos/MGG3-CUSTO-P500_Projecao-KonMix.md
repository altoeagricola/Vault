---
titulo: Projeção de Custo P500 - KonMix / MGg 3.0
tipo: registro-documento
produto: MGg3
codigo_fonte: MGG3-CUSTO-P500
fonte_arquivo: "P500_Custo de Produção - 1 turno - KonMix - MGg 3.0.xlsx"
caminho_fonte: "Products/MGg3/MGg2/Custos/P500_Custo de Produção - 1 turno - KonMix - MGg 3.0.xlsx"
nome_original: "P500_Custo de Produção - 1 turno - KonMix - MGg 3.0.xlsx"
organizacao: MGg3 / KonMix
tipo_documento: projecao economica / planilha de custo escalonado
data_documento: 2026
confidencialidade: interno
status_extracao: extraido_parcial
confianca_extracao: media
temas:
  - projecao de custos
  - escalamento P500
  - economia de escala
  - viabilidade comercial
  - MGg3
produtos:
  - MGgrafeno
  - MGg3
aplicacoes:
  - grafeno
  - escalamento comercial
metricas_chave:
  - capacidade P500 (500 L / turno)
  - custo por litro P500 vs P100
  - economia de escala
  - comparacao com P100
  - premissas de operacao
  - breakeven point
riscos_uso:
  - projecao baseada em extrapolacao de dados P100; validacao em operacao necessaria
  - confidencialidade de modelo; nao compartilhar com terceiros
  - atualizacoes de premissas de insumo podem afetar significativamente resultados
  - riscos de operacao em escala maior nao captados em modelo P100
links_relacionados:
  - "[[Custos de producao P100 P500]]"
  - "[[MGG3-FORN01_Fornecedores-grafeno]]"
  - "[[MGG3-FORN02_Fornecedores-insumos-grafeno-startup]]"
  - "[[Benchmark internacional - fornecedores de grafeno]]"
  - "[[Planta piloto CDTN]]"
  - "[[MGG2-CUSTO-P100_Modelo-custo-planta-piloto]]"
  - "[[Saneamento custos P100 P500]]"
  - "[[MGg2]]"
atualizado: 2026-06-11
---
# MGG3-CUSTO-P500: Projeção de Custo P500 - KonMix / MGg 3.0

## Identificacao

| Campo | Valor |
|---|---|
| Arquivo | `P500_Custo de Produção - 1 turno - KonMix - MGg 3.0.xlsx` |
| Tipo | Projeção econômica / Planilha de custo escalonado |
| Origem | KonMix (partner de escalamento MGg3) |
| Data | 2026 (recente) |
| Escala | P500 (500 L/turno, 1 turno) |
| Confidencialidade | Interno |
| Status | Projeção em validação; baseada em extrapolação de dados P100 |

## Resumo executivo

Modelo de projeção de custos para escalonamento da produção de grafeno em escala P500, desenvolvido por KonMix no contexto da iniciativa MGg3. Planilha que compara economia de escala entre P100 (2021) e P500 (projeção 2026), fornecendo métricas críticas para decisão de investimento em planta em escala comercial.

## Papel no briefing

Fonte primária para:
- avaliar viabilidade econômica de escalamento de P100 para P500;
- identificar economia de escala e redução de custo/litro;
- estabelecer cenários de breakeven e rentabilidade;
- subsidiar decisões de captação de recursos para escalonamento;
- validar tese de viabilidade comercial para investidores.

## Conteudo esperado (abas)

- **Configurações P500**: parâmetros de operação 1 turno
- **Comparação P100 x P500**: evolução de custos e economia
- **MGg3.0**: aba específica com premissas e cenários revisados
- **Dashboard economico**: sumário de viabilidade
- **Insumos e equipamentos**: detalhamento por fator de custo
- **Sensibilidade**: variações de premissas-chave

## Lacunas e cautelas

- Projeção baseada em extrapolação de dados de P100 (2021); validação em operação piloto P500 é crítica.
- Confidencialidade do modelo; nao compartilhar com parceiros sem aprovacao KonMix/MGg3.
- Premissas sobre preço de insumos, energia e mao-de-obra podem divergir de realidade operacional.
- Riscos de escalonamento (controle de qualidade, downtime, variabilidade de processo) podem impactar custos reais.
- Atualizacao Konmix 2026: usar [[MGG3-CUSTO-P500-v2_Escalonamento-Engenharia-P100-P500]] como leitura canonica de CAPEX/OPEX reconciliado. As evidencias de cotacao de cisalhador ficam em [[MGG3-COT-20260506-01_konmix-inline-homogenizer-krb75-3]] e [[MGG3-COT-20260505-01_konmix-inline-homogenizer-krb15-3]]; esta nota permanece como registro da planilha/projecao original.

## Proximas acoes

- Usar [[Saneamento custos P100 P500]] como leitura preliminar de equipamentos, rendimento, ponte de custos e comparabilidade com P100.
- Para cisalhador P500, usar a v2 como fonte de CAPEX; nao reutilizar estimativas antigas da planilha/projecao sem a ressalva de sanity check.
- Validar premissas com equipe operacional de KonMix antes de apresentacao a investidores.
- Incluir análise de risco e cenários de downside em sumário executivo para captacao.
