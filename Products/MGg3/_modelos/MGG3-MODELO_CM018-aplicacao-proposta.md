---
titulo: CM018 — Proposta de registros e expansão de schema (mg-grafeno)
tipo: proposta-modelo-dados
produto: MGg3
fonte_documento: GG-CM018 (CM018-Atualização-dez2024.pdf)
schema_alvo: aplicacao
status: proposta — aguardando revisão antes de migração
confidencialidade: restrito
criado: 2026-06-08
atualizado: 2026-06-08
---

# CM018 — Proposta de registros e expansão de schema

Proposta derivada da leitura integral do PDF **CM018-Atualização-dez2024** (Gerdau Graphene P&D, dez/2024). Objetivo: levar a matriz técnica do CM018 para o banco `mg-grafeno` em vez de duplicá-la como Markdown canônico, conforme regra de fonte-de-verdade estruturada do Vault.

> **Natureza:** este documento é **proposta**. Nenhum DDL/INSERT aqui foi executado. Mutação no banco é tarefa separada e revisada (não roda a partir de nota Obsidian).

---

## 1. O que JÁ existe no banco (não recriar)

| Objeto | Registro existente | Observação |
|--------|--------------------|------------|
| `aplicacao.plataforma` | `concreto` ("Concreto / Cimenticio") | OK |
| `aplicacao.produto_comercial` | `cm018` (fase `p&d-avancado`, fornecedor `blackswan-graphene`) | OK |
| `aplicacao.produto_comercial` | `nanocons-w104` (piloto) | referência comercial correlata |
| `aplicacao.case_aplicacao` | `cm018-bs3-pasta` | caso da campanha de pasta |
| `aplicacao.player_mercado` | `nanoxplore`, `first-graphene`, `blackswan-graphene`, `hexographene` | todos com FY2025 |
| `documental.documento` | `GG-CM018` | fonte |
| `aplicacao.resultado_tecnico` | 8 linhas cm018 | **apenas melhores resultados @7d + 2 Raman + placeholder @28d** |

**Conclusão:** a estrutura de cabeçalho está pronta. Falta (a) **completar a matriz de resultados** e (b) **abrir lar para a caracterização dos grades de grafeno**.

---

## 2. Registros a ADICIONAR dentro do schema atual (`aplicacao.resultado_tecnico`)

As 8 linhas atuais cobrem só o pico por grafeno aos 7 dias. Faltam, com `fonte_documento_id = GG-CM018`, `case = cm018-bs3-pasta`, `status_dado = 'observado'`:

### 2.1 Melhores resultados @7d ausentes
| metrica | condicao | valor_ref | valor_result | ganho_pct |
|---|---|---|---|---|
| Resistencia a compressao @7d (FG10) | FG10 0,03%, pasta | 100 | 117 | 17 |
| Resistencia a compressao @7d (HP10) | HP10 0,02%, pasta | 100 | 113 | 13 |
| Resistencia a compressao @7d (FG20) | FG20 0,03%, pasta | 100 | 112 | 12 |

### 2.2 Melhores resultados @3d (idade inteira ausente)
| metrica | condicao | valor_ref | valor_result | ganho_pct |
|---|---|---|---|---|
| Resistencia a compressao @3d (BS3) | BS3 0,015%, pasta | 100 | 101 | 1 |
| Resistencia a compressao @3d (BS8) | BS8 0,03%, pasta | 100 | 100 | 0 |
| Resistencia a compressao @3d (FG05) | FG05 0,015%, pasta | 100 | 98 | −2 |
| (demais 0X/HP/FG10/FG20 @3d) | melhor teor, pasta | 100 | 75–96 | <0 |

### 2.3 Raman A_D/A_G — ganhos ausentes
Faltam `0X (+24%)`, `BS8 (+16%)`, `HP10 (+27%)` (BS3 +17% e HP50 +58% já existem). Para FG05/FG10/FG20 o ganho é nulo/negativo (defeitos nativos altos).

> **Limitação:** `resultado_tecnico` só tem `condicao` (texto livre) para guardar grafeno + teor + idade. A **matriz completa 8 grafenos × 5 teores × 2 idades = 80 pontos** fica **não-consultável por dimensão** (não dá para filtrar "tudo a 0,015%" ou "tudo @3d"). Isso motiva a expansão da §3.

---

## 3. GAP de schema e proposta de expansão

Dois problemas estruturais:

1. **Não há tabela para o grade de grafeno de entrada.** Os 8 grades (0X, BS3, BS8, FG05, FG10, FG20, HP10, HP50) e sua caracterização (D₅₀, A_D/A_G nativo, A_D/A_G funcionalizado, potencial zeta, viscosidade da dispersão, distribuição de camadas) são **propriedades do insumo**, não desempenho-vs-referência. Não cabem em `resultado_tecnico`.
2. **`resultado_tecnico` não dimensiona** grafeno/teor/idade — campos vão para `condicao` em texto livre.

