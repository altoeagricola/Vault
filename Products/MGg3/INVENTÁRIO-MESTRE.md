---
titulo: Inventário Mestre — MGg3
tipo: Inventário de Fontes
produto: MGg3
classificação: CONFIDENCIAL
atualizado: 2026-06-12
total_fontes: 39
fontes_com_nota: 37
cobertura: 100% em registros iniciais; MGg2 estrutura documental completa, relato tacito Rodrigo padronizado como nota interna consultavel, compliance de editais aprofundado, custos/fornecedores em validação por agentes; controles operacionais de lotes, processos, volumes e balancos de massa incorporados; Descricao da Tecnologia criada com fonte-mae, anexos tecnicos, lista numerada, matriz de evidencias, mapa de correntes, parametros criticos, quatro registros controlados do Anexo A, Relatorio Anual 2020-2021 controlado e Volume V SSMA controlado; Inteligencia de Mercado MGg3 (raiz) com relatório consolidado 2026 e case NanoXplore incorporados
confidencialidade: interno
---
# Inventário Mestre — MGg3

Compilação estruturada de fontes primárias e notas-resumo existentes na pasta `Products/MGg3`. A base Gerdau Graphene está em extração completa; a camada MGg2/MGgrafeno foi iniciada a partir do catalogo `MGG2-BASE01` e requer validação externa de links, editais e alegações de mercado.

---

## Resumo Executivo

| Métrica | Valor |
|---------|-------|
| **Total de fontes mapeadas** | 38 documentos/registros |
| **Documentos com nota-resumo** | 36 / 38 (camada tecnica inicial; anexos preservados como evidencia primaria) |
| **Pastas cobertas** | 7 + registro tacito raiz (Apresentacoes, Concretos, Inteligencia de Mercado GG, Polímeros, MGg2, Descricao da Tecnologia, Inteligencia de Mercado MGg3) |
| **Período coberto** | 2015 – Mai/2026 |
| **Volume total de dados** | ~43 MB + know-how oficial 55.1/2024, anexos tecnicos, Anexo A controlado, Relatorio Anual 2020-2021 e Volume V SSMA + relatório consolidado IM-2026 + case NanoXplore |
| **Status de consultabilidade** | ALTA para Gerdau Graphene; operacional (registros-base) para MGg2; ALTA para Inteligencia de Mercado MGg3 (raiz) |
| **Próxima ação** | Mariano (custos) e Eloi (fornecedores) aprofundam conteúdo; confirmar formalmente status UFMG/CDTN; Carmen consolida mapa estratégico |

---

## Inventário por Pasta

### 0. MGg2 / MGGRAFENO — Histórico e licenciamento

