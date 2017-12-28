#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

""" Niveles del logging:
DEBUG, INFO, WARNING, ERROR, CRITICAL
"""

# Logging con el nombre del archivo
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Handler de salida por consola
handler = loggging.StreamHandler()
handler.setLevel(logging.DEBUG)

# Formato del logging
__format__ = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
formatter = logging.Formatter(__format__)

# Manejador del logging
handler.setFormatter(formatter)
logger.addHandler(handler)


"""
StreamHandler() envía la salida del logging a canales
como sys.stdout, sys.stderr o cualquier objeto de tipo fichero
(más precisamente, cualquier objeto que soporte los métodos flush() y write()).

Los loggers hijos propagan mensajes hacia arriba a los handlers asociados
con sus loggers ancestros. Debido a esto, no es necesario definir y configurar
handlers para todos los loggers que usa una aplicación. Es suficiente con
configurar handlers para un logger de nivel superior y crear loggers hijos
según sea necesario. (Sin embargo, puedes desactivar la propagación
configurando el atributo propagate de un logger a False)
"""