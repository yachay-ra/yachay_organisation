# Spec de diseño — Identidad visual de Yachay Research Associates

> **Fecha:** 2026-07-17 · **Estado:** aprobado por Darwin en sesión de co-creación (companion visual)
> Deriva de `branding/01_estrategia_de_marca.md` (arquetipo Sabio) y actualiza la dirección propuesta en `branding/04_identidad_visual.md` (v0.1) con decisiones validadas.

## Contexto

Yachay Research Associates LLC necesita una identidad visual v1 utilizable de inmediato (propuestas, deck, LinkedIn) sin esperar un ciclo de diseño externo. Se co-creó en sesión interactiva: tres direcciones de símbolo → híbrido elegido por el usuario → lockup → tipografía → sistema completo aprobado.

## Decisiones validadas

### Símbolo: "Telar"

Un quipu abstracto cuyas dos cuerdas centrales convergen y forman la inicial "Y". Doble narrativa: el quipu como sistema andino de registro de datos + la convergencia de evidencia en una decisión (nudo ámbar).

Geometría de referencia (viewBox `0 0 120 120`, trazos `stroke-linecap="round"` salvo indicación):

| Elemento | Especificación |
|---|---|
| Cuerda madre | línea (14,18)→(106,18), azul petróleo, grosor 5 |
| Cuerda lateral izq. | línea (25,18)→(25,76), azul acero, grosor 2.5; nudo circular r=4 en (25,48) |
| Cuerda lateral der. | línea (95,18)→(95,68), azul acero, grosor 2.5; nudo circular r=4 en (95,42) |
| Brazo izq. de la Y | línea (43,18)→(60,62), azul petróleo, grosor 3.2; nudo r=4.5 en (51,39) |
| Brazo der. de la Y | línea (77,18)→(60,62), azul petróleo, grosor 3.2; nudo r=4.5 en (69,39) |
| Tronco de la Y | línea (60,62)→(60,102), azul petróleo, grosor 3.2 |
| Nudo central | círculo r=6.5 en (60,62), **ámbar** — único elemento ámbar del símbolo |
| Nudo del tronco | círculo r=4.5 en (60,84), azul petróleo |

### Marca mínima: "Cascada" (derivada, para ≤32px)

Misma familia geométrica, menos elementos y trazos engrosados: cuerda madre (18,18)→(102,18) grosor 7; brazos (38,18)→(60,58) y (82,18)→(60,58) grosor 6; tronco (60,58)→(60,100) grosor 6; nudo central único ámbar r=11. Uso: favicon, avatares pequeños, marcas de agua diminutas.

### Wordmark y descriptor

- "Yachay" en **Source Serif 4 SemiBold (600)**, azul petróleo. (Finalista descartada: Fraunces 600 — documentada por si un diseñador retoma el refinamiento.)
- Descriptor "RESEARCH ASSOCIATES" en **Source Sans 3 SemiBold**, mayúsculas, tracking `0.22em`, color azul niebla `#5F7A8C`. Omisible en usos pequeños.

### Sistema de versiones (lockups)

| Versión | Composición | Uso |
|---|---|---|
| **Horizontal (principal)** | símbolo izq. + wordmark/descriptor der.; altura del símbolo ≈ 1.8× el tamaño de fuente del wordmark; separación ≈ 0.4× | encabezados de documentos, web, firma email |
| **Apilado (secundario)** | símbolo centrado arriba + wordmark/descriptor centrados debajo | LinkedIn (formato cuadrado), portadas, slide inicial |
| **Símbolo solo** | Telar sin texto | sellos, marca de agua |
| **Marca mínima** | Cascada | favicon, ≤32px |

**Versión inversa** (sobre azul petróleo u oscuro): trazos azul petróleo → hueso `#F7F5F0`; las cuerdas laterales azul acero y el nudo ámbar **no cambian** (constancia del acento). Monocromo: todo un solo color (petróleo, negro o blanco) para usos de una tinta.

### Paleta