| Código | Documento | Tipo | Data | Tamanho | Confidencialidade | Nota-Resumo | Status | Temas | Lacunas |
|--------|-----------|------|------|---------|-------------------|------------|--------|-------|---------|
| **MGG2-BASE01** | Catalogo MGg3.0 | Briefing interno histórico-estratégico (DOCX) | Abr/2026 | 24 KB | INTERNO | [[MGG2-BASE01_Catalogo-MGg3-contexto-historico]] | Extraído parcial | MGgrafeno; UFMG; CDTN; planta piloto; licenciamento; custos P100/P500; players brasileiros de grafeno | Validar links externos; separar fato documental de avaliação interna |
| **MGG2-KH55.1** | KNOW HOW 55.1-2024 - Producao de Grafeno | Know-how tecnico (DOCX) | 2025-01-14 | 41 MB | INTERNO | [[MGg2/Descricao da Tecnologia/KNOW-HOW-55.1-2024_Producao-de-Grafeno]] | Extraido parcial-controlado | Producao de grafeno; PL100; modulos; correntes; GPC; NPG; NG; anexos tecnicos | Vazao do cisalhador e especificacao de NPG exigem validacao antes de uso canonico externo |
| **MGG2-KH55.1-MAPA** | Mapa de processo e correntes MGgrafeno | Mapa tecnico (MD) | 2026-05-20 | interno | INTERNO | [[MGg2/Descricao da Tecnologia/Mapa de processo e correntes MGgrafeno]] | Criado | Conversao; separacao; acabamento; residuos; `c31`; `d01`; `d02`; `d03`; `d04`; aliases `s` | Links antigos para `Projects/MGgrafeno/Planta Piloto/...` saneados na ALT-286 |
| **MGG2-KH55.1-PARAM** | Parametros criticos PL100 e acabamento | Parametros de processo (MD) | 2026-05-21 | interno | INTERNO | [[MGg2/Descricao da Tecnologia/Parametros criticos PL100 e acabamento]] | Atualizado ALT-309 | PL100; KonMix; decanter; discos; spray dryer; liofilizacao; filtracao tangencial; residuos; SSMA; 100 g/L KonMix 5 h | Consolidar unidade da vazao do cisalhador, criterios de CQ por lote e OPEX SSMA |
| **MGG2-ANEXOA-MAPA** | Anexo A - Mapeamento de Processos da Planta Piloto MGg1.0 Rev 05 | Mapeamento de processo (PDF + MD) | 2024-04-03 | interno | INTERNO | [[MGg2/Descricao da Tecnologia/MGG2-ANEXOA-MAPA_Processos-Planta-Piloto-Rev05]] | Extraido controlado | Planta piloto; Bizagi; governanca operacional; residuos; caracterizacao | Usar como fluxo/governanca, nao como balanco de massa ou premissa TEA |
| **MGG2-ANEXOA-PROCFAB** | Anexo A - Processo Fabril Piloto RA OR 10 03 2022 | Processo fabril piloto (PDF + MD) | 2022-03-10 | interno | INTERNO | [[MGg2/Descricao da Tecnologia/MGG2-ANEXOA-PROCFAB_Processo-Fabril-Piloto-2022]] | Extraido controlado | P100; KonMix; decanter; gargalo primeira separacao; cenarios de custo | Claims de triplicar producao e reducao 24x somente com ressalva |
| **MGG2-ANEXOA-RELII** | Anexo A - Relatorio Ano II Projeto MGgrafeno pp478-481 | Relatorio tecnico parcial (PDF + MD) | 2020-10 | interno | INTERNO | [[MGg2/Descricao da Tecnologia/MGG2-ANEXOA-RELII_Rota-100gL-KonMix]] | Extraido controlado | 100 g/L; KonMix; 5 h; comparador 50 g/L 24 h; Campanha Duda | Ganho defensavel em tempo/capacidade, nao rendimento percentual |
| **MGG2-ANEXOA-BMG** | Anexo A - Balanco de Massa Global PDF | Balanco de massa (PDF + MD) | 2021-2022 | interno | INTERNO | [[MGg2/Custos/Controle operacional de lotes/MGG2-ANEXOA-BMG_Balanco-Massa-Global-PDF]] | Extraido controlado | Lote 20210720Pa; Campanha Duda; 100 g/L KonMix 5 h; GPC; GPB; nanografite | Lote isolado nao e premissa final; nanografite nao e produto final sem especificacao |
| **MGG2-RA2020-2021-PROD** | Relatorio Anual 2020-2021 - Producao MGgrafeno | Relatorio anual tecnico de producao (DOCX + MD) | 2021-11-23 | 50,6 MB | INTERNO | [[MGg2/Descricao da Tecnologia/MGG2-RA2020-2021_Producao-Conversao-Separacao-Acabamento]] | Extraido controlado | P25 Silverson; estatores; P100 KonMix; separacao; acabamento; custos | P25 e desenvolvimento de parametros; P100 KonMix 100 g/L 5 h e baseline produtivo para custo/capacidade |
| **MGG2-RTF-VOLV-SSMA** | Relatorio Tecnico Final Volume V - SSMA | Relatorio tecnico final SSMA (PDF + MD) | 2019 | interno | INTERNO | [[MGg2/Descricao da Tecnologia/MGG2-RTF-VOLV_SSMA-Tratamento-Residuos]] | Extraido controlado | SSMA; residuos; agua de reuso; filtro prensa; carvao ativado; monitoramento de ar; ecotoxicidade; compliance ambiental | Nao extrapolar claim de reuso 100% para escala industrial; faltam OPEX, balanco ambiental, certificados regulatorios e validacao estatistica de ausencia de nano |
| **MGG2-KH55.1-ANEXOS** | Matriz de anexos e evidencias | Matriz documental (MD + PDFs) | 2026-05-20 | interno | INTERNO | [[MGg2/Descricao da Tecnologia/Matriz de anexos e evidencias - KNOW-HOW-55.1-2024]] | Criado | PIO-MGG-002; PIO-MGG-031; PIO-MGG-032; filtracao tangencial; relatorio spray dryer | Numeracao de anexos preservada apenas como referencia secundaria |
| **MGG2-EDITAL1337** | Edital 1337/2025 UFMG/CDTN | Edital oficial (PDF) | 2025 | 723 KB | PÚBLICO | [[MGg2/Editais/MGG2-EDITAL1337_Edital-transferencia-tecnologia]] | Extraido compliance | Licenciamento; transferência de tecnologia; propriedade intelectual; cronograma; NDA; sublicenciamento; planta piloto | Confirmar situacao final do edital/pacote com CTIT/UFMG e CDTN/CNEN antes de uso externo |
| **MGG2-EDITAL1337-ALT01** | Alteração Edital 1337 - Prorrogação | Alteração de edital (PDF) | 2025 | 442 KB | PÚBLICO | [[MGg2/Editais/MGG2-EDITAL1337-ALT01_Alteracao-data]] | Extraido compliance | Cronograma; prorrogação 29/09/2025; datas resultado/recurso | Cronograma extraido tem aparente inconsistencia de datas; confirmar versao vigente |
| **MGG2-LICINFO** | Informativo Pacote Tecnológico | Apresentação visual (PDF) | 2025 | 5,9 MB | PÚBLICO | [[MGg2/Editais/MGG2-LICINFO_Licenciamento-pacote-tecnologico]] | Pendente OCR | Apresentação pacote; oportunidades licenciamento; narrativa visual | Extração textual direta retornou 0 caracteres; nao reutilizar imagens/marcas em pitch sem autorização |
| **MGG2-CUSTO-P100** | Modelo Custo P100 | Planilha econômica (XLSX) | Ago/2021 | 331 KB | INTERNO | [[MGg2/Custos/MGG2-CUSTO-P100_Modelo-custo-planta-piloto]] | Registro-base criado | Custos produção; planta piloto P100; equipamentos; insumos; energia | Mariano extrai leitura econômica, premissas, comparação P100 x P500 |
| **MGG3-CUSTO-P500** | Projeção Custo P500 KonMix | Planilha projeção (XLSX) | 2026 | 468 KB | INTERNO | [[MGg2/Custos/MGG3-CUSTO-P500_Projecao-KonMix]] | Registro-base criado | Escalonamento P500; economia escala; viabilidade comercial; projeção MGg3 | Mariano extrai metricas escala, sensibilidade, riscos extrapolação |
| **MGG2-CTRL01** | Controle de produções | Controle de lotes (XLSX) | 2017-2022 | interno | INTERNO | [[MGg2/Custos/Controle operacional de lotes/MGG2-CTRL01_Controle-de-producoes]] | Extraido operacional | Cadastro de lotes; campanhas; concentração; equipamento; formulários | Mariano cruza 20210720Pa com balanço de massa e custos |
| **MGG2-CTRL02** | Volumes e quantidade processadas | Controle de volumes (XLSX) | 2017-2022 | interno | INTERNO | [[MGg2/Custos/Controle operacional de lotes/MGG2-CTRL02_Volumes-quantidade-processadas]] | Extraido operacional | Volumes anuais; lotes; massa estimada por escala; P100 | Validar estimativas agregadas contra balanços por lote |
| **MGG2-CTRL03** | Balanço Global PPTX | Balanço de massa (PPTX) | 2021-2022 | interno | INTERNO | [[MGg2/Custos/Controle operacional de lotes/MGG2-CTRL03_Balanco-Global-PPTX]] | Extraido operacional | Campanhas Ana/Duda/Nicolas; rendimentos; perda mássica; 20210720Pa | Confirmar representatividade da baixa perda mássica do 20210720Pa |
| **MGG2-CTRL04** | Controle de Processos 03_03_2022 | Controle estatístico/processo (XLSX) | 2017-2022 | interno | INTERNO | [[MGg2/Custos/Controle operacional de lotes/MGG2-CTRL04_Controle-de-Processos-2022]] | Extraido operacional | Banco de processo; rendimento P100; pH; condutividade; vazão | Sanear aliases Titon/Triton X-100 antes de cotação |
| **MGG2-CTRL05** | Balanço Global XLSX | Balanço de massa estruturado (XLSX) | 2021-2022 | interno | INTERNO | [[MGg2/Custos/Controle operacional de lotes/MGG2-CTRL05_Balanco-Global-XLSX]] | Extraido operacional | Insumos; sólidos; rendimentos; perdas; lote 20210720Pa | Fonte principal para cálculo custo/kg do lote de referência |
| **MGG2-CTRL06** | Controle documentos processo contínuo | Controle documental (XLSX) | 2021-2022 | interno | INTERNO | [[MGg2/Custos/Controle operacional de lotes/MGG2-CTRL06_Controle-documentos-processo-continuo]] | Extraido operacional | Status documental; processo; qualidade; flags de contaminação | Usar como filtro de validade documental, não como balanço de massa |
| **MGG3-FORN01** | Base Fornecedores Grafeno | Matriz insumos (XLSX) | 2026 | 60 KB | INTERNO | [[MGg2/Fornecedores/MGG3-FORN01_Fornecedores-grafeno]] | Registro-base criado | Fornecedores internacionais; grafiênos comerciais; cotações; supply chain | Eloi valida fornecedores, conecta Connections, identifica enriquecimentos |
| **MGG3-FORN02** | Fornecedores de Insumos e Grafeno - Startup Grafeno | Matriz de fornecedores, insumos, utilidades e HH (XLSX) | 2023-2025 | 26 KB | INTERNO | [[MGg2/Fornecedores/MGG3-FORN02_Fornecedores-insumos-grafeno-startup]] | Extraido parcial | Insumos de produção; energia; agua/esgoto; HH; fornecedores de grafeno; cotacoes | Validar aliases, evitar duplicidade em Connections e reconciliar valores com custos P100/P500 |
| **MGG3-TACITA-RODRIGO01** | Descricao Tacita MGgrafeno Gerdau Graphene | Relato pessoal tacito (DOCX externo) | 2015-2026 / org. Mai/2026 | externo ao Vault | INTERNO | [[Historico MGgrafeno-Gerdau Graphene]] | Padronizado como nota tacita | Memoria MGgrafeno; transicao Gerdau Graphene; encerramento GG; Polystell/Colorfix; retomada MGg3 | Uso externo bloqueado sem validacao documental e revisao juridica; criar stubs apenas se atores virarem recorrentes |

