#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import websockets # pip3 install websockets

HOST, PORT = ("localhost", 8765)

async def server(websocket, path): # Se ejecuta en cada conexión recibida
    recv = await websocket.recv()
    print("< {}".format(recv))

    if recv == "PING":
        print("> PONG")
        await websocket.send("PONG")
        
    
if __name__ == "__main__":
    start_server = websockets.serve(server, HOST, PORT)

    asyncio.get_event_loop().run_until_complete(start_server)
    try:
        print("Running websocket server at %s:%d" % (HOST, PORT))
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        print("Stopping server...")

"""
Fuente:
https://websockets.readthedocs.io/en/stable/intro.html
"""
