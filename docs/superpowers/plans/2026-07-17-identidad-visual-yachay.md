# Identidad Visual Yachay — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Producir los archivos definitivos de la identidad visual de Yachay: SVGs del sistema de logo, archivos vectoriales editables para diseñadores (contornos + lienzo maestro), favicon, brand board HTML, tema Quarto revealjs y colores LaTeX del MOF.

**Architecture:** Activos SVG con la geometría exacta del spec en `branding/assets/`; un script Python reproducible (fonttools + uharfbuzz) convierte el wordmark a contornos y ensambla un lienzo maestro para Figma/Illustrator; un brand board HTML autocontenido sirve de manual v1; un tema scss para revealjs y variables LaTeX aplican la marca a los documentos Quarto existentes. Sin build system — la "suite de pruebas" es validación XML (`xmllint`), greps de contenido, renders de Quarto y verificación visual.

**Tech Stack:** SVG 1.1, HTML/CSS standalone, Python 3 (fonttools, uharfbuzz, en venv `.superpowers/venv-branding`), Quarto (revealjs scss + PDF LaTeX), Google Fonts (Source Serif 4, Source Sans 3, JetBrains Mono).

## Global Constraints

- Spec fuente: `docs/superpowers/specs/2026-07-17-identidad-visual-yachay-design.md` — geometría y colores se copian de ahí **verbatim**.
- Paleta exacta: azul petróleo `#1B4965`, azul acero `#5FA8D3`, ámbar andino `#E8A13D`, gris pizarra `#2E3440`, hueso `#F7F5F0`, azul niebla `#5F7A8C`; descriptor sobre fondo oscuro `#9DC3DA`.
- Ámbar ≤10% de cualquier pieza; en versiones inversas el ámbar y el azul acero NO cambian.
- Fuentes: Source Serif 4 (600) títulos/marca, Source Sans 3 (400/600) cuerpo, JetBrains Mono código. Solo Google Fonts.
- Textos de documentos en español; términos de industria en inglés (convención del repo, CLAUDE.md).
- Editar solo fuentes; jamás editar a mano salidas renderizadas (`.html`/`.pdf` generados y `*_files/`) — se regeneran con `quarto render`.
- Commits: mensaje en español; trailer con dos flags `-m` separados (el shell es zsh y los mensajes multilínea entre comillas dobles fallan): `git commit -m 'mensaje' -m 'Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>'`.
- El árbol tiene una reorganización de carpetas sin commitear ajena a este plan — `git add` siempre con rutas explícitas, nunca `git add -A` ni `git add .`.

---

### Task 1: Símbolo "Telar" (3 SVGs)

**Files:**
- Create: `branding/assets/simbolo.svg`
- Create: `branding/assets/simbolo_inverso.svg`
- Create: `branding/assets/simbolo_mono.svg`

**Interfaces:**
- Produces: la geometría Telar canónica (viewBox `0 0 120 120`, 6 líneas + 6 círculos) que las Tasks 3, 4, 5 y 6 reutilizan copiándola tal cual.

- [ ] **Step 1: Crear `branding/assets/simbolo.svg`**

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" role="img" aria-labelledby="titulo-simbolo">
  <title id="titulo-simbolo">Yachay — símbolo Telar</title>
  <line x1="14" y1="18" x2="106" y2="18" stroke="#1B4965" stroke-width="5" stroke-linecap="round"/>
  <line x1="25" y1="18" x2="25" y2="76" stroke="#5FA8D3" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="95" y1="18" x2="95" y2="68" stroke="#5FA8D3" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="43" y1="18" x2="60" y2="62" stroke="#1B4965" stroke-width="3.2"/>
  <line x1="77" y1="18" x2="60" y2="62" stroke="#1B4965" stroke-width="3.2"/>
  <line x1="60" y1="62" x2="60" y2="102" stroke="#1B4965" stroke-width="3.2" stroke-linecap="round"/>
  <circle cx="25" cy="48" r="4" fill="#5FA8D3"/>
  <circle cx="95" cy="42" r="4" fill="#5FA8D3"/>
  <circle cx="51" cy="39" r="4.5" fill="#1B4965"/>
  <circle cx="69" cy="39" r="4.5" fill="#1B4965"/>
  <circle cx="60" cy="62" r="6.5" fill="#E8A13D"/>
  <circle cx="60" cy="84" r="4.5" fill="#1B4965"/>
</svg>
```

- [ ] **Step 2: Crear `branding/assets/simbolo_inverso.svg`** (fondos oscuros: petróleo→hueso; acero y ámbar sin cambio)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" role="img" aria-labelledby="titulo-simbolo-inv">
  <title id="titulo-simbolo-inv">Yachay — símbolo Telar (inverso)</title>
  <line x1="14" y1="18" x2="106" y2="18" stroke="#F7F5F0" stroke-width="5" stroke-linecap="round"/>
  <line x1="25" y1="18" x2="25" y2="76" stroke="#5FA8D3" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="95" y1="18" x2="95" y2="68" stroke="#5FA8D3" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="43" y1="18" x2="60" y2="62" stroke="#F7F5F0" stroke-width="3.2"/>
  <line x1="77" y1="18" x2="60" y2="62" stroke="#F7F5F0" stroke-width="3.2"/>
  <line x1="60" y1="62" x2="60" y2="102" stroke="#F7F5F0" stroke-width="3.2" stroke-linecap="round"/>
  <circle cx="25" cy="48" r="4" fill="#5FA8D3"/>
  <circle cx="95" cy="42" r="4" fill="#5FA8D3"/>
  <circle cx="51" cy="39" r="4.5" fill="#F7F5F0"/>
  <circle cx="69" cy="39" r="4.5" fill="#F7F5F0"/>
  <circle cx="60" cy="62" r="6.5" fill="#E8A13D"/>
  <circle cx="60" cy="84" r="4.5" fill="#F7F5F0"/>
</svg>
```

