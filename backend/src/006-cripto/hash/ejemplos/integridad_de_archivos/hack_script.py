#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Este fichero es una simulación de inyección de código malicioso
en un código fuente"""

import os
import re

if __name__ == "__main__":
    target_file = os.path.join(os.path.dirname(__file__), "lib", "codigo_fuente.py")
    with open(target_file, "r") as cf:
        content = cf.read()

    # Buscamos al destinatario al que se le va a enviar dinero en el script
    destinatario = re.search(r'\s{4}enviar_dinero.*', content).group().split('"')[1]

    # Reemplazamos el destinatario por nuestra cuenta
    new_content = re.sub(destinatario, "Juanito", content)

    with open(target_file, "w") as cf:
        cf.write(new_content)
