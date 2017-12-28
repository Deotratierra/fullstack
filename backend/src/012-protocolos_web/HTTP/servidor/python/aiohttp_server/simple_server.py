#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
from aiohttp import web  # pip3 install aiohttp

HOST = "127.0.0.1"
PORT = 8080

# Handlers
async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

# Routes
app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/{name}', handle)

# Server
class HTTPServer:
    def __init__(self, loop, host="127.0.0.1", port=8080):
        self.loop = loop
        self.host = host
        self.port = port

    async def start(self):
        #await self.redis.start()
        await self._start_http_server()

    async def _start_http_server(self):
        return await self.loop.create_server(
            app.make_handler(),
            self.host,
            self.port)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    server = HTTPServer(loop, host, port)
    loop.run_until_complete(server.start())
    print("Listening to {0}:{1}".format(host, port))

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        loop.call_soon(loop.stop)
        print("Stopping server...")