- [ ] **Step 3: Crear `branding/assets/simbolo_mono.svg`** (una tinta: recolorear editando `style` del root)

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" style="color:#1B4965" role="img" aria-labelledby="titulo-simbolo-mono">
  <title id="titulo-simbolo-mono">Yachay — símbolo Telar (monocromo)</title>
  <line x1="14" y1="18" x2="106" y2="18" stroke="currentColor" stroke-width="5" stroke-linecap="round"/>
  <line x1="25" y1="18" x2="25" y2="76" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="95" y1="18" x2="95" y2="68" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/>
  <line x1="43" y1="18" x2="60" y2="62" stroke="currentColor" stroke-width="3.2"/>
  <line x1="77" y1="18" x2="60" y2="62" stroke="currentColor" stroke-width="3.2"/>
  <line x1="60" y1="62" x2="60" y2="102" stroke="currentColor" stroke-width="3.2" stroke-linecap="round"/>
  <circle cx="25" cy="48" r="4" fill="currentColor"/>
  <circle cx="95" cy="42" r="4" fill="currentColor"/>
  <circle cx="51" cy="39" r="4.5" fill="currentColor"/>
  <circle cx="69" cy="39" r="4.5" fill="currentColor"/>
  <circle cx="60" cy="62" r="6.5" fill="currentColor"/>
  <circle cx="60" cy="84" r="4.5" fill="currentColor"/>
</svg>
```

- [ ] **Step 4: Validar XML**

Run: `xmllint --noout branding/assets/simbolo.svg branding/assets/simbolo_inverso.svg branding/assets/simbolo_mono.svg && echo OK`
Expected: `OK`

- [ ] **Step 5: Verificación visual**

Run: `open branding/assets/simbolo.svg`
Confirmar: cuerda madre arriba, dos laterales celestes con nudo, Y central azul con nudo ámbar en la unión.

- [ ] **Step 6: Commit**

```bash
git add branding/assets/simbolo.svg branding/assets/simbolo_inverso.svg branding/assets/simbolo_mono.svg
git commit -m 'Agregar símbolo Telar en SVG (normal, inverso, monocromo)' -m 'Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>'
```

---

### Task 2: Marca mínima "Cascada" y favicon (4 SVGs)

**Files:**
- Create: `branding/assets/marca_minima.svg`
- Create: `branding/assets/marca_minima_inverso.svg`
- Create: `branding/assets/marca_minima_mono.svg`
- Create: `branding/assets/favicon.svg`

**Interfaces:**
- Produces: geometría Cascada (5 elementos) que Task 4 reutiliza en el lienzo maestro; `favicon.svg` para uso web.

- [ ] **Step 1: Crear `branding/assets/marca_minima.svg`**

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" role="img" aria-labelledby="titulo-minima">
  <title id="titulo-minima">Yachay — marca mínima Cascada</title>
  <line x1="18" y1="18" x2="102" y2="18" stroke="#1B4965" stroke-width="7" stroke-linecap="round"/>
  <line x1="38" y1="18" x2="60" y2="58" stroke="#1B4965" stroke-width="6"/>
  <line x1="82" y1="18" x2="60" y2="58" stroke="#1B4965" stroke-width="6"/>
  <line x1="60" y1="58" x2="60" y2="100" stroke="#1B4965" stroke-width="6" stroke-linecap="round"/>
  <circle cx="60" cy="58" r="11" fill="#E8A13D"/>
</svg>
```

- [ ] **Step 2: Crear `branding/assets/marca_minima_inverso.svg`**

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" role="img" aria-labelledby="titulo-minima-inv">
  <title id="titulo-minima-inv">Yachay — marca mínima Cascada (inverso)</title>
  <line x1="18" y1="18" x2="102" y2="18" stroke="#F7F5F0" stroke-width="7" stroke-linecap="round"/>
  <line x1="38" y1="18" x2="60" y2="58" stroke="#F7F5F0" stroke-width="6"/>
  <line x1="82" y1="18" x2="60" y2="58" stroke="#F7F5F0" stroke-width="6"/>
  <line x1="60" y1="58" x2="60" y2="100" stroke="#F7F5F0" stroke-width="6" stroke-linecap="round"/>
  <circle cx="60" cy="58" r="11" fill="#E8A13D"/>
</svg>
```

- [ ] **Step 3: Crear `branding/assets/marca_minima_mono.svg`**

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" style="color:#1B4965" role="img" aria-labelledby="titulo-minima-mono">
  <title id="titulo-minima-mono">Yachay — marca mínima Cascada (monocromo)</title>
  <line x1="18" y1="18" x2="102" y2="18" stroke="currentColor" stroke-width="7" stroke-linecap="round"/>
  <line x1="38" y1="18" x2="60" y2="58" stroke="currentColor" stroke-width="6"/>
  <line x1="82" y1="18" x2="60" y2="58" stroke="currentColor" stroke-width="6"/>
  <line x1="60" y1="58" x2="60" y2="100" stroke="currentColor" stroke-width="6" stroke-linecap="round"/>
  <circle cx="60" cy="58" r="11" fill="currentColor"/>
</svg>
```

- [ ] **Step 4: Crear el favicon (copia exacta)**

Run: `cp branding/assets/marca_minima.svg branding/assets/favicon.svg`

- [ ] **Step 5: Validar XML y legibilidad a 16px**

Run: `xmllint --noout branding/assets/marca_minima.svg branding/assets/marca_minima_inverso.svg branding/assets/marca_minima_mono.svg branding/assets/favicon.svg && echo OK`
Expected: `OK`
Luego `open branding/assets/favicon.svg` y reducir el zoom para confirmar que la Y y el nudo ámbar se distinguen pequeños.

- [ ] **Step 6: Commit**

```bash
git add branding/assets/marca_minima.svg branding/assets/marca_minima_inverso.svg branding/assets/marca_minima_mono.svg branding/assets/favicon.svg
git commit -m 'Agregar marca mínima Cascada y favicon en SVG' -m 'Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>'
```

---

### Task 3: Lockups horizontal y apilado (6 SVGs)

**Files:**
- Create: `branding/assets/logo_horizontal.svg`, `branding/assets/logo_horizontal_inverso.svg`, `branding/assets/logo_horizontal_mono.svg`
- Create: `branding/assets/logo_apilado.svg`, `branding/assets/logo_apilado_inverso.svg`, `branding/assets/logo_apilado_mono.svg`

