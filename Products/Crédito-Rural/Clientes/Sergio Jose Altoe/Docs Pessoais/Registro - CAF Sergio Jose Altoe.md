---
tipo_documento: CAF (Cadastro de Agricultores Familiares)
titular: Sergio Jose Altoe
cpf: "a confirmar"
orgao_emissor: MAPA (Ministério da Agricultura e Pecuária)
numero_documento: "a confirmar no PDF"
data_emissao: "a confirmar no PDF"
data_vencimento: "CRÍTICO - deve estar válido para Pronaf"
competencia: "a confirmar"
enquadramento: "Pronaf - a confirmar"
status_documental: "existente"
status_conferencia: "precisa_confirmar"
fonte_arquivo: "Docs Pessoais/CAF. Sergio.pdf"
fonte_ocr: "não processado"
data_conferencia: 2026-05-05
conferido_por: Cacilda
confianca_extracao: "baixa - PDF sem OCR"
divergencias: "nenhuma identificada até agora"
pendencias: "validar validade; confirmar enquadramento Pronaf aplicável ao caso de habitação rural; extrair número CAF"
tags:
  - pronaf
  - enquadramento-agricultor-familiar
  - validade-crítica
  - precisa-confirmar
  - credito-rural
checklist_ref: "[[Checklist Documental - Sergio Jose Altoe]]"
dossie_ref: "[[Sergio Jose Altoe - Dossie Rural]]"
---

# Registro — CAF de Sergio Jose Altoe

## Resumo Operacional

Cadastro de Agricultores Familiares (CAF) de Sergio Jose Altoe, documento **essencial para caracterização de beneficiário Pronaf**. Conforme MCR 10-2, a presença de CAF válido é requisito mandatório para acesso a operações Pronaf (incluindo Pronaf Habitação Rural).

Localizado em: `Docs Pessoais/CAF. Sergio.pdf`

---

## Campos Extraídos

| Campo | Valor | Status |
|-------|-------|--------|
| **Tipo documento** | CAF | Confirmado |
| **Titular** | Sergio Jose Altoe | Confirmado |
| **CPF** | — | Extrair do PDF |
| **Órgão emissor** | MAPA (Ministério da Agricultura e Pecuária) | Presumido |
| **Nº CAF** | *a confirmar no PDF* | **PENDENTE** |
| **Data emissão** | *a confirmar no PDF* | **PENDENTE** |
| **Data vencimento** | *a confirmar no PDF* | **CRÍTICO — PENDENTE** |
| **Enquadramento Pronaf** | *a confirmar no PDF* | **CRÍTICO — PENDENTE** |

---

## Conferência e Divergências

### Status Atual

- PDF localizado: ✓ `Docs Pessoais/CAF. Sergio.pdf`
- OCR processado: ✗ Não (PDF com scan sem texto pesquisável)
- Validade confirmada: ✗ Não (exigido antes de protocolo)
- Enquadramento Pronaf validado: ✗ Não

### Riscos Normativos Críticos

Segundo **BCB Manual de Crédito Rural (MCR 10-2)**:

> "Operações de crédito Pronaf dependem de beneficiário com Cadastro de Agricultores Familiares válido."

**Consequências se CAF for inválido, vencido ou sem enquadramento**:
1. **Recusa automática de aprovação** — banco não pode liberar recursos
2. **Exigência de renovação** — CAF vencido não vale, mesmo com dados corretos
3. **Divergência de enquadramento** — se CAF define programa diferente do solicitado (ex.: CAF para Pronaf Custeio, mas operação é Habitação), pode impedir operação

### Próximas Ações Críticas

1. **Extrair do PDF original**:
   - Número CAF
   - Data de emissão e vencimento
   - Enquadramento Pronaf registrado
2. **Validar validade** contra data presente (2026-05-05)
3. **Conferir enquadramento** — se o CAF consta Pronaf Habitação Rural ou programa compatível
4. **Processar OCR** (futuro): se necessário para auditoria, gerar texto pesquisável em `_registros/`

---

## Base Normativa

| Norma | Requisito |
|-------|-----------|
| **BCB MCR 10-2** | CAF válido obrigatório para beneficiário Pronaf |
| **BCB MCR 10-5** | Investimento Pronaf em habitação requer projeto técnico específico |
| **IN MAPA 109/2023** | Procedimento atual de CAF (substitui SRA) |

---

## Armazenamento

| Tipo | Caminho |
|------|---------|
| Original | `Docs Pessoais/CAF. Sergio.pdf` |
| Nota operacional | Esta nota |
| OCR/transcrição | *a criar quando necessário em `_registros/`* |

---

## Referências Operacionais

- [[Sergio Jose Altoe]] — ficha do cliente
- [[Checklist Documental - Sergio Jose Altoe]] — checklist mestre
- [[Sergio Jose Altoe - Dossie Rural]] — índice do caso
- [[Pronaf Habitacao - Sergio Jose Altoe]] — enquadramento de crédito (relacionado)
- [[Cresol]] — banco executante

---

## Observações de Conferência

**Data:** 2026-05-05  
**Conferido por:** Cacilda

Conferência por índice e checklist — CAF encontrado, mas **status definido como `precisa_confirmar`** até extração e validação de:
- Data de vencimento (obrigatório estar válido)
- Enquadramento Pronaf (deve constar habitação ou programa compatível)
- Número CAF para rastreamento

Checklist mestre (ALT-?) já sinaliza: "CAF invalido, vencido ou sem enquadramento Pronaf aplicavel" é impedimento potencial máximo.

**Ação imediata recomendada:** Validar CAF antes de qualquer submissão ao banco. Se vencido, solicitar renovação urgente.