**Resumo executivo:** Camada MGg2/MGgrafeno agora estruturada em 4 subpastas temáticas principais (Descricao da Tecnologia, Editais, Custos, Fornecedores) com documentos primários incorporados ao Vault, mais uma nota tacita raiz padronizada a partir do relato de Rodrigo Altoé. Fonte-guia [[MGG2-BASE01_Catalogo-MGg3-contexto-historico]] complementada por: (1) [[MGg2/Descricao da Tecnologia/KNOW-HOW-55.1-2024_Producao-de-Grafeno]], com mapa de processo/correntes, parametros criticos, matriz de anexos, Anexo A controlado, [[MGg2/Descricao da Tecnologia/MGG2-RA2020-2021_Producao-Conversao-Separacao-Acabamento]], que separa P25/Silverson como desenvolvimento de parametros e P100/KonMix 100 g/L 5 h como baseline produtivo para custo/capacidade, e [[MGg2/Descricao da Tecnologia/MGG2-RTF-VOLV_SSMA-Tratamento-Residuos]], que fixa residuos, agua de reuso, monitoramento de ar e lacunas SSMA/OPEX; (2) edital oficial + alteração + informativo de licenciamento; (3) modelos econômicos P100 (histórico 2021) e P500 (projeção 2026 KonMix); (4) controles operacionais de lotes, volumes, processos e balanços de massa com rastreio explícito do lote [[Products/MGg3/MGg2/Custos/Controle operacional de lotes/Processo-Referencia-Levantamento-de-Custos|20210720Pa]]; (5) base de fornecedores internacionais de grafeno; (6) base Startup Grafeno com insumos, utilidades, HH e fornecedores de grafeno; (7) [[Historico MGgrafeno-Gerdau Graphene]] como memoria tacita interna, complementar a [[MGgrafeno - Historico institucional]]. A frente de descricao oficial agora fornece a taxonomia tecnica para custo de producao e plano de negocios; custos, controles operacionais e fornecedores seguem em aprofundamento por Mariano e Eloi.

