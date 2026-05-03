---
name: ingest-business
description: Ingest business documents into the operational areas of the vault — personal/corporate identity documents (CNH, RG, CPF, IRPF, Contrato Social, CNPJ, Certidões, Comprovantes), editais de fomento agropecuário (Plano Safra, Pronaf, Pronamp, FNE, programas estaduais), and official bank/regulatory documents for rural credit and fomento (MCR, normativos BCB, manuais BB/Sicredi/Sicoob, Lei do Bem, marcos legais de CT&I). Use when the user provides files or URLs to such documents and wants them filed and indexed in the structural layers of the vault. Triggers include "ingest business", "ingest documento", "ingest edital fomento", "ingest MCR", "arquivar documento", or any request to file an official/operational business document.
---

# Business Documents Ingestion Skill

This skill files **operational and regulatory business documents** into the structural layers of the vault (Areas, Products), **not** the Wiki. It is a domain specialist that does NOT delegate to `/ingest`.

The vault keeps a clean separation:
- `Wiki/` and `Wiki-Comercial/` hold **synthesized knowledge** (concepts, summaries, analyses) — fed by `/ingest`, `/ingest-pdf`, etc.
- `Areas/` and `Products/` hold **operational artifacts** that the human owns — what `/ingest-business` writes to.

## When to Use This Skill vs. Others

| If the document is… | Use |
|---|---|
| A research paper, article, video, tweet | `/ingest`, `/ingest-pdf`, `/ingest-youtube`, `/ingest-tweet` |
| A public **R&D** call (FAPES, FINEP, CNPq research) | `/ingest-call` |
| A personal/corporate identity doc (CNH, CNPJ, IRPF, Certidão, Contrato Social, Comprovante) | `/ingest-business` → **Personal/Corporate** branch |
| An **agricultural** funding/credit call (Plano Safra, Pronaf, FNE, programas estaduais rurais) | `/ingest-business` → **Edital Fomento** branch |
| An official BCB/bank rule, MCR chapter, manual de crédito rural, marco legal | `/ingest-business` → **Regulatory** branch |

If a single document fits two branches (e.g., an edital that also defines new credit rules), pick the **primary intent** and cross-link the other location.

## Input

One or more of:
- Local file paths (PDF, DOCX, JPEG, PNG)
- URLs to download (BCB portal, Plano Safra portal, gov.br, bank portals)
- Multica attachment IDs (use `multica attachment download <id>`)

The user should also provide the **document subject** in plain language (e.g., "CNH renovada do Rodrigo", "Plano Safra 2026/27", "Resolução BCB 4.966 sobre PCLD"). If unclear, ask before proceeding.

## Workflow

### Step 1: Classify the Document

Read the document (or its filename + first pages if large). Decide which of the three branches applies:

- **A. Personal/Corporate Identity Document** — belongs to a specific person or to the empresa
- **B. Edital de Fomento Agropecuário** — a funding/credit call targeting rural producers or agribusiness
- **C. Bank/Regulatory Document** — a normative document defining rules for rural credit or fomento

State the classification to the user in one short sentence and proceed. Only ask for confirmation if the document is genuinely ambiguous (e.g., a bank manual that includes an edital).

### Step 2: Branch-Specific Workflow

Pick the matching branch below. All branches end at Step 3 (commit).

---

#### Branch A — Personal / Corporate Identity Documents

**Destination root:** `Areas/ALTOE Agricola/Documents/<Pessoa|Empresa>/`

**A.1. Identify the owner.** Match against the existing folders:
`Empresa`, `Rodrigo Altoè`, `Eliane Ayumi Okuma`, `Graziela`, `Luis Eduardo Gottardo`. If the owner is new, ask the user to confirm the canonical name and create the subfolder + an overview file using the same template as the existing ones.

**A.2. Place the file.** Move/copy the original PDF/JPG into the owner's folder, preserving a clean filename (e.g., `CNH_Rodrigo Altoè.pdf`, `IRPF 2025 — Declaração.pdf`). Use the same naming style already present in that folder.

**A.3. Extract metadata.** From the document, pull:
- Document type (CNH, RG, CPF, IRPF, Certidão de Casamento, Contrato Social, CNPJ, Comprovante de Endereço/Residência, União Estável, CTPS, etc.)
- Document number / código (CPF, CNPJ, RG, número da CNH, número da inscrição etc.)
- Issuing organ (Detran-ES, Receita Federal, Cartório, JUCEES, Município, etc.)
- Issue date and expiration date (validade)
- Any field relevant for bank cadastro (endereço, regime de bens, situação cadastral, etc.)

