---
titulo: Relatorio Tecnico Final Volume V - SSMA e Tratamento de Residuos
tipo: registro-documento
produto: MGg3
fase: MGg2
codigo_fonte: MGG2-RTF-VOLV-SSMA
fonte_arquivo: MGG2-RTF-VOLV_SSMA.pdf
caminho_fonte: /Users/okumaaltoe/Documents/MGgrafeno 3.0/EVT-MGg3/Ingestao 20Maio2026/VAI/Relatório Técnico Final - Volume V_SSMA.pdf
nome_original: Relatório Técnico Final - Volume V_SSMA.pdf
organizacao: MGgrafeno / UFMG / CDTN / CODEMGE
tipo_documento: relatorio tecnico final ssma
data_documento: 2019
confidencialidade: interno
status_extracao: extraido-controlado
confianca_extracao: alta
temas:
  - SSMA
  - residuos
  - tratamento de agua
  - monitoramento de ar
  - ecotoxicidade
  - compliance ambiental
metricas_chave:
  - 18000 L de residuo liquido tipo 1 tratados ate julho de 2019
  - 246 L de residuo liquido tipo 2 destinados para incineracao SEGRE
  - 40 kg de residuo solido tipo 1 destinados a aterro Classe I
  - 86 kg de residuo solido tipo 2 destinados a incineracao SEGRE
  - turbidez pos-filtro prensa menor que 5 NTU
  - surfactante final 0,18 ppm por HPLC
  - troca preventiva de carvao a cada 1000 L
riscos_uso:
  - claim de reuso 100% da agua e historico de planta piloto/CDTN, nao prova de operacao industrial atual
  - ausencia de grafeno por Raman na agua final nao elimina falso negativo
  - DBO e DQO da agua SSMA exigem ressalva para uso ambiental e ESG
  - OPEX ambiental nao esta fechado no documento
links_relacionados:
  - "[[Mapa de processo e correntes MGgrafeno]]"
  - "[[Parametros criticos PL100 e acabamento]]"
  - "[[MGG2-ANEXOA-MAPA_Processos-Planta-Piloto-Rev05]]"
  - "[[../Custos/Saneamento custos P100 P500]]"
  - "[[../../Compliance - licenciamento UFMG CDTN]]"
atualizado: 2026-05-21
---
# Relatorio Tecnico Final Volume V - SSMA e Tratamento de Residuos

## Resumo executivo

Registro documental controlado do Volume V do Relatorio Tecnico Final MGgrafeno, dedicado a SSMA. O documento e uma fonte primaria sobre gestao de riscos ocupacionais, ecotoxicidade, monitoramento de ar e tratamento de residuos da planta piloto. Para o Vault, sua funcao e fixar a camada SSMA como parte do processo tecnico e do custo operacional, nao como apendice ambiental.

O dado mais acionavel e o sistema piloto de tratamento de residuos liquidos: filtro prensa, membranas 0,45 um e 0,22 um, carvao ativado, resina mista, controle microbiologico, UV e osmose reversa. O relatorio sustenta que a planta piloto tratou mais de 18.000 L de residuo liquido ate julho de 2019, com reuso de agua no contexto da Licenca Ambiental de Operacao do CDTN. Para due diligence, o pacote ainda exige fechamento de balanco de massa ambiental, OPEX, documentacao regulatoria e validacao analitica de ausencia de nanomateriais.

## Identificacao

| Campo | Valor |
|---|---|
| Arquivo preservado | `Descricao da Tecnologia/Anexos/MGG2-RTF-VOLV_SSMA.pdf` |
| Fonte Markdown | `Sources/Papers/Relatorio Tecnico Final Volume V SSMA.md` |
| Caminho externo usado | `/Users/okumaaltoe/Documents/MGgrafeno 3.0/EVT-MGg3/Ingestao 20Maio2026/VAI/Relatório Técnico Final - Volume V_SSMA.pdf` |
| Documento | Relatorio Tecnico Final - Volume V SSMA |
| Data | 2019 |
| Status | Registro documental controlado |
| Confianca | Alta para dados reportados de piloto; media para extrapolacao TEA/OPEX; baixa para claim industrial sem validacao adicional |

## Separacao obrigatoria: observado, estimado e lacuna

