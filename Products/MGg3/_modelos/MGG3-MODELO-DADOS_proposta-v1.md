---
titulo: Modelagem de dados MGgrafeno - proposta v1
tipo: modelo-dados
produto: MGg3
subproduto: MGg2
codigo_fonte: MGG3-MODELO-DADOS-v1
status: proposta-inicial
audiencia: time tecnico, time de produto, Mariano, Eloi, Carmen, Valdemiro, Julio
fontes_base:
  - "[[INVENTÁRIO-MESTRE]]"
  - "[[Parametros criticos PL100 e acabamento]]"
  - "[[Mapa de processo e correntes MGgrafeno]]"
  - "[[KNOW-HOW-55.1-2024_Producao-de-Grafeno]]"
  - "[[Processo-Referencia-Levantamento-de-Custos]]"
  - "[[MGG2-CTRL01_Controle-de-producoes]]"
  - "[[MGG2-CTRL04_Controle-de-Processos-2022]]"
  - "[[MGG2-CTRL05_Balanco-Global-XLSX]]"
  - "[[MGG2-ANEXOA-BMG_Balanco-Massa-Global-PDF]]"
  - "[[MGG2-RTF-VOLV_SSMA-Tratamento-Residuos]]"
  - "[[MGG3-FORN01_Fornecedores-grafeno]]"
  - "[[MGG3-FORN02_Fornecedores-insumos-grafeno-startup]]"
  - "[[MGG3-PAD-FORN02_Padrao-registro-precos-grafeno]]"
  - "[[MGG3-LEV-P100-v10_Levantamento-Custos-Cenarios-Desenvolvimento-Producao-Consolidado]]"
  - "[[MGG3-CUSTO-P500_Projecao-KonMix]]"
  - "[[Modelo de negocios MGgrafeno - orquestracao aplicada]]"
confidencialidade: interno
atualizado: 2026-05-29
---

# Modelagem de dados MGgrafeno — proposta v1

## Objetivo

Organizar, em um modelo de dados relacional, todos os parametros que aparecem hoje espalhados em notas, planilhas, PDFs e relatorios da camada MGg2/MGg3 — preservando a rastreabilidade de evidencia, a separacao entre dado observado e premissa, e a taxonomia canonica ja consolidada nas notas tecnicas. A referencia de implementacao e PostgreSQL, mas o modelo e portavel para qualquer SGBD relacional moderno.

A proposta nao substitui o Vault: o Vault continua sendo o repositorio narrativo e de evidencia primaria. O banco entra como camada estruturada para consultas, cruzamentos e indicadores que hoje exigem leitura manual de notas e planilhas.

## Principios de modelagem

1. **Evidencia versus interpretacao.** Toda medicao numerica entra ligada a um documento-fonte com data, tipo, status de confiabilidade e confidencialidade. Premissas e cenarios sao tabelas separadas das observacoes, com fonte de derivacao explicita.
2. **Taxonomia canonica.** Codigos de corrente (`c31`, `d01`, `d02`, `d03`, `d04`, `s02`-`s04`, `ssma-lq1`...), produtos (`GPC`, `NPG`, `NG`), modulos (Conversao, Separacao, Acabamento, SSMA) e lotes (`20210720Pa`) sao chaves naturais consultaveis.
3. **Aliases preservados, nao duplicados.** `Grafeno A = GPC`, `Grafeno B = NPG`, `Nanografite = NG`, `Triton X-100 = Titon X-100`, `Frist Graphene = First Graphene`, `CamGraph = Levidian`, etc. ficam em uma tabela de alias amarrada ao canonico, conforme padrao MGG3-PAD-FORN02.
4. **Status semantico do dado.** Cada valor carrega `status_dado` ∈ {`observado`, `calculado`, `premissa`, `estimado`, `defasado`, `conflito`, `nao_comparavel`} alinhado ao vocabulario ja praticado pelo padrao de precos e pelas notas tecnicas.
5. **Confidencialidade obrigatoria.** Todo registro carrega nivel `publico | interno | confidencial | restrito`, espelhando o frontmatter das notas.
6. **Camadas separadas por schema.** Sete schemas — documental, tecnologia, operacao, ssma, suprimentos, custo, aplicacao — permitem que cada agente (Mariano, Eloi, Carmen, Julio, Valdemiro) trabalhe sua camada sem misturar concerns.

## Mapa de camadas

| Schema | Conteudo | Fontes representativas |
|---|---|---|
| `documental` | Inventario de fontes, notas, anexos, links, agentes, issues. | INVENTÁRIO-MESTRE; Matriz de anexos; frontmatter das notas. |
| `tecnologia` | Modulos, equipamentos, correntes, produtos, parametros canonicos baseline. | Mapa de processo e correntes; Parametros criticos PL100; KNOW-HOW 55.1; Relatorio Anual 2020-2021. |
| `operacao` | Campanhas, lotes, balanco de massa, medicoes de processo, formularios. | Controle de producoes; Controle de Processos 03_03_2022; Balanco Global XLSX/PPTX; Anexo A BMG; lote `20210720Pa`. |
| `ssma` | Tipos de residuo, eventos de tratamento, criterios SSMA, consumiveis. | Relatorio Tecnico Final Volume V - SSMA. |
| `suprimentos` | Fornecedores, materiais, produtos/grades, insumos, utilidades, HH, cotacoes/precos. | MGG3-FORN01, MGG3-FORN02, Benchmark internacional, MGG3-PAD-FORN02. |
| `custo` | Cenarios, premissas, blocos de custo, valores OPEX/CAPEX, condicoes de rendimento, custo unitario por produto, sensibilidades. | MGG3-LEV-P100-v3..v10; MGG3-CUSTO-P500; Saneamento custos P100 P500. |
| `aplicacao` | Plataformas, produtos comerciais, cases, resultados tecnicos quantificados, parceiros, players de mercado, editais. | Apresentacoes GG; Concretos CM018; Polimeros BlackSwan; Inteligencia de Mercado GG; Inteligencia de Mercado MGg3; Case NanoXplore; Edital 1337/2025. |

## Diagrama logico (resumo)

