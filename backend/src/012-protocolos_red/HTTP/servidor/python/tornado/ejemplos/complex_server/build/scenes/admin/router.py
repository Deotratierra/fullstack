#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Admin routes provider"""

from routers import SubRouter

from .Workers import AdminWorkersRenderHandler

class AdminRouter(SubRouter):
    """Admin subrouter"""
    ROUTES = [
        ["/workers", AdminWorkersRenderHandler],
    ]

    def __init__(self, prefix):
    	super(AdminRouter, self).__init__(prefix)