**Interfaces:**
- Consumes: geometría Telar de Task 1 (copiada dentro de cada archivo — los SVG standalone no referencian archivos externos de forma portable).
- Produces: lockups con wordmark `<text>` editable; Task 5 los embebe en el brand board. La versión sin fuentes (contornos) la genera Task 4.

- [ ] **Step 1: Crear `branding/assets/logo_horizontal.svg`**

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 345 120" role="img" aria-labelledby="titulo-lockup-h">
  <title id="titulo-lockup-h">Yachay Research Associates — logo horizontal</title>
  <g id="simbolo">
    <line x1="14" y1="18" x2="106" y2="18" stroke="#1B4965" stroke-width="5" stroke-linecap="round"/>
    <line x1="25" y1="18" x2="25" y2="76" stroke="#5FA8D3" stroke-width="2.5" stroke-linecap="round"/>
    <line x1="95" y1="18" x2="95" y2="68" stroke="#5FA8D3" stroke-width="2.5" stroke-linecap="round"/>
    <line x1="43" y1="18" x2="60" y2="62" stroke="#1B4965" stroke-width="3.2"/>
    <line x1="77" y1="18" x2="60" y2="62" stroke="#1B4965" stroke-width="3.2"/>
    <line x1="60" y1="62" x2="60" y2="102" stroke="#1B4965" stroke-width="3.2" stroke-linecap="round"/>
    <circle cx="25" cy="48" r="4" fill="#5FA8D3"/>
    <circle cx="95" cy="42" r="4" fill="#5FA8D3"/>
    <circle cx="51" cy="39" r="4.5" fill="#1B4965"/>
    <circle cx="69" cy="39" r="4.5" fill="#1B4965"/>
    <circle cx="60" cy="62" r="6.5" fill="#E8A13D"/>
    <circle cx="60" cy="84" r="4.5" fill="#1B4965"/>
  </g>
  <text x="138" y="64" font-family="Source Serif 4, Georgia, serif" font-weight="600" font-size="46" fill="#1B4965">Yachay</text>
  <text x="140" y="86" font-family="Source Sans 3, Helvetica Neue, Arial, sans-serif" font-weight="600" font-size="11.5" letter-spacing="2.5" fill="#5F7A8C">RESEARCH ASSOCIATES</text>
</svg>
```

- [ ] **Step 2: Crear `branding/assets/logo_horizontal_inverso.svg`** — igual que Step 1 con estos reemplazos exactos: todos los `#1B4965` → `#F7F5F0` (incluido el fill del wordmark); el fill del descriptor `#5F7A8C` → `#9DC3DA`; `#5FA8D3` y `#E8A13D` sin cambio; ids → `titulo-lockup-h-inv`; título "Yachay Research Associates — logo horizontal (inverso)".

- [ ] **Step 3: Crear `branding/assets/logo_horizontal_mono.svg`** — igual que Step 1 con: root con atributo `style="color:#1B4965"`; TODOS los valores de `stroke` y `fill` (líneas, círculos y ambos `<text>`) → `currentColor`; ids → `titulo-lockup-h-mono`; título "… logo horizontal (monocromo)".

- [ ] **Step 4: Crear `branding/assets/logo_apilado.svg`**

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 200" role="img" aria-labelledby="titulo-lockup-a">
  <title id="titulo-lockup-a">Yachay Research Associates — logo apilado</title>
  <g id="simbolo" transform="translate(60,0)">
    <line x1="14" y1="18" x2="106" y2="18" stroke="#1B4965" stroke-width="5" stroke-linecap="round"/>
    <line x1="25" y1="18" x2="25" y2="76" stroke="#5FA8D3" stroke-width="2.5" stroke-linecap="round"/>
    <line x1="95" y1="18" x2="95" y2="68" stroke="#5FA8D3" stroke-width="2.5" stroke-linecap="round"/>
    <line x1="43" y1="18" x2="60" y2="62" stroke="#1B4965" stroke-width="3.2"/>
    <line x1="77" y1="18" x2="60" y2="62" stroke="#1B4965" stroke-width="3.2"/>
    <line x1="60" y1="62" x2="60" y2="102" stroke="#1B4965" stroke-width="3.2" stroke-linecap="round"/>
    <circle cx="25" cy="48" r="4" fill="#5FA8D3"/>
    <circle cx="95" cy="42" r="4" fill="#5FA8D3"/>
    <circle cx="51" cy="39" r="4.5" fill="#1B4965"/>
    <circle cx="69" cy="39" r="4.5" fill="#1B4965"/>
    <circle cx="60" cy="62" r="6.5" fill="#E8A13D"/>
    <circle cx="60" cy="84" r="4.5" fill="#1B4965"/>
  </g>
  <text x="120" y="156" text-anchor="middle" font-family="Source Serif 4, Georgia, serif" font-weight="600" font-size="40" fill="#1B4965">Yachay</text>
  <text x="120" y="178" text-anchor="middle" font-family="Source Sans 3, Helvetica Neue, Arial, sans-serif" font-weight="600" font-size="10.5" letter-spacing="2.3" fill="#5F7A8C">RESEARCH ASSOCIATES</text>
