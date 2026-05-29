---
titulo: Padrao operacional - registros consultaveis MGg3
tipo: padrao-operacional
produto: MGg3
status: aprovado
atualizado: 2026-05-07
confidencialidade: interno
---
# Padrao operacional - registros consultaveis MGg3

Objetivo: cada PDF, PPTX ou anexo deve funcionar como evidencia primaria. A interface normal de consulta deve ser a nota em Markdown, com dados, contexto, metricas, riscos e links suficientes para responder perguntas recorrentes sem abrir o arquivo original.

## Taxonomia minima de notas

1. **Indice raiz**
   - Caminho: `Products/MGg3/MGg3.md`.
   - Funcao: listar organizacoes/fontes, padroes, modelos e mapa estrategico.

2. **Indice por organizacao/fonte**
   - Caminhos:
     - `Products/MGg3/Gerdau Graphene/Gerdau Graphene.md`;
     - `Products/MGg3/MGg2/MGg2.md`.
   - Funcao: consolidar documentos daquela fonte, status de extracao, temas cobertos, restricoes de uso e links para sinteses.

3. **Registro por documento**
   - Caminho recomendado: mesma pasta tematica do anexo, com o mesmo nome-base do arquivo.
   - Exemplo: `Products/MGg3/Gerdau Graphene/Concretos/CM018-Atualização-dez2024.md`.
   - Funcao: transformar um anexo especifico em registro consultavel, incluindo metadados, resumo estruturado, metricas, evidencias, riscos e perguntas abertas.

4. **Nota tacita / perspectiva pessoal**
   - Caminho recomendado: raiz do produto quando o relato cruza varias organizacoes, ou pasta tematica quando o relato se restringe a uma frente documental.
   - Exemplo: `Products/MGg3/Historico MGgrafeno-Gerdau Graphene.md`.
   - Funcao: preservar memoria tacita, contexto de bastidor, leitura pessoal de atores e hipoteses operacionais que nao aparecem integralmente em documentos institucionais.
   - Regra de uso: nao tratar como fonte institucional nem como evidencia externa sem validacao documental. Juizos de valor, atribuicoes de motivacao, avaliacoes culturais e alegacoes sensiveis devem ficar marcados como perspectiva do autor.

5. **Sintese por tema**
   - Caminhos atuais a manter e evoluir:
     - `Products/MGg3/Gerdau Graphene/Apresentacoes/Apresentacoes.md`;
     - `Products/MGg3/Gerdau Graphene/Concretos/Concretos.md`;
     - `Products/MGg3/Gerdau Graphene/Inteligencia de Mercado/Inteligencia de Mercado.md`;
     - `Products/MGg3/Gerdau Graphene/Polimeros/Polimeros.md`.
   - Funcao: responder perguntas por dominio, comparar documentos do tema e apontar conclusoes para MGg3.

6. **Mapa estrategico MGg3**
   - Caminho previsto: `Products/MGg3/Mapa estrategico MGg3.md`.
   - Funcao: sintetizar implicacoes para estrategia, priorizacao de aplicacoes, fornecedores, riscos de adoção, lacunas de validacao e proximos experimentos.

## Frontmatter minimo para registros de documentos

```yaml
---
titulo:
tipo: registro-documento
fonte_arquivo:
organizacao:
tipo_documento:
data_documento:
confidencialidade:
status_extracao:
confianca_extracao:
temas: []
produtos: []
aplicacoes: []
metricas_chave: []
riscos_uso: []
links_relacionados: []
atualizado:
---
```

### Valores recomendados

- `tipo_documento`: apresentacao institucional, apresentacao tecnica, proposta comercial, estudo de caso, paper, relatorio de P&D, especificacao de produto.
- `confidencialidade`: publico, interno, confidencial, restrito, desconhecido.
- `status_extracao`: pendente, parcial, completo, revisao-necessaria.
- `confianca_extracao`: alta, media, baixa.

## Politica para anexos

Decisao: **manter os anexos nas pastas atuais por enquanto**.

Racional:

- preserva links existentes em notas ja criadas;
- evita quebra de referencias no Obsidian;
- reduz risco operacional enquanto os registros por documento ainda nao existem.

