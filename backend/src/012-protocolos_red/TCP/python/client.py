#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import socket
import time
import argparse

ADDRESS = "127.0.0.1"

def echo_client(port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Utilizamos el método connect para conectarnos a un socket
    sock.connect((ADDRESS, port))
    print("Conectando a %s:%d" % (ADDRESS, port))

    for msg in ["hola", message, "off"]:
        try:
            # Enviar mensaje
            print("< Enviado: %s" % msg)
            # Codificamos desde utf8 para enviar el mensaje
            sock.sendall(msg.encode("utf-8"))

            # Obtener respuesta
            cantidad_recibida = 0
            cantidad_esperada = len(msg)
            while True:
                # Obtenemos la respuesta
                data = sock.recv(16)
                # Decodificamos para obtener la respuesta en utf-8
                data_decoded = data.decode("utf-8")
                cantidad_recibida += len(data)
                print("> Recibido: %s" % data_decoded)
                if cantidad_recibida >= cantidad_esperada:
                    break
        except socket.errno as err:
            print("Error de socket: %s" % str(err))
            sys.exit(1)
        except KeyboardInterrupt:
            print("Socket interrumpido manualmente.")
        except Exception as err:
            print("Excepción desconocida: %s" % str(err))
            sys.exit(1)
        finally:
            if msg not in ("close", "off", "exit", "CLOSE", "OFF", "EXIT"):
                time.sleep(1)

    # Cerrar el socket
    sock.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ejemplo de socket cliente')
    parser.add_argument('--port', "-p", action="store", 
                        dest="port", type=int, required=True)
    parser.add_argument('--message', "-m", action="store",
                        dest="message", type=str, required=True)
    args = parser.parse_args()
    port = args.port
    message = args.message

    echo_client(port, message)
    sys.exit(0)