</svg>
```

- [ ] **Step 5: Crear `branding/assets/logo_apilado_inverso.svg`** — igual que Step 4 con los reemplazos de Step 2 (ids → `titulo-lockup-a-inv`, título "… logo apilado (inverso)").

- [ ] **Step 6: Crear `branding/assets/logo_apilado_mono.svg`** — igual que Step 4 con los reemplazos de Step 3 (ids → `titulo-lockup-a-mono`, título "… logo apilado (monocromo)").

- [ ] **Step 7: Validar y verificar**

Run: `xmllint --noout branding/assets/logo_horizontal.svg branding/assets/logo_horizontal_inverso.svg branding/assets/logo_horizontal_mono.svg branding/assets/logo_apilado.svg branding/assets/logo_apilado_inverso.svg branding/assets/logo_apilado_mono.svg && echo OK`
Expected: `OK`
Luego `open branding/assets/logo_horizontal.svg branding/assets/logo_apilado.svg` — proporción símbolo≈1.8× wordmark, descriptor alineado, apilado centrado.

- [ ] **Step 8: Commit**

```bash
git add branding/assets/logo_horizontal.svg branding/assets/logo_horizontal_inverso.svg branding/assets/logo_horizontal_mono.svg branding/assets/logo_apilado.svg branding/assets/logo_apilado_inverso.svg branding/assets/logo_apilado_mono.svg
git commit -m 'Agregar lockups horizontal y apilado en SVG (normal, inverso, monocromo)' -m 'Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>'
```

---

### Task 4: Vectorizado para diseño humano — contornos y lienzo maestro

**Files:**
- Create: `branding/scripts/generar_contornos.py`
- Create (generados por el script): `branding/assets/logo_horizontal_contornos.svg`, `branding/assets/logo_apilado_contornos.svg`, `branding/assets/master_yachay.svg`

**Interfaces:**
- Consumes: geometría Telar (Task 1) y Cascada (Task 2), replicadas dentro del script.
- Produces: `texto_a_path(ttf, texto, font_size, letter_spacing=0.0) -> tuple[str, float]` (path SVG y ancho en px, origen en la línea base); los tres SVG generados, sin ningún `<text>`, editables en Figma/Illustrator/Inkscape.

- [ ] **Step 1: Crear venv e instalar dependencias**

```bash
python3 -m venv .superpowers/venv-branding
.superpowers/venv-branding/bin/pip -q install fonttools uharfbuzz
.superpowers/venv-branding/bin/python -c 'import fontTools, uharfbuzz; print("deps OK")'
```
Expected: `deps OK`

- [ ] **Step 2: Descargar fuentes variables e instanciarlas al peso 600**

```bash
FDIR="${TMPDIR:-/tmp}/yachay_fonts" && mkdir -p "$FDIR" \
&& curl -Lso "$FDIR/serif-var.ttf" 'https://github.com/google/fonts/raw/main/ofl/sourceserif4/SourceSerif4%5Bopsz%2Cwght%5D.ttf' \
&& curl -Lso "$FDIR/sans-var.ttf" 'https://github.com/google/fonts/raw/main/ofl/sourcesans3/SourceSans3%5Bwght%5D.ttf' \
&& .superpowers/venv-branding/bin/python -m fontTools.varLib.instancer "$FDIR/serif-var.ttf" opsz=40 wght=600 -o "$FDIR/serif600.ttf" \
&& .superpowers/venv-branding/bin/python -m fontTools.varLib.instancer "$FDIR/sans-var.ttf" wght=600 -o "$FDIR/sans600.ttf" \
&& ls "$FDIR"
```
Expected: listado con `serif600.ttf` y `sans600.ttf`. (Las fuentes quedan fuera del repo — licencia OFL, pero no las versionamos; el script las toma del directorio temporal.)

- [ ] **Step 3: Crear `branding/scripts/generar_contornos.py`**

```python
#!/usr/bin/env python3
"""Genera los SVG con wordmark en contornos y el lienzo maestro editable.

Salidas (en branding/assets/):
  - logo_horizontal_contornos.svg
  - logo_apilado_contornos.svg
  - master_yachay.svg  (todas las versiones en un lienzo, para Figma/Illustrator)

Uso: .superpowers/venv-branding/bin/python branding/scripts/generar_contornos.py <dir_fuentes>
     <dir_fuentes> debe contener serif600.ttf (Source Serif 4 wght=600, opsz=40)
     y sans600.ttf (Source Sans 3 wght=600).
"""
import sys
from pathlib import Path

import uharfbuzz as hb
from fontTools.misc.transform import Transform
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

ASSETS = Path(__file__).resolve().parent.parent / "assets"
PETROLEO, ACERO, AMBAR = "#1B4965", "#5FA8D3", "#E8A13D"
HUESO, NIEBLA, NIEBLA_INV, PIZARRA = "#F7F5F0", "#5F7A8C", "#9DC3DA", "#2E3440"


def texto_a_path(ttf, texto, font_size, letter_spacing=0.0):
    """Contornea `texto` con shaping real. Devuelve (path_d, ancho_px); origen (0,0) en la línea base."""
    data = Path(ttf).read_bytes()
    face = hb.Face(data)
    fuente = hb.Font(face)
    upem = face.upem
    fuente.scale = (upem, upem)
    buf = hb.Buffer()
    buf.add_str(texto)
    buf.guess_segment_properties()
    hb.shape(fuente, buf)
    tt = TTFont(ttf)
    glifos = tt.getGlyphSet()
    orden = tt.getGlyphOrder()
    s = font_size / upem
    x, partes = 0.0, []
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        pen = SVGPathPen(glifos)
        tpen = TransformPen(pen, Transform(s, 0, 0, -s, x + pos.x_offset * s, -pos.y_offset * s))
        glifos[orden[info.codepoint]].draw(tpen)
        cmds = pen.getCommands()
        if cmds:
            partes.append(cmds)
        x += pos.x_advance * s + letter_spacing
    return " ".join(partes), x - letter_spacing


def simbolo_telar(principal=PETROLEO):
    return f'''<line x1="14" y1="18" x2="106" y2="18" stroke="{principal}" stroke-width="5" stroke-linecap="round"/>
    <line x1="25" y1="18" x2="25" y2="76" stroke="{ACERO}" stroke-width="2.5" stroke-linecap="round"/>
    <line x1="95" y1="18" x2="95" y2="68" stroke="{ACERO}" stroke-width="2.5" stroke-linecap="round"/>
    <line x1="43" y1="18" x2="60" y2="62" stroke="{principal}" stroke-width="3.2"/>
    <line x1="77" y1="18" x2="60" y2="62" stroke="{principal}" stroke-width="3.2"/>
    <line x1="60" y1="62" x2="60" y2="102" stroke="{principal}" stroke-width="3.2" stroke-linecap="round"/>
    <circle cx="25" cy="48" r="4" fill="{ACERO}"/>
    <circle cx="95" cy="42" r="4" fill="{ACERO}"/>
    <circle cx="51" cy="39" r="4.5" fill="{principal}"/>
    <circle cx="69" cy="39" r="4.5" fill="{principal}"/>
    <circle cx="60" cy="62" r="6.5" fill="{AMBAR}"/>
    <circle cx="60" cy="84" r="4.5" fill="{principal}"/>'''


