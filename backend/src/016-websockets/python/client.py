#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import websockets

HOST, PORT = ("localhost", 8765)

async def client():
    async with websockets.connect("ws://%s:%d" % (HOST, PORT)) as websocket:
        await websocket.send("PING")
        print("> PING")

        response = await websocket.recv()
        print("< {}".format(response))

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(client())