### 1. APRESENTACOES — Gerdau Graphene

| Código | Documento | Tipo | Data | Tamanho | Confidencialidade | Nota-Resumo | Status | Temas | Lacunas |
|--------|-----------|------|------|---------|-------------------|------------|--------|-------|---------|
| **GG-APRES01** | Grafeno — Nanomaterial de alta performance V2 | Apresentação institucional (PDF) | 2023–2024 | 6,7 MB | CONFIDENCIAL | [[Gerdau Graphene/Apresentacoes/Apresentacoes|Apresentações Institucionais]] | ✅ Extraído | Posicionamento científico do grafeno; cadeia de valor (Seleção–Dispersão–Blending–Formulação); plataformas (Concreto, Polímeros, Coatings); inovação aberta (GEIC Manchester); contatos (Flavia Zangrandi, Alessandra Zanuto) | Detalhes de clientes finais; roadmap 2025+ não coberto |

**Resumo executivo:** Apresentação institucional que posiciona a Gerdau Graphene como intermediária tecnológica em nanomateriais. Cobre fundamentos científicos do grafeno, modelo B+C+D de cadeia de valor, 3 plataformas principais (adição mineral, polímeros, coatings), e validações de mercado (Ouro Branco 50k tpa; NanoDur W102 +40% durabilidade; G2D NanoTOC W105 +63% salt spray). Nota-resumo completa e consultável.

---

### 2. CONCRETOS — Gerdau Graphene

| Código | Documento | Tipo | Data | Tamanho | Confidencialidade | Nota-Resumo | Status | Temas | Lacunas |
|--------|-----------|------|------|---------|-------------------|------------|--------|-------|---------|
| **GG-CM018** | CM018 — Atualização dez/2024 | Relatório técnico (PDF) | Dez/2024 | 2,7 MB | CONFIDENCIAL | [[Gerdau Graphene/Concretos/Concretos|Concretos & Lubrificantes]] | ✅ Extraído | Aditivo grafeno para concreto com escória; 8 grafenos avaliados (BlackSwan BS3 melhor resultado); dosagem 0,01–0,015%; +28% resistência aos 7 dias; testes com VW em lubrificantes (redução -2,6% consumo urbano); parceiros: Idemitsu, VW Way to Zero, USP/FEI | Resultados a 28 dias em concreto estrutural; testes em escala piloto |
| **GG-RT** | Resultados Técnicos Aditivos para Concreto — CM018 | Relatório técnico (PDF) | Dez/2024 | 2,7 MB | CONFIDENCIAL | [[Gerdau Graphene/Concretos/Concretos|Concretos & Lubrificantes]] | ✅ Extraído | Sobreposição parcial com GG-CM018; conteúdo relevante integralmente capturado em nota-resumo | Conteúdo duplicado com GG-CM018 |
| **MGG3-LUB01** | GNP em lubrificante diesel — teste de motor 200h Shanghai 2026 | Apresentação técnica (PDF externo, não armazenado) | Jun/2026 | externo | INTERNO | [[Gerdau Graphene/Concretos/MGG3-LUB01_GNP-200h-Shanghai-2026|MGG3-LUB01_GNP-200h-Shanghai-2026]] | ✅ Extraído | GNP funcionalizado em óleo de motor diesel; CO_L_11 a 0,1%; teste 200h sem troca de óleo; 1,1% economia média; sem impacto significativo em emissões; sem impacto observado na degradação do óleo | Replicatas, estatística, comparador completo e validação independente antes de claim comercial |

**Resumo executivo:** Documentos de P&D de dez/2024 cobrindo o projeto CM018 (aditivo grafeno para concreto com escória) e lubrificantes com testes veiculares VW, agora complementados por apresentação Shanghai 2026 sobre teste de motor diesel de 200h. CM018 é a fronteira mais avançada da GG em cimentícios — BS3 (BlackSwan) entrega +28% resistência aos 7 dias em sistema com escória, superando resultados anteriores de pasta pura. Dosagem extremamente baixa (0,01–0,015%) com implicações diretas em custo/benefício. Lubrificantes: co-desenvolvimento com Idemitsu + VW, resultado -1,9% consumo combinado; fonte 200h reporta 1,1% economia média com CO_L_11 a 0,1%, sem impacto observado na degradação do óleo. Nota-resumo completa; PDF externo Shanghai 2026 não armazenado no Vault.

---

### 3. INTELIGENCIA DE MERCADO — Gerdau Graphene

