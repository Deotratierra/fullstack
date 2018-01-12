#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from subprocess import call

def simple_call(command):
    try:
        return call(parse(command)) # 0   # <--- Código de salida del proceso
    except Exception as e:
        print("Error realizando una llamada simple: %s" % e)

# ====================================================================

#####   TUBERÍAS   #####
# https://docs.python.org/3/library/pipes.html

import pipes

def pipeline(template_commands, exec_commands):
    """Implementa una tubería

    :param template_commands: Lista de comandos que
        modificaran la ejecución mediante una tubería
    :type template_commands: list

    :param exec_commands: Lista de comandos a ejecutar
    :type exec_commands: list
    """
    template = pipes.Template()
    for command in template_commands:
        template.append(command, "--")
        # "--" indica cómo se leerán las entradas y salidas

    with template.open("pipefile", "w") as fichero:
        for command in exec_commands: # Comandos de ejecución
            fichero.write(command)

    with open("pipefile", "r") as fichero:
        response = fichero.read()
    return response

# ====================================================================

if __name__ == "__main__":
    # Convertir de mayúsculas a minúsculas la fecha
    pipeline(["tr a-z A-Z"], [stdout_call("date")]) # LUN OCT 30 11:21:10 CET 2017