### Proposta 3.1 — Nova tabela `aplicacao.grafeno_grade`
Catálogo dos grades de grafeno de entrada avaliados.

```sql
-- PROPOSTA (não executar aqui)
CREATE TABLE aplicacao.grafeno_grade (
    id            uuid DEFAULT gen_random_uuid() NOT NULL,
    slug          text NOT NULL,              -- '0x','bs3','bs8','fg05'...
    codigo        text NOT NULL,              -- '0X','BS3'...
    player_id     uuid REFERENCES aplicacao.player_mercado(id),
    fornecedor_id uuid REFERENCES suprimentos.fornecedor(id),
    d50_um        numeric,                    -- D50 granulométrico
    observacoes   text,
    -- + colunas de auditoria padrão (created_at/by, updated_at/by, seed_reasoning)
    PRIMARY KEY (id)
);
```

| slug | codigo | player | d50_um |
|---|---|---|---|
| 0x | 0X | nanoxplore | 13,0 |
| bs3 | BS3 | blackswan-graphene | 5,4 |
| bs8 | BS8 | blackswan-graphene | 6,4 |
| fg05 | FG05 | first-graphene | — |
| fg10 | FG10 | first-graphene | 10,0 |
| fg20 | FG20 | first-graphene | 18,0 |
| hp10 | HP10 | hexographene | 5,6 |
| hp50 | HP50 | hexographene | 5,2 |

### Proposta 3.2 — Nova tabela `aplicacao.grafeno_grade_caracterizacao`
Caracterização do grade num dado processo/documento (permite versionar nativo vs. pós-CM018).

```sql
-- PROPOSTA
CREATE TABLE aplicacao.grafeno_grade_caracterizacao (
    id                  bigint GENERATED ALWAYS AS IDENTITY,
    grafeno_grade_id    uuid NOT NULL REFERENCES aplicacao.grafeno_grade(id),
    contexto            text,        -- 'nativo' | 'pos-CM018'
    ad_ag               numeric,     -- razão Raman A_D/A_G
    potencial_zeta_mv   numeric,     -- dispersão 1%
    viscosidade_disp_cp numeric,     -- 250 RPM
    fonte_documento_id  uuid REFERENCES documental.documento(id),
    status_dado         public.status_dado_t DEFAULT 'observado',
    observacoes         text,
    PRIMARY KEY (id)
);
```

| grade | contexto | ad_ag | zeta_mv | visc_cp |
|---|---|---|---|---|
| 0X | nativo / pós | 0,273 / 0,339 | 33 | ~17 |
| BS3 | nativo / pós | 0,272 / 0,319 | 35 | ~18,4 |
| BS8 | nativo / pós | 0,257 / 0,298 | 42 | ~17 |
| FG05 | nativo / pós | 1,118 / 1,047 | ~38 | ~17 |
| FG10 | nativo / pós | 1,154 / 0,783 | 45 | ~17 |
| FG20 | nativo / pós | 1,057 / 1,120 | 31 | ~17 |
| HP10 | nativo / pós | 0,230 / 0,293 | 42 | ~17 |
| HP50 | nativo / pós | 0,191 / 0,301 | 27 | ~17 |

### Proposta 3.3 — Dimensionar os resultados mecânicos
Duas opções (recomenda-se **A**, menos invasiva):

**Opção A — adicionar colunas a `aplicacao.resultado_tecnico`:**
```sql
-- PROPOSTA
ALTER TABLE aplicacao.resultado_tecnico
  ADD COLUMN grafeno_grade_id uuid REFERENCES aplicacao.grafeno_grade(id),
  ADD COLUMN dosagem_pct      numeric,   -- 0.005 .. 0.030
  ADD COLUMN idade_dias       integer;   -- 3, 7, 28
```
Isso torna a matriz 8×5×2 consultável por dimensão e desocupa o campo `condicao`.

**Opção B —** tabela-filha `resultado_tecnico_ponto` (1:N) se quiser preservar `resultado_tecnico` como "resultado-síntese" e guardar os 80 pontos brutos à parte. Mais normalizado, mais custo.

---

## 4. Próximos passos sugeridos

1. **Revisar esta proposta** (Rodrigo / dono do schema mg-grafeno).
2. Se aprovada a §3: criar **migração** em `~/Base/Products/MG-Grafeno/db/migrations/` com as novas tabelas/colunas.
3. Carregar a matriz completa (depende do PDF original ter os 80 valores por teor — o documento traz os radares por teor; extração fina possível dos gráficos de 3d/7d).
4. Após carga, a nota `GG-CM018` mantém só a narrativa + query read-only `mg-grafeno-sql` (já adicionada).

---

## Links

- Fonte: [[GG-CM018_Aditivo-Escoria]]
- Modelo macro: [[MGG3-MODELO-DADOS_proposta-v1]]
- Correlato comercial: NanoCons W104 · GG03 (inteligência de aditivos)
