---
tipo: Índice de Documentos / Registro Documental
cliente: "[[Sergio Jose Altoe]]"
dossie: "[[Sergio Jose Altoe - Dossie Rural]]"
checklist_ref: "[[Checklist Documental - Sergio Jose Altoe]]"
produto: "Pronaf Habitacao Rural"
banco_alvo: "[[Cresol]]"
data_criacao: 2026-05-05
data_atualizacao: 2026-05-29
responsavel_organizacao: "Cacilda"
status_geral: "parcialmente-validado"
tags:
  - indice-documental
  - registro-documental
  - compilacao-mestre
  - credito-rural
  - piloto-operacional
---

# Registro Documental — Pacote de Sergio Jose Altoe

## Resumo Executivo

Este documento consolida o inventário de documentos críticos para a operação de Pronaf Habitação Rural de Sergio Jose Altoe. Cada documento crítico tem:

1. **Localização:** caminho no Vault
2. **Status:** existente / ausente / precisa_confirmar / vencido
3. **Nota operacional:** markdown com campos extraídos, riscos, próximas ações
4. **Validade/pendências:** data de vencimento, se aplicável

A estrutura segue a proposta de Carmen: **preservar PDFs originais + criar notas com frontmatter estruturado + linkar a checklist e dossie**.

---

## 1. Documentos Pessoais (Identificação e Renda)

### 1.1 Identificação Primária — RG + CPF

| Artefato | Local | Status | Nota Operacional |
|----------|-------|--------|------------------|
| **PDF original** | `Docs Pessoais/RG + CPF - SERGIO.pdf` | existente | Scan de RG + CPF combinados |
| **Registro markdown** | `Registro - CNH Sergio Jose Altoe.md` (referência cruzada) | precisa_confirmar | Conferir legibilidade e CPF sem divergência |

**Observação:** RG + CPF é documento primário de identidade. CNH é documento secundário (validação de validade crítica).

---

### 1.2 Identificação Secundária — CNH

| Artefato | Local | Status | Nota Operacional |
|----------|-------|--------|------------------|
| **PDF original** | `Docs Pessoais/CNH - SERGIO.pdf` | existente | Carteira Nacional de Habilitação |
| **Registro markdown** | `[[Registro - CNH Sergio Jose Altoe.md]]` | validado_visual | CNH válida até 04/08/2027 |

**Riscos:** CNH saneada quanto à validade; conferir dados contra RG/CPF no cadastro final.

---

### 1.3 Qualificação Pronaf — CAF

| Artefato | Local | Status | Nota Operacional |
|----------|-------|--------|------------------|
| **PDF histórico no Vault** | `Docs Pessoais/CAF. Sergio.pdf` | existente | Cadastro de Agricultores Familiares anterior |
| **PDFs novos consultados** | Downloads, sem cópia no Vault | consultado_sem_internalizar | Extrato completo e carteirinhas de CAF, por instrução do usuário |
| **Registro markdown** | `[[Registro - CAF Sergio Jose Altoe.md]]` | renovado_vigente | CAF ativo, atualizado/emissão em 28/05/2026, validade 28/05/2029 |

**Riscos:** validade saneada, mas área UFPA 30,18 ha precisa ser conciliada com CCIR/ITR/CAR/escritura.  
**Ação:** validar coerência territorial e confirmar se a Cresol exigirá anexar o PDF novo ao pacote.

---

### 1.4 Renda — Comprovante de Aposentadoria

| Artefato | Local | Status | Nota Operacional |
|----------|-------|--------|------------------|
| **PDF original** | `Docs Pessoais/COMP. DE APOSENTADORIA Maria de Lourdes e Sergio.pdf` | existente | Comprovante de renda previdenciária |
| **Nota operacional** | `[[Registro - Comprovante Aposentadoria]]` | validado_visual_parcial | Entrada para análise financeira; falta extrato INSS completo com CPF |

**Observação:** Documento bifaria (ambos os cônjuges). Base para avaliação de capacidade de pagamento.

---

### 1.5 Renda Rural — NF-e Venda de Cafe Conilon

