#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio

from wrapper import AsyncPymarketcap


async def main(loop):
    # We init the client - extension of aiohttp.ClientSession
    async with AsyncPymarketcap(loop=loop, debug=True) as acmc:
        pass


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
