---
tipo_documento: Comprovante de Aposentadoria / Renda Previdenciária
titulares: "Sergio Jose Altoe e Maria de Lourdes Bernabe Altoe"
cpf_primario: "não consta no comprovante visualizado"
cpf_secundario: "não consta no comprovante visualizado"
orgao_emissor: "INSS (Instituto Nacional do Seguro Social)"
tipo_beneficio: "Saque de benefício — INSS pago benefício"
status_renda: "ativo"
status_documental: "existente"
status_conferencia: "validado_visual_com_pendencia_cpf_e_recencia"
fonte_arquivo: "Docs Pessoais/COMP. DE APOSENTADORIA Maria de Lourdes e Sergio.pdf"
fonte_ocr: "PDF sem texto pesquisável; conferência visual em PNG temporário"
data_conferencia: 2026-05-23
conferido_por: Cacilda
confianca_extracao: "média - leitura visual direta do scan; comprovante não contém CPF"
divergencias: "nenhuma identificada até agora"
pendencias: "solicitar comprovante INSS mais completo/recente com CPF; validar aceitação bancária; recalcular capacidade de pagamento"
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
| **Tipo documento** | Comprovante de saque de benefício INSS via Banco do Brasil | Confirmado visualmente |
| **Titular 1** | Sergio Jose Altoe | Confirmado visualmente |
| **Benefício titular 1** | 548.408.852-2 | Confirmado visualmente |
| **Data comprovante titular 1** | 02/04/2026 | Confirmado visualmente |
| **Valor saque titular 1** | R$ 1.620,00 | Confirmado visualmente |
| **Próximo pagamento titular 1** | A partir de 27/04/2026 | Confirmado visualmente |
| **Titular 2** | Maria de Lourdes Bernabe | Confirmado visualmente |
| **Benefício titular 2** | 162.730.510-3 | Confirmado visualmente |
| **Data comprovante titular 2** | 15/04/2026 | Confirmado visualmente |
| **Valor saque titular 2** | R$ 8,00 | Confirmado visualmente |
| **Próximo pagamento titular 2** | A partir de 08/05/2026 | Confirmado visualmente |
| **CPF (titular 1/2)** | Não consta no comprovante | **PENDENTE** |
| **Renda mensal total comprovada no scan** | R$ 1.628,00 | **Parcial; validar com extrato INSS completo** |

---

## Conferência e Divergências

### Status Atual

- PDF localizado: ✓ `Docs Pessoais/COMP. DE APOSENTADORIA Maria de Lourdes e Sergio.pdf`
- OCR processado: ✗ Não (PDF com scan sem texto pesquisável)
- Datas dos comprovantes confirmadas: ✓ 02/04/2026 e 15/04/2026
- Renda/saques extraídos: ✓ Parcial — R$ 1.620,00 e R$ 8,00
- Adequação para operação validada: ✗ Não

### Riscos de Renda

1. **Comprovante incompleto para banco:** O scan mostra saque de benefício, mas não mostra CPF dos titulares.
2. **Valor de Maria de Lourdes:** O comprovante visualizado mostra saque de apenas R$ 8,00; isso não parece comprovar renda mensal normal dela.
3. **Recência:** Comprovantes de abril/2026 estão dentro de 90 dias em 23/05/2026, mas podem ficar vencidos rapidamente.
4. **Capacidade de pagamento:** Renda comprovada visualmente é parcial e insuficiente para concluir capacidade de pagamento.

### Próximas Ações Críticas

1. Solicitar comprovante/extrato INSS completo e recente contendo CPF, espécie de benefício e valor mensal bruto/líquido.
2. Confirmar se o valor de Maria de Lourdes é renda mensal efetiva ou apenas saldo/saque residual.
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

6. Processar OCR pesquisável apenas se o banco ou auditoria exigir cópia textual.

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

**Data:** 2026-05-23  
**Conferido por:** Cacilda

Conferência visual realizada a partir de renderização PNG temporária do PDF original. O scan contém dois comprovantes Banco do Brasil/SISBB de "Saque de benefício — INSS pago benefício": Sergio Jose Altoe em 02/04/2026, benefício 548.408.852-2, saque R$ 1.620,00; Maria de Lourdes Bernabe em 15/04/2026, benefício 162.730.510-3, saque R$ 8,00.

**Ação crítica:** solicitar extrato INSS/Meu INSS completo, pois o comprovante atual não traz CPF e o valor de Maria de Lourdes não comprova renda mensal usual.

**Nota operacional futura:** Uma vez extraída a renda, integrar a `Analise Financeira - Sergio Jose Altoe.md` (ainda a criar) para cálculo de capacidade de pagamento e dimensionamento da operação.