| Artefato | Local | Status | Nota Operacional |
|----------|-------|--------|------------------|
| **PDF original** | Não anexado ao Vault por instrução do usuário | nao_anexado | Fonte externa informada pelo usuário |
| **Registro markdown** | `[[Registro - Nota Fiscal Rural 250520001 Sergio Jose Altoe]]` | conferencia_visual | NF-e nº 250520001, série 026, emitida em 25/05/2026; 112 sacas de café conilon; total R$ 100.800,00 |

**Uso operacional:** evidência complementar de renda rural para renovação do CAF no Sindicato Rural de Marilândia, com atendimento informado por [[Higor Loss Altoé]].  
**Ação:** validar chave de acesso no portal NF-e antes de uso formal.

---

### 1.6 Regularidade Fiscal Federal — CND RFB/PGFN

| Artefato | Local | Status | Nota Operacional |
|----------|-------|--------|------------------|
| **PDF original** | Não anexado ao Vault por instrução do usuário | nao_anexado | Fonte consultada em Downloads |
| **Registro markdown** | `[[Registro - Certidao Negativa RFB PGFN Sergio Jose Altoe]]` | vigente | CND RFB/PGFN emitida em 29/05/2026, válida até 25/11/2026, código 40BC.FBDD.5CC5.D80A |

**Uso operacional:** evidencia regularidade fiscal federal do CPF perante RFB/PGFN na data de emissão.  
**Ação:** validar autenticidade pelo código de controle antes de protocolo e manter o DARF ITR em trilha própria se a Cresol exigir comprovante específico.

---

### 1.7 Acessório — Documento de Patrimônio (Motocicleta)

| Artefato | Local | Status | Nota Operacional |
|----------|-------|--------|------------------|
| **PDF original** | `Docs Pessoais/DOC - MOTO.pdf` | existente | Documento de Motocicleta (bem acessório) |
| **Classific.** | Acessório (não obrigatório) | a_classificar | Usar apenas se banco solicitar patrimônio complementar |

---

## 2. Documentos de Conjuge (Maria de Lourdes Bernabe Altoe)

### 2.1 Identificação — RG + CPF de Conjuge

| Artefato | Local | Status | Nota Operacional |
|----------|-------|--------|------------------|
| **PDF original** | `Docs Pessoais/RG E CPF - MARIA DE LOURDES BERNABE ALTOE.pdf` | existente | Documentação de cônjuge |
| **Registro markdown** | A criar (mesmo padrão) | a_criar | Conferir legibilidade e CPF |

---

### 2.2 Estado Civil — Certidão de Casamento

| Artefato | Local | Status | Nota Operacional |
|----------|-------|--------|------------------|
| **PDF original** | `Docs Pessoais/CERTIDAO DE CASAMENTO Sergio e Lourdes.pdf` | existente | Comprovante de união legal |
| **Registro markdown** | `[[Registro - Certidao de Casamento Sergio e Lourdes.md]]` | validado_visual | Regime de comunhão de bens; certidão emitida em 07/04/2026 |

**Riscos:** Regime desconhecido pode exigir anuência de cônjuge não planejada. Averbação de divórcio anterior pode indicar situação não resolvida.

---

## 3. Documentos de Propriedade Rural

### 3.1 Registro Rural — CCIR 2025

| Artefato | Local | Status | Nota Operacional |
|----------|-------|--------|------------------|
| **PDF original** | `Docs Propriedade/CCIR 2025 Sergio Altoe.pdf` | existente | Documento-chave de cadastro INCRA |
| **Registro markdown** | `[[Registro - CCIR Sergio Jose Altoe.md]]` | validado_visual_parcial | Quitado; área 31,3677 ha; conferir escritura e divergência com CAR |

**Riscos:** Divergência de titularidade, área ou regularidade impede operação.

---

### 3.2 Documento de Propriedade — Escritura

| Artefato | Local | Status | Nota Operacional |
|----------|-------|--------|------------------|
| **PDF original** | `Docs Propriedade/ESCRITURA Sergio Altoe.pdf` | existente | Prova de domínio registrado |
| **Registro markdown** | `[[Registro - Escritura Sergio Jose Altoe.md]]` | precisa_confirmar | **CRÍTICO:** Conferir matrícula, titularidade, onus |