```
documental.documento ── 1:N ──┐
                              │
tecnologia.modulo ── 1:N ── tecnologia.equipamento
tecnologia.modulo ── 1:N ── tecnologia.corrente ── 1:N ── tecnologia.corrente_alias
tecnologia.produto_canonico ── 1:N ── tecnologia.produto_acabamento
tecnologia.parametro ── 1:N ── tecnologia.parametro_baseline

operacao.campanha ── 1:N ── operacao.lote ── 1:N ── operacao.lote_insumo
                                    │           ── 1:N ── operacao.lote_saida
                                    │           ── 1:N ── operacao.lote_medicao
                                    │           ── 1:N ── operacao.lote_formulario
                                    └── N:1 ── tecnologia.equipamento

ssma.residuo_tipo ── 1:N ── ssma.residuo_evento ── N:1 ── operacao.lote (opcional)
ssma.criterio ── 1:N ── ssma.criterio_observado
ssma.consumivel ── 1:N ── ssma.consumivel_consumo

suprimentos.fornecedor ── 1:N ── suprimentos.fornecedor_alias
suprimentos.fornecedor ── 1:N ── suprimentos.produto_fornecedor ── N:1 ── suprimentos.material
suprimentos.produto_fornecedor ── 1:N ── suprimentos.cotacao
suprimentos.insumo / utilidade / hh ── 1:N ── suprimentos.cotacao

custo.cenario ── 1:N ── custo.premissa
custo.cenario ── 1:N ── custo.bloco_valor ── N:1 ── custo.bloco_tipo
custo.cenario ── 1:N ── custo.condicao_rendimento ── 1:N ── custo.custo_unitario_produto
custo.cenario ── 1:N ── custo.sensibilidade

aplicacao.plataforma ── 1:N ── aplicacao.produto_comercial ── 1:N ── aplicacao.resultado_tecnico
aplicacao.produto_comercial ── 1:N ── aplicacao.case_aplicacao ── N:1 ── aplicacao.parceiro
aplicacao.player_mercado, aplicacao.parceiro_institucional, aplicacao.edital sao referencias laterais.
```

Toda tabela tem coluna `fonte_documento_id` (FK para `documental.documento`) e `status_dado` para preservar evidencia + interpretacao.

## DDL PostgreSQL (referencia v1)

