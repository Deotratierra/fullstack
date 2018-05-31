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
        stderr, stdout_live_call = process.communicate()
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

# ===========================================================0

if __name__ == "__main__":
    print(simple_call("date"))
    print(stdout_defer_call("date"))
    print(stdout_live_call("date"))