def cascada(principal=PETROLEO):
    return f'''<line x1="18" y1="18" x2="102" y2="18" stroke="{principal}" stroke-width="7" stroke-linecap="round"/>
    <line x1="38" y1="18" x2="60" y2="58" stroke="{principal}" stroke-width="6"/>
    <line x1="82" y1="18" x2="60" y2="58" stroke="{principal}" stroke-width="6"/>
    <line x1="60" y1="58" x2="60" y2="100" stroke="{principal}" stroke-width="6" stroke-linecap="round"/>
    <circle cx="60" cy="58" r="11" fill="{AMBAR}"/>'''


def main(dir_fuentes):
    serif = Path(dir_fuentes) / "serif600.ttf"
    sans = Path(dir_fuentes) / "sans600.ttf"
    yachay46, _ = texto_a_path(serif, "Yachay", 46)
    desc115, _ = texto_a_path(sans, "RESEARCH ASSOCIATES", 11.5, letter_spacing=2.5)
    yachay40, ancho40 = texto_a_path(serif, "Yachay", 40)
    desc105, ancho105 = texto_a_path(sans, "RESEARCH ASSOCIATES", 10.5, letter_spacing=2.3)

    horizontal = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 345 120">
  <title>Yachay Research Associates — logo horizontal (contornos)</title>
  <g id="simbolo">
    {simbolo_telar()}
  </g>
  <path id="wordmark" transform="translate(138,64)" d="{yachay46}" fill="{PETROLEO}"/>
  <path id="descriptor" transform="translate(140,86)" d="{desc115}" fill="{NIEBLA}"/>
