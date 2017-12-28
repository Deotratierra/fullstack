#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""API Router"""

from routers import SubRouter

from services.api.endpoints.workers import APIWorkersRequestHandler

class APIRouter(SubRouter):
    """API subrouter"""
    ROUTES = [
        ["/workers", APIWorkersRequestHandler],
    ]

    def __init__(self, prefix):
    	super(APIRouter, self).__init__(prefix)
