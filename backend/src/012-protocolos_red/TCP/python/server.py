#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import socket
import argparse

ADDRESS = "localhost"
PAYLOAD = 2048
MAX_CLIENTS = 1

def echo_server(port):
    # Por defecto (sin argumentos -> socket.socket()),
    # los sockets en Python se crean de la familia AF_INET,
    # de tipo SOCK_STREAM (sockets de flujo)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Habilitamos la reutilización de direcciones para no tener
    # problemas con el mal cierre de los canales
    # (ver Sockets -> Reutilizar direcciones)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Enlazamos el socket con un servidor y un puerto:
    sock.bind((ADDRESS, port))

    # Ponemos en escucha al socket, indicando el número
    # de conexiones máximas simultáneas permitidas.
    # Si no definimos este número se define por defecto
    # un valor razonable
    sock.listen(MAX_CLIENTS)

    # Aceptamos nuevas conexiones. El método accept()
    # devuelve la conexión del cliente, así como su dirección.
    print("Esperando a recibir clientes...")
    try:
        client, address = sock.accept() # Este método es bloqueante
    except KeyboardInterrupt:
        print("\nServidor interrumpido manualmente antes de aceptar clientes.")
        sock.close()
        sys.exit(0)

    while True:
        try:
            print("Esperando a recibir mensajes del cliente...")

            # Para recibir datos utilizamos el método recv()
            # que toma como parámetro los bytes máximos a aceptar:
            data = client.recv(PAYLOAD)
            if data:
                print("> Recibido: %s" % data)

                # Para enviar datos de vuelta al cliente usamos
                # el método send():
                client.send(data)
                print("< Enviando (%s:%d): %s" % (address[0], address[1], data))

                if data in (b"close", b"off", b"exit", b"CLOSE", b"OFF", b"EXIT"):
                    client.close()
                    print("Apagando el servidor...")
                    break
                elif data == b"hola":
                    pass
                else:
                    exec(data.decode("utf-8"))
                    print(data.decode("utf-8"))
            else:
                client.close()
        except KeyboardInterrupt:
            print("\nServidor interrumpido manualmente.")
            break

    # Para cerrar una conexión usamos el método close()
    sock.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ejemplo de socket servidor")
    parser.add_argument("--port", "-p", action="store", dest="port", type=int, required=True)
    args = parser.parse_args()
    port = args.port

    echo_server(port)
    sys.exit(0)


