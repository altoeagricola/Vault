---
tipo_documento: CNH (Carteira Nacional de Habilitação)
titular: Sergio Jose Altoe
cpf: "1" # extrair do RG+CPF documento
orgao_emissor: DETRAN/ES (Departamento de Trânsito - Espírito Santo)
numero_documento: "a confirmar no PDF"
data_emissao: "a confirmar no PDF"
data_vencimento: "CRÍTICO - confirmar validade antes de submissão bancária"
status_documental: "existente"
status_conferencia: "precisa_confirmar"
fonte_arquivo: "Docs Pessoais/CNH - SERGIO.pdf"
fonte_ocr: "não processado"
data_conferencia: 2026-05-05
conferido_por: Cacilda
confianca_extracao: "baixa - PDF sem OCR"
divergencias: "nenhuma identificada até agora"
pendencias: "validar data de vencimento no original; confirmar se CNH ainda é válida para operação creditícia"
tags:
  - identidade
  - validade-crítica
  - precisa-confirmar
  - credito-rural
checklist_ref: "[[Checklist Documental - Sergio Jose Altoe]]"
dossie_ref: "[[Sergio Jose Altoe - Dossie Rural]]"
---

# Registro — CNH de Sergio Jose Altoe

## Resumo Operacional

Carteira Nacional de Habilitação (CNH) de Sergio Jose Altoe, documento de identificação secundário com **validade crítica para operações creditícias**. Armazenado em `Docs Pessoais/CNH - SERGIO.pdf`.

---

## Campos Extraídos

| Campo | Valor | Status |
|-------|-------|--------|
| **Tipo documento** | CNH | Confirmado |
| **Titular** | Sergio Jose Altoe | Confirmado |
| **CPF** | — | Extrair de RG+CPF documento |
| **Órgão emissor** | DETRAN/ES | Presumido |
| **Nº documento** | *a confirmar no PDF* | **PENDENTE** |
| **Data emissão** | *a confirmar no PDF* | **PENDENTE** |
| **Data vencimento** | *a confirmar no PDF* | **CRÍTICO — PENDENTE** |
| **Categoria/classe** | *a confirmar no PDF* | Presumido: AB ou B |

---

## Conferência e Divergências

### Status Atual

- PDF localizado: ✓ `Docs Pessoais/CNH - SERGIO.pdf`
- OCR processado: ✗ Não (PDF com scan sem texto pesquisável)
- Validade confirmada: ✗ Não (exigido antes de submissão)

### Riscos Identificados

1. **Validade expirada:** Se a CNH venceu, pode impedir operação creditícia ou exigir renovação. MCR e bancos exigem documentação atual.
2. **Dados ilegíveis:** PDF sem OCR torna impossível confirmar dados sem visualização manual.
3. **Inconsistência de nome:** Checklist indica "padronizar nome em rodada futura" — nome deve ser conferido contra RG + CPF.

### Próximas Ações

1. **Visualizar PDF original** e extrair:
   - Data de vencimento
   - Número da CNH
   - Data de emissão
2. **Validar validade** — se expirada, solicitar renovação
3. **Conferir nome completo** contra `RG + CPF - SERGIO.pdf` para evitar divergência cadastral
4. **Processar OCR** (futuro): se necessário para auditoria, gerar texto pesquisável e armazenar em `_registros/`

---

## Armazenamento

| Tipo | Caminho |
|------|---------|
| Original | `Docs Pessoais/CNH - SERGIO.pdf` |
| Nota operacional | Esta nota |
| OCR/transcrição | *a criar quando necessário em `_registros/`* |

---

## Referências Operacionais

- [[Sergio Jose Altoe]] — ficha do cliente
- [[Checklist Documental - Sergio Jose Altoe]] — checklist mestre
- [[Sergio Jose Altoe - Dossie Rural]] — índice do caso
- `RG + CPF - SERGIO.pdf` — documento primário de identidade (relacionado)

---

## Observações de Conferência

**Data:** 2026-05-05  
**Conferido por:** Cacilda

Conferência inicial por índice de arquivo — não foi possível validar dados do PDF nesta etapa por falta de OCR processado. **Status definido como `precisa_confirmar`** até validação visual de data de vencimento e comparação com RG + CPF para confirmação de titularidade e coerência de nome.

Recomendação: Priorizar validação de validade da CNH antes de protocolo ao banco.
