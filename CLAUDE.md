# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

Not a software project. It holds organizational and business documents (written in Spanish) for **Yachay Research Associates LLC**, a binational USA–Peru consultancy in health analytics (HEOR, RWE, clinical trial statistics, data engineering) serving pharma/biotech/CROs and NGOs in Latin America.

Documents are authored in Quarto (`.qmd`), Markdown, and LaTeX (the MOF); PDFs and HTML files are rendered outputs.

## Source vs. generated files

| Source | Rendered output |
|---|---|
| `MOF/MOF_v1.tex` + `MOF/preamble/preambulo.tex` — Manual de Organización y Funciones (LaTeX; el preámbulo contiene paquetes, colores de marca y metadatos del título) | `MOF/MOF_v1.pdf` |
| `pitch-deck/pitch_deck_revealjs_quarto.qmd` — pitch deck (renders to revealjs HTML, tema `pitch-deck/yachay.scss`) | `pitch-deck/pitch_deck_revealjs_quarto.html`, `pitch-deck/pitch_deck_revealjs_quarto_files/` |
| `branding/01-04_*.md`, `branding/brand_board.html` (hand-authored), `branding/assets/*.svg` — identidad visual v1 (sistema "Telar") | `branding/assets/logo_*_contornos.svg` y `master_yachay.svg` se regeneran con `branding/scripts/generar_contornos.py` |

**MOF: la fuente de verdad es el `.tex`.** El antiguo `MOF_v1.qmd` fue eliminado (decisión 2026-07-17; recuperable del historial de git). No recrear un `.qmd` del MOF ni renderizarlo con Quarto: pisaría `MOF_v1.tex` y destruiría la estructura dividida con `preamble/`.

Edit only the sources listed above. Never hand-edit `.pdf`, generated `.html`, or anything under `*_files/` — regenerate them instead. (`branding/brand_board.html` es fuente escrita a mano, no salida generada.)

## Commands

There is no `_quarto.yml` project file; each Quarto document carries its own `format:` configuration in YAML frontmatter and is rendered individually:

```bash
latexmk -xelatex -cd MOF/MOF_v1.tex           # MOF PDF (XeLaTeX obligatorio: pdfLaTeX falla por un carácter U+2194)
quarto render pitch-deck/pitch_deck_revealjs_quarto.qmd  # revealjs slides
quarto preview pitch-deck/pitch_deck_revealjs_quarto.qmd # live-reload preview while editing
```

## Conventions

- All documents are in Spanish (`lang: es` where set in frontmatter); keep new content and edits in Spanish.
- Business/domain terms kept in English where the industry uses them (RWE, HEOR, SoW, QA/QC, retainer, pipeline) — follow the existing mix.
- The MOF frontmatter sets `execute: echo: false` — documents are prose-first; any embedded code chunks should not display their source in output.
