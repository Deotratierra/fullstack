#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
El siguiente script crea un logger principal de tipo archivo
en el cual se van insertando los mensajes. Si este archivo supera
un máximo de 20 bytes, se crea un backup con su contenido.
Si el número de backups supera los 5, los primeros backups se
van eliminando en el orden en el que fueron creados.
"""

import logging
from logging import handlers
import time


def create_rotating_log(path):
    logger = logging.getLogger(__file__)
    logger.setLevel(logging.INFO)

    handler = handlers.RotatingFileHandler(
    	path, maxBytes=20, backupCount=5, encoding="utf-8")
    logger.addHandler(handler)

    return logger

def log_lines(logger, num):
    for i in range(1, num + 1):
        logger.info("Línea del logger número %d", i)
        time.sleep(1)

if __name__ == "__main__":
    logger = create_rotating_log("rotatorio.log")
    log_lines(logger, 10)
