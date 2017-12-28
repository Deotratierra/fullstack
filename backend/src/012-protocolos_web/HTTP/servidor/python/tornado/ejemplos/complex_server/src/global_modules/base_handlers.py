#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""BaseHandlers"""

from json import dumps
from tornado.web import RequestHandler

from database_ops import MotorOps
from verifier import Verifier

class BaseRequestHandler(RequestHandler):
    """Base handler for all requests handlers"""

    # =========   INFORMATION METHODS   =========
    @property
    def server_port(self):
        return self.application.server_port

    @property
    def server_host(self):
        return self.application.server_host

    @property
    def domain(self):
        return self.application.domain

    # ==========================================
    
    @property
    def loop(self):
        return self.application.loop

    @property
    def db(self):
        return self.application.db
    
    @property
    def logger(self):
        return self.application.logger



# =======================================================
#   ==========   Page Render Base Handler   ==========

class BaseRenderHandler(BaseRequestHandler):
    pass

# =======================================================



# =======================================================
#   ==============   API Base Handler   =============

SuperAPI = (BaseRequestHandler, MotorOps, Verifier)

class BaseAPIRequestHandler(*SuperAPI):
    """Base handler for all API requests"""
    @property
    def request_arguments(self):
        """Return all arguments of a request in a dict"""
        response = {}
        for key in self.request.arguments:
            value = self.get_argument(key)
            if value != "":
                response[key] = value
        return response

# =======================================================


