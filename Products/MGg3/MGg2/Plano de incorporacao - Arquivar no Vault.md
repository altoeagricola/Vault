---
titulo: Plano de incorporacao - Arquivar no Vault
tipo: plano-operacional
produto: MGg3
origem: "/Users/okumaaltoe/Documents/MGgrafeno 3.0/Arquivar no Vault"
status: planejado-agentes-acionados
atualizado: 2026-05-07
confidencialidade: interno
---
# Plano de incorporacao - Arquivar no Vault

## Escopo verificado

Pasta local: `/Users/okumaaltoe/Documents/MGgrafeno 3.0/Arquivar no Vault`

### Editais

| Arquivo | Leitura inicial | Correspondencia no briefing | Local recomendado no Vault |
|---|---|---|---|
| `SEI-4216192-Edital-1337-pdf-D4Sign.pdf` | Edital 1337/2025 CTIT-UFMG e CDTN/CNEN para transferencia/licenciamento sem exclusividade das tecnologias de grafeno | Complementa [[Licenciamento UFMG CDTN]] e [[Compliance - licenciamento UFMG CDTN]] | `Products/MGg3/MGg2/Editais/` com registro `MGG2-EDITAL1337_Edital-transferencia-tecnologia.md` |
| `Alterao-data-Edital-MGGrafeno-pdf-D4Sign.pdf` | Alteracao de cronograma do edital, prorrogando entrega dos envelopes para 29/09/2025 e prevendo etapas de resultado/recurso | Complementa status temporal e cautelas de compliance | `Products/MGg3/MGg2/Editais/` com registro `MGG2-EDITAL1337-ALT01_Alteracao-data.md` |
| `UFMG e CDTN - Licenciamento de Pacote Tecnologico.pdf` | Informativo/apresentacao do pacote licenciavel; extração textual direta limitada, mas o arquivo e complementar ao edital | Complementa narrativa executiva do licenciamento e deve ser tratado como fonte primaria visual | `Products/MGg3/MGg2/Editais/` com registro `MGG2-LICINFO_Licenciamento-pacote-tecnologico.md` |

### Levantamento de Custos

| Arquivo | Leitura inicial | Correspondencia no briefing | Local recomendado no Vault |
|---|---|---|---|
| `P100_Custo de Producao - CLT_2021 - 9 de agosto de 2021 (CERES).xlsx` | Modelo de custo da planta piloto P100, com abas de configuracoes, dashboard, custos finais, equipe, insumos, equipamentos e energia | Complementa [[Custos de producao P100 P500]] e [[Planta piloto CDTN]] | `Products/MGg3/MGg2/Custos/` com registro `MGG2-CUSTO-P100_Modelo-custo-planta-piloto.md` |
| `P500_Custo de Producao - 1 turno - KonMix - MGg 3.0.xlsx` | Modelo de custo/projecao P500, com comparacao P500 x P100 e aba MGg3.0 | Complementa escalonamento MGg3, premissas economicas e comparacao com P100 | `Products/MGg3/MGg2/Custos/` com registro `MGG3-CUSTO-P500_Projecao-KonMix.md` |
| `Fornecedores de Grafeno_Editado.xlsx` | Base de fornecedores/insumos; contem NanoXplore 0X/3X e outras linhas de fornecedores, status e cotacoes | Complementa [[Ecossistema brasileiro de grafeno]], [[Validacao externa - players de mercado MGg3.0]] e Connections de fornecedores | `Products/MGg3/MGg2/Fornecedores/` com registro `MGG3-FORN01_Fornecedores-grafeno.md` |

## Complementaridade com o briefing

- O catalogo `MGG2-BASE01` funcionou como mapa narrativo e estrategico.
- A pasta `Arquivar no Vault` contem as fontes primarias que fecham lacunas documentais do briefing:
  - edital oficial e alteracao;
  - informativo visual do pacote tecnologico;
  - modelos economicos P100/P500;
  - base de fornecedores de grafeno.
- Portanto, estes arquivos devem ser incorporados como **evidencias primarias**, nao como anexos soltos.

## Padrao de incorporacao

1. Copiar os arquivos para subpastas tematicas dentro de `Products/MGg3/MGg2`.
2. Criar um registro documental por arquivo, usando o padrao de `Products/MGg3/_modelos/Registro de documento tecnico-comercial - modelo.md`.
3. Atualizar [[INVENTÁRIO-MESTRE]] com codigos, status, confidencialidade, nota documental, lacunas e proxima acao.
4. Atualizar notas tematicas:
   - [[Licenciamento UFMG CDTN]]
   - [[Compliance - licenciamento UFMG CDTN]]
   - [[Planta piloto CDTN]]
   - [[Custos de producao P100 P500]]
   - [[Ecossistema brasileiro de grafeno]]
5. Atualizar [[MGg2]] com a nova estrutura de subpastas.
6. Separar sempre:
   - fato documental;
   - inferencia estrategica;
   - hipotese ainda dependente de confirmacao;
   - alerta de compliance.

## Agentes necessarios

| Agente | Frente | Entrega esperada |
|---|---|---|
| Cacilda | Organizacao documental e padrao do Vault | Criar ou auditar registros documentais, estrutura de pastas, inventario e links internos |
| Tereza | Edital, PI, confidencialidade e risco de comunicacao | Concluido: registros dos editais e nota de compliance atualizados com cautelas e campos de restricao |
| Mariano | Custos P100/P500 | Extrair leitura economica, premissas, metricas e comparacao P100 x P500 |
| Eloi | Fornecedores e mercado | Validar fornecedores e players em fontes publicas, conectando a Connections sem duplicidade |

## Sequencia recomendada

1. Cacilda cria a estrutura fisica e registros-base dos 6 documentos.
2. Tereza aprofunda os 3 documentos de edital/licenciamento e atualiza a nota de compliance. **Concluido em 2026-05-07.**
3. Mariano extrai as planilhas P100/P500 e define metricas economicas consultaveis.
4. Eloi valida a planilha de fornecedores e sugere atualizacoes de Connections.
5. Carmen consolida as implicacoes no [[Mapa estrategico MGg3]] depois das quatro entregas.

## Cautelas

- `UFMG e CDTN - Licenciamento de Pacote Tecnologico.pdf` pode exigir leitura visual/OCR; nao marcar como completo se a extracao textual for insuficiente.
- Os PDFs do edital devem ser tratados como fontes oficiais e podem conter anexos juridicos sensiveis.
- As planilhas devem preservar premissas, unidade, aba, celula/linha de origem e data de atualizacao.
- Fornecedores nao devem gerar duplicidade em Connections; usar notas existentes e aliases quando houver variacao de grafia.