```sql
-- =============================================================
-- MGG3 / MGgrafeno - Modelo de dados v1 (PostgreSQL 15+)
-- Autoria editorial: Cacilda - 2026-05-29
-- =============================================================
-- Convencoes:
--   * UUID como PK gerado por gen_random_uuid() (pgcrypto)
--   * Codigos canonicos (slug) sao UNIQUE em paralelo a UUID
--   * Timestamps com TIMESTAMPTZ; datas observadas com DATE
--   * Numeric/Decimal com precisao explicita para massa/dinheiro
--   * ENUM via tipos nomeados; tabelas-look-up onde a lista pode crescer
--   * Comentarios COMMENT ON TABLE/COLUMN para rastreabilidade
-- =============================================================

CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- =============================================================
-- SCHEMAS
-- =============================================================
CREATE SCHEMA documental;
CREATE SCHEMA tecnologia;
CREATE SCHEMA operacao;
CREATE SCHEMA ssma;
CREATE SCHEMA suprimentos;
CREATE SCHEMA custo;
CREATE SCHEMA aplicacao;

-- =============================================================
-- ENUMs compartilhados
-- =============================================================
CREATE TYPE confidencialidade_t AS ENUM
    ('publico','interno','confidencial','restrito','desconhecido');

CREATE TYPE status_dado_t AS ENUM
    ('observado','calculado','premissa','estimado','defasado','conflito','nao_comparavel');

CREATE TYPE status_confiabilidade_t AS ENUM
    ('forte','medio','fraco','obsoleto','nao_comparavel');

CREATE TYPE tipo_agente_t AS ENUM
    ('humano','agente_ai','organizacao_externa');

-- =============================================================
-- documental.*  -- rastreabilidade de evidencia
-- =============================================================
CREATE TABLE documental.agente (
    id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    slug          TEXT UNIQUE NOT NULL,           -- 'cacilda','mariano','eloi','carmen','julio','valdemiro'
    nome          TEXT NOT NULL,
    tipo          tipo_agente_t NOT NULL,
    papel         TEXT,                            -- responsavel editorial, custos, fornecedores, etc.
    ativo         BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE documental.tipo_documento (
    id            SMALLSERIAL PRIMARY KEY,
    slug          TEXT UNIQUE NOT NULL,           -- 'briefing','know-how','mapa-processo','parametros',
    descricao     TEXT                              --   'anexo','edital','planilha-balanco','planilha-custo','nota-canonica','registro-evidencia',
);                                                  --   'apresentacao','relatorio-tecnico','case','inventario'

CREATE TABLE documental.documento (
    id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    codigo              TEXT UNIQUE NOT NULL,        -- 'MGG2-BASE01', 'MGG2-KH55.1', 'MGG3-FORN02', 'GG-CM018'...
    titulo              TEXT NOT NULL,
    tipo_id             SMALLINT NOT NULL REFERENCES documental.tipo_documento(id),
    data_documento      DATE,
    periodo_coberto_ini DATE,
    periodo_coberto_fim DATE,
    tamanho_bytes       BIGINT,
    confidencialidade   confidencialidade_t NOT NULL DEFAULT 'interno',
    status_extracao     TEXT,                        -- 'extraido','extraido_parcial','extraido_controlado','criado','pendente','obsoleto'
    caminho_vault       TEXT,                        -- 'Products/MGg3/MGg2/Custos/...'
    origem_externa      TEXT,                        -- '/Users/.../EVT-MGg3/...'
    observacoes         TEXT,
    fonte_base_id       UUID REFERENCES documental.documento(id), -- documento-mae quando esta nota deriva de outro
    criado_por          UUID REFERENCES documental.agente(id),
    criado_em           TIMESTAMPTZ NOT NULL DEFAULT now(),
    atualizado_em       TIMESTAMPTZ NOT NULL DEFAULT now()
);
COMMENT ON TABLE documental.documento IS
  'Inventario mestre de fontes (INVENTARIO-MESTRE.md). Toda medicao no banco aponta para uma linha aqui.';

CREATE TABLE documental.documento_tema (
    documento_id  UUID NOT NULL REFERENCES documental.documento(id) ON DELETE CASCADE,
    tema          TEXT NOT NULL,
    PRIMARY KEY (documento_id, tema)
);

CREATE TABLE documental.documento_lacuna (
    id            BIGSERIAL PRIMARY KEY,
    documento_id  UUID NOT NULL REFERENCES documental.documento(id) ON DELETE CASCADE,
    descricao     TEXT NOT NULL,
    prioridade    TEXT                              -- 'alta','media','baixa'
);

CREATE TABLE documental.link_documento (
    origem_id     UUID NOT NULL REFERENCES documental.documento(id) ON DELETE CASCADE,
    destino_id    UUID NOT NULL REFERENCES documental.documento(id) ON DELETE CASCADE,
    tipo_link     TEXT NOT NULL,                    -- 'deriva-de','valida','contradiz','complementa'
    PRIMARY KEY (origem_id, destino_id, tipo_link)
);

CREATE TABLE documental.issue (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    chave           TEXT UNIQUE NOT NULL,            -- 'ALT-301','ALT-440','ALT-462'
    titulo          TEXT NOT NULL,
    status          TEXT,                            -- 'todo','in_progress','in_review','done','blocked'
    responsavel_id  UUID REFERENCES documental.agente(id),
    criado_em       TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE documental.documento_issue (
    documento_id  UUID NOT NULL REFERENCES documental.documento(id) ON DELETE CASCADE,
    issue_id      UUID NOT NULL REFERENCES documental.issue(id)     ON DELETE CASCADE,
    PRIMARY KEY (documento_id, issue_id)
);

-- =============================================================
-- tecnologia.*  -- taxonomia canonica do processo
-- =============================================================
CREATE TABLE tecnologia.modulo (
    id            SMALLSERIAL PRIMARY KEY,
    slug          TEXT UNIQUE NOT NULL,           -- 'conversao','separacao','acabamento','ssma'
    nome          TEXT NOT NULL,
    descricao     TEXT,
    ordem         SMALLINT                          -- 1..n na cadeia produtiva
);

CREATE TABLE tecnologia.equipamento (
    id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    slug          TEXT UNIQUE NOT NULL,           -- 'p25-silverson-verso','p100-konmix','ika-bancada','decanter','discos','spray-dryer','liofilizador','filtracao-tangencial'
    nome          TEXT NOT NULL,
    modulo_id     SMALLINT NOT NULL REFERENCES tecnologia.modulo(id),
    escala        TEXT,                             -- 'P25','P100','P500','bancada','planta-piloto','planta-industrial'
    papel         TEXT,                             -- 'desenvolvimento','baseline-produtivo','escala'
    fabricante    TEXT,
    modelo        TEXT,
    volume_nominal_l NUMERIC(10,2),
    observacoes   TEXT
);

CREATE TABLE tecnologia.corrente (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    codigo          TEXT UNIQUE NOT NULL,           -- 'c31','d01','d02','d03','d04','s02','s03','s04',
    nome_canonico   TEXT NOT NULL,                   --   'ssma-lq1','ssma-lq2','ssma-sol1','ssma-sol2','ssma-fp-solido','ssma-agua-reuso'
    tipo            TEXT NOT NULL,                  -- 'intermediario','produto','subproduto','residuo-liquido','residuo-solido','agua-reuso'
    modulo_id       SMALLINT NOT NULL REFERENCES tecnologia.modulo(id),
    origem          TEXT,                            -- equipamento/operacao que produz
    observacoes     TEXT
);

CREATE TABLE tecnologia.corrente_alias (
    corrente_id   UUID NOT NULL REFERENCES tecnologia.corrente(id) ON DELETE CASCADE,
    alias         TEXT NOT NULL,                   -- 's02' alias de 'd02' (rota discos), 'Grafeno B' alias do NPG
    contexto      TEXT,                             -- 'rota-discos','nome-comercial','historico'
    PRIMARY KEY (corrente_id, alias)
);

CREATE TABLE tecnologia.produto_canonico (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    sigla           TEXT UNIQUE NOT NULL,           -- 'GPC','NPG','NG'
    nome            TEXT NOT NULL,                  -- 'Grafeno de Poucas Camadas','NanoPlaca de Grafeno','Nanografite/Nanoplaca de grafite'
    descricao       TEXT,
    posicao_valor   SMALLINT                        -- ranking de valor tecnico (4 GPC, 2 NPG, 1 NG) - alinhado ao MGG3-LEV-P100-v10
);

CREATE TABLE tecnologia.produto_alias (
    produto_id    UUID NOT NULL REFERENCES tecnologia.produto_canonico(id) ON DELETE CASCADE,
    alias         TEXT NOT NULL,                   -- 'Grafeno A','Grafeno B','Nanoplaca de grafite','Few-layer graphene','FLG'
    contexto      TEXT,
    PRIMARY KEY (produto_id, alias)
);

CREATE TABLE tecnologia.produto_acabamento (
    id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    slug          TEXT UNIQUE NOT NULL,           -- 'gpc-seco-spray','gpc-seco-liofilizado','npg-seco','ng-seco','gpc-c','gpc-bf'
    nome          TEXT NOT NULL,
    produto_id    UUID NOT NULL REFERENCES tecnologia.produto_canonico(id),
    rota          TEXT NOT NULL,                  -- 'spray-dryer','liofilizacao','filtracao-tangencial','diafiltracao','troca-aditivo'
    descricao     TEXT
);

CREATE TABLE tecnologia.parametro (
    id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    slug          TEXT UNIQUE NOT NULL,           -- 'ph','rotacao','frequencia','tempo','temperatura','vazao','condutividade','razao-grafite-agua','rendimento-fracao'
    nome          TEXT NOT NULL,
    unidade       TEXT NOT NULL,                  -- 'pH','rpm','Hz','h','degC','L/h','L/min','uS','g/L','%','kg','kg/L'
    contexto      TEXT                              -- 'conversao','separacao-decanter','separacao-discos','acabamento-spray-dryer','filtracao-tangencial','ssma','agua-reuso'
);

CREATE TABLE tecnologia.parametro_baseline (
    id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    parametro_id      UUID NOT NULL REFERENCES tecnologia.parametro(id),
    equipamento_id    UUID REFERENCES tecnologia.equipamento(id),
    corrente_id       UUID REFERENCES tecnologia.corrente(id),
    valor_min         NUMERIC,
    valor_max         NUMERIC,
    valor_nominal     NUMERIC,
    descricao_valor   TEXT,                          -- 'Padrao 10 com NaOH','60 Hz / ~3500 rpm','75 L/h','100 g/L'
    status_dado       status_dado_t NOT NULL DEFAULT 'observado',
    fonte_documento_id UUID NOT NULL REFERENCES documental.documento(id),
    observacoes       TEXT,                          -- 'conflito de unidade entre 4700-5100 L/h e 4700 L/min'
    UNIQUE (parametro_id, equipamento_id, corrente_id, status_dado, fonte_documento_id)
);
COMMENT ON TABLE tecnologia.parametro_baseline IS
  'Valor canonico (faixa ou nominal) por parametro+equipamento+corrente, com fonte e status. Origem direta: Parametros criticos PL100 e acabamento + Mapa de processo e correntes.';

-- =============================================================
-- operacao.*  -- lotes, campanhas, balanco de massa
-- =============================================================
CREATE TABLE operacao.campanha (
    id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    slug          TEXT UNIQUE NOT NULL,           -- 'duda','ana','otto','bertha','katrina','prod-cont-camp-01'
    nome          TEXT NOT NULL,
    objetivo      TEXT,
    inicio        DATE,
    fim           DATE
);

CREATE TABLE operacao.lote (
    id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    codigo              TEXT UNIQUE NOT NULL,         -- '20210720Pa'
    data_producao       DATE NOT NULL,
    piloto              TEXT,                          -- 'P25','P50','P100','P100-1','P100-2','P500'
    equipamento_id      UUID REFERENCES tecnologia.equipamento(id),
    campanha_id         UUID REFERENCES operacao.campanha(id),
    concentracao_nominal_g_l   NUMERIC(8,2),         -- 100 (rotulo operacional)
    concentracao_calculada_g_l NUMERIC(8,3),         -- 95.502 (XLSX) - separar nominal x calculado
    tempo_conversao_h   NUMERIC(6,2),
    base_quimica        TEXT,                          -- 'NaOH','NH4OH','sem-ajuste'
    rotacao_rpm         INTEGER,
    frequencia_hz       INTEGER,
    rota_primeira_separacao TEXT,                     -- 'estatica','decanter'
    rota_segunda_separacao  TEXT,                     -- 'discos','membrana','spray-dryer-direto'
    objetivo_lote       TEXT,
    observacoes         TEXT,
    fonte_documento_id  UUID REFERENCES documental.documento(id),
    status_dado         status_dado_t NOT NULL DEFAULT 'observado'
);
COMMENT ON TABLE operacao.lote IS
  'Registro mestre de lote produtivo. Campos cobrem MGG2-CTRL01, CTRL04 e CTRL05; o lote 20210720Pa e a referencia canonica para custo.';

CREATE TABLE operacao.lote_formulario (
    lote_id       UUID NOT NULL REFERENCES operacao.lote(id) ON DELETE CASCADE,
    formulario    TEXT NOT NULL,                    -- 'F-185','F-192','F-220' ou numero direto
    etapa         TEXT,                              -- 'conversao','separacao','acabamento'
    PRIMARY KEY (lote_id, formulario)
);

CREATE TABLE operacao.lote_insumo (
    id            BIGSERIAL PRIMARY KEY,
    lote_id       UUID NOT NULL REFERENCES operacao.lote(id) ON DELETE CASCADE,
    item          TEXT NOT NULL,                    -- 'agua','grafite','aditivo','base'
    massa_kg      NUMERIC(12,5),
    volume_l      NUMERIC(12,5),
    especificacao TEXT,                              -- 'Triton X-100 0,1% m/m','NaOH ajuste pH10','agua tipo II'
    status_dado   status_dado_t NOT NULL DEFAULT 'observado',
    fonte_documento_id UUID REFERENCES documental.documento(id)
);

CREATE TABLE operacao.lote_saida (
    id            BIGSERIAL PRIMARY KEY,
    lote_id       UUID NOT NULL REFERENCES operacao.lote(id) ON DELETE CASCADE,
    produto_id    UUID REFERENCES tecnologia.produto_canonico(id),
    corrente_id   UUID REFERENCES tecnologia.corrente(id),
    massa_kg      NUMERIC(12,5),
    rendimento_pct NUMERIC(7,4),                     -- % em massa rel. grafite alimentado
    eh_perda      BOOLEAN NOT NULL DEFAULT FALSE,
    observacoes   TEXT,
    status_dado   status_dado_t NOT NULL DEFAULT 'observado',
    fonte_documento_id UUID REFERENCES documental.documento(id)
);
COMMENT ON COLUMN operacao.lote_saida.rendimento_pct IS
  'Rendimento percentual em massa relativo a massa inicial de grafite seco alimentado (convencao MGG3-LEV-P100-v10).';

CREATE TABLE operacao.lote_medicao (
    id            BIGSERIAL PRIMARY KEY,
    lote_id       UUID NOT NULL REFERENCES operacao.lote(id) ON DELETE CASCADE,
    parametro_id  UUID NOT NULL REFERENCES tecnologia.parametro(id),
    corrente_id   UUID REFERENCES tecnologia.corrente(id),
    etapa         TEXT,                              -- 'conversao','primeira-separacao','segunda-separacao','acabamento','ssma'
    valor         NUMERIC(14,4),
    unidade       TEXT,
    observado_em  TIMESTAMPTZ,
    status_dado   status_dado_t NOT NULL DEFAULT 'observado',
    fonte_documento_id UUID REFERENCES documental.documento(id)
);

CREATE INDEX ON operacao.lote_medicao (parametro_id);
CREATE INDEX ON operacao.lote_medicao (lote_id, etapa);

CREATE TABLE operacao.volume_processado_periodo (
    id            BIGSERIAL PRIMARY KEY,
    ano           SMALLINT NOT NULL,
    mes           SMALLINT,
    piloto        TEXT,                              -- agregacao por piloto P100/P25/...
    lotes_qtd     INTEGER,
    massa_total_kg NUMERIC(14,3),
    fonte_documento_id UUID REFERENCES documental.documento(id),
    status_dado   status_dado_t NOT NULL DEFAULT 'observado'
);

-- =============================================================
-- ssma.*  -- residuos, agua de reuso, consumiveis SSMA
-- =============================================================
CREATE TABLE ssma.residuo_tipo (
    id            SMALLSERIAL PRIMARY KEY,
    slug          TEXT UNIQUE NOT NULL,           -- 'lq1','lq2','sol1','sol2','fp-solido','agua-reuso'
    nome          TEXT NOT NULL,
    classe        TEXT,                             -- 'classe-I','perigoso','reaproveitavel','reuso'
    destinacao    TEXT,                             -- 'tratamento-interno-ssma','incineracao-SEGRE','aterro-classe-I','reuso-interno'
    descricao     TEXT
);

CREATE TABLE ssma.residuo_evento (
    id                 BIGSERIAL PRIMARY KEY,
    residuo_tipo_id    SMALLINT NOT NULL REFERENCES ssma.residuo_tipo(id),
    lote_id            UUID REFERENCES operacao.lote(id),
    periodo_ini        DATE,
    periodo_fim        DATE,
    volume_l           NUMERIC(14,3),
    massa_kg           NUMERIC(14,3),
    destinacao_real    TEXT,
    observacoes        TEXT,
    fonte_documento_id UUID REFERENCES documental.documento(id),
    status_dado        status_dado_t NOT NULL DEFAULT 'observado'
);

CREATE TABLE ssma.criterio (
    id            SMALLSERIAL PRIMARY KEY,
    slug          TEXT UNIQUE NOT NULL,           -- 'turbidez-filtrado','surfactante-final','condutividade-reuso','cloro-livre','db-dqo'
    nome          TEXT NOT NULL,
    unidade       TEXT,                             -- 'NTU','ppm','uS','mg/L'
    limite_min    NUMERIC,
    limite_max    NUMERIC,
    referencia    TEXT
);

CREATE TABLE ssma.criterio_observado (
    id                 BIGSERIAL PRIMARY KEY,
    criterio_id        SMALLINT NOT NULL REFERENCES ssma.criterio(id),
    lote_id            UUID REFERENCES operacao.lote(id),
    valor              NUMERIC,
    data_observacao    DATE,
    aprovado           BOOLEAN,
    fonte_documento_id UUID REFERENCES documental.documento(id),
    status_dado        status_dado_t NOT NULL DEFAULT 'observado'
);

CREATE TABLE ssma.consumivel (
    id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    slug          TEXT UNIQUE NOT NULL,           -- 'carvao-GAC400','hipoclorito-11','resina-mista','membrana-045','membrana-022','filtro-prensa-lona'
    nome          TEXT NOT NULL,
    funcao        TEXT                              -- 'remocao-surfactante','desinfeccao','deionizacao','filtracao-fina'
);

CREATE TABLE ssma.consumivel_consumo (
    id                 BIGSERIAL PRIMARY KEY,
    consumivel_id      UUID NOT NULL REFERENCES ssma.consumivel(id),
    periodo_ini        DATE,
    periodo_fim        DATE,
    quantidade         NUMERIC,
    unidade            TEXT,                         -- 'kg','L','un','m2'
    volume_tratado_l   NUMERIC,
    troca_a_cada_l     NUMERIC,                       -- 'troca preventiva a cada 1000 L'
    observacoes        TEXT,
    fonte_documento_id UUID REFERENCES documental.documento(id),
    status_dado        status_dado_t NOT NULL DEFAULT 'observado'
);

-- =============================================================
-- suprimentos.*  -- fornecedores, materiais, insumos, utilidades, HH, cotacoes
-- =============================================================
CREATE TABLE suprimentos.fornecedor (
    id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    slug          TEXT UNIQUE NOT NULL,           -- 'nanoxplore','first-graphene','blackswan','versarien','levidian','thomas-swan','universal-matter','hexographene','nanum','nacional-de-grafite','carbon-rivers','mstnland','idemitsu','indorama','allnex','sabesp','enel'
    nome_canonico TEXT NOT NULL,
    pais          TEXT,
    tipo          TEXT,                             -- 'player','trader','marketplace','utilidade','integrador','servico'
    site          TEXT,
    confidencialidade confidencialidade_t NOT NULL DEFAULT 'interno',
    observacoes   TEXT
);

CREATE TABLE suprimentos.fornecedor_alias (
    fornecedor_id UUID NOT NULL REFERENCES suprimentos.fornecedor(id) ON DELETE CASCADE,
    alias         TEXT NOT NULL,                   -- 'Frist Graphene','CamGraph','Cambridge Nanosystems','AGM','Applied Graphene Materials','Genable','CR Nano','NG','MSTN'
    PRIMARY KEY (fornecedor_id, alias)
);

CREATE TABLE suprimentos.material_familia (
    id            SMALLSERIAL PRIMARY KEY,
    slug          TEXT UNIQUE NOT NULL,           -- 'flg','gnp','go','rgo','grafite-micronizado','dispersao','masterbatch','aditivo-formulado'
    nome          TEXT NOT NULL
);

CREATE TABLE suprimentos.material (
    id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    slug          TEXT UNIQUE NOT NULL,           -- 'grafeno-flg','grafeno-gnp','grafeno-go','grafite-natural','triton-x100','naoh','nh4oh','byk-2013','esferas-zirconia','n2','co2'
    nome          TEXT NOT NULL,
    familia_id    SMALLINT REFERENCES suprimentos.material_familia(id),
    categoria     TEXT NOT NULL,                  -- 'grafeno-acabado','grafite-insumo','aditivo','base','solvente','gas','consumivel','reagente-laboratorial'
    especificacao_default TEXT,                     -- 'teor C >99%','poucas camadas','GNP','grade tecnico'
    forma_entrega TEXT                              -- 'po','dispersao-aquosa','dispersao-solvente','masterbatch','pellet','formulado','liquido','gas-cilindro'
);

CREATE TABLE suprimentos.produto_fornecedor (
    id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    fornecedor_id     UUID NOT NULL REFERENCES suprimentos.fornecedor(id) ON DELETE CASCADE,
    material_id       UUID NOT NULL REFERENCES suprimentos.material(id),
    grade             TEXT,                          -- 'BS3','BS8','GCT0953','FG05','FG10','PureGRAPH 5','0X','3X','HP10','HP50','CAMGRAPH G1','GRAPHINK 2','F7P1518','Genable 1000','Micrograf 99518UJ'
    especificacao     TEXT,                          -- TDS/SDS, area superficial, tamanho lateral, pureza, umidade, cinzas
    tds_sds_disponivel BOOLEAN,
    aplicacao_preferencial TEXT,                     -- 'concreto','polimeros','coatings','lubrificantes'
    observacoes       TEXT,
    UNIQUE (fornecedor_id, material_id, grade)
);

CREATE TABLE suprimentos.utilidade (
    id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    slug          TEXT UNIQUE NOT NULL,           -- 'energia-tusd-sp','energia-te-sp','energia-ob-fora-ponta','energia-ob-ponta','agua-sabesp','esgoto-sabesp','gas-n2','gas-co2'
    nome          TEXT NOT NULL,
    categoria     TEXT NOT NULL,                  -- 'energia','agua','esgoto','gas','vapor','ar-comprimido'
    unidade       TEXT NOT NULL                    -- 'kWh','m3','m3-gas','kg'
);

CREATE TABLE suprimentos.categoria_hh (
    id            SMALLSERIAL PRIMARY KEY,
    slug          TEXT UNIQUE NOT NULL,           -- 'operador','tecnico','analista','pesquisador','supervisor','coordenacao','manutencao-ssma'
    nome          TEXT NOT NULL,
    descricao     TEXT
);

CREATE TYPE tipo_fonte_cotacao_t AS ENUM
    ('publica','player_declarado','interna','confidencial','marketplace','compilacao','inferencia');

CREATE TABLE suprimentos.cotacao (
    id                 UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    codigo             TEXT UNIQUE,                   -- 'MGG3-PRECO-20250613-01_nanoxplore-0x-gnp'
    produto_fornecedor_id UUID REFERENCES suprimentos.produto_fornecedor(id),
    material_id        UUID REFERENCES suprimentos.material(id),     -- usado quando o item nao tem fornecedor identificado
    utilidade_id       UUID REFERENCES suprimentos.utilidade(id),
    categoria_hh_id    SMALLINT REFERENCES suprimentos.categoria_hh(id),
    descricao_item     TEXT,
    preco              NUMERIC(14,4) NOT NULL,
    moeda              CHAR(3) NOT NULL,              -- 'USD','BRL','EUR'
    unidade            TEXT NOT NULL,                 -- 'kg','g','L','m3','t','lote','mes','kWh','un'
    quantidade_pack    NUMERIC(14,4),
    moq                NUMERIC(14,4),
    incoterm           TEXT,                          -- 'FOB','CIF','DDP','interno'
    impostos_pct       NUMERIC(5,2),
    data_fonte         DATE,
    tipo_fonte         tipo_fonte_cotacao_t NOT NULL,
    status_confiabilidade status_confiabilidade_t NOT NULL,
    confidencialidade  confidencialidade_t NOT NULL DEFAULT 'interno',
    comparabilidade    TEXT,
    fonte_documento_id UUID REFERENCES documental.documento(id),
    url_documento      TEXT,
    observacoes        TEXT,
    CHECK (
      (produto_fornecedor_id IS NOT NULL)::int
    + (material_id IS NOT NULL)::int
    + (utilidade_id IS NOT NULL)::int
    + (categoria_hh_id IS NOT NULL)::int >= 1
    )
);
COMMENT ON TABLE suprimentos.cotacao IS
  'Registro de evidencia de preco - conformidade direta com MGG3-PAD-FORN02. Toda cotacao referencia ao menos um item (produto_fornecedor, material, utilidade ou HH).';

CREATE INDEX ON suprimentos.cotacao (data_fonte);
CREATE INDEX ON suprimentos.cotacao (status_confiabilidade);
CREATE INDEX ON suprimentos.cotacao (confidencialidade);

-- =============================================================
-- custo.*  -- cenarios TEA/OPEX, premissas, rendimentos, sensibilidades
-- =============================================================
CREATE TABLE custo.cenario (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    slug            TEXT UNIQUE NOT NULL,         -- 'p100-desenvolvimento','p100-producao','p500-konmix','p100-recomissionamento-v9'
    nome            TEXT NOT NULL,
    versao          TEXT,                            -- 'v10','v9','v8'
    escala          TEXT,                            -- 'P100','P500'
    data_referencia DATE,
    status          TEXT,                            -- 'consolidado','draft','obsoleto'
    audiencia       TEXT,                            -- 'investidor','interno','tecnico','due-diligence'
    base_anterior_id UUID REFERENCES custo.cenario(id),
    issue_chave     TEXT,                            -- 'ALT-440','ALT-450'
    fonte_documento_id UUID REFERENCES documental.documento(id)
);

CREATE TABLE custo.premissa (
    id            BIGSERIAL PRIMARY KEY,
    cenario_id    UUID NOT NULL REFERENCES custo.cenario(id) ON DELETE CASCADE,
    bloco         TEXT,                            -- 'regime','mix','equipe','cq','lotes-a-la-carte','risco-tecnico','manutencao'
    descricao     TEXT NOT NULL,
    valor_numerico NUMERIC,
    unidade       TEXT,
    status_dado   status_dado_t NOT NULL DEFAULT 'premissa',
    fonte_documento_id UUID REFERENCES documental.documento(id)
);

CREATE TYPE natureza_custo_t AS ENUM ('direto','indireto');
CREATE TYPE comportamento_custo_t AS ENUM ('fixo','variavel','semi-fixo');

CREATE TABLE custo.bloco_tipo (
    id            SMALLSERIAL PRIMARY KEY,
    slug          TEXT UNIQUE NOT NULL,           -- 'equipe-tecnica','cq-externo','consumiveis-lab','manutencao-prontidao','campanhas-desenvolvimento',
    nome          TEXT NOT NULL,                  --   'overhead-institucional','ssma-licencas','admin-ti','equipe-fixa-producao','insumos-producao',
    natureza      natureza_custo_t NOT NULL,      --   'utilidades-produtivas','manutencao-prevcorr','cq-rotineiro','consumiveis-cq','residuo-reprocesso','indiretos-empresariais'
    comportamento comportamento_custo_t NOT NULL
);

CREATE TABLE custo.bloco_valor (
    id            BIGSERIAL PRIMARY KEY,
    cenario_id    UUID NOT NULL REFERENCES custo.cenario(id) ON DELETE CASCADE,
    bloco_tipo_id SMALLINT NOT NULL REFERENCES custo.bloco_tipo(id),
    cadencia      TEXT,                             -- 'mensal','anual','base','conservador','intensivo','8-campanhas','12-campanhas','18-campanhas'
    valor_brl     NUMERIC(14,2) NOT NULL,
    percentual_total NUMERIC(6,3),
    observacoes   TEXT,
    fonte_documento_id UUID REFERENCES documental.documento(id),
    UNIQUE (cenario_id, bloco_tipo_id, cadencia)
);

CREATE TABLE custo.condicao_rendimento (
    id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    cenario_id    UUID NOT NULL REFERENCES custo.cenario(id) ON DELETE CASCADE,
    slug          TEXT NOT NULL,                    -- 'conservadora','media-historica-v9','otimista'
    base_grafite_kg NUMERIC(10,3) NOT NULL,         -- e.g. 100 kg
    gpc_kg        NUMERIC(10,3),
    npg_kg        NUMERIC(10,3),
    ng_kg         NUMERIC(10,3),
    residual_kg   NUMERIC(10,3),
    descricao     TEXT,
    UNIQUE (cenario_id, slug)
);

CREATE TABLE custo.custo_unitario_produto (
    id                BIGSERIAL PRIMARY KEY,
    condicao_id       UUID NOT NULL REFERENCES custo.condicao_rendimento(id) ON DELETE CASCADE,
    produto_id        UUID NOT NULL REFERENCES tecnologia.produto_canonico(id),
    custo_brl_kg      NUMERIC(14,2) NOT NULL,
    massa_mes_kg      NUMERIC(12,3),
    massa_ano_kg      NUMERIC(12,3),
    criterio_alocacao TEXT,                          -- 'massa-ponderada-complexidade GPC=4,NPG=2,NG=1','massa-pura','receita'
    observacoes       TEXT
);

CREATE TABLE custo.sensibilidade (
    id            BIGSERIAL PRIMARY KEY,
    cenario_id    UUID NOT NULL REFERENCES custo.cenario(id) ON DELETE CASCADE,
    posicao       SMALLINT,                          -- ranking 1..n
    variavel      TEXT NOT NULL,                    -- 'indiretos-c2-mensais','rendimento-npg','rendimento-nanografite','cadencia-d1','rendimento-gpc'
    caso_baixo    NUMERIC,
    caso_base     NUMERIC,
    caso_alto     NUMERIC,
    unidade       TEXT,
    impacto       TEXT,
    observacoes   TEXT
);

CREATE TABLE custo.capex_item (
    id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    cenario_id        UUID NOT NULL REFERENCES custo.cenario(id) ON DELETE CASCADE,
    categoria         TEXT NOT NULL,                 -- 'recomissionamento','equipamento-producao','equipamento-ssma','utilidades','laudo-art','seguranca-nr12'
    descricao         TEXT NOT NULL,
    valor_brl         NUMERIC(14,2) NOT NULL,
    base_temporal     TEXT,                          -- 'historico-2021','estimativa-2026'
    inclui_depreciacao BOOLEAN NOT NULL DEFAULT FALSE,
    fonte_documento_id UUID REFERENCES documental.documento(id),
    status_dado       status_dado_t NOT NULL DEFAULT 'estimado',
    observacoes       TEXT
);

-- =============================================================
-- aplicacao.*  -- plataformas Gerdau Graphene, cases, mercado
-- =============================================================
CREATE TABLE aplicacao.plataforma (
    id            SMALLSERIAL PRIMARY KEY,
    slug          TEXT UNIQUE NOT NULL,           -- 'coatings','polimeros','concreto','lubrificantes','cimento'
    nome          TEXT NOT NULL,
    descricao     TEXT
);

CREATE TABLE aplicacao.produto_comercial (
    id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    slug              TEXT UNIQUE NOT NULL,        -- 'g2d-nanolav-w107','nanodur-w102','nanocorr-w108','nanocorr-shield','poly-g-pe','poly-g-pp','nanocons-w104','cm018'
    nome              TEXT NOT NULL,
    plataforma_id     SMALLINT NOT NULL REFERENCES aplicacao.plataforma(id),
    fase              TEXT,                          -- 'comercial','piloto','p&d-avancado','desenvolvimento'
    fornecedor_grafeno_id UUID REFERENCES suprimentos.fornecedor(id),
    produto_fornecedor_id UUID REFERENCES suprimentos.produto_fornecedor(id),
    descricao         TEXT
);

CREATE TABLE aplicacao.parceiro (
    id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    slug          TEXT UNIQUE NOT NULL,           -- 'allnex','indorama','vw-way-to-zero','idemitsu','ambev','manchester-geic','ufmg','usp','ipt','senai','cdtn','gerdau-ouro-branco'
    nome          TEXT NOT NULL,
    tipo          TEXT,                             -- 'cliente','codesenvolvimento','academico','institucional','offtake'
    pais          TEXT,
    observacoes   TEXT
);

CREATE TABLE aplicacao.case_aplicacao (
    id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    slug              TEXT UNIQUE NOT NULL,        -- 'pindamonhangaba','ciclovia-mogi','ambev-packseven','case-cm018-bs3','case-indorama','vw-l66-2'
    nome              TEXT NOT NULL,
    produto_comercial_id UUID REFERENCES aplicacao.produto_comercial(id),
    parceiro_id       UUID REFERENCES aplicacao.parceiro(id),
    inicio            DATE,
    fim               DATE,
    status            TEXT,                          -- 'concluido','em-campo','piloto','prospeccao'
    fonte_documento_id UUID REFERENCES documental.documento(id),
    observacoes       TEXT
);

CREATE TABLE aplicacao.resultado_tecnico (
    id                BIGSERIAL PRIMARY KEY,
    produto_comercial_id UUID REFERENCES aplicacao.produto_comercial(id),
    case_aplicacao_id UUID REFERENCES aplicacao.case_aplicacao(id),
    metrica           TEXT NOT NULL,                 -- 'resistencia-compressao','modulo-young','salt-spray','elongacao','consumo-combustivel','redurcao-coating','durabilidade'
    unidade_medida    TEXT,                          -- '%','MPa','horas','kg/m2','% reducao'
    valor_referencia  NUMERIC,
    valor_resultado   NUMERIC,
    ganho_pct         NUMERIC,                       -- +28%, +75%, -33%
    condicao          TEXT,                          -- '7 dias','28 dias','0,01%','LDPE x2','FTP-75 urbano'
    laboratorio_campo TEXT,                          -- 'laboratorio','campo','piloto'
    fonte_documento_id UUID REFERENCES documental.documento(id),
    status_dado       status_dado_t NOT NULL DEFAULT 'observado',
    observacoes       TEXT
);

CREATE TABLE aplicacao.player_mercado (
    id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    slug              TEXT UNIQUE NOT NULL,        -- 'nanoxplore','blackswan','first-graphene','hexographene','versarien','levidian','thomas-swan','universal-matter','nacional-de-grafite','mstnland','carbon-rivers','gerdau-graphene','nanum'
    nome              TEXT NOT NULL,
    pais              TEXT,
    fornecedor_id     UUID REFERENCES suprimentos.fornecedor(id),
    modelo_negocio    TEXT,                          -- 'verticalizacao','licenciamento','b+c+d','marketplace','codesenvolvimento'
    fy_referencia     INTEGER,
    receita_fy_usd    NUMERIC,
    observacoes       TEXT
);

CREATE TABLE aplicacao.edital (
    id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    slug          TEXT UNIQUE NOT NULL,           -- 'edital-1337-2025-ufmg-cdtn'
    titulo        TEXT NOT NULL,
    orgao         TEXT,                             -- 'UFMG/CDTN','FAPEMIG','FINEP','CNPq'
    data_publicacao DATE,
    data_resultado DATE,
    data_recurso  DATE,
    prorrogacao   DATE,
    status        TEXT,                              -- 'aberto','prorrogado','encerrado','aguardando-resultado'
    objeto        TEXT,
    fonte_documento_id UUID REFERENCES documental.documento(id)
);

-- =============================================================
-- VIEWS sugeridas (camada de leitura para Mariano / Carmen / Julio)
-- =============================================================

-- 1. Massa e rendimento por lote
CREATE OR REPLACE VIEW operacao.v_lote_massa_rendimento AS
SELECT l.codigo AS lote, l.data_producao, l.piloto, l.concentracao_nominal_g_l,
       p.sigla AS produto, ls.massa_kg, ls.rendimento_pct
  FROM operacao.lote l
  LEFT JOIN operacao.lote_saida ls ON ls.lote_id = l.id
  LEFT JOIN tecnologia.produto_canonico p ON p.id = ls.produto_id;

-- 2. OPEX por cenario e cadencia
CREATE OR REPLACE VIEW custo.v_opex_cenario AS
SELECT c.slug AS cenario, c.versao, bv.cadencia, SUM(bv.valor_brl) AS opex_total
  FROM custo.cenario c
  JOIN custo.bloco_valor bv ON bv.cenario_id = c.id
 GROUP BY c.slug, c.versao, bv.cadencia;

-- 3. Cotacao mais recente por produto-fornecedor, somente confiabilidade >= medio
CREATE OR REPLACE VIEW suprimentos.v_cotacao_atual AS
SELECT DISTINCT ON (pf.id) pf.id AS produto_fornecedor_id,
       f.slug AS fornecedor, m.slug AS material, pf.grade,
       q.preco, q.moeda, q.unidade, q.data_fonte, q.status_confiabilidade
  FROM suprimentos.produto_fornecedor pf
  JOIN suprimentos.fornecedor f ON f.id = pf.fornecedor_id
  JOIN suprimentos.material m   ON m.id = pf.material_id
  LEFT JOIN suprimentos.cotacao q ON q.produto_fornecedor_id = pf.id
 WHERE q.status_confiabilidade IN ('forte','medio')
 ORDER BY pf.id, q.data_fonte DESC;

-- 4. Documentos sem nota / lacunas abertas
CREATE OR REPLACE VIEW documental.v_lacunas_abertas AS
SELECT d.codigo, d.titulo, dl.descricao AS lacuna, dl.prioridade
  FROM documental.documento d
  JOIN documental.documento_lacuna dl ON dl.documento_id = d.id;
```

