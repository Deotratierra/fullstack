#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""AdminHome handlers"""

import os

from base_handlers import BaseRenderHandler

class AdminWorkersRenderHandler(BaseRenderHandler):
    """AdminWorkersRenderHandler"""
    def get(self):
        html = os.path.join(os.path.dirname(__file__), "index.html")
        return self.render(html)
