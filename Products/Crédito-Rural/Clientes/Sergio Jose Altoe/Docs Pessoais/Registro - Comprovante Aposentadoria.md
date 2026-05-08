---
tipo_documento: Comprovante de Aposentadoria / Renda Previdenciária
titulares: "Sergio Jose Altoe e Maria de Lourdes Bernabe Altoe"
cpf_primario: "a confirmar"
cpf_secundario: "a confirmar"
orgao_emissor: "INSS (Instituto Nacional do Seguro Social)"
tipo_beneficio: "Aposentadoria (presumido)"
status_renda: "ativo"
status_documental: "existente"
status_conferencia: "precisa_confirmar"
fonte_arquivo: "Docs Pessoais/COMP. DE APOSENTADORIA Maria de Lourdes e Sergio.pdf"
fonte_ocr: "não processado"
data_conferencia: 2026-05-05
conferido_por: Cacilda
confianca_extracao: "baixa - PDF sem OCR"
divergencias: "nenhuma identificada até agora"
pendencias: "confirmar competência (mês/ano de emissão); validar se é documento recente; extrair valores de renda de ambos; validar se renda é suficiente para operação"
tags:
  - renda
  - aposentadoria
  - previdencia
  - documento-entrada-analise-financeira
  - precisa-confirmar
  - credito-rural
checklist_ref: "[[Checklist Documental - Sergio Jose Altoe]]"
dossie_ref: "[[Sergio Jose Altoe - Dossie Rural]]"
---

# Registro — Comprovante de Aposentadoria de Sergio e Maria de Lourdes

## Resumo Operacional

Comprovante de Aposentadoria do INSS emitido em nome de Sergio Jose Altoe e/ou Maria de Lourdes Bernabe Altoe, **documento essencial para análise de capacidade de pagamento**. Em operações de crédito rural, renda previdenciária é frequentemente a renda principal ou complementar de agricultores em regime de reforma agrária ou proprietários rurais aposentados.

Localizado em: `Docs Pessoais/COMP. DE APOSENTADORIA Maria de Lourdes e Sergio.pdf`

---

## Campos Extraídos

| Campo | Valor | Status |
|-------|-------|--------|
| **Tipo documento** | Comprovante de Aposentadoria INSS | Presumido (confirmar no PDF) |
| **Titulares** | Sergio Jose Altoe e Maria de Lourdes | Presumido (confirmar no PDF) |
| **CPF (titular 1)** | *a confirmar no PDF* | **PENDENTE** |
| **CPF (titular 2)** | *a confirmar no PDF* | **PENDENTE** |
| **Tipo de benefício** | Aposentadoria (presumido) | **PENDENTE** |
| **Competência/mês de emissão** | *a confirmar no PDF* | **CRÍTICO — PENDENTE** |
| **Renda mensal (titular 1)** | *a confirmar no PDF* | **CRÍTICO — PENDENTE** |
| **Renda mensal (titular 2)** | *a confirmar no PDF* | **CRÍTICO — PENDENTE** |
| **Renda total (ambos)** | *a confirmar no PDF* | **CRÍTICO — PENDENTE** |

---

## Conferência e Divergências

### Status Atual

- PDF localizado: ✓ `Docs Pessoais/COMP. DE APOSENTADORIA Maria de Lourdes e Sergio.pdf`
- OCR processado: ✗ Não (PDF com scan sem texto pesquisável)
- Competência confirmada: ✗ Não
- Renda extraída: ✗ Não
- Adequação para operação validada: ✗ Não

### Riscos de Renda

1. **Documento desatualizado:** Se comprovante tem competência anterior a 90 dias, pode ser exigido comprovante mais recente (depende da política do banco).
2. **Renda insuficiente:** Se renda total de ambos não cobre prestações da operação (capacidade de pagamento negativa), operação é recusada ou redimensionada.
3. **Alteração de renda:** Se entre emissão do comprovante e protocolo ao banco há aumento/redução significativa de renda, pode requerer novo comprovante.
4. **Divergência de CPF:** Se CPFs no comprovante divergem de RG + CPF apresentados, impede operação.
5. **Renda de apenas um:** Se comprovante está em nome de apenas uma pessoa, renda do cônjuge não pode ser considerada (exceto em regime de separação de bens).