| Categoria | Registro |
|---|---|
| Dado observado | O relatorio registra quatro classes de residuos, volumes/quantidades acumuladas, rotas de tratamento/destinacao e operacao de tratamento de mais de 18.000 L de residuos liquidos ate julho de 2019. |
| Dado observado | O sistema SSMA implementado inclui filtro prensa, filtros de polipropileno, carvao ativado, resina mista, UV e osmose reversa; a etapa de coagulacao/floculacao com sulfato de aluminio entra como alternativa para residuos mais dificeis. |
| Dado observado | Raman nao detectou grafeno nas membranas de agua final analisadas, mas o proprio relatorio registra a limitacao de falsos negativos por ser analise pontual. |
| Premissa tecnica | Para TEA preliminar, usar 750 g de carvao ativado por ate 1.000 L tratados como regra operacional historica, nao como especificacao industrial final. |
| Premissa tecnica | A agua tratada pode ser considerada adequada para entrada na osmose reversa, pias do processo e irrigacao de jardins dentro do recorte do sistema piloto. |
| Inferencia | SSMA deve ser modelado como modulo de processo e custo, porque recebe residuos de conversao, separacao, acabamento, caracterizacao e aplicacoes. |
| Lacuna | Falta balanco de massa do tratamento: entrada de solidos, solidos capturados, agua recuperada, perdas, lodos, carvao/resina/membranas exauridos e purgas. |
| Lacuna | Falta matriz regulatoria rastreavel com normas exatas, condicionantes CDTN/COPASA/IBAMA, MTRs, certificados de incineracao/aterro e classificacao formal dos residuos. |
| Lacuna | Falta OPEX: consumiveis, energia, manutencao, HH, analises, destinacao externa e custo de automacao. |

## Fluxos de residuos

| Fluxo | Composicao reportada | Quantidade reportada | Tratamento / destinacao | Natureza do dado |
|---|---:|---:|---|---|
| Residuo liquido tipo 1 | Solucao aquosa com surfactante/aditivo e solidos carbonaceos em suspensao: grafite, grafeno e/ou nanoplaca | ~18.000 L | Tratamento interno SSMA | Dado observado/reportado |
| Residuo liquido tipo 2 | Solventes organicos, enxofre e solucao acida com nanomaterial residual | 246 L | Incineracao via SEGRE | Dado observado/reportado |
| Residuo solido tipo 1 | Luvas, papeis e embalagens impregnados com nanomaterial fixo em matriz | 40 kg | Aterro sanitario Classe I | Dado observado/reportado |
| Residuo solido tipo 2 | Nanomateriais livres em po, restos de amostras | 86 kg | Incineracao via SEGRE | Dado observado/reportado |
| Solido retido no filtro prensa | Mistura rica em Grafeno B e nanoplaca de grafite; possivel Grafeno A e grafite residual | ~250 g por batelada de filtro prensa de bancada | Retido nas lonas; potencial de reaproveitamento | Dado observado em bancada; escala ainda lacuna |

## Sistema de tratamento de residuos liquidos

Fluxo operacional reportado:

1. Estocagem externa dos residuos liquidos em tanques 1 e 2.
2. Bombeamento para tanques 3 e 4 no mezanino do Predio 21.
3. Filtro prensa ate turbidez inferior a 5 NTU; se nao atingir, o residuo e repassado.
4. Filtros de membrana 0,45 um e 0,22 um para solidos/microrganismos remanescentes.
5. Carvao ativado para remocao de surfactante.
6. Resina mista quando necessario para ajuste de condutividade.
7. Controle microbiologico por hipoclorito, UV e recirculacao.
8. Osmose reversa para producao de agua deionizada usada na producao.

| Parametro | Valor reportado | Uso no Vault |
|---|---:|---|
| Turbidez do residuo bruto | Geralmente >40 NTU; casos dificeis >500 NTU | Dado observado; define carga de tratamento |
| Criterio pos-filtro prensa | <5 NTU | Criterio operacional SSMA |
| Coagulacao/floculacao | Sulfato de aluminio; 80 L em tanques de 100 L; espessador de 200 L testado | Etapa alternativa, nao fluxo unico |
| Al dissolvido no sobrenadante | <0,1 mg/L em 6 amostras pH 6-6,5; limite CONAMA citado 0,2 mg/L | Evidencia de controle quimico |
| Carvao ativado | GAC400; 750 g; 340 mL/min; ~500 L/dia | Premissa historica de OPEX/consumivel |
| Troca do carvao | Preventiva a cada 1.000 L tratados | Premissa historica; exige validacao em escala |
| Surfactante final | 0,18 ppm por HPLC em jan/2019; limite citado 2 ppm | Dado observado; evidencia de eficiencia |
| Condutividade alvo | <100 uS apos resina mista | Criterio interno de reuso |
| Entrada osmose | CE <250 uS/cm, cloro livre 0,5-2,0 ppm, dureza <125 ppm, TOC <1,5 ppm | Especificacao de equipamento, nao norma geral |
| Controle microbiologico | 80 mL de hipoclorito 11% por 600 L quando cloro livre <0,2 ppm; UV/recirculacao | Dado operacional |

