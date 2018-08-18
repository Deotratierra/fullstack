# -*- coding: utf-8 -*-

"""
RPyC (pronunciado como ar-pay-si), o "Remote Python Call" 
  es una biblioteca transparente de Python para llamadas a procedimientos
  simétricas, clustering y computación distribuida. RPyC hace uso de
  patrón de diseño Proxy aplicado a objetos, una técnica que emplea la
  naturaleza dinámica de Python para salvar los límites físicos entre
  procesos y computadoras, así esos objetos remotos pueden ser manipulados
  como si fueran locales.

- Instalación: `pip install rpyc`
- Documentación: https://rpyc.readthedocs.io/en/latest/
- Código fuente: https://github.com/tomerfiliba/rpyc

"""

import rpyc

class MiServicio(rpyc.Service):
    def on_connect(self, conn):
        """Código que corre cuando se crea una conexión
        (para iniciar el servicio, si es necesario)
        """
        pass

    def on_disconnect(self, conn):
        """Código que corre tras el cierre de una conexión
        (para finalizar el servicio, si es necesario).
        """
        pass

    def exposed_get_answer(self): # Este es un método expuesto
        return 42

    exposed_the_real_answer_though = 43   # Un atributo expuesto

    def get_question(self):  # Este método no está expuesto
        return int

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MiServicio, port=18861)
    t.start()


""" Fuentes:
https://es.wikipedia.org/wiki/Llamada_a_procedimiento_remoto
https://es.wikipedia.org/wiki/Cl%C3%BAster_(inform%C3%A1tica)
https://es.wikipedia.org/wiki/Proxy_(patr%C3%B3n_de_dise%C3%B1o)
"""
