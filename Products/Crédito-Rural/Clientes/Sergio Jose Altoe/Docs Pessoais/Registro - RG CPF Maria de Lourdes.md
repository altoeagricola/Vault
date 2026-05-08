---
tipo_documento: RG + CPF (Registro Geral + Cadastro de Pessoas Físicas)
titular: Maria de Lourdes Bernabe Altoe
cpf: "a confirmar no PDF"
rg: "a confirmar no PDF"
relacao_caso: cônjuge de Sergio Jose Altoe
orgao_emissor_rg: "SSP/ES (Secretaria de Segurança Pública - Espírito Santo)"
orgao_emissor_cpf: "Receita Federal do Brasil"
data_emissao_rg: "a confirmar no PDF"
data_vencimento_rg: "a confirmar no PDF (RG tem validade de 10 anos)"
numero_rg: "a confirmar no PDF"
data_emissao_cpf: "a confirmar no PDF"
status_documental: "existente"
status_conferencia: "precisa_confirmar"
fonte_arquivo: "Docs Pessoais/RG E CPF - MARIA DE LOURDES BERNABE ALTOE.pdf"
fonte_ocr: "não processado"
data_conferencia: 2026-05-05
conferido_por: Cacilda
confianca_extracao: "baixa - PDF sem OCR"
divergencias: "nenhuma identificada até agora"
pendencias: "confirmar legibilidade; validar CPF; validar coerência de nome com certidão de casamento; extrair números"
tags:
  - identidade-cônjuge
  - documento-obrigatorio
  - rg-cpf
  - nucleo-familiar
  - precisa-confirmar
  - credito-rural
checklist_ref: "[[Checklist Documental - Sergio Jose Altoe]]"
dossie_ref: "[[Sergio Jose Altoe - Dossie Rural]]"
---

# Registro — RG + CPF de Maria de Lourdes Bernabe Altoe

## Resumo Operacional

Registro Geral (RG) e Cadastro de Pessoas Físicas (CPF) de Maria de Lourdes Bernabe Altoe, cônjuge de Sergio Jose Altoe, **documento de identidade essencial para operações em que cônjuge precisa assinar ou anuir**. Em operações de crédito rural com regime de comunhão de bens, cônjuge é automaticamente envolvido na operação.

Localizado em: `Docs Pessoais/RG E CPF - MARIA DE LOURDES BERNABE ALTOE.pdf`

---

## Campos Extraídos

| Campo | Valor | Status |
|-------|-------|--------|
| **Tipo documento** | RG + CPF | Confirmado |
| **Titular** | Maria de Lourdes Bernabe Altoe | Presumido (confirmar no PDF) |
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

- PDF localizado: ✓ `Docs Pessoais/RG E CPF - MARIA DE LOURDES BERNABE ALTOE.pdf`
- OCR processado: ✗ Não (PDF com scan sem texto pesquisável)
- CPF confirmado: ✗ Não
- Legibilidade validada: ✗ Não
- Coerência de nome com certidão: ✗ Não

### Riscos de Identidade do Cônjuge

1. **CPF divergente:** Se CPF do cônjuge divergir de registros, impede operação até esclarecimento.
2. **RG expirado:** Válido por 10 anos — se vencido, pode ser exigida renovação.
3. **Nome divergente:** Variações de nome (ex.: "Maria de Lourdes" vs. "Maria Lourdes" vs. apelido) entre RG, CPF e Certidão de Casamento causam rejeição.
4. **Restrição de crédito do cônjuge:** Se cônjuge tem restrição bancária, CPF em atraso ou operação em nome de cônjuge pode ser travada.

### Próximas Ações Críticas

1. **Visualizar PDF original** e extrair:
   - Número completo do RG
   - Data de emissão e vencimento do RG
   - Número do CPF
   - Data de emissão do CPF
   - **Nome completo exato** (validar contra certidão de casamento)

2. **Validar CPF**:
   - Conferir integridade (dígitos verificadores)
   - Conferir contra registros de ALTOE Agricola
   - Conferir contra cadastro do banco Cresol

3. **Validar RG**:
   - Confirmar validade (10 anos)
   - Se expirado, solicitar renovação

4. **Conferir coerência de nome**:
   - RG vs. CPF (devem coincidir)
   - RG vs. Certidão de Casamento (nome de solteira? mudança de nome?)
   - **Divergências de nome de cônjuge são frequentes — esclarecer antes de protocolo**

5. **Verificar restrições**:
   - Se cônjuge tem restrição de crédito, pode afetar operação (depende de regime de bens e política do banco)

6. **Processar OCR** (futuro) se necessário para auditoria

---

## Base Normativa

| Norma | Requisito |
|-------|-----------|
| **Lei 7.116/1983** | RG — Registro de Identidade Civil |
| **Lei 9.534/1997** | CPF — Cadastro de Pessoas Físicas |
| **CC artigos 1.639–1.688** | Regimes de bens — cônjuge pode ser obrigado a assinar conforme regime |
| **BCB MCR 1** | Identificação obrigatória para cônjuge em operações de crédito com comunhão de bens |

---

## Armazenamento

| Tipo | Caminho |
|------|---------|
| Original | `Docs Pessoais/RG E CPF - MARIA DE LOURDES BERNABE ALTOE.pdf` |
| Nota operacional | Esta nota |
| Certidão de casamento | `Docs Pessoais/CERTIDAO DE CASAMENTO Sergio e Lourdes.pdf` (relacionada) |
| OCR/transcrição | *a criar quando necessário em `_registros/`* |

---

## Referências Operacionais

- [[Sergio Jose Altoe]] — cliente (titular da operação)
- [[Checklist Documental - Sergio Jose Altoe]] — checklist mestre
- [[Sergio Jose Altoe - Dossie Rural]] — índice do caso
- `RG + CPF - SERGIO.pdf` — RG/CPF do titular (relacionado)
- `CERTIDAO DE CASAMENTO Sergio e Lourdes.pdf` — estado civil (relacionado, para validação de nome)
- `COMP. DE APOSENTADORIA Maria de Lourdes e Sergio.pdf` — renda do cônjuge (relacionada)

---

## Observações de Conferência

**Data:** 2026-05-05  
**Conferido por:** Cacilda

Conferência por índice — RG + CPF de cônjuge localizado, mas **status definido como `precisa_confirmar`** até:
- Extração de dados (números RG, CPF, datas)
- Validação de legibilidade
- **Conferência crítica:** Nome no RG vs. nome na Certidão de Casamento (validar se houve mudança de nome ou variação de sobrenome)
- Confirmação de validade do RG

Checklist mestre já sinaliza: "Confirmar se o banco exigira assinatura/anuencia da conjuge" como ação condicional antes da submissão ao banco.

**Observação importante:** Em operações de habitação rural com regime de comunhão de bens, cônjuge é automaticamente co-proprietária e pode ser exigida sua assinatura na escritura e na operação creditícia. CPF do cônjuge precisa estar válido e sem restrições para que a operação avance.
