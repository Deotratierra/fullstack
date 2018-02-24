#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

from aiohttp import ClientSession
from tqdm import tqdm


logger = logging.getLogger(__name__)
console = logging.StreamHandler()
logger.addHandler(console)

class AsyncPymarketcapScraper(ClientSession):
    def __init__(self, queue_size=10,
    	         progress_bar=False, debug=False,
    	         num_dlq_consumers=10, **kwargs):
        super(AsyncPymarketcap, self).__init__(**kwargs)
        self.queue_size = queue_size
        self._responses = []
        self.progress_bar = progress_bar
        self.num_dlq_consumers = num_dlq_consumers
	        if debug:
	    logger.setLevel(logging.DEBUG)

	async def single_download(self, url):
        async with self.get(url) as res:
            return await res.json()