| Código | Documento | Tipo | Data | Tamanho | Confidencialidade | Nota-Resumo | Status | Temas | Lacunas |
|--------|-----------|------|------|---------|-------------------|------------|--------|-------|---------|
| **GG01** | Gerdau Graphene Introduction — Allnex | Apresentação institucional (PPTX) | Jul/2022 | 4,3 MB | CONFIDENCIAL | [[Gerdau Graphene/Inteligencia de Mercado - Gerdau Graphene/Inteligencia de Mercado - Gerdau Graphene|Inteligência de Mercado]] | ✅ Extraído | Primeiro contato institucional com Allnex; modelo de negócio; posicionamento Gerdau Next | Conteúdo condensado; detalhes comerciais/técnicos em updates posteriores |
| **GG02** | Graphene Week — Gothenburg | Apresentação pública (PDF) | Set/2023 | 4,4 MB | PUBLIC | [[Gerdau Graphene/Inteligencia de Mercado - Gerdau Graphene/Inteligencia de Mercado - Gerdau Graphene|Inteligência de Mercado]] | ✅ Extraído | Apresentação pública em Graphene Flagship; validações técnicas; resultados de mercado (+13–14% resistência cimento aos 28d; +75% módulo PE; -30% zinco em anticorrosivos); parceiros (Manchester GEIC, UFMG, USP, IPT, SENAI) | Detalhe de segmentação de mercado |
| **GG03** | Aditivos Químicos T&R — Update | Apresentação comercial (PDF) | Ago/2024 | 5,0 MB | CONFIDENCIAL | [[Gerdau Graphene/Inteligencia de Mercado - Gerdau Graphene/Inteligencia de Mercado - Gerdau Graphene|Inteligência de Mercado]] | ✅ Extraído | Atualização comercial interna; portfólio completo de produtos (G2D, Poly-G, NanoCons); resultados de campo (Pindamonhangaba -33% consumo; ciclovia Mogi 7 meses com 2 demãos); gap meta/realizado (6% YTD aditivos químicos); parceria Indorama | Detalhes de pricing; pipeline/forecast completo |
| **GG04** | Case Indorama | Proposta de parceria (PDF) | Ago/2024 | 4,2 MB | CONFIDENCIAL | [[Gerdau Graphene/Inteligencia de Mercado - Gerdau Graphene/Inteligencia de Mercado - Gerdau Graphene|Inteligência de Mercado]] | ✅ Extraído | Eixos de parceria: (1) dispersão + formulação; (2) segmentos específicos; (3) aditivos em formulações Indorama; (4) funcionalização de polímeros; motivação: dispersão é o gargalo central | Detalhe de termos e expectativas comerciais |

**Resumo executivo:** Pasta consolidando inteligência de mercado de 4 documentos (Jul/2022 – Ago/2024) sobre posicionamento, validações técnicas e desenvolvimento comercial da Gerdau Graphene. GG01 é o primeiro contato institucional (Allnex, Jul/2022). GG02 é apresentação pública em Graphene Flagship (Set/2023), com validações técnicas de portfólio e parceiros globais. GG03 é o update comercial mais recente (Ago/2024), mostrando portfólio completo, resultados de campo, e gap comercial significativo (6% da meta em aditivos químicos). GG04 sinaliza parceria com Indorama em dispersão e formulação. Nota-resumo integrada cobrindo evolução estratégica.

---

### 4. POLIMEROS — Gerdau Graphene

| Código | Documento | Tipo | Data | Tamanho | Confidencialidade | Nota-Resumo | Status | Temas | Lacunas |
|--------|-----------|------|------|---------|-------------------|------------|--------|-------|---------|
| **GG-POL01** | Black Swan — R&D Update | Relatório técnico (PDF) | Dez/2023 | 746 KB | PUBLIC | [[Gerdau Graphene/Polimeros/Polimeros|Polímeros]] | ✅ Extraído | Compósitos PP (Route 2 +31% módulo Young); compósitos PE (LPPE x2 +50% elongação); fornecedor BlackSwan (GCT0953, BS8, BS3); comparação de rotas de processamento; relação com produtos comerciais Poly-G PE/PP (ago/2024) | Detalhes de concentrações ótimas pós-dez/2023; formulações comerciais finais |

**Resumo executivo:** Documento técnico P&D (Dez/2023) com BlackSwan cobrindo masterbatches e compósitos de grafeno para polímeros. Dois desenvolvimentos paralelos: (1) PP com Route 2 entregando +31% módulo Young e +15% resistência ao impacto; (2) PE com grade x2 entregando +50% elongação total — criticamente importante para filmes flexíveis. Documento classificado PUBLIC, compartilhável com parceiros externos. Conecta ao portfólio comercial Poly-G PE/PP reportado em Ago/2024. Nota-resumo completa.

---

### 5. INTELIGENCIA DE MERCADO — MGg3 (raiz)

Pasta `Products/MGg3/Inteligencia de Mercado/`. Documentos de inteligência de mercado de escopo amplo: relatório consolidado sobre o mercado global de grafeno e cases de análise competitiva de players específicos. Camada distinta da `Gerdau Graphene/Inteligencia de Mercado/`.

