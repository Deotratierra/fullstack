#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from shlex import split as parse

"""Existe una implementación de Popen con la biblioteca psutil
que trae algunas características adicionales:
http://psutil.readthedocs.io/en/latest/#psutil.Popen
"""

# ====================================================================

#####   SUBPROCESO SIMPLE   #####
# https://docs.python.org/3/library/subprocess.html

from subprocess import call

def simple_call(command):
    try:
        return call(parse(command)) # 0   # <--- Código de salida del proceso
    except Exception as e:
        print("Error realizando una llamada simple: %s" % e)

# ====================================================================

#####   SUBPROCESO CON SALIDA EN DIFERIDO   #####

from subprocess import Popen, PIPE

def stdout_defer_call(command):
    try:
        process = Popen(parse(command), stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
    except Exception as e:
        print("Error realizando una llamada con pipeline: %s" % e)
        return stderr.decode("utf-8")
    else:
        return stdout.decode("utf-8") # <class 'bytes'>  --->  <class 'str'>


# ====================================================================

#####   SUBPROCESO CON SALIDA EN VIVO   #####

def stdout_live_call(command):
    process = Popen(shlex.split(command), stdout=PIPE, stderr=PIPE)
    while True:
        out = process.stdout.read(1)
        out = out.decode("utf-8") # Añadir errors="ignore" con caracteres extraños
                                  # o decodificar con otro codec
        if out == '' and process.poll() != None:
            break
        if out != '':
            sys.stdout.write(out)
            sys.stdout.flush()


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
    print(simple_call("date"))
    print(stdout_defer_call("date"))
    print(stdout_live_call("date"))

    # Convertir de mayúsculas a minúsculas la fecha
    pipeline(["tr a-z A-Z"], [stdout_call("date")]) # LUN OCT 30 11:21:10 CET 2017