## Como popular o modelo (carga inicial)

1. **`documental.documento`** — carregar diretamente do `INVENTÁRIO-MESTRE.md` (uma linha por codigo `MGG2-*`, `MGG3-*`, `GG-*`).
2. **`tecnologia.modulo`, `corrente`, `produto_canonico`, `produto_acabamento`, `parametro`** — carregar de `Mapa de processo e correntes MGgrafeno.md` + `Parametros criticos PL100 e acabamento.md`.
3. **`tecnologia.parametro_baseline`** — uma linha por par `(parametro, equipamento, corrente)` com a faixa/nominal e o status (`aproveitavel` → `observado`; `conflito de unidade` → `conflito`).
4. **`operacao.lote` e dependentes** — carregar `MGG2-CTRL01/CTRL04/CTRL05` por aba, com chave natural `codigo` (`20210720Pa`, `20210719Pa`, etc.).
5. **`ssma.*`** — carregar de `MGG2-RTF-VOLV_SSMA-Tratamento-Residuos`.
6. **`suprimentos.fornecedor*`** — carregar de `MGG3-FORN01`, `MGG3-FORN02`, normalizando aliases conforme a tabela de "Controle de duplicidade" da FORN02.
7. **`suprimentos.cotacao`** — uma linha por registro `MGG3-PRECO-AAAAMMDD-SEQ` em `Products/MGg3/MGg2/Fornecedores/Precos/`, conforme padrao MGG3-PAD-FORN02.
8. **`custo.*`** — carregar de `MGG3-LEV-P100-v10` (caso-base v10), preservando v3..v9 como `cenario.base_anterior_id` para historico, alem de `MGG3-CUSTO-P500`.
9. **`aplicacao.*`** — carregar das notas `Apresentacoes/`, `Concretos/`, `Polimeros/`, `Inteligencia de Mercado/` e `Case NanoXplore`.

