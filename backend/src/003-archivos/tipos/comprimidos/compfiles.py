#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ========================================================================

# Comprimir archivos y directorios en .zip (algoritmo DEFLATED)
import os
import zipfile

def compress_file_zip(inpath, outpath):
    """Comprime un archivo en ZIP con el algoritmo DEFLATED

    :param inpath: Ruta del archivo a comprimir
    :type inpath: str

    :param outpath: Ruta del archivo zip resultante.
    :type outpath: str
    """
    if os.path.exists(inpath):
        if os.path.isfile(inpath):
            with zipfile.ZipFile(outpath, "w", 
                                 zipfile.ZIP_DEFLATED) as zip_handler:
                zip_handler.write(inpath)
        else:
            if os.path.isdir(inpath):
                raise IsADirectoryError("%s is a directory" % str(inpath))
            else:
                raise RuntimeError("Error compressing file")
    else:
        raise FileNotFoundError("%s doesn't exists" % str(inpath))


def compress_dir_zip(inpath, outpath):
    """Comprime un directorio en ZIP con el algoritmo DEFLATED

    :param inpath: Ruta del directorio a comprimir
    :type inpath: str

    :param outpath: Ruta del archivo zip resultante.
    :type outpath: str
    """
    if os.path.exists(inpath):
        if os.path.isdir(inpath):
            with zipfile.ZipFile(outpath, "w", 
                                 zipfile.ZIP_DEFLATED) as zip_handler:
                for root, dirs, files in os.walk(inpath):
                    for dir in dirs:
                        for file in files:
                            zip_handler.write(os.path.join(root, file))
        else:
            raise NotADirectoryError("%s is not a directory" % str(inpath))
    else:
        raise FileNotFoundError("%s doesn't exists" % str(inpath))


# ------------------------------------------------------------------------

# Descomprimir archivos o directorios de .zip (algoritmo DEFLATED)
def decompress_zip(inpath, outpath=None, password=None):
    """Descomprime un directorio zip

    :param inpath: Ruta del directorio zip a descomprimir
    :type inpath: str

    :param outpath: Ruta al directorio donde se guardarán 
        los archivos resultantes. Por defecto se crea un nuevo
        directorio con el directorio base del directorio de entrada.
        (optional, default == None)
    :type outpath: str

    :param password: Contraseña usada al encriptar.
    :type password: str
    """
    if zipfile.is_zipfile(inpath):
    	if not outpath: outpath = os.path.basename(inpath)
    	if not os.path.isdir(outpath): outpath = outpath.split(".")[0]
        with zipfile.ZipFile(inpath) as zip_handler:
            zip_handler.extractall(outpath, pwd=password)
    else:
        raise zipfile.BadZipFile("%s is not a valid .zip file" % inpath)

# ========================================================================


# Fuentes:
# https://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory
# https://docs.python.org/3/library/zipfile.html