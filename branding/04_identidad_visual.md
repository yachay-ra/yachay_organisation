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