## Qualidade da agua tratada

| Tema | Leitura controlada |
|---|---|
| Ausencia de grafeno | Raman nao detectou grafeno nas membranas finais analisadas. A ressalva obrigatoria e que Raman e pontual e nao exclui falso negativo. |
| Comparacao com COPASA/poco | Agua SSMA e comparavel em turbidez, condutividade, dureza, aluminio, tensoativos e TOC, com alguns parametros ate inferiores. |
| DBO/DQO | Agua SSMA mostrou DQO 100-110 e DBO 39,1-43, acima da agua COPASA/poco e acima dos valores de referencia da tabela. |
| Classe de uso | O relatorio enquadra a agua como Classe 2 considerando DBO/DQO/OD; nao usar para consumo humano ou irrigacao de hortalicas. |
| Uso defendavel | Entrada em osmose reversa, abastecimento de pias do processo e eventual irrigacao de jardins, desde que mantido ciclo de reuso sem longa estocagem. |

## Monitoramento de ar e seguranca ocupacional

| Categoria | Registro controlado |
|---|---|
| Risco ocupacional | Analises de risco cobriram escala bancada, escala piloto, liofilizacao, sintese grafeno-enxofre, preparo de amostras, filtro prensa e amostradores de ar. |
| Medidas implementadas | Paramentacao, pass-through, EPIs, exaustao, caixa acustica, contencao de vazamentos, canaletas e procedimentos operacionais. |
| Ar interno | Foram detectados grafite, nanoplaca e grafeno em filtros internos por tecnicas como MEV/EDS, Raman, TG/DTG e DRX. |
| Ar externo | O relatorio afirma que nenhuma amostra externa analisada detectou grafeno, nanoplaca ou grafite. |
| Ocupacional | Spray dryer e manipulacao do solido do filtro prensa reforcam necessidade de controles coletivos e uso adequado de EPI. |

## Ecotoxicidade

Ensaios com `Daphnia similis` e `Raphidocelis subcapitata` indicaram efeitos danosos de amostras de grafeno/grafeno B e dispersoes aquosas. O dado mais sensivel e que grafeno em agua causou mortalidade de 50% dos microcrustaceos na concentracao de 0,017 g/L, e que a solucao de surfactante tambem foi toxica. A leitura correta para due diligence e que surfactante e dispersao aquosa sao fatores ambientais relevantes; nao reduzir a avaliacao a "grafeno puro".

## Implicacoes para OPEX, compliance e ESG

| Frente | Implicacao |
|---|---|
| OPEX | Consumiveis relevantes: carvao ativado, membranas 0,45/0,22 um, resina mista, hipoclorito, sulfato de aluminio quando aplicavel, energia/bombeamento/UV/osmose, analises HPLC/ICP/Raman/DBO/DQO/coliformes e destinacao externa. |
| Compliance | Ponto positivo: segregacao por risco fisico do nanomaterial, tratamento interno do maior fluxo liquido, controle analitico e alinhamento com SEGRE/CDTN. |
| ESG | Claim defensavel: planta piloto implementou tratamento e reuso de agua por principio de precaucao. Claim bloqueado sem ressalva: "processo industrial sustentavel" ou "100% reuso" fora do recorte historico/CDTN. |
| TEA | O Volume V fornece premissas tecnicas de modulo SSMA, mas nao custo unitario, HH, energia, vida util de consumiveis nem balanco hidrico fechado. |

## Links relacionados

- [[Mapa de processo e correntes MGgrafeno]]
- [[Parametros criticos PL100 e acabamento]]
- [[MGG2-ANEXOA-MAPA_Processos-Planta-Piloto-Rev05]]
- [[../Custos/Saneamento custos P100 P500]]
- [[../../Compliance - licenciamento UFMG CDTN]]