### Próximas Ações Críticas

1. **Extrair do PDF original**:
   - **Competência** (mês/ano de emissão) — essencial para validar "recência"
   - CPF de Sergio Jose Altoe
   - CPF de Maria de Lourdes Bernabe Altoe
   - Valor de renda mensal de Sergio
   - Valor de renda mensal de Maria de Lourdes
   - Renda total (soma)
   - Tipo de benefício (aposentadoria, pensão, auxílio)

2. **Validar recência**:
   - Se comprovante foi emitido há mais de 90 dias, solicitar novo comprovante ao INSS

3. **Calcular capacidade de pagamento**:
   - Renda total mensal de ambos vs. prestação da operação proposta
   - Aplicar coeficiente de endividamento do banco (geralmente máximo 30-40% da renda para crédito rural)
   - Se renda for insuficiente, redimensionar operação ou procurar recursos complementares

4. **Conferir coerência de CPF**:
   - CPF no comprovante vs. RG + CPF de Sergio
   - CPF no comprovante vs. RG + CPF de Maria de Lourdes

5. **Validar modalidade**:
   - Se é aposentadoria rural, pode ter tratamento diferenciado em banco agrícola
   - Se é aposentadoria urbana de pessoa que migrou para rural, pode ter restrições

6. **Processar OCR** (futuro) se necessário para auditoria

---

## Base Normativa

| Norma | Requisito |
|-------|-----------|
| **Lei 8.212/1991** | INSS — comprovante de renda previdenciária |
| **Lei 8.213/1991** | Beneficiários e filiação ao INSS |
| **BCB MCR 7** | Análise de capacidade de pagamento baseada em renda comprovada |
| **Resolução BCB** | Coeficiente de endividamento para crédito pessoa física |

---

## Análise Financeira

Este documento é **entrada primária para análise financeira** do caso. A renda aqui informada será base para:
- Cálculo de capacidade de pagamento
- Redimensionamento da operação se necessário
- Validação de sustentabilidade do investimento em habitação rural

---

## Armazenamento

| Tipo | Caminho |
|------|---------|
| Original | `Docs Pessoais/COMP. DE APOSENTADORIA Maria de Lourdes e Sergio.pdf` |
| Nota operacional | Esta nota |
| Análise financeira | A criar quando entregue (`Analise Financeira - Sergio Jose Altoe.md`) |
| OCR/transcrição | *a criar quando necessário em `_registros/`* |

---

## Referências Operacionais

- [[Sergio Jose Altoe]] — cliente (titular)
- [[Checklist Documental - Sergio Jose Altoe]] — checklist mestre
- [[Sergio Jose Altoe - Dossie Rural]] — índice do caso
- `RG + CPF - SERGIO.pdf` — validação de identidade de Sergio (relacionada)
- `RG E CPF - MARIA DE LOURDES BERNABE ALTOE.pdf` — validação de identidade de cônjuge (relacionada)
- [[Pronaf Habitacao - Sergio Jose Altoe]] — enquadramento de crédito (relacionado)

---

## Observações de Conferência

**Data:** 2026-05-05  
**Conferido por:** Cacilda

Conferência por índice — Comprovante de aposentadoria localizado, mas **status definido como `precisa_confirmar`** até:
- Extração de dados (competência, CPFs, rendas de ambos)
- Validação de recência (menos de 90 dias)
- Conferência de CPFs contra RG + CPF de ambos os titulares
- Cálculo de capacidade de pagamento para operação proposta

Checklist mestre já sinaliza: "Atualizar se o comprovante nao for de competencia recente" como ação obrigatória antes da submissão ao banco.

**Ação crítica:** Validar competência do comprovante — se anterior a 90 dias, solicitar novo comprovante ao INSS. Renda desatualizada pode resultar em recusa do banco ou redimensionamento da operação.

**Nota operacional futura:** Uma vez extraída a renda, integrar a `Analise Financeira - Sergio Jose Altoe.md` (ainda a criar) para cálculo de capacidade de pagamento e dimensionamento da operação.