| Rol | Nombre | Hex | Regla |
|---|---|---|---|
| Primario | Azul petróleo | `#1B4965` | logo, títulos, elementos clave |
| Secundario | Azul acero | `#5FA8D3` | gráficos, enlaces, cuerdas laterales |
| Acento | Ámbar andino | `#E8A13D` | nudo central, CTAs, bullets; ≤10% por pieza |
| Texto | Gris pizarra | `#2E3440` | cuerpo de texto |
| Fondo | Hueso | `#F7F5F0` | fondos de documentos y web |
| Apoyo | Azul niebla | `#5F7A8C` | descriptor, metadatos, texto secundario |

Contraste WCAG AA obligatorio en combinaciones texto/fondo.

### Tipografía del sistema

| Rol | Fuente | Fallback |
|---|---|---|
| Títulos y marca | Source Serif 4 (600) | Georgia, serif |
| Cuerpo, tablas, UI | Source Sans 3 (400/600) | Helvetica Neue, Arial |
| Código | JetBrains Mono | monospace |

Todas Google Fonts (open source, sin licencias).

### Restricciones de diseño

1. **Distancia visual del logo de la "Semana de la Evidencia" (evento, Perú):** motivo por el que se descartó el quipu puro; la Y debe mantenerse protagonista en cualquier refinamiento futuro.
2. Referencia andina **sutil y abstracta** — nunca folklorismo literal.
3. Solo fuentes open source.
4. El eco del sistema: el nudo/cuadrado ámbar reutilizable como bullet y micro-acento en documentos.

## Entregables de implementación

En `branding/assets/`:

1. `logo_horizontal.svg` (principal), `logo_apilado.svg`, `simbolo.svg`, `marca_minima.svg` — cada uno con variante `_inverso.svg` y `_mono.svg`. El wordmark va como `<text>` con la pila de fuentes (`Source Serif 4, Georgia, serif`) para mantenerlo editable como texto; la fidelidad sin fuentes la cubren los archivos de contornos (punto 6).
6. **Archivos para trabajo de diseño humano** (editables en Illustrator/Figma/Inkscape):
   - `logo_horizontal_contornos.svg` y `logo_apilado_contornos.svg` — wordmark y descriptor convertidos a contornos (paths) con shaping tipográfico real (fonttools + uharfbuzz), de modo que rendericen idénticos sin fuentes instaladas.
   - `master_yachay.svg` — lienzo único con todas las versiones (lockups en contornos, símbolo, mínima, panel inverso, paleta) en grupos con `id` nombrados, listo para importar a herramientas de diseño.
   - `branding/scripts/generar_contornos.py` — script reproducible que genera los tres archivos anteriores desde las fuentes originales.
2. `favicon.svg` (Cascada).
3. `brand_board.html` — página autocontenida con todo el sistema (logo, versiones, paleta, tipografía, ejemplos ✓/✗ de uso) como manual v1 navegable.
4. Tema Quarto: `pitch-deck/yachay.scss` aplicado al frontmatter de `pitch_deck_revealjs_quarto.qmd` (colores, fuentes, logo en slides); variables de color LaTeX para el MOF (colorlinks y titulares en azul petróleo).
5. Actualizar `branding/04_identidad_visual.md` v0.1 → v1.0 con las decisiones de este spec (reemplazando las propuestas provisionales: Fraunces→Source Serif 4, Inter→Source Sans 3, brief de logo→sistema Telar).

## Fuera de alcance

- Búsqueda legal de marca (USPTO/Indecopi) — responsabilidad del usuario antes de inversión mayor en la marca.
- Archivos propietarios (.ai, .fig), papelería impresa, animaciones.
- Rediseño del contenido del pitch deck (solo tema visual).
- Plantilla de gráficos ggplot2/matplotlib — fase 2, tras validar el tema Quarto.

## Criterios de aceptación

- Los SVG renderizan idénticos a los bocetos aprobados de la sesión (geometría de las tablas anteriores).
- Los archivos `_contornos` no contienen ningún elemento `<text>` y renderizan el wordmark fiel en un sistema sin las fuentes instaladas; `generar_contornos.py` es re-ejecutable.
- El favicon es legible a 16px y 32px.
- `quarto render pitch-deck/pitch_deck_revealjs_quarto.qmd` produce el deck con tema Yachay sin errores.
- El brand board se ve correcto en claro y oscuro y no depende de recursos externos salvo Google Fonts.
- Ninguna pieza usa ámbar por encima del ~10% de su superficie.
