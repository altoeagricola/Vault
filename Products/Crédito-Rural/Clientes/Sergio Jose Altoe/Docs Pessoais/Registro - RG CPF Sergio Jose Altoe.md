---
tipo_documento: RG + CPF (Registro Geral + Cadastro de Pessoas Físicas)
titular: Sergio Jose Altoe
cpf: "a confirmar no PDF"
rg: "a confirmar no PDF"
orgao_emissor_rg: "SSP/ES (Secretaria de Segurança Pública - Espírito Santo)"
orgao_emissor_cpf: "Receita Federal do Brasil"
data_emissao_rg: "a confirmar no PDF"
data_vencimento_rg: "a confirmar no PDF (RG tem validade de 10 anos)"
numero_rg: "a confirmar no PDF"
data_emissao_cpf: "a confirmar no PDF"
status_documental: "existente"
status_conferencia: "precisa_confirmar"
fonte_arquivo: "Docs Pessoais/RG + CPF - SERGIO.pdf"
fonte_ocr: "não processado"
data_conferencia: 2026-05-05
conferido_por: Cacilda
confianca_extracao: "baixa - PDF sem OCR"
divergencias: "nenhuma identificada até agora"
pendencias: "confirmar legibilidade; validar CPF sem divergência cadastral; validar validade do RG; extrair números"
tags:
  - identidade-primaria
  - documento-obrigatorio
  - rg-cpf
  - precisa-confirmar
  - credito-rural
checklist_ref: "[[Checklist Documental - Sergio Jose Altoe]]"
dossie_ref: "[[Sergio Jose Altoe - Dossie Rural]]"
---

# Registro — RG + CPF de Sergio Jose Altoe

## Resumo Operacional

Registro Geral (RG) e Cadastro de Pessoas Físicas (CPF) de Sergio Jose Altoe, **documento primário de identidade e qualificação fiscal**. RG é documento de identidade estadual; CPF é identificação fiscal federal. Ambos são obrigatórios para qualquer operação creditícia.

Localizado em: `Docs Pessoais/RG + CPF - SERGIO.pdf`

---

## Campos Extraídos

| Campo | Valor | Status |
|-------|-------|--------|
| **Tipo documento** | RG + CPF | Confirmado |
| **Titular** | Sergio Jose Altoe | Presumido (confirmar no PDF) |
| **Nº RG** | *a confirmar no PDF* | **PENDENTE** |
| **Órgão emissor RG** | SSP/ES | Presumido |
| **Data emissão RG** | *a confirmar no PDF* | **PENDENTE** |
| **Data vencimento RG** | *a confirmar no PDF* | **PENDENTE** |
| **Nº CPF** | *a confirmar no PDF* | **CRÍTICO — PENDENTE** |
| **Órgão emissor CPF** | Receita Federal | Presumido |
| **Data emissão CPF** | *a confirmar no PDF* | **PENDENTE** |

---

## Conferência e Divergências

### Status Atual

- PDF localizado: ✓ `Docs Pessoais/RG + CPF - SERGIO.pdf`
- OCR processado: ✗ Não (PDF com scan sem texto pesquisável)
- CPF confirmado: ✗ Não
- Legibilidade validada: ✗ Não
- Validade de RG confirmada: ✗ Não

### Riscos de Identidade

1. **CPF divergente:** Se CPF do PDF for diferente do CPF registrado no sistema do banco ou ALTOE, impede operação até esclarecimento.
2. **RG expirado:** RG tem validade de 10 anos. Se vencido, pode ser exigida renovação.
3. **Ilegibilidade:** Scan pode estar borrado, cortado ou ilegível — impedindo confirmação de dados.
4. **Nome divergente:** Nomes em RG vs. CPF vs. outros documentos devem coincidir. Variações (apelidos, diminutivos) podem causar rejeição bancária.

### Próximas Ações Críticas

1. **Visualizar PDF original** e extrair:
   - Número completo do RG
   - Data de emissão e vencimento do RG
   - Número do CPF (essencial para rastreamento)
   - Data de emissão do CPF
   - Nome completo (validar contra CNH, Escritura, outros documentos)

2. **Validar CPF**:
   - Conferir CPF contra registros de ALTOE Agricola
   - Conferir CPF contra cadastro do banco Cresol (quando houver)
   - Calcular dígito verificador se necessário (validação de integridade)

3. **Validar RG**:
   - Confirmar se ainda é válido (10 anos de emissão)
   - Se expirado, solicitar renovação ou RG novo

4. **Conferir coerência de nome**:
   - RG vs. CPF
   - RG vs. CNH
   - RG vs. Escritura
   - RG vs. CCIR
   - **Qualquer divergência deve ser esclarecida antes de protocolo**

5. **Processar OCR** (futuro) se necessário para auditoria

---

## Base Normativa

| Norma | Requisito |
|-------|-----------|
| **Lei 7.116/1983** | RG — Registro de Identidade Civil |
| **Lei 9.534/1997** | CPF — Cadastro de Pessoas Físicas |
| **Resolução INMETRO** | Padrão Nacional de RG (desde 2018) |
| **BCB MCR 1** | Identificação obrigatória para operações de crédito |

---

## Armazenamento

| Tipo | Caminho |
|------|---------|
| Original | `Docs Pessoais/RG + CPF - SERGIO.pdf` |
| Nota operacional | Esta nota |
| OCR/transcrição | *a criar quando necessário em `_registros/`* |

---

## Referências Operacionais

- [[Sergio Jose Altoe]] — ficha do cliente
- [[Checklist Documental - Sergio Jose Altoe]] — checklist mestre
- [[Sergio Jose Altoe - Dossie Rural]] — índice do caso
- `CNH - SERGIO.pdf` — documento secundário de identidade (relacionado)
- `CCIR 2025 Sergio Altoe.pdf` — confirmação de CPF em documento rural (relacionado)
- `ESCRITURA Sergio Altoe.pdf` — confirmação de CPF em documento de propriedade (relacionado)

---

## Observações de Conferência

**Data:** 2026-05-05  
**Conferido por:** Cacilda

Conferência por índice — RG + CPF localizado, mas **status definido como `precisa_confirmar`** até:
- Extração de dados (números RG, CPF, datas)
- Validação de legibilidade e completude do scan
- Confirmação de validade do RG
- Conferência de coerência de nome contra outros documentos

Checklist mestre já sinaliza: "Confirmar legibilidade, nome completo e CPF sem divergencia cadastral" como ação obrigatória antes da submissão ao banco.

**Ação imediata recomendada:** Validar CPF (número e dígitos verificadores) antes de qualquer ação operacional. CPF incorreto ou divergente compromete toda a operação creditícia.