</svg>
'''
    apilado = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 200">
  <title>Yachay Research Associates — logo apilado (contornos)</title>
  <g id="simbolo" transform="translate(60,0)">
    {simbolo_telar()}
  </g>
  <path id="wordmark" transform="translate({120 - ancho40 / 2:.1f},156)" d="{yachay40}" fill="{PETROLEO}"/>
  <path id="descriptor" transform="translate({120 - ancho105 / 2:.1f},178)" d="{desc105}" fill="{NIEBLA}"/>
</svg>
'''
    swatches = ""
    for i, (nombre, hexcolor) in enumerate([
        ("petroleo", PETROLEO), ("acero", ACERO), ("ambar", AMBAR),
        ("pizarra", PIZARRA), ("hueso", HUESO), ("niebla", NIEBLA),
    ]):
        x = 60 + i * 110
        borde = f' stroke="{PIZARRA}" stroke-width="1"' if hexcolor == HUESO else ""
        swatches += f'    <rect id="swatch-{nombre}" x="{x}" y="540" width="90" height="90" rx="8" fill="{hexcolor}"{borde}/>\n'

    master = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680">
  <title>Yachay — lienzo maestro (todas las versiones, contornos)</title>
  <rect width="1100" height="680" fill="{HUESO}"/>
  <g id="lockup-horizontal" transform="translate(40,50)">
    <g>
      {simbolo_telar()}
    </g>
    <path transform="translate(138,64)" d="{yachay46}" fill="{PETROLEO}"/>
    <path transform="translate(140,86)" d="{desc115}" fill="{NIEBLA}"/>
  </g>
  <g id="lockup-apilado" transform="translate(480,30)">
    <g transform="translate(60,0)">
      {simbolo_telar()}
    </g>
    <path transform="translate({120 - ancho40 / 2:.1f},156)" d="{yachay40}" fill="{PETROLEO}"/>
    <path transform="translate({120 - ancho105 / 2:.1f},178)" d="{desc105}" fill="{NIEBLA}"/>
  </g>
  <g id="simbolo-solo" transform="translate(800,60)">
    {simbolo_telar()}
  </g>
  <g id="marca-minima" transform="translate(960,60)">
    {cascada()}
  </g>
  <g id="panel-inverso">
    <rect x="40" y="280" width="1020" height="220" rx="10" fill="{PETROLEO}"/>
    <g transform="translate(90,330)">
      <g>
        {simbolo_telar(HUESO)}
      </g>
      <path transform="translate(138,64)" d="{yachay46}" fill="{HUESO}"/>
      <path transform="translate(140,86)" d="{desc115}" fill="{NIEBLA_INV}"/>
    </g>
    <g transform="translate(560,330)">
      {simbolo_telar(HUESO)}
    </g>
    <g transform="translate(730,330)">
      {cascada(HUESO)}
    </g>
  </g>
  <g id="paleta">
{swatches}  </g>
</svg>
'''
    (ASSETS / "logo_horizontal_contornos.svg").write_text(horizontal, encoding="utf-8")
    (ASSETS / "logo_apilado_contornos.svg").write_text(apilado, encoding="utf-8")
    (ASSETS / "master_yachay.svg").write_text(master, encoding="utf-8")
    print("generados: logo_horizontal_contornos.svg, logo_apilado_contornos.svg, master_yachay.svg")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
```

- [ ] **Step 4: Ejecutar el script**

Run: `.superpowers/venv-branding/bin/python branding/scripts/generar_contornos.py "${TMPDIR:-/tmp}/yachay_fonts"`
Expected: `generados: logo_horizontal_contornos.svg, logo_apilado_contornos.svg, master_yachay.svg`

- [ ] **Step 5: Verificar que no queda ningún `<text>` y validar XML**

Run: `grep -L '<text' branding/assets/logo_horizontal_contornos.svg branding/assets/logo_apilado_contornos.svg branding/assets/master_yachay.svg && xmllint --noout branding/assets/logo_horizontal_contornos.svg branding/assets/logo_apilado_contornos.svg branding/assets/master_yachay.svg && echo OK`
Expected: los tres nombres de archivo listados por `grep -L` (ninguno contiene `<text`), luego `OK`.

- [ ] **Step 6: Verificación visual**

Run: `open branding/assets/logo_horizontal_contornos.svg branding/assets/master_yachay.svg`
Confirmar: el wordmark de contornos se ve idéntico al de Task 3 (misma serif, mismo tracking del descriptor) y el lienzo maestro muestra lockups, símbolo, mínima, panel inverso y 6 swatches.

- [ ] **Step 7: Commit**

```bash
git add branding/scripts/generar_contornos.py branding/assets/logo_horizontal_contornos.svg branding/assets/logo_apilado_contornos.svg branding/assets/master_yachay.svg
git commit -m 'Agregar vectorizado para diseño: contornos del wordmark y lienzo maestro' -m 'Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>'
```

---

### Task 5: Brand board HTML

**Files:**
- Create: `branding/brand_board.html`

**Interfaces:**
- Consumes: `assets/logo_horizontal.svg`, `assets/logo_apilado.svg`, `assets/simbolo.svg`, `assets/marca_minima.svg`, `assets/logo_horizontal_inverso.svg`, `assets/favicon.svg` (Tasks 1–3) vía `<img>` con rutas relativas.

- [ ] **Step 1: Crear `branding/brand_board.html`**

```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Yachay — Brand Board v1</title>
<link rel="icon" href="assets/favicon.svg">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&family=Source+Sans+3:wght@400;600&family=JetBrains+Mono&display=swap');
  :root {
    --petroleo:#1B4965; --acero:#5FA8D3; --ambar:#E8A13D;
    --pizarra:#2E3440; --hueso:#F7F5F0; --niebla:#5F7A8C;
    --fondo:var(--hueso); --texto:var(--pizarra); --tarjeta:#FFFFFF;
  }
  @media (prefers-color-scheme: dark) {
    :root { --fondo:#15222B; --texto:var(--hueso); --tarjeta:#1B4965; }
  }
  * { margin:0; padding:0; box-sizing:border-box; }
  body { background:var(--fondo); color:var(--texto); font-family:'Source Sans 3','Helvetica Neue',Arial,sans-serif; line-height:1.6; padding:40px 20px; }
  main { max-width:960px; margin:0 auto; display:grid; gap:28px; }
  h1,h2 { font-family:'Source Serif 4',Georgia,serif; color:var(--petroleo); }
  @media (prefers-color-scheme: dark) { h1,h2 { color:var(--acero); } }
  h2 { font-size:1.25rem; margin-bottom:12px; }
  section { background:var(--tarjeta); border-radius:10px; padding:24px 28px; }
  .lockup-hero { text-align:center; padding:44px 20px; background:#FFFFFF; }
  .lockup-hero img { max-width:340px; width:80%; }
  .lockup-hero p { color:var(--niebla); margin-top:14px; }
  .grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:14px; }
  .celda { background:var(--hueso); border-radius:8px; padding:18px; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:10px; text-align:center; }
  .celda.oscura { background:var(--petroleo); }
  .celda img { max-width:110px; max-height:96px; }
  .celda small { font-size:0.72rem; color:var(--niebla); letter-spacing:0.06em; text-transform:uppercase; }
  .celda.oscura small { color:#9DC3DA; }
  .swatch { border-radius:8px; padding:14px 12px; color:#fff; min-height:96px; }
  .swatch code { font-family:'JetBrains Mono',monospace; font-size:0.75rem; opacity:0.9; display:block; }
  .swatch small { display:block; font-size:0.75rem; margin-top:2px; }
  ul.reglas { padding-left:20px; }
  ul.reglas li::marker { color:var(--ambar); }
  .tipo-serif { font-family:'Source Serif 4',Georgia,serif; font-weight:600; font-size:1.5rem; color:var(--petroleo); }
  @media (prefers-color-scheme: dark) { .tipo-serif { color:var(--acero); } }
  .tipo-mono { font-family:'JetBrains Mono',monospace; font-size:0.85rem; background:var(--hueso); color:var(--pizarra); padding:4px 8px; border-radius:4px; display:inline-block; }
  .dos-col { display:grid; grid-template-columns:1fr 1fr; gap:16px; }
  @media (max-width:640px) { .dos-col { grid-template-columns:1fr; } }
  .ok { border-left:4px solid #4C9A6A; padding-left:12px; }
  .mal { border-left:4px solid #B3544F; padding-left:12px; }
  .nota { font-size:0.85rem; color:var(--niebla); margin-top:10px; }
  footer { text-align:center; font-size:0.8rem; color:var(--niebla); }
</style>
</head>
<body>
<main>
  <section class="lockup-hero">
    <img src="assets/logo_horizontal.svg" alt="Yachay Research Associates — logo horizontal">
    <p>Brand board v1 · Evidencia que decide.</p>
  </section>

  <section>
    <h2>Sistema de versiones</h2>
    <div class="grid">
      <div class="celda"><img src="assets/logo_apilado.svg" alt="Lockup apilado"><small>Apilado · LinkedIn, portadas</small></div>
      <div class="celda"><img src="assets/simbolo.svg" alt="Símbolo Telar"><small>Símbolo · sellos, marca de agua</small></div>
      <div class="celda"><img src="assets/marca_minima.svg" alt="Marca mínima Cascada" style="max-width:34px;"><small>Mínima · favicon ≤32px</small></div>
      <div class="celda oscura"><img src="assets/logo_horizontal_inverso.svg" alt="Logo inverso"><small>Inverso · fondos oscuros</small></div>
    </div>
    <p class="nota">Para trabajo de diseño: <code>assets/master_yachay.svg</code> (lienzo con todo, sin dependencia de fuentes) y <code>assets/logo_*_contornos.svg</code>.</p>
  </section>

  <section>
    <h2>Paleta</h2>
    <div class="grid">
      <div class="swatch" style="background:#1B4965;"><strong>Azul petróleo</strong><code>#1B4965</code><small>primario · logo, títulos</small></div>
      <div class="swatch" style="background:#5FA8D3;"><strong>Azul acero</strong><code>#5FA8D3</code><small>gráficos, enlaces</small></div>
      <div class="swatch" style="background:#E8A13D;"><strong>Ámbar andino</strong><code>#E8A13D</code><small>acento · ≤10% por pieza</small></div>
      <div class="swatch" style="background:#2E3440;"><strong>Gris pizarra</strong><code>#2E3440</code><small>texto</small></div>
      <div class="swatch" style="background:#F7F5F0;color:#2E3440;border:1px solid #ccc;"><strong>Hueso</strong><code>#F7F5F0</code><small>fondos</small></div>
      <div class="swatch" style="background:#5F7A8C;"><strong>Azul niebla</strong><code>#5F7A8C</code><small>descriptor, metadatos</small></div>
    </div>
  </section>

  <section>
    <h2>Tipografía</h2>
    <p class="tipo-serif">Source Serif 4 — títulos y marca</p>
    <p>Source Sans 3 — cuerpo de texto, tablas y UI.</p>
    <p class="tipo-mono">JetBrains Mono — código en entregables reproducibles</p>
    <p class="nota">Los SVG con <code>&lt;text&gt;</code> requieren las fuentes instaladas (Google Fonts) para render fiel; las versiones <code>_contornos</code> no dependen de fuentes.</p>
  </section>

  <section>
    <h2>Reglas de uso</h2>
    <div class="dos-col">
      <div class="ok">
        <strong>Sí</strong>
        <ul class="reglas">
          <li>Lockup horizontal como versión por defecto</li>
          <li>Apilado en formatos cuadrados (LinkedIn) y portadas</li>
          <li>Inverso sobre azul petróleo u oscuro; ámbar y acero no cambian</li>
          <li>Área de respeto: la altura de la "Y" del símbolo</li>
          <li>Nudo cuadrado ámbar como bullet en documentos</li>
        </ul>
      </div>
      <div class="mal">
        <strong>No</strong>
        <ul class="reglas">
          <li>No estirar, rotar ni cambiar colores</li>
          <li>No usar sombras, degradados ni efectos</li>
          <li>No usar el Telar completo por debajo de 32px (usar la mínima)</li>
          <li>No superar ~10% de ámbar en una pieza</li>
          <li>No colocar sobre fondos con ruido visual</li>
        </ul>
      </div>
    </div>
  </section>

  <footer>Yachay Research Associates LLC · Identidad v1 · 2026 — Spec: docs/superpowers/specs/2026-07-17-identidad-visual-yachay-design.md</footer>
</main>
</body>
</html>
```

- [ ] **Step 2: Verificar en navegador**

Run: `open branding/brand_board.html`
Confirmar: los 4 SVG del sistema cargan, swatches correctos, y con el sistema en modo oscuro la página cambia (fondo oscuro, títulos en acero).

- [ ] **Step 3: Commit**

```bash
git add branding/brand_board.html
git commit -m 'Agregar brand board HTML v1' -m 'Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>'
```

---

### Task 6: Tema revealjs del pitch deck

**Files:**
- Create: `pitch-deck/yachay.scss`
- Create: `pitch-deck/assets/simbolo.svg` (copia del asset — recurso local al deck; sin `_quarto.yml`, Quarto no resuelve recursos fuera del directorio del documento)
- Modify: `pitch-deck/pitch_deck_revealjs_quarto.qmd:7` (línea `theme: [default]`)

**Interfaces:**
- Consumes: `branding/assets/simbolo.svg` (Task 1).
- Produces: deck renderizado con tema Yachay (regenera `pitch_deck_revealjs_quarto.html` y `pitch_deck_revealjs_quarto_files/`).

- [ ] **Step 1: Crear `pitch-deck/yachay.scss`**

```scss
/*-- scss:defaults --*/
$body-bg: #F7F5F0;
$body-color: #2E3440;
$link-color: #5FA8D3;
$presentation-heading-font: "Source Serif 4", Georgia, serif;
$presentation-heading-color: #1B4965;
$font-family-sans-serif: "Source Sans 3", "Helvetica Neue", Arial, sans-serif;
$font-family-monospace: "JetBrains Mono", monospace;

/*-- scss:rules --*/
@import url('https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,600&family=Source+Sans+3:wght@400;600&family=JetBrains+Mono&display=swap');

.reveal .slides section h2 {
  border-bottom: 2px solid #1B4965;
  padding-bottom: 0.15em;
}

.reveal ul li::marker,
.reveal ol li::marker {
  color: #E8A13D;
}

.reveal strong {
  color: #1B4965;
}

.reveal .slide-logo {
  max-height: 2.4em !important;
}

#title-slide .title {
  color: #1B4965;
}

#title-slide .subtitle,
#title-slide .quarto-title-author-name {
  color: #5F7A8C;
}
```

- [ ] **Step 2: Copiar el símbolo como recurso del deck**

Run: `mkdir -p pitch-deck/assets && cp branding/assets/simbolo.svg pitch-deck/assets/simbolo.svg`

- [ ] **Step 3: Modificar el frontmatter del deck**

En `pitch-deck/pitch_deck_revealjs_quarto.qmd`, reemplazar la línea `    theme: [default]` por:

```yaml
    theme: [default, yachay.scss]
    logo: assets/simbolo.svg
```

(el resto del frontmatter no se toca)

- [ ] **Step 4: Renderizar y verificar**

Run: `quarto render pitch-deck/pitch_deck_revealjs_quarto.qmd`
Expected: `Output created: pitch_deck_revealjs_quarto.html`, sin errores de compilación scss.
Luego `open pitch-deck/pitch_deck_revealjs_quarto.html` — fondo hueso, títulos serif azul petróleo con línea inferior, markers ámbar, símbolo como logo de slide.

- [ ] **Step 5: Commit** (fuente + tema + recurso + salida regenerada)

```bash
git add pitch-deck/yachay.scss pitch-deck/assets/simbolo.svg pitch-deck/pitch_deck_revealjs_quarto.qmd pitch-deck/pitch_deck_revealjs_quarto.html pitch-deck/pitch_deck_revealjs_quarto_files
git commit -m 'Aplicar tema visual Yachay al pitch deck (revealjs)' -m 'Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>'
```

---

### Task 7: Colores LaTeX del MOF

**Files:**
- Modify: `MOF/MOF_v1.qmd:6-12` (bloque `format: pdf:`)

**Interfaces:**
- Consumes: paleta del spec (hex verbatim).
- Produces: `MOF/MOF_v1.pdf` regenerado con titulares y enlaces de marca.

- [ ] **Step 1: Modificar el frontmatter del MOF**

En `MOF/MOF_v1.qmd`, dentro de `format: pdf:` (manteniendo `toc`, `number-sections`, `documentclass`, `geometry`, `colorlinks` tal como están), agregar estas claves al mismo nivel de indentación:

```yaml
    include-in-header:
      text: |
        \usepackage{sectsty}
        \definecolor{yachaypetroleo}{HTML}{1B4965}
        \definecolor{yachayacero}{HTML}{5FA8D3}
        \allsectionsfont{\color{yachaypetroleo}}
    linkcolor: yachaypetroleo
    urlcolor: yachayacero
    toccolor: yachaypetroleo
```

(no agregar `\usepackage{xcolor}` — Quarto ya lo carga y duplicarlo provoca option clash)

- [ ] **Step 2: Renderizar y verificar**

Run: `quarto render MOF/MOF_v1.qmd`
Expected: `Output created: MOF_v1.pdf`. Si falla por falta de LaTeX: `quarto install tinytex` y reintentar.
Abrir el PDF: títulos de sección en azul petróleo, TOC en petróleo, URLs en acero.

- [ ] **Step 3: Commit**

```bash
git add MOF/MOF_v1.qmd MOF/MOF_v1.pdf
git commit -m 'Aplicar colores de marca Yachay al MOF (LaTeX)' -m 'Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>'
```

---

### Task 8: Actualizar `branding/04_identidad_visual.md` a v1.0

**Files:**
- Modify: `branding/04_identidad_visual.md` (reemplazo completo del contenido)

**Interfaces:**
- Consumes: rutas de assets de Tasks 1–6 y decisiones del spec.

- [ ] **Step 1: Reemplazar el contenido completo del archivo con:**

```markdown
# Identidad visual — Yachay Research Associates LLC

> **Versión:** 1.0 (sistema aprobado) · **Fecha:** 2026-07-17
> Co-creada en sesión interactiva; spec técnico con geometría exacta en
> `docs/superpowers/specs/2026-07-17-identidad-visual-yachay-design.md`.
> Manual navegable: [brand_board.html](brand_board.html) · Archivos: [assets/](assets/)

## 1. Concepto

**"Telar"**: un quipu abstracto cuyas cuerdas centrales convergen formando la inicial "Y".
Doble narrativa: el quipu como sistema andino de registro de datos + la convergencia de
evidencia en una decisión (nudo ámbar). Raíz andina sutil: quien la conoce, la ve;
quien no, percibe una marca científica sólida.

## 2. Sistema de logo

| Versión | Archivo | Uso |
|---|---|---|
| Horizontal (principal) | `assets/logo_horizontal.svg` | documentos, web, firma de email |
| Apilado (secundario) | `assets/logo_apilado.svg` | LinkedIn (cuadrado), portadas, slide inicial |
| Símbolo solo | `assets/simbolo.svg` | sellos, marca de agua, logo de slides |
| Marca mínima "Cascada" | `assets/marca_minima.svg`, `assets/favicon.svg` | favicon, tamaños ≤32px |

Cada versión tiene variantes `_inverso` (fondos oscuros: petróleo→hueso; acero y ámbar
no cambian) y `_mono` (una tinta, recolorable editando `style="color:…"` del SVG).

**Para trabajo de diseño humano:** `assets/master_yachay.svg` (lienzo único con todas
las versiones en grupos nombrados, sin dependencia de fuentes) y
`assets/logo_horizontal_contornos.svg` / `assets/logo_apilado_contornos.svg` (wordmark
en contornos). Se regeneran con `branding/scripts/generar_contornos.py`.

Reglas: no estirar/rotar/recolorear; sin efectos; área de respeto = altura de la "Y";
el Telar completo nunca por debajo de 32px (usar la mínima).

## 3. Paleta

| Rol | Color | Hex |
|---|---|---|
| Primario | Azul petróleo | `#1B4965` |
| Secundario | Azul acero | `#5FA8D3` |
| Acento (≤10% por pieza) | Ámbar andino | `#E8A13D` |
| Texto | Gris pizarra | `#2E3440` |
| Fondos | Hueso | `#F7F5F0` |
| Apoyo (descriptor, metadatos) | Azul niebla | `#5F7A8C` |

Contraste WCAG AA obligatorio en combinaciones texto/fondo.

## 4. Tipografía

| Rol | Fuente |
|---|---|
| Títulos y marca | Source Serif 4 (600) — finalista descartada: Fraunces |
| Cuerpo, tablas, UI | Source Sans 3 (400/600) |
| Código | JetBrains Mono |

Todas Google Fonts. Los SVG con `<text>` requieren la fuente instalada o webfont;
las versiones `_contornos` no.

## 5. Aplicaciones implementadas

- Pitch deck: `pitch-deck/yachay.scss` (tema revealjs) + símbolo como logo de slides.
- MOF PDF: titulares y enlaces en colores de marca (frontmatter LaTeX).
- El nudo cuadrado ámbar se reutiliza como bullet/acento en documentos.

## 6. Restricciones y pendientes

- **Restricción:** mantener distancia visual del logo de la "Semana de la Evidencia"
  (evento, Perú); la Y debe seguir siendo protagonista en cualquier refinamiento.
- Pendiente (responsabilidad del usuario): búsqueda legal de marca (USPTO/Indecopi)
  antes de inversión mayor.
- Fase 2: plantilla de gráficos ggplot2/matplotlib; refinamiento con diseñador
  (el lienzo maestro es el punto de partida).
```

- [ ] **Step 2: Verificar consistencia de rutas**

Run: `ls branding/assets/ && grep -o 'assets/[a-z_]*\.svg' branding/04_identidad_visual.md | sort -u`
Expected: cada ruta que imprime el `grep` existe en el listado del `ls`.

- [ ] **Step 3: Commit**

```bash
git add branding/04_identidad_visual.md
git commit -m 'Actualizar identidad visual a v1.0 con el sistema Telar aprobado' -m 'Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>'
```
