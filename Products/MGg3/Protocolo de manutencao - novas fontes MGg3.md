---
titulo: Protocolo de manutencao - novas fontes MGg3
tipo: protocolo-operacional
produto: MGg3
status: aprovado
atualizado: 2026-05-20
responsaveis:
  - Carmen
  - Cacilda
estados_controle:
  - novo
  - extraido_parcial
  - consultavel
  - precisa_confirmar
  - obsoleto
  - confidencial_restrito
confidencialidade: interno
---
# Protocolo de manutencao - novas fontes MGg3

Objetivo: toda nova fonte adicionada a `Products/MGg3` deve virar registro operacional antes de ser usada como base de consulta, argumento comercial ou leitura estrategica. O anexo continua sendo evidencia primaria; a nota documental passa a ser a interface normal de trabalho.

## Roteamento MGg3 x Projects/MGgrafeno

Antes de arquivar qualquer documento novo de MGgrafeno, decidir se ele e **conhecimento tecnico-historico do produto** ou **execucao viva do projeto**.

### Vai para `Products/MGg3/MGg2/`

Use `Products/MGg3/MGg2/` quando a fonte documentar conhecimento tecnico, historico, institucional ou economico herdado da fase MGgrafeno/MGg2:

- editais, anexos, alteracoes e informacoes de licenciamento UFMG/CDTN que sejam fonte primaria historica;
- modelos de custo P100/P500, planilhas de CAPEX/OPEX, saneamentos de custo e premissas tecnicas;
- historico institucional da tecnologia, planta CDTN, validacoes externas, fornecedores e players de mercado;
- documentos que servem como evidencia, comparativo, baseline tecnico ou memoria de origem da tecnologia.

Regra pratica: se o documento responde "de onde veio a tecnologia, quais evidencias existem, quais custos e premissas herdadas temos?", ele pertence a `Products/MGg3/MGg2/`.

### Vai para `Projects/MGgrafeno/<subpasta>/`

Use `Projects/MGgrafeno/` quando a fonte orientar execucao atual da startup MGgrafeno:

- `Licenciamento/`: tratativas, checklist, pendencias, comunicacoes, cronogramas e decisoes atuais sobre licenciamento UFMG/CDTN;
- `Planta Piloto/`: plano de recomissionamento, operacao, infraestrutura, seguranca, fornecedores de equipamento, capacidade e verificacoes fisicas atuais;
- `Parceiros/`: relacionamento, alinhamentos, responsabilidades e proximos passos com UFMG, CDTN/CNEN, Flavio Plentz, Adelina Pinheiro e outros atores do projeto;
- `Plano de Negocios/`: tese executiva, proposta a investidores, modelo financeiro, estrategia comercial, go-to-market e materiais de captacao;
- `Investidores/`: perfis, relatorios, reunioes, perguntas, objeções e aderencia de investidores.

Regra pratica: se o documento responde "o que vamos fazer agora, com quem, em que prazo e para qual decisao executiva?", ele pertence a `Projects/MGgrafeno/`.

### Duplicidade controlada

Nao duplicar anexo primario entre `Products` e `Projects`. Quando um documento tecnico-historico sustentar uma frente executiva, manter o anexo e o registro consultavel em `Products/MGg3/MGg2/` e criar no projeto apenas uma nota operacional com link para a fonte. Quando um documento de projeto gerar aprendizado tecnico reutilizavel, registrar a decisao em `Projects/MGgrafeno/` e criar ou atualizar a sintese correspondente em `Products/MGg3`.

## Checklist: entrada de nova fonte MGg3

1. **Classificar a fonte**
   - Identificar organizacao ou origem: `Gerdau Graphene`, `MGg2`, parceiro, cliente, paper, fornecedor ou fonte publica.
   - Identificar tema principal: apresentacoes, concretos, inteligencia de mercado, polimeros, coatings, lubrificantes, fornecedores, comercial, regulatorio ou outro.
   - Definir confidencialidade inicial: `publico`, `interno`, `confidencial`, `restrito` ou `desconhecido`.

2. **Mover ou registrar a fonte**
   - Colocar o anexo na pasta da organizacao e do tema correspondente.
   - Se a classificacao ainda estiver incerta, manter o arquivo na pasta de origem e registrar no inventario como `novo` com observacao de classificacao pendente.
   - Nunca apagar nem substituir o arquivo original sem registrar a mudanca no inventario.

3. **Criar nota documental**
   - Criar uma nota Markdown para cada PDF, PPTX, DOCX, planilha ou fonte primaria relevante.
   - Usar o modelo `Products/MGg3/_modelos/Registro de documento tecnico-comercial - modelo.md`.
   - Preencher no minimo: `fonte_arquivo`, `organizacao`, `tipo_documento`, `confidencialidade`, `status_extracao`, `confianca_extracao`, `temas`, `links_relacionados` e `atualizado`.

4. **Atualizar o inventario mestre**
   - Registrar codigo, nome do arquivo, caminho, tipo, data, confidencialidade, status, nota documental, temas, metricas relevantes, lacunas e proxima acao.
   - Se a fonte ainda nao tiver nota documental consultavel, ela deve aparecer explicitamente como pendente.
   - Ajustar totais de cobertura no frontmatter e no resumo executivo do inventario.