**Riscos:** Hipoteca ativa, domínio de terceiro ou divergência de matrícula impede operação.  
**Ação:** Extrair matrícula; solicitar certidão atualizada se banco exigir.

---

### 3.3 Imposto Territorial Rural — ITR 2025

| Artefato | Local | Status | Nota Operacional |
|----------|-------|--------|------------------|
| **PDF original** | `Docs Propriedade/ITR 2025 Sergio Altoe.pdf` | existente | Regularidade fiscal rural |
| **Registro markdown** | `[[Registro - ITR Sergio Jose Altoe.md]]` | validado_visual_parcial | DARF/recibo DITR extraídos; falta comprovante de pagamento |

**Riscos:** ITR não pago gera restrição Receita Federal. Divergência de área é comum.  
**Ação:** Obter recibo de quitação; conferir coerência de área com CCIR e escritura.

---

### 3.4 Ambiental — CAR + Recibo

| Artefato | Local | Status | Nota Operacional |
|----------|-------|--------|------------------|
| **PDF original** | `Docs Propriedade/RECIBO DO CAR E CAR Sergio Altoe.pdf` | existente | Cadastro Ambiental Rural |
| **Registro markdown** | `[[Registro - CAR Sergio Jose Altoe.md]]` | validado_visual_parcial | Registro/protocolo/área extraídos; falta validar SICAR/IDAF |

**Riscos:** Embargo ambiental, sobreposição a TI/UC ou status pendente impede operação.  
**Ação:** Validar status no SICAR online antes de protocolo.

---

### 3.5 Recursos Hídricos — Outorga

| Artefato | Local | Status | Nota Operacional |
|----------|-------|--------|------------------|
| **PDF original** | `Docs Propriedade/Outorga-Sergio-Jose-Altoe.pdf` | existente | Autorização para uso de água (irrigação) |
| **Nota operacional** | `[[Outorga Sergio Jose Altoe.md]]` | existente-estruturado | Nota operacional já existe com boas práticas |

**Observação:** Outorga é crítica para caso de irrigação. Validade: até 10 anos (IN AGERH nº 002/2023). Renovação: 90 dias antes do vencimento.  
**Risco:** Não foi essencial para análise de habitação rural, mas deve ser mantida em ordem para coerência ambiental.

---

## 4. Status Consolidado por Categoria

### Documentos Válidos e Estruturados

✓ **Outorga Sergio Jose Altoe** — Nota existente, boa estrutura, credenciais movidas para gerenciador seguro

### Documentos Conferidos Visualmente em 2026-05-23

✓ **CNH** — válida até 04/08/2027  
✓ **CAF** — renovado/ativo em 28/05/2026, válido até 28/05/2029; PDFs novos consultados em Downloads, sem cópia no Vault  
✓ **CCIR** — quitado no documento; área 31,3677 ha  
⚠️ **ITR** — DARF e recibo DITR presentes; falta comprovante de pagamento  
⚠️ **CAR** — recibo/cadastro extraídos; falta validação online SICAR/IDAF  
⚠️ **Escritura** — PDF existe, precisa validar matrícula, titularidade e onus  
✓ **Certidão de Casamento** — comunhão de bens; emitida em 07/04/2026  
✓ **CND RFB/PGFN** — emitida em 29/05/2026; válida até 25/11/2026; PDF consultado em Downloads, sem cópia no Vault  
⚠️ **Comprovante de Aposentadoria** — valores visuais extraídos, mas falta extrato INSS completo com CPF

### Documento Conferido Visualmente em 2026-05-27

⚠️ **NF-e venda café conilon** — registro criado sem anexar PDF; 112 sacas, R$ 100.800,00, emissão 25/05/2026; validar chave de acesso antes de uso formal

### Documentos Ausentes ou Não Localizados

✗ **Comprovante de endereço rural/residencial** — Ausente  
✗ **Projeto técnico de habitação rural** — Ausente  
✗ **Orçamento e cronograma da obra** — Ausente  
✗ **Certidão atualizada de matrícula** — Não obtida (pode ser exigida pelo banco)  
✗ **Comprovante de quitação de ITR** — Não localizado (crítico)  
✗ **Confirmação de status CAR no SICAR** — Não realizada (crítica)