## Decisoes editoriais não-obvias

1. **Nominal versus calculado.** `operacao.lote.concentracao_nominal_g_l` e `concentracao_calculada_g_l` ficam separados — refletindo a divergencia documentada `100 g/L` (rotulo) vs `95,502 g/L` (XLSX) do lote `20210720Pa`.
2. **Conflitos viraram dado.** `status_dado = 'conflito'` em `parametro_baseline` preserva, por exemplo, o conflito de unidade da vazao do cisalhador (`4700-5100 L/h` vs `4700 L/min`) sem forcar resolucao prematura.
3. **Cenarios de custo são imutaveis.** A v9 nao deve ser "atualizada"; v10 vira nova linha com `base_anterior_id` apontando para v9. O DDL preserva o historico inteiro.
4. **Cotacoes confidenciais.** O CHECK em `cotacao` permite que utilidades/HH apareçam sem produto_fornecedor; a confidencialidade obrigatoria suporta a regra MGG3-PAD-FORN02 de nao expor cotacao interna fora do Vault.
5. **Residual e custo, nao receita.** `condicao_rendimento.residual_kg` e dado, mas nao gera `custo_unitario_produto` no caso-base — alinhado a decisao editorial 5 do MGG3-LEV-P100-v10.
6. **Aliases preservam historia.** `fornecedor_alias`, `corrente_alias`, `produto_alias`: nao apagar `Frist Graphene`, `Grafeno A`, `Cambridge Nanosystems`, `Titon X-100`. Eles aparecem em planilhas historicas e seu apagamento quebra rastreabilidade.