**A.4. Update the owner's overview file** (`<Owner>/<Owner>.md`):
- Add or update a row in the **Documentos** table (filename + short descrição)
- For empresa or sócios, update the **Dados Cadastrais** or **Quadro Societário** sections if the document changes them (alteração contratual, novo endereço, nova validade de CNH, etc.)
- Refresh the `atualizado:` frontmatter date

**A.5. Update the index** (`Areas/ALTOE Agricola/Documents/Documents.md`): bump the per-owner doc count in the Estrutura table if the count changed; refresh `atualizado:`.

**A.6. Cross-reference downstream.** If the new document unblocks or affects a bank cadastro (e.g., new alteração contratual that resolves a Sicredi block), append a brief note in the relevant `Connections/Banks/<Bank>/Cadastro/Cadastro.md` and link back with `[[]]`.

---

#### Branch B — Edital de Fomento Agropecuário

**Destination root:** `Products/Fomento/Editais/<Nome do Edital>/`

This is **distinct** from `/ingest-call`, which targets `Prospections/R&D Public Calls/` for research-and-development calls. Use this branch for **agricultural / rural / agribusiness** funding programs (Plano Safra, Pronaf, Pronamp, Pronara, FNE-Agro, FCO-Rural, programas estaduais como Banestes Agro, Bandes, Funse-ES, etc.).

**B.1. Download all documents.** Save the main edital + annexes into:
```
Products/Fomento/Editais/<Edital Name>/
├── <Edital Name>.md                  ← structured note (B.4)
└── _attachments/
    ├── edital.pdf
    ├── manual-operativo.pdf
    └── ...
```

**B.2. Extract metadata** (rural-fomento focus):
- Programa / nome do edital / safra (ex: Plano Safra 2026/2027)
- Órgão emissor (BCB, MAPA, BB, BNDES, Sicredi, Sicoob, agência estadual)
- Público-alvo: porte do produtor (Pronaf, Pronamp, demais produtores), atividade (lavoura, pecuária, agroindústria), DAP/CAF requerido
- Modalidades de crédito: custeio, investimento, comercialização, industrialização
- Volume total e teto por beneficiário
- Taxas de juros (efetiva e equalizada), prazo, carência
- Garantias aceitas, contrapartida, cobertura de seguro (Proagro, PSR)
- Cronograma: vigência, prazo de contratação, prazo de execução
- Documentação exigida (cross-link para `Areas/ALTOE Agricola/Documents/`)

**B.3. First inspection (interactive).** Present a narrative for the user covering: o que financia, a quem se aplica, taxas e tetos, prazos críticos, encaixe com nossos clientes atuais. Aguarde confirmação antes de criar a nota.

**B.4. Create the structured note** at `Products/Fomento/Editais/<Edital Name>/<Edital Name>.md`:

```markdown
---
root: "[[Editais]]"
programa: "[[<Programa>]]"
emissor: "[[<Órgão>]]"
safra: "2026/2027"
status: analyzing            # analyzing | active | preparing | submitted | contracted | closed | archived
volume_total: "R$ X.XXX.XXX,XX"
teto_beneficiario: "R$ XXX.XXX,XX"
taxa_juros: "X,XX% a.a."
prazo_meses: NN
carencia_meses: NN
publico_alvo:
  - "Pronaf"
  - "Pronamp"
modalidades:
  - "Custeio"
  - "Investimento"
contratacao_inicio: YYYY-MM-DD
contratacao_fim: YYYY-MM-DD
link: "<URL principal>"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - Fomento
  - edital
  - credito-rural
---

## Visão Geral
## Público-alvo e Elegibilidade
## Modalidades e Condições Financeiras
## Garantias e Seguros
## Cronograma
## Documentação Exigida
## Encaixe com Carteira Atual
## Documentos Anexados
## Notas
```

Valores monetários em formato BR (R$ X.XXX.XXX,XX); datas no frontmatter em ISO (YYYY-MM-DD); datas no corpo podem usar DD/MM/YYYY.