---

## 5. Documentos Críticos — Próximos Passos

### Prazo Imediato (antes de protocolo)

1. **CNH:**  
   - [x] Visualizar PDF; extrair data de vencimento  
   - [x] Validar se ainda é válida — válida até 04/08/2027  
   - [ ] Conferir dados contra RG/CPF no cadastro final  

2. **CAF:**  
   - [x] Visualizar PDF; extrair número, datas, enquadramento  
   - [x] Validar se ainda é válido — novo CAF ativo, validade 28/05/2029  
   - [ ] Cruzar área UFPA 30,18 ha contra CCIR/ITR/CAR/escritura  
   - [ ] Confirmar se a Cresol exige PDF novo arquivado no pacote, já que o usuário pediu para não internalizar PDFs  

3. **CCIR:**  
   - [x] Visualizar PDF; extrair código, datas, quitação, área  
   - [x] Validar quitação no documento — consta quitado  
   - [ ] Conferir área contra ESCRITURA e divergência com CAR  

4. **ITR:**  
   - [x] Visualizar PDF; extrair DARF, datas, valor e recibo DITR  
   - [ ] **CRÍTICO:** Obter recibo de quitação (não apenas PDF bruto)  
   - [ ] Conferir coerência de área com CCIR e ESCRITURA  