Padrao futuro: quando uma pasta tiver todos os documentos com registro consultavel completo, pode-se criar `Anexos/` dentro da propria pasta tematica e migrar os arquivos em lote, atualizando `fonte_arquivo` e links. Nao usar `_fontes` neste produto agora, porque a estrutura atual ja organiza anexos por tema e a migracao imediata nao agrega consulta.

## Manutencao de novas fontes

Toda nova fonte adicionada a `Products/MGg3` deve seguir o protocolo [[Protocolo de manutencao - novas fontes MGg3]] antes de ser usada como referencia operacional. A regra central e simples: arquivo novo sem nota documental consultavel deve aparecer no inventario mestre como pendente e acionar Cacilda; arquivo novo que altere estrategia, posicionamento, oportunidade ou risco deve acionar Carmen para atualizar o mapa estrategico.

## Checklist: documento consultavel sem abrir anexo

Um registro de documento so deve ser marcado como `status_extracao: completo` quando cumprir todos os itens:

- frontmatter minimo preenchido, incluindo `fonte_arquivo`, `organizacao`, `data_documento`, `confidencialidade`, `status_extracao`, `confianca_extracao` e `atualizado`;
- resumo executivo com objetivo do documento, contexto, autoria/fonte e uso pretendido;
- lista dos produtos, aplicacoes e segmentos mencionados;
- metricas quantitativas transcritas com unidade, condicao experimental, comparador e resultado;
- principais conclusoes tecnicas separadas de inferencias estrategicas;
- riscos de uso explicitados: confidencialidade, maturidade tecnica, ausencia de validacao, dependencia de fornecedor, extrapolacao comercial;
- links para sintese tematica, organizacao/fonte e mapa estrategico;
- perguntas abertas ou proximas verificacoes quando houver lacunas;
- indicacao clara de que o anexo deve ser aberto apenas para auditoria, citação visual ou verificacao fina.

## Campos obrigatorios por escopo

### Gerdau Graphene

Obrigatorios para todos os registros:

- `fonte_arquivo`
- `organizacao`
- `tipo_documento`
- `data_documento`
- `confidencialidade`
- `status_extracao`
- `confianca_extracao`
- `temas`
- `produtos`
- `aplicacoes`
- `metricas_chave`
- `riscos_uso`
- `links_relacionados`
- `atualizado`

Motivo: a pasta contem documentos tecnicos e comerciais com diferentes niveis de confidencialidade, dados numericos e implicacoes estrategicas. A rastreabilidade precisa ser completa.

### MGg2

Obrigatorios:

- `fonte_arquivo`
- `organizacao`
- `tipo_documento`
- `status_extracao`
- `confianca_extracao`
- `temas`
- `links_relacionados`
- `atualizado`

Opcionais ate haver acervo tecnico/comercial suficiente:

- `data_documento`
- `confidencialidade`
- `produtos`
- `aplicacoes`
- `metricas_chave`
- `riscos_uso`

Regra de maturidade: assim que MGg2 tiver documento tecnico, proposta comercial, especificacao de produto ou evidencia quantitativa, os campos opcionais passam a ser obrigatorios naquele registro.

### Notas tacitas

Obrigatorios:

- `fonte_arquivo`
- `autor_relato`
- `organizacao`
- `tipo_documento`
- `natureza`
- `periodo_coberto`
- `confidencialidade`
- `status_extracao`
- `confianca_extracao`
- `temas`
- `riscos_uso`
- `links_relacionados`
- `atualizado`

Valores recomendados:

- `tipo`: `nota-tacita`
- `tipo_documento`: relato pessoal tacito, entrevista, memoria operacional, leitura de bastidor.
- `natureza`: perspectiva pessoal, memoria tacita, hipotese operacional, relato interno.
- `status_extracao`: completo, parcial, revisao-necessaria.
- `confianca_extracao`: alta quando a transcricao/organizacao do relato estiver estabilizada; media quando houver fatos sensiveis sem validacao documental; baixa quando a nota depender de memoria nao corroborada.

Regras adicionais:

- separar fatos documentaveis, inferencias e opinioes do autor;
- marcar explicitamente trechos sensiveis que nao podem sair em comunicacao externa;
- preferir links para registros documentais ja existentes quando houver suporte cruzado;
- quando a nota duplicar historico institucional, manter a nota tacita como complementar, nao como substituta da fonte documental.
