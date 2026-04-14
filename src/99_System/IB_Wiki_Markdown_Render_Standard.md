You are working on an IB (Investment Banking) Risk Wiki written in Markdown.

The system currently has a critical problem:
Markdown documents are visually splitting, fragmenting, or rendering inconsistently due to structural conflicts between Markdown block elements and the renderer.

Your task is to FIX STRUCTURAL CONSISTENCY while preserving ALL financial meaning.

────────────────────────────────────
## 🎯 PRIMARY GOAL

Create a unified Markdown structure standard so that:

1. Each document renders as a single continuous page
2. No visual or logical fragmentation occurs
3. No HTML-like splitting or renderer misinterpretation happens
4. All financial logic (PD, LGD, EAD, Cashflow, Risk models) remains unchanged
5. Korean terminology is primary with English in parentheses

────────────────────────────────────
## 🚨 ABSOLUTE CONSTRAINTS (DO NOT VIOLATE)

### 1. Remove ALL horizontal rules
Delete:
- ---
- ***
- ___

Replace with:
- blank line OR "### ─────────────"

---

### 2. Remove ALL callouts
Delete:
> [!NOTE]
> [!IMPORTANT]

Replace with:
### NOTE
### IMPORTANT

---

### 3. Mermaid isolation rule
Every Mermaid block MUST:

- be in its own section
- NOT be adjacent to tables or lists
- have blank lines before and after

---

### 4. Table isolation rule
Every table MUST:

- have a blank line before
- have a blank line after
- NOT be adjacent to mermaid or lists

---

### 5. NO mixed block sections
Never combine in the same section:
- table + mermaid
- list + table
- callout + code block

Each must be separated into independent sections.

---

### 6. Heading discipline
Allowed structure:

# Document Title
## Section
### Subsection

Do NOT exceed 3 levels unless absolutely required.

---

### 7. No semantic rewriting
DO NOT change:
- financial formulas (PD, LGD, EAD, EL)
- definitions of PF / NPL / ABS / Equity
- Cashflow logic
- Risk architecture

ONLY fix formatting and structure.

────────────────────────────────────
## 🧠 CORE DESIGN PRINCIPLE

The root cause of fragmentation is:

> Markdown block boundary ambiguity in renderer interpretation.

Therefore the solution is:

✔ isolate every block element
✔ enforce spacing rules
✔ eliminate structural conflicts
✔ enforce deterministic layout

────────────────────────────────────
## 📦 OUTPUT REQUIREMENTS

For every document:

1. Return FULL corrected Markdown file
2. Ensure it renders as a SINGLE continuous document
3. Ensure no visual segmentation occurs in any Markdown renderer
4. Keep IB Risk model semantics unchanged

────────────────────────────────────
## 📚 APPLY TO ALL DOCUMENTS

Apply this standard to:

- IB Risk Data Model
- PF Mapping
- NPL Mapping
- ABS Mapping
- Equity Mapping
- Cashflow Schema
- Deal Schema
- Position Schema
- Risk Result Schema
- PD / LGD / EAD definitions

────────────────────────────────────
## 🎯 FINAL GOAL

A unified IB Risk Wiki where:

- all documents are structurally consistent
- rendering is deterministic
- no Markdown fragmentation occurs
- system is ready for production-grade financial documentation use