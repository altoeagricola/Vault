---
tipo_documento: CCIR (Certificado de Cadastro de Imóvel Rural)
titular: Sergio Jose Altoe
cpf_cnpj: "a confirmar"
imovel: "Propriedade Rural - Marilândia/ES (a confirmar no PDF)"
orgao_emissor: INCRA (Instituto Nacional de Colonização e Reforma Agrária)
numero_documento: "a confirmar no PDF"
data_emissao: "a confirmar no PDF"
data_vencimento: "a confirmar no PDF (CCIR anual)"
competencia: "2025 (conforme nome)"
status_documental: "existente"
status_quitacao: "a confirmar"
status_conferencia: "precisa_confirmar"
fonte_arquivo: "Docs Propriedade/CCIR 2025 Sergio Altoe.pdf"
fonte_ocr: "não processado"
data_conferencia: 2026-05-05
conferido_por: Cacilda
confianca_extracao: "baixa - PDF sem OCR"
divergencias: "nenhuma identificada até agora"
pendencias: "confirmar quitação; validar area declarada contra escritura e ITR; extrair número NIRF e dados do imóvel"
tags:
  - propriedade-rural
  - ccir
  - documento-chave-credito
  - precisa-confirmar
  - credito-rural
  - marilândia
checklist_ref: "[[Checklist Documental - Sergio Jose Altoe]]"
dossie_ref: "[[Sergio Jose Altoe - Dossie Rural]]"
---

# Registro — CCIR 2025 de Sergio Jose Altoe

## Resumo Operacional

Certificado de Cadastro de Imóvel Rural (CCIR) 2025 de Sergio Jose Altoe, **documento-chave para operações de crédito rural**. CCIR é prova de registro do imóvel no INCRA, com atualização anual obrigatória.

Localizado em: `Docs Propriedade/CCIR 2025 Sergio Altoe.pdf`

---

## Campos Extraídos

| Campo | Valor | Status |
|-------|-------|--------|
| **Tipo documento** | CCIR | Confirmado |
| **Titular** | Sergio Jose Altoe | Presumido (confirmar no PDF) |
| **Propriedade** | Rural — Marilândia/ES | Presumido (confirmar no PDF) |
| **Órgão emissor** | INCRA | Confirmado |
| **Nº NIRF** | *a confirmar no PDF* | **PENDENTE** |
| **Data emissão** | *a confirmar no PDF* | **PENDENTE** |
| **Data vencimento/validade** | *a confirmar no PDF* | **PENDENTE** |
| **Situação de quitação** | *a confirmar no PDF* | **CRÍTICO — PENDENTE** |
| **Área total (ha)** | *a confirmar no PDF* | **PENDENTE** |

---

## Conferência e Divergências

### Status Atual

- PDF localizado: ✓ `Docs Propriedade/CCIR 2025 Sergio Altoe.pdf`
- OCR processado: ✗ Não (PDF sem texto pesquisável)
- Quitação confirmada: ✗ Não
- Área conferida com escritura: ✗ Não
- Área conferida com ITR: ✗ Não

### Riscos e Divergências Potenciais

1. **Não-quitação:** Se propriedade ou CCIR tem pendência fiscal ou ambiental, banco pode exigir regularização ou bloquear operação.
2. **Divergência de área:** CCIR pode declarar área diferente da escritura ou ITR (comum em imóveis antigos sem demarcação recente). Divergências>10% geralmente geram exigências bancárias.
3. **Divergência de titularidade:** Se CCIR consta nome de terceiro ou falecido, impede operação.
4. **CCIR anual:** CCIR 2025 é válido enquanto dados do imóvel não mudarem. Se houve transferência de área ou alienação, pode estar desatualizado.

### Próximas Ações Críticas

1. **Extrair do PDF original**:
   - Número NIRF
   - Data de emissão e validade
   - Situação de quitação/regularidade
   - Área total declarada
   - Proprietário(s)
2. **Validar quitação** — verificar se há pendência fiscal, ambiental ou de crédito
3. **Conferir coerência**:
   - Área contra ESCRITURA (devem ser próximas)
   - Área contra ITR 2025 (devem ser próximas)
   - Titularidade contra ESCRITURA (devem ser idênticos)
4. **Processar OCR** (futuro) se necessário para auditoria

---

## Base Normativa

| Norma | Requisito |
|-------|-----------|
| **Lei 5.868/1972** | CCIR obrigatório para propriedade rural |
| **IN INCRA 76/2014** | Procedimento anual de emissão de CCIR |
| **BCB MCR 2-1** | CCIR ou inscrição fundiária obrigatória para operações rurais |

---

## Armazenamento

| Tipo | Caminho |
|------|---------|
| Original | `Docs Propriedade/CCIR 2025 Sergio Altoe.pdf` |
| Nota operacional | Esta nota |
| OCR/transcrição | *a criar quando necessário em `_registros/`* |

---

## Referências Operacionais

- [[Sergio Jose Altoe]] — ficha do cliente
- [[Checklist Documental - Sergio Jose Altoe]] — checklist mestre
- [[Sergio Jose Altoe - Dossie Rural]] — índice do caso
- `ESCRITURA Sergio Altoe.pdf` — documento de propriedade (relacionado, para conferência)
- `ITR 2025 Sergio Altoe.pdf` — documento fiscal rural (relacionado, para conferência)
- [[Marilandia]] — localização/contexto regional

---

## Observações de Conferência

**Data:** 2026-05-05  
**Conferido por:** Cacilda

Conferência por índice — CCIR 2025 localizado, mas **status definido como `precisa_confirmar`** até:
- Extração de dados (NIRF, datas, quitação, área)
- Validação de quitação fiscal/ambiental
- Conferência de coerência com escritura e ITR

Checklist mestre já sinaliza: "Confirmar quitacao/regularidade e consistencia de area/titularidade" como ação obrigatória antes da submissão ao banco.

**Risco:** Divergência de área entre CCIR, escritura e ITR é frequente em propriedades antigas sem revisão cadastral recente. Recomenda-se conferência cruzada antes de envio ao banco.
