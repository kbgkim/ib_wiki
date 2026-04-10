# [Feature Name] Implementation Plan: IB Wiki Foundations

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Establish the foundational Markdown structure and core domain knowledge (NPL, PF, Equity, ABS) for the IB Wiki.

**Architecture:** Markdown-First repository centered on asset-class modularity and cross-domain integration logic.

**Tech Stack:** Markdown, Git.

---

### Task 1: Scaffolding & Plan Persistence
**Files:**
- Create: `/home/kbgkim/antigravity/projects/ib_wiki/src/99_System/plans/2026-04-10-ib-wiki-foundations.md`
- Create: `/home/kbgkim/antigravity/projects/ib_wiki/src/01_Foundations/.gitkeep`
- Create: `/home/kbgkim/antigravity/projects/ib_wiki/src/02_Integrated_IB/.gitkeep`
- Create: `/home/kbgkim/antigravity/projects/ib_wiki/src/03_Assets_Verticals/NPL/.gitkeep`
- Create: `/home/kbgkim/antigravity/projects/ib_wiki/src/03_Assets_Verticals/PF/.gitkeep`
- Create: `/home/kbgkim/antigravity/projects/ib_wiki/src/03_Assets_Verticals/Equity/.gitkeep`
- Create: `/home/kbgkim/antigravity/projects/ib_wiki/src/03_Assets_Verticals/ABS/.gitkeep`

- [x] **Step 1: Create directory hierarchy**
    Run: `mkdir -p /home/kbgkim/antigravity/projects/ib_wiki/src/{01_Foundations,02_Integrated_IB,03_Assets_Verticals/{NPL,PF,Equity,ABS},99_System/plans}`
- [ ] **Step 2: Write this plan to the project directory**
    Save the content of this artifact to `/home/kbgkim/antigravity/projects/ib_wiki/src/99_System/plans/2026-04-10-ib-wiki-foundations.md`.
- [ ] **Step 3: Commit the initial structure**
    Run: `git init /home/kbgkim/antigravity/projects/ib_wiki && git add . && git commit -m "chore: initial wiki scaffold"`

### Task 2: Foundational Ingestion - IB Basics & ABS
**Files:**
- Create: `/home/kbgkim/antigravity/projects/ib_wiki/src/01_Foundations/IB_Overview.md`
- Create: `/home/kbgkim/antigravity/projects/ib_wiki/src/03_Assets_Verticals/ABS/Basics.md`

- [ ] **Step 1: Write IB General Overview**
    Focus on the role of IB in capital markets and the integration of structured finance.
- [ ] **Step 2: Write ABS Core Concepts**
    Detail Securitization, SPVs, and Credit Enhancement.

### Task 3: Domain Ingestion - NPL & PF
**Files:**
- Create: `/home/kbgkim/antigravity/projects/ib_wiki/src/03_Assets_Verticals/NPL/Basics.md`
- Create: `/home/kbgkim/antigravity/projects/ib_wiki/src/03_Assets_Verticals/PF/Basics.md`

- [ ] **Step 1: Write NPL Evaluation & Recovery strategies**
- [ ] **Step 2: Write PF Structural Risk & Cash Flow modeling**

### Task 4: Integration Logic - "The Synthesis"
**Files:**
- Create: `/home/kbgkim/antigravity/projects/ib_wiki/src/02_Integrated_IB/Synthesis_Map.md`

- [ ] **Step 1: Map the lifecycle of a stressed PF asset becoming an NPL and its eventual exit via ABS or Equity recapitalization.**