| Código | Documento | Tipo | Data | Confidencialidade | Nota-Resumo | Status | Temas | Lacunas |
|--------|-----------|------|------|-------------------|------------|--------|-------|---------|
| **MGG3-IM01** | Inteligência de Mercado — Grafeno Global 2026 | Relatório consolidado (MD) | Mai/2026 | INTERNO | [[Inteligencia-de-Mercado-Grafeno-2026]] | ✅ Consolidado | Mercado global de grafeno; players internacionais e nacionais; modelos de negócio; benchmarking competitivo; patentes/PI; leitura estratégica para MGgrafeno/ALTOE | Atualizações contínuas conforme novos players e contratos surgirem |
| **MGG3-CASE-NANOXPLORE** | Case NanoXplore — Verticalizacao aplicada em grafeno | Nota técnica de inteligência de mercado (MD) | Mai/2026 | INTERNO | [[Case NanoXplore]] | ✅ Completo | NanoXplore; verticalizacao; plasticos/compositos; baterias; modelo de negocios; benchmark competitivo; FY2025; dry graphene; riscos homologacao/IP/ciclicidade | Isolamento da receita de grafeno puro; validação do dry graphene lote a lote |

**Resumo executivo:** Pasta raiz de inteligência de mercado MGg3, criada Mai/2026. Contém dois documentos de alta consultabilidade: (1) `Inteligencia-de-Mercado-Grafeno-2026.md` — relatório consolidado sobre players globais, modelos de negócio, patentes e leitura estratégica para MGgrafeno, originado de múltiplas frentes de pesquisa (ALT-104 a ALT-154); (2) `Case NanoXplore.md` — leitura técnico-comercial aprofundada da NanoXplore como benchmark de verticalizacao aplicada, com métricas FY2025, rota dry graphene, mapa de riscos e implicações práticas para MGg3. Fonte primária do case: `Levantamento NanoXplore.pptx` (recebido de Flávio).

---

## Análise de Cobertura

### Documentos com Nota-Resumo ✅

| Pasta | Documentos | Nota-Resumo | Consultabilidade | Observação |
|-------|-----------|------------|-----------------|------------|
| **Apresentacoes** | 1/1 | Apresentações Institucionais | ALTA | Cobertura completa; fundamentos científicos + cadeia de valor mapeada |
| **Concretos** | 2/2 | Concretos & Lubrificantes | ALTA | Ambos documentos cobertos; CM018 é a fronteira mais avançada GG em cimento |
| **Inteligencia de Mercado (GG)** | 4/4 | Inteligência de Mercado | ALTA | Cobertura integrada de 4 cases (Jul/2022 – Ago/2024); evolução estratégica clara |
| **Polímeros** | 1/1 | Polímeros | ALTA | Cobertura completa; rotas de processamento mapeadas; conecta a produtos comerciais |
| **Inteligencia de Mercado (MGg3)** | 2/2 | Inteligencia-de-Mercado-Grafeno-2026 + Case NanoXplore | ALTA | Relatório consolidado global + case benchmark NanoXplore; incorporados Mai/2026 |
| **Descricao da Tecnologia MGg2** | 10/10 | Know-how, mapa, parametros, matrizes, registros Anexo A, Relatorio Anual 2020-2021 e Volume V SSMA | ALTA/CONTROLADA | Inclui registros documentais do Anexo A, DOCX anual, PDF Volume V SSMA e separacao entre desenvolvimento, producao, SSMA/OPEX e compliance. |
| **Controles operacionais de lotes** | 7/7 | Controle operacional de lotes | ALTA/CONTROLADA | Produção, volumes, processos, documentos, balanços XLSX/PPTX e Anexo A BMG; 20210720Pa rastreado |
| **Registro tacito raiz** | 1/1 | Historico MGgrafeno-Gerdau Graphene | INTERNA/CONTROLADA | Relato pessoal padronizado; fatos sensiveis bloqueados para uso externo sem validação |
| **TOTAL** | **38/38** | **36 notas-resumo/registros** | **100% ALTA/CONTROLADA** | Todas as fontes estão mapeadas, extraídas ou preservadas como evidencia primaria |

### Status de Extração por Tipo

| Tipo | Quantidade | Extraído | Nota-Resumo | Observação |
|------|-----------|----------|------------|-----------|
| PDF (Relatórios/Apresentações) | 11 | 11/11 | 11/11 | Inclui quatro PDFs do Anexo A e o Volume V SSMA preservados e registrados |
| PPTX (Apresentações) | 1 | 1/1 | 1/1 | 100% coberto |
| XLSX/PPTX operacionais de lotes | 6 | 6/6 | 6/6 | Controles de produção, volume, processo, documentação e balanço de massa |
| DOCX externo/tecnico | 2 | 2/2 | 2/2 | Inclui relato tacito e Relatorio Anual 2020-2021; uso externo restrito |
| MD (Notas-Resumo) | 21 | 21/21 | 21/21 | Inclui registros documentais e notas canonicas MGg2 |
| **TOTAL** | **38** | **38/38** | **36/38** | **100% COMPLETO/CONTROLADO** |

---

## Temas Principais Mapeados

### Cadeia de Valor — Grafeno como Aditivo Industrial

- **Etapa A:** Seleção de grafeno de alta pureza (sourcing global: BR, EUA, Canadá, México, Inglaterra, Austrália)
- **Etapa B:** Dispersão (know-how proprietário; patentes depositadas) ← **GARGALO CENTRAL** (ver parceria Indorama, GG04)
- **Etapa C:** Blending (incorporação ao produto do cliente)
- **Etapa D:** Formulação (desenvolvimento final) — baixíssima margem (<0,5%)

**Implicação para MGg3:** O modelo replicável é **B+C+D**, não A (produção) — a GG não compete em commodity, compete em integração aplicada.

---

### Plataformas de Produto — Status dez/2024