5. **CAR:**  
   - [x] Visualizar PDF; extrair registro, protocolo, data e área  
   - [ ] **CRÍTICO:** Validar status no SICAR (https://www.car.gov.br/)  
   - [ ] Confirmar ausência de embargo/sobreposição a TI, UC ou áreas restritas  

6. **Escritura:**  
   - [ ] Visualizar PDF; extrair matrícula, cartório, titularidade, datas, área, onus  
   - [ ] Validar que Sergio Jose Altoe é titular  
   - [ ] Conferir ausência de hipoteca ativa ou onus que impeça operação  
   - [ ] Se banco exigir, solicitar certidão atualizada de matrícula  

7. **Certidão de Casamento:**  
   - [x] Visualizar PDF; extrair datas, regime de bens, averbações  
   - [x] **CRÍTICO:** Determinar regime — comunhão de bens  
   - [ ] Conferir nomes contra RG/CPF de ambos  

### Prazo Operacional (antes de submissão ao banco)

8. **Processamento de OCR (futuro):**  
   - Se necessário para auditoria futura, gerar OCR/transcrição de documentos críticos  
   - Armazenar em `_registros/` ou `_ocr/` (conforme estrutura futura)  

9. **Atualização de notas:**  
   - Após confirmação de cada documento, atualizar nota correspondente com campos extraídos  
   - Marcar `status_conferencia: "validado"` quando pronto  

---

## 6. Padrão de Notas Operacionais Criadas

Cada documento crítico agora tem uma **nota markdown estruturada** em `Registro - <Tipo> <Cliente>.md` com:

| Campo | Propósito |
|-------|-----------|
| **frontmatter** | Metadados estruturados (tipo, titular, datas, status, tags) |
| **Resumo Operacional** | Contexto breve e essencial |
| **Campos Extraídos** | Tabela com dados esperados e status de preenchimento |
| **Conferência e Divergências** | Riscos identificados, próximas ações |
| **Base Normativa** | Referências a Lei, Manual de Crédito Rural, normativos |
| **Armazenamento** | Localização de documentos relacionados |
| **Referências Operacionais** | Links a cliente, checklist, dossie e documentos relacionados |
| **Observações de Conferência** | Assinatura, data, status atual |

Padrão aplicado a:  
- `Registro - CNH Sergio Jose Altoe.md`  
- `Registro - CAF Sergio Jose Altoe.md`  
- `Registro - CCIR Sergio Jose Altoe.md`  
- `Registro - ITR Sergio Jose Altoe.md`  
- `Registro - CAR Sergio Jose Altoe.md`  
- `Registro - Escritura Sergio Jose Altoe.md`  
- `Registro - Certidao de Casamento Sergio e Lourdes.md`  

---

## 7. Validação contra Proposta de Carmen

✓ **Preservar PDFs originais:** Feito — nenhum PDF foi deletado ou sobrescrito.

✓ **Criar notas markdown com frontmatter:** Feito — 7 notas estruturadas criadas.

✓ **Usar frontmatter mínimo:** Feito — tipo_documento, titular, datas, orgao_emissor, status_documental, status_conferencia, fontes, tags, referências.

✓ **Separar resumo operacional, campos extraídos, conferência, divergências:** Feito — estrutura consistente nas 7 notas.

✓ **Linkar ao checklist e ao dossie:** Feito — cada nota tem campos `checklist_ref` e `dossie_ref`.

✓ **Criar nota índice do pacote:** Feito — esta nota.

✓ **Consolidar documentos válidos, vencidos, em `precisa_confirmar`, divergências e próximos passos:** Feito — ver seção 4 e 5.

⚠️ **OCR/transcrição:** Ainda não processado — recomendado para auditoria futura.

⚠️ **Segurança de credenciais:** Já tratado na nota Outorga (credenciais movidas para gerenciador seguro).

---

## 8. Recomendação de Padrão Reutilizável para Próximos Clientes Rurais

Para **próximas operações de crédito rural**, seguir esta estrutura já validada no caso Sergio:

### Fase 1: Preparação (pasta do cliente)

1. Criar pastas: `Docs Pessoais/`, `Docs Propriedade/`, `Docs Avalista/`, `Projetos/`
2. Armazenar PDFs originais sem renomeação em massa (preservar rastreamento de origem)
3. Criar `<Cliente> - Dossie Rural.md` como índice mestre

### Fase 2: Checklist Documental

4. Criar `Checklist Documental - <Cliente>.md`  
5. Mapear documentos esperados por bloco (identidade, propriedade, ambiental, etc.)  
6. Marcar status: existente / ausente / precisa_confirmar

### Fase 3: Notas Operacionais Estruturadas

7. Para cada documento crítico (CNH, CAF, CCIR, ITR, CAR, Escritura, Certidões):  
   - Criar `Registro - <Tipo> <Cliente>.md`  
   - Incluir frontmatter com tipo_documento, titular, datas, status_conferencia, tags  
   - Incluir seções: Resumo, Campos Extraídos, Conferência/Riscos, Normativa, Próximas Ações  

### Fase 4: Índice Consolidado

8. Criar `Registro Documental - Pacote <Cliente>.md`  
9. Consolidar status de todos os documentos  
10. Listar próximos passos e prazos críticos

### Fase 5: Linkagem

11. Linkar cada nota ao cliente, checklist, dossie e banco alvo  
12. Atualizar referências cruzadas conforme trabalho avança

---

## 9. Observações Finais de Organização

| Aspecto | Status | Observação |
|--------|--------|-----------|
| **Organização física** | ✓ Completa | Pastas bem estruturadas, PDFs preservados |
| **Documentação operacional** | ⚠️ Parcial | Notas críticas preenchidas por conferência visual; OCR pesquisável segue pendente |
| **Validação de dados** | ⚠️ Parcial | CNH, CCIR, ITR, CAR, certidão e aposentadoria conferidos em 2026-05-23; CAF renovado conferido em 2026-05-28 |
| **Linkagem interna** | ✓ Completa | Todas as notas linkem a cliente, checklist, dossie |
| **Padrão reutilizável** | ✓ Validado | Estrutura pronta para aplicação em próximos clientes |
| **Segurança** | ⚠️ Atenção | Credenciais já foram movidas para gerenciador seguro (Outorga); sem achados novos |

---

## 10. Próxima Entrega

Esta nota consolida o trabalho de **registro e organização estruturada de documentos**. Os dados específicos de cada documento (CNH válida até X, CAF número Y, CCIR quitado Z) devem ser preenchidos na etapa de **conferência visual**, que fica como responsabilidade operacional do caso.

Estrutura está pronta para:
- ✓ Rastreamento de documentos  
- ✓ Auditoria de completude  
- ✓ Escalação de pendências ao banco  
- ✓ Reutilização em próximos clientes  

---

**Criado por:** Cacilda  
**Data:** 2026-05-05  
**Referência:** [[ALT-71]] (problema) | [[ALT-66]] (proposta) | [[ALT-69]] (origem)