**B.5. Update indices:**
- `Products/Fomento/Editais/Editais.md` (or create it if missing) — adicionar linha
- `Products/Fomento/PainelF/PainelF.md` — atualizar se houver dashboard de editais ativos

---

#### Branch C — Bank / Regulatory Documents (Rural Credit & Fomento Rules)

**Destination root:**
- Crédito rural (MCR, normativos BCB, manuais BB/Sicredi/Sicoob, Resoluções CMN aplicadas a crédito rural) → `Products/Crédito-Rural/WikiCR/`
- Fomento e marcos legais de CT&I, Lei do Bem, leis estaduais de fomento → `Products/Fomento/WikiF/`

**C.1. Identify the regulation.** Capture: número/título oficial (ex: "Resolução BCB nº 4.966", "MCR 2-1", "Lei 11.196/2005 — Lei do Bem"), órgão emissor, data de publicação, vigência.

**C.2. Save the original.** Place the source PDF in `_attachments/` of the destination subfolder (create if needed).

**C.3. Create or update the regulation page.** Filename = título limpo (ex: `Resolução BCB 4.966 — PCLD.md`, `MCR 2 — Beneficiários do Crédito Rural.md`). Use this frontmatter:

```markdown
---
root: "[[WikiCR]]"               # ou [[WikiF]]
tipo: Norma                      # Norma | Manual | Lei | Resolução | Circular | Manual Operativo
numero: "4.966"
emissor: "[[Banco Central do Brasil]]"
publicado: YYYY-MM-DD
vigencia_inicio: YYYY-MM-DD
vigencia_fim: null               # null se vigente
substitui: "[[<Norma Anterior>]]"
substituido_por: null
escopo:
  - "Crédito Rural"
  - "Pronaf"
tags:
  - regulacao
  - credito-rural                # ou fomento
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

## Resumo
## Escopo de Aplicação
## Principais Regras
## Impactos Operacionais
## Documentos
## Histórico de Versões
```

**C.4. Cascade impact analysis.** Procure páginas existentes em `WikiCR/`, `WikiF/`, `Products/Crédito-Rural/Operacoes/`, e `Products/Crédito-Rural/Propostas/` que citem a norma anterior ou o tema. Liste-as ao usuário com a pergunta: "essas páginas precisam ser revisadas?" — não edite sem confirmação.

**C.5. Update indices:**
- `Products/Crédito-Rural/WikiCR/WikiCR.md` ou `Products/Fomento/WikiF/WikiF.md` — adicionar/atualizar linha
- Se substituiu uma norma anterior, atualizar a frontmatter `substituido_por` da página antiga

---

### Step 3: Git Commit & Push

Stage all created/modified files. Use this commit format:

```
ingest-business: <branch> — <document subject>

- <path 1> (created|updated)
- <path 2> (created|updated)
```

`<branch>` is one of `personal`, `corporate`, `edital-fomento`, `regulatory`.

Push to remote.

## Quality Guidelines

- **Never write to `Wiki/`** from this skill. The Wiki is fed by `/ingest` and friends.
- **Never modify `Sources/`** — that is the immutable raw layer for the knowledge pipeline.
- Preserve original filenames where readable and sensible; otherwise rename consistently with siblings in the same folder.
- Brazilian formatting throughout: monetary `R$ X.XXX.XXX,XX`, datas no corpo `DD/MM/YYYY`, frontmatter ISO.
- For documents with PII (CPF, RG, dados bancários), do not paste the raw numbers into wiki-link descriptions or commit messages — keep them inside the structured note where they are expected.
- DOCX and scanned/encrypted PDFs that cannot be read: still file the attachment, fill metadata from filename + user input, and flag what could not be extracted.
- When a document obsoletes another (alteração contratual substitui contrato social, nova CNH substitui anterior), keep both — mark the older as `status: superseded` in its row and add a wiki-link from old → new.

## Notes

- This skill is owned jointly by **Katrina** (process design) and **Bob** (vault organization). Katrina drives flows that touch operational structure (Areas, Products, indices, cross-links to bank cadastros). Bob drives flows that demand strict adherence to vault conventions (frontmatter, naming, índices).
- Cross-reference with `/ingest-call` when an edital straddles fomento + R&D — file the primary copy in one location and add a wiki-link from the other.
- Cross-reference with `/update-mcr` for monthly MCR sync — Branch C should consult the latest MCR version before claiming a rule is current.