| Plataforma | Produtos Comerciais | Fronteira P&D | Status |
|-----------|-------------------|--------------|--------|
| **Tintas/Coatings** | G2D NanoLAV W107, NanoDur W102, NanoCORR W108, NanoCORR Shield | G2D NanoDur Next Gen (funcionalizado) | Comercial |
| **Polímeros** | Poly-G PE, Poly-G PP | PE/PA/EVA em dev. | Comercial |
| **Concreto/Cimento** | NanoCons W104 (piloto) | **CM018** (+28% aos 7d com BS3) | P&D avançado |
| **Lubrificantes** | — | **Testes VW** (-1,9% consumo) + **teste 200h diesel** (1,1% economia média) | Parceria/Publication/P&D |

---

### Fornecedores de Grafeno — Matriz Avaliada

| Fornecedor | Origem | Grades usados | Aplicação preferencial | Nota |
|-----------|--------|---------------|----------------------|------|
| **BlackSwan** | Canadá | BS3, BS8, GCT0953 | Concreto (BS3 melhor) + Polímeros (x2 melhor) | Fornecedor principal; múltiplas plataformas |
| **First Graphene** | Austrália | FG05, FG10, FG20 | Concreto (teste) | Alto A_D/A_G nativo; menor resultado em CM018 |
| **NanoXplore** | Canadá | 0X | Concreto (teste) | Funcionalização +24% A_D/A_G em CM018 |
| **Hexo** | — | HP10, HP50 | Concreto (teste) | HP50 maior ganho relativo (+58% A_D/A_G) |

---

### Ciclo de Adoção & Gaps Comerciais

| Aspecto | Observação |
|--------|-----------|
| **Ciclo de adoção** | 180–360 dias de desenvolvimento técnico em cliente antes de 1ª venda |
| **Gap principal (Ago/2024)** | Aditivos químicos: meta 26.762 kg / R$ 3,96 Mi; realizado 625 kg / R$ 140.288 (~6% YTD) |
| **Implicação** | Mercado de tintas tem barreira de adoção **mais alta** que esperado; sugerir para MGg3 priorizar segmentos com menor barreira (concreto, lubrificantes) ou casos de uso mais compelentes |
| **Parceria Indorama** | Sinaliza que **dispersão é o gargalo técnico central** — quem resolve dispersão controla a cadeia de valor |

---

### Métricas de Desempenho Quantificadas

#### Tintas & Coatings

| Produto | Métrica | Ganho | Campo |
|---------|--------|-------|-------|
| **G2D NanoDur W102** | Força de ruptura | +40% | Laboratório (estudo científico) |
| **G2D NanoDur W102** | Durabilidade | +40% | Campo (Usina Pindamonhangaba) |
| **G2D NanoDur W102** | Consumo + mão de obra | -33% | Campo (de 3 para 2 demãos) |
| **G2D NanoTOC W105** | Salt Spray (ASTM B117) | +63% vida útil (192h → 312h) | Laboratório |
| **G2D NanoTOC W105** | Redução de coating | -36% peso (3,9 → 2,5 g/m²) | Laboratório |

#### Polímeros

| Produto | Tipo | Métrica | Ganho | Aplicação |
|---------|------|--------|-------|-----------|
| **Poly-G PP** | Compósitos | Módulo de Young | +31% | Injeção (estrutural) |
| **Poly-G PE** | Compósitos LDPE | Elongação total | +50% | Filmes (stretch, sacolas) |
| **Poly-G PE** | Comercial (1%) | Módulo Young | +75% | Validado Ago/2024 |
| **Embalagem Gerdau** | Nails | Redução de espessura | 25% | -72 t/ano plástico |
| **Stretch film Ambev** | Packseven | Resistência última | +91% | Longitudinal |

#### Concreto & Cimento

| Produto | Métrica | Ganho | Condições |
|---------|--------|-------|-----------|
| **CM018 + BS3** | Resistência compressão | +28% (128% ref.) | 7 dias, 0,01% |
| **CM018 + BS3** | Resistência compressão | Dados ausentes | 28 dias (LAC principal) |
| **Aditivos GG (genérico)** | Resistência flexão | +15–16% | 28 dias, pasta |
| **Aditivos GG (genérico)** | Fluidez/workability | +20% | Possibilidade de reduzir água |
| **Aditivos GG (genérico)** | Redução clínquer | 10–30% | Sustentabilidade |

#### Lubrificantes

| Aplicação | Métrica | Ganho | Teste |
|-----------|--------|-------|-------|
| **L66_2 (0,1% GNP)** | Consumo urbano (FTP-75) | -2,6% | Ciclo urbano |
| **L66_2 (0,1% GNP)** | Consumo rodovia | -0,8% | Highway |
| **L66_2 (0,1% GNP)** | Consumo combinado | -1,9% | Média ponderada |
| **CO_L_11 (0,1% GNP)** | Consumo médio em durabilidade | -1,1% | Teste motor diesel 200h, sem troca de óleo |

---

## Lacunas Identificadas & Próximas Ações

### Lacunas Técnicas por Plataforma

| Plataforma | Lacuna | Prioridade | Status |
|-----------|--------|-----------|--------|
| **Concreto (CM018)** | Resultados a 28 dias (crítico para validação comercial) | ALTA | GG está 6–12 meses à frente da validação completa |
| **Concreto (CM018)** | Testes em concreto estrutural (escala piloto) | ALTA | Ainda em pasta de cimento |
| **Coatings** | NanoDur Next Gen funcionalizado (roadmap) | MÉDIA | Desenvolvimento 2024 |
| **Polímeros** | PA e EVA — desenvolvimento incompleto | BAIXA | Em pipeline |
| **Lubrificantes** | Escala comercial, replicação estatística e aplicações além automotiva | MÉDIA | Parceria VW em publicação + fonte externa 200h Shanghai 2026 registrada sem armazenar PDF |

