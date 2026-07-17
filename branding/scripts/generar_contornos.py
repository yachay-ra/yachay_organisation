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
    if not serif.is_file() or not sans.is_file():
        sys.exit(f"Faltan fuentes en {dir_fuentes}: se requieren serif600.ttf y sans600.ttf")
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
