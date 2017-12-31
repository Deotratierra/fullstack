import os
from multiprocessing import Process, Queue

# ============  OPCION 1: Colas # ============

def enviar(cola, *mensajes):
    info = (os.getpid(), mensajes)
    print("Proceso %d enviando los mensajes: %r" % info)
    [cola.put(mensaje) for mensaje in mensajes]

def recibir(cola):
    mensajes = []  # Recoge todos los mensajes de la cola
    while not cola.empty():
       mensajes.append(cola.get())
    info = (os.getpid(), mensajes)
    print("Proceso %d recibe los mensajes: %r" % info)
    

# La clase Queue() del módulo multiprocessing es casi un clon 
# de la del módulo queue. Gracias a esta podemos intercambiar
# información entre procesos
cola = Queue()    

# Creamos un proceso que envía información...
remitente = Process(target=enviar, 
                    args=(cola, "Mensaje 1", 2, True))
# ... y otro que la recibe
receptor = Process(target=recibir, args=(cola,))

remitente.start()
remitente.join()

receptor.start()
receptor.join()

# =================================================

print("\n ====================== \n")

# =============  OPCIÓN 2: Tuberías ===============

import time
from multiprocessing import Pipe

def servidor(conexion):
    while True:
        mensaje = conexion.recv()
        info = (os.getpid(), mensaje)
        print("Proceso %d (servidor) recibe el mensaje: %r" % info)
        if mensaje in ("PING", "OFF"):
            break
        conexion.send(True)
    
    if mensaje == "PING":
        conexion.send("PONG")
    conexion.close()
    print("Proceso %d (servidor): conexión cerrada" % os.getpid())

def cliente(conexion, *mensajes):
    for mensaje in mensajes:
        info = (os.getpid(), mensaje)
        print("Proceso %d (cliente) envía el mensaje: %r" % info)
        conexion.send(mensaje)
        recibido = conexion.recv()
        info = (os.getpid(), recibido)
        print("Proceso %d (cliente) recibe el mensaje: %r" % info)
        if mensaje == "PONG":
            conexion.close()
            print("Proceso %d (cliente): conexión cerrada" % os.getpid())
            break

# Creamos dos extremos de conexión de la tubería
extremo1, extremo2 = Pipe()
p_cliente = Process(target=cliente,
                    args=(extremo1, "Primer mensaje", "PING"))
p_servidor = Process(target=servidor,
                     args=(extremo2,))

# Lanzamos el proceso servidor
p_servidor.start()
time.sleep(1)
p_cliente.start()

p_cliente.join()
p_servidor.join()

# ================================================
