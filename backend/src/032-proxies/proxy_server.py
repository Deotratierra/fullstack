#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import threading
import signal
import sys
import webbrowser
import os


config =  {
            "HOST":               "0.0.0.0",
            "PORT":               12345,
            "MAX_REQUEST_LEN" :   1024,
            "CONNECTION_TIMEOUT": 5,

            # Dominios prohibidos
            "BLACKLIST_DOMAINS":  ["http://es.pornhub.com/",
                                   "https://www.pornhub.com/"],

            # Dominios maliciosos
            "MALICIOUS_DOMAINS": ["http://ocsp.digicert.com/"]
          }

# Plantilla para mostrar una página web prohibida
template_forbidden_page = """
<html>
<head> <meta charset="UTF-8"></head>
<body>
<h4>
La página web  %s  está prohibida.
</h4>
</body>
<html>
"""

class Server:
    """ La clase principal del servidor """

    def __init__(self, config):
        signal.signal(signal.SIGINT, self.shutdown)  # signal.SIGINT == Ctrl+C
        # https://es.wikipedia.org/wiki/Se%C3%B1al_(inform%C3%A1tica)  
         
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Crea un socket TCP
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)    # Re-use the socket
        self.serverSocket.bind((config['HOST'], config['PORT'])) # Enlaza el socket a u host público y un puerto
        self.serverSocket.listen(10)
        self.__clients = {}


    def listenForClient(self):
        """ Espera a la conexión de los clientes """
        while True:
            (clientSocket, client_address) = self.serverSocket.accept()   # Establece la conexión
            #print("Un cliente se ha conectado:", clientSocket, client_address)
            #print("---------------------------------------------------------")
            d = threading.Thread(name=self._getClientName(client_address), 
                                 target=self.proxy_thread, args=(clientSocket, client_address))
            d.setDaemon(True)
            d.start()
        self.shutdown(0,0)

    def filter(url):
        """ Filtro infantil y contra software malicioso """
	    if url in config["MALICIOUS_DOMAINS"]:
            return True

        if url in config["BLACKLIST_DOMAINS"]:
            print("Dominio %s prohibido para el cliente: %s" % (url, client_addr))
            current_dir = os.path.dirname(os.path.abspath(__file__))
	        with open("forbidden.html", "w") as f:
	            f.write(template_forbidden_page % url)
	        return webbrowser.open("file:///%s/forbidden.html" % current_dir)
            return True
        return False

    def proxy_thread(self, conn, client_addr):
        """
        ********************************************
        ************ PROXY_THREAD FUNC *************
        Thread para manejar peticiones del navegador
        ********************************************
        """

        request = conn.recv(config["MAX_REQUEST_LEN"])   # Obtenemos la petición
        headers, sep, body = request.partition(b"\r\n\r\n") # La parseamos (ver 3ª fuente)
        headers = headers.decode('latin1')   # Codificación en latin1 (otras fallan)
        print("------------------------------------")
        print(headers)                   
        first_line = headers.split("\n")[0]  # Obtenemos la primera línea
        url = first_line.split(" ")[1]       # Parseamos la url
        print(url)
        print("------------------------------------")

        if self.filter(url):   # Filtro infantil y contra software malicioso
            return
        
        # Busca el servidor web y el puerto
        http_pos = url.find("://")          # Buscamos la posición de ://
        if (http_pos==-1):
            temp = url
        else:
            temp = url[(http_pos+3):]       # Obtenemos el resto de la url

        port_pos = temp.find(":")           # Buscamos el puerto (si hay)

        # find end of web server
        webserver_pos = temp.find("/")
        if webserver_pos == -1:
            webserver_pos = len(temp)

        webserver = ""
        port = -1
        if (port_pos==-1 or webserver_pos < port_pos):      # Puerto por defecto
            port = 80
            webserver = temp[:webserver_pos]
        else:                                               # Puerto específico
            port = int((temp[(port_pos+1):])[:webserver_pos-port_pos-1])
            webserver = temp[:port_pos]

        try:
            # Creamos un socket para conectarnos con el servidor web
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(config["CONNECTION_TIMEOUT"])
            s.connect((webserver, port))
            s.sendall(request)             # Enviamos la petición al servidor web

            while 1:
                data = s.recv(config["MAX_REQUEST_LEN"])  # Recibimos info del servidor
                if (len(data) > 0):
                    conn.send(data)                      # y la enviamos al navegador
                else:
                    break
            s.close()
            conn.close()
        except socket.error as error_msg:
            print("ERROR: ", client_addr, error_msg)
            if s:
                s.close()
            if conn:
                conn.close()


    def _getClientName(self, cli_addr):
        """ Return the clientName.
        """
        return cli_addr


    def shutdown(self, signum, frame):
        """ Handle the exiting server. Clean all traces """
        self.serverSocket.close()
        print("Cerrando el servidor en %s:%d" % (config["HOST"], config["PORT"]))
        sys.exit(0)


if __name__ == "__main__":
    server = Server(config)
    server.listenForClient()

"""
Fuentes:
http://www.geeksforgeeks.org/creating-a-proxy-webserver-in-python-set-1/
http://www.geeksforgeeks.org/creating-a-proxy-webserver-in-python-set-2/
https://stackoverflow.com/questions/27356946/how-should-i-decode-http-headers-from-bytes-to-string
"""