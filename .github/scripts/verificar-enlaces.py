#!/usr/bin/env python3
"""Verifica las reglas de enlaces del README en todos los .md del repositorio.

Comprueba dos cosas:

1. Que no haya wikilinks [[asi]]. Se ven rotos en GitHub (README, regla 2).
2. Que todo enlace relativo apunte a un archivo o carpeta que existe de verdad.

No mira lo que esté dentro de bloques de código (``` ... ```) ni de código en
linea (`asi`), porque ahi el texto es un ejemplo, no un enlace real.

Escape: si una linea necesita un [[wikilink]] literal fuera de codigo, se le
agrega el comentario <!-- ok-wikilink --> en la misma linea.

Uso:  python3 .github/scripts/verificar-enlaces.py
Devuelve 0 si todo esta bien, 1 si encontro problemas.
"""

import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]

WIKILINK = re.compile(r"\[\[[^\]\n]+\]\]")
ENLACE = re.compile(r"(?<!!)\[[^\]\n]*\]\(([^)\s]+)\)")
CODIGO_EN_LINEA = re.compile(r"`[^`\n]*`")
EXTERNOS = ("http://", "https://", "mailto:", "tel:", "//")


def lineas_fuera_de_codigo(texto):
    """Devuelve (numero_de_linea, linea_sin_codigo) saltando bloques cercados."""
    dentro_de_bloque = False
    for numero, linea in enumerate(texto.splitlines(), start=1):
        if linea.lstrip().startswith("```"):
            dentro_de_bloque = not dentro_de_bloque
            continue
        if dentro_de_bloque:
            continue
        yield numero, CODIGO_EN_LINEA.sub("", linea)


def revisar(archivo):
    problemas = []
    relativo = archivo.relative_to(RAIZ)
    texto = archivo.read_text(encoding="utf-8")

    for numero, linea in lineas_fuera_de_codigo(texto):
        if "<!-- ok-wikilink -->" not in linea:
            for encontrado in WIKILINK.findall(linea):
                problemas.append(
                    f"{relativo}:{numero}  wikilink {encontrado} "
                    f"-> usa [texto](ruta/archivo.md)"
                )

        for destino in ENLACE.findall(linea):
            if destino.startswith(EXTERNOS) or destino.startswith("#"):
                continue
            ruta = destino.split("#")[0].split("?")[0]
            if not ruta:
                continue
            objetivo = (archivo.parent / ruta).resolve()
            if not objetivo.exists():
                problemas.append(
                    f"{relativo}:{numero}  enlace roto ({destino}) "
                    f"-> no existe {ruta}"
                )

    return problemas


def main():
    archivos = sorted(
        p for p in RAIZ.rglob("*.md") if ".git" not in p.relative_to(RAIZ).parts
    )
    problemas = [p for archivo in archivos for p in revisar(archivo)]

    if problemas:
        print(f"Se encontraron {len(problemas)} problema(s):\n")
        for problema in problemas:
            print(f"  {problema}")
        print("\nReglas: README, puntos 2 y 4.")
        return 1

    print(f"OK: {len(archivos)} archivos .md revisados, sin problemas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