## Lacunas reconhecidas nesta v1

- **Sem dimensao temporal completa.** Cenarios de custo tem `data_referencia`, mas o modelo ainda nao tem `fato_mes` granular tipo data warehouse. Pode entrar em v2 se Mariano precisar de serie temporal.
- **Sem CAPEX detalhado por equipamento.** `custo.capex_item` cobre o nivel agregado v9/v10; itens equipamento-a-equipamento dependem de RFQs ainda pendentes.
- **Sem modelo de IP/patentes.** Mencionado como gap no INVENTÁRIO; entra como tabela separada (`mercado.patente`) quando o portfolio for documentado.
- **Sem clientes finais validados** alem de cases (gap declarado no INVENTÁRIO).
- **CQ / caracterizacao laboratorial** entra como ENUM por enquanto; pode virar tabela proprio quando o protocolo CQ por lote estiver formalizado.

## Próximos passos sugeridos

1. **Cacilda** — auditar este modelo contra padroes do Vault e identificar omissoes.
2. **Mariano** — validar tabelas `custo.*` e `operacao.lote_*` antes de carregar dados.
3. **Eloi** — validar tabelas `suprimentos.*` e a normalizacao de aliases.
4. **Carmen** — validar tabelas `aplicacao.*` e plataformas/cases.
5. **Valdemiro / Julio** — validar views e completar lacunas tecnicas/comerciais que orientam decisao.
6. **Implementacao** — quando o time tiver consenso, gerar o esquema em um Postgres local, popular a partir dos MD/XLSX, e validar contra o lote `20210720Pa` como caso de teste de ponta a ponta.

---

*Proposta inicial v1 - Cacilda, 2026-05-29. Esta nota e modelo, nao implantacao: nenhum dado foi materializado. Recomenda-se ciclo de revisao com os agentes antes de transformar o DDL em migracao real.*
