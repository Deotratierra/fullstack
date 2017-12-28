#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import json

BROKEN_URLS_PATH = "metadata/assets/data/urls_broken.json"

def main():
    # Obtenemos el número de URLs caidas
    with open(BROKEN_URLS_PATH, "r", encoding="utf-8") as broken_urls_file:
        urls_broken = len(json.loads(broken_urls_file.read()))

    # Determinamos el color del campo
    shield_color = "brightgreen"
    if urls_broken > 0:
        shield_color = "red"

    # Abrimos el README principal
    with open("README.md", "r", encoding="utf-8") as index_file:
        content = index_file.read()

    # Reemplazamos el antiguo campo con el nuevo
    new_shield = "Links_down-%d-%s.svg" % (urls_broken, shield_color)
    content = re.sub(r"Links_down-.+\.svg", new_shield, content)

    # Sobreescribimos el README principal con los cambios
    with open("README.md", "w", encoding="utf-8") as index_file:
        index_file.write(content)

if __name__ == "__main__":
    main()