5. **Atualizar indice tematico**
   - Inserir a fonte na sintese do tema correspondente.
   - Separar fato documental de inferencia.
   - Registrar metricas com unidade, condicao, comparador e resultado quando houver dado quantitativo.

6. **Registrar implicacoes para MGg3**
   - Atualizar `Products/MGg3/Mapa estrategico MGg3.md` quando a fonte alterar prioridade, posicionamento, oportunidade, risco, fornecedor, segmento de entrada ou necessidade de validacao.
   - Se a fonte nao alterar leitura estrategica, registrar no proprio documento: "sem implicacao estrategica nova nesta versao".

## Estados de controle

| Estado | Definicao | Uso esperado |
|--------|-----------|--------------|
| `novo` | Fonte recebida ou detectada, ainda sem leitura documental suficiente. | Entrada inicial no inventario; exige triagem. |
| `extraido_parcial` | Parte do conteudo foi convertida em nota, mas ainda faltam metricas, riscos, links ou verificacao. | Pode apoiar leitura preliminar, mas nao deve sustentar decisao final. |
| `consultavel` | Nota documental permite responder perguntas recorrentes sem abrir o anexo. | Estado alvo para fonte operacionalmente madura. |
| `precisa_confirmar` | Ha dado ambiguo, contraditorio, sem fonte clara ou dependente de verificacao externa. | Exige checagem antes de uso comercial ou estrategico. |
| `obsoleto` | Fonte foi superada por versao posterior ou perdeu validade operacional. | Manter rastreabilidade, mas evitar como referencia principal. |
| `confidencial_restrito` | Fonte contem informacao sensivel, sob NDA, restricao comercial ou risco de exposicao. | Usar apenas internamente e com alerta visivel na nota. |

Regra pratica: uma fonte pode ter um estado de maturidade e um alerta de restricao. Exemplo: `status_extracao: consultavel` com `confidencialidade: confidencial` e alerta operacional `confidencial_restrito`.

## Regra de nomeacao

### Codigos

Usar codigos curtos, estaveis e legiveis:

- `GG-` para Gerdau Graphene.
- `MGG2-` para MGgrafeno 2.
- `MGG3-` para documentos internos da tese MGg3.
- `FORN-` para fornecedores.
- `PARC-` para parceiros.
- `PUB-` para papers, apresentacoes publicas ou fontes abertas.

Quando o documento ja tiver codigo conhecido, preservar esse codigo. Quando nao tiver, criar no formato `PREFIXO-AAAAMMDD-SEQ`, por exemplo `GG-20240507-01`.

### Notas documentais

Formato recomendado:

```text
<CODIGO>_<slug-curto-do-documento>.md
```

Exemplos:

- `GG-CM018_atualizacao-dez2024.md`
- `GG-APRES01_grafeno-nanomaterial-alta-performance.md`
- `PUB-20230901_graphene-flagship-gerdau-graphene.md`

A nota deve preservar a rastreabilidade ao arquivo original por frontmatter:

```yaml
codigo_fonte:
fonte_arquivo:
caminho_fonte:
nome_original:
data_ingestao:
```

### Anexos

Padrao conservador: preservar o nome original do anexo sempre que ele ja estiver depositado no Vault e referenciado por notas.

Para novos anexos ainda nao referenciados, pode-se normalizar para:

```text
<CODIGO> - <nome-original-ou-titulo-curto>.<extensao>
```

Mesmo quando o arquivo for renomeado, registrar o `nome_original` na nota documental e no inventario. Isso evita perda de rastreabilidade entre o arquivo recebido, a fonte primaria e a nota consultavel.

## Gatilhos de acionamento

### Acionar Cacilda

Acionar Cacilda quando existir qualquer fonte nova em `Products/MGg3` que ainda nao tenha nota documental em estado `consultavel`.

Pedido padrao:

> Criar ou completar o registro documental consultavel da nova fonte MGg3, atualizar o inventario mestre e apontar lacunas de extracao.

### Acionar Carmen

Acionar Carmen quando a fonte nova alterar qualquer uma destas dimensoes:

- estrategia de entrada do MGg3;
- posicionamento tecnico-comercial;
- oportunidade de produto, segmento, parceiro ou fornecedor;
- risco de confidencialidade, IP, validacao, adoção ou extrapolacao comercial;
- prioridade relativa entre cimenticios, polimeros, coatings, lubrificantes ou novas plataformas;
- necessidade de experimento, prova de conceito, parceria academica ou validacao de campo.

Pedido padrao:

> Avaliar implicacoes estrategicas da nova fonte para MGg3 e atualizar o mapa estrategico, separando fato documental de inferencia.

## Cadencia minima

- **Na entrada de arquivo:** aplicar checklist completo antes de usar a fonte.
- **Revisao mensal:** comparar anexos existentes contra `INVENTÁRIO-MESTRE.md` e listar fontes sem nota consultavel.
- **Revisao estrategica:** atualizar o mapa estrategico sempre que uma nova fonte mudar tese, prioridade ou risco.

## Links operacionais

- [[MGg3]]
- [[INVENTÁRIO-MESTRE]]
- [[Padrao operacional - registros consultaveis MGg3]]
- [[Registro de documento tecnico-comercial - modelo]]
- [[Mapa estrategico MGg3]]