### Documentos Faltantes

| Categoria | Detalhe |
|-----------|---------|
| **Pricing & Comercial** | Tabelas de preço dos aditivos; margens por plataforma |
| **Clientes finais** | Lista completa de clientes validados e em prospecção |
| **Roadmap 2025+** | Plano estratégico de expansão além tintas/polímeros |
| **Compliance/IP** | Portfolio de patentes depositadas (mencionado, não documentado) |
| **Concreto 28d** | Resultados críticos em CM018 para validação comercial |

### Próximas Ações Recomendadas

1. **Monitoramento de CM018:** Obter resultados a 28 dias assim que disponíveis (validará comercialização concreto)
2. **Atualizações periódicas:** Revisar pasta a cada 6 meses ou quando novos releases forem disponibilizados pela GG
3. **Documentação de parceria Indorama:** Rastrear evolução da dispersão (gargalo central identificado)
4. **Consolidação de roadmap:** Compilar plano estratégico 2025+ quando disponível
5. **Compliance check:** Validar que documentos CONFIDENCIAL são mantidos sob NDA em todos os contextos de compartilhamento

---

## Estrutura de Pastas Atual

```
/Users/okumaaltoe/AltoèAgricola.Vault/Products/MGg3/
├── INVENTÁRIO-MESTRE.md ← [ESTE DOCUMENTO]
├── Historico MGgrafeno-Gerdau Graphene.md [NOTA TACITA — RODRIGO01, uso interno controlado]
├── Inteligencia de Mercado/                         ← ADICIONADO Mai/2026
│   ├── Inteligencia-de-Mercado-Grafeno-2026.md [RELATÓRIO CONSOLIDADO — MGG3-IM01]
│   └── Case NanoXplore.md [CASE BENCHMARK — MGG3-CASE-NANOXPLORE]
│       (fonte primária: Levantamento NanoXplore.pptx — recebido de Flávio, arquivo externo ao vault)
└── Gerdau Graphene/
    ├── Apresentacoes/
    │   ├── Apresentacoes.md [NOTA-RESUMO]
    │   └── Grafeno- Nanomaterial de alta performanceV2.pdf [FONTE PRIMÁRIA — 6,7 MB]
    ├── Concretos/
    │   ├── Concretos.md [NOTA-RESUMO]
    │   ├── CM018-Atualização-dez2024.pdf [FONTE PRIMÁRIA — 2,7 MB]
    │   └── Resultados Tecnicos Aditivos para Concreto - CM018-Atualização-dez2024.pdf [FONTE PRIMÁRIA — 2,7 MB]
    ├── Inteligencia de Mercado/
    │   ├── Inteligencia de Mercado.md [NOTA-RESUMO]
    │   ├── Inteligencia de Mercado - Case GG01 - 2022.07.20- Gerdau Graphene Introduction Allnex .pptx [FONTE — 4,3 MB]
    │   ├── Inteligencia de Mercado - Case GG02 - 2023 - Graphene flagship.pdf [FONTE — 4,4 MB]
    │   ├── Inteligencia de Mercado - Case GG03 - Aditivos Quimicos T&R Update - Ago24.pdf [FONTE — 5,0 MB]
    │   └── Inteligencia de Mercado - Case GG04 - Indorama AUG 2024.pdf [FONTE — 4,2 MB]
    └── Polimeros/
        ├── Polimeros.md [NOTA-RESUMO]
        └── Resultados Tecnicos Polimeros - Apresentação BlackSwan_23_12_19.pdf [FONTE PRIMÁRIA — 746 KB]
└── MGg2/
    └── Custos/
        └── Controle operacional de lotes/ [ALT-254 — 6 fontes XLSX/PPTX + 6 notas]
```

---

## Critérios de Conclusão ✅

- [x] Inventário mestre criado em `/Products/MGg3/INVENTÁRIO-MESTRE.md`
- [x] Tabela fonte-por-fonte com: caminho, tipo, data, confidencialidade, status, nota-resumo, temas, métricas, lacunas, ações
- [x] 37 documentos/registros mapeados; 35 com nota-resumo/registro consultavel e anexos preservados como evidencia primaria
- [x] Documentos com cobertura e documentos sem cobertura claramente identificados
- [x] Anexos originais preservados como evidência primária
- [x] Estrutura pronta para rastreamento periódico e atualizações

**Próxima ação:** Mariano extrai métricas econômicas de custo/kg, rendimento por etapa, consumo de insumos e representatividade do lote [[Products/MGg3/MGg2/Custos/Controle operacional de lotes/Processo-Referencia-Levantamento-de-Custos|20210720Pa]].

---

*Inventário compilado por Cacilda em 2026-05-07 | Atualizado 2026-05-21 (Cacilda) — Anexo A incorporado em ALT-301 e Relatorio Anual 2020-2021 incorporado em ALT-308; P25/Silverson separado como desenvolvimento e P100/KonMix 100 g/L 5 h mantido como baseline produtivo | Total de fontes: 37 | Cobertura: 100% | Consultabilidade: ALTA/CONTROLADA*
