#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main application router"""

import os
from functools import partial
from json import dumps

from tornado.web import asynchronous
from tornado.gen import coroutine


from base_handlers import BaseAPIRequestHandler
from services.api.models import WorkerModel
from bson_utils import BsonEncoder

class APIWorkersRequestHandler(BaseAPIRequestHandler):
    @property
    def collection(self):
        return self.db["main"]["workers"]

    @asynchronous
    def post(self):
        worker = WorkerModel(self.request_arguments)
        find_queries = [{"title": worker.title},
                        {"address": worker.address}]
        
        async_insert =  partial(
            self.insert_one_if_not_exists, 
                self.collection, find_queries,
                worker.__dict__, on_success=self.on_success_post,
                on_exists=self.on_exists_post, on_error=self.on_error_post
        )
        self.loop.spawn_callback(async_insert)

    def on_success_post(self):
        self.set_status(200)
        self.finish("The worker have been successfully added.")

    def on_exists_post(self):
        self.set_status(202, reason="exists")
        self.finish("The worker already exists!")

    def on_error_post(self, error):
        self.set_status(500, reason=error)
        self.finish(error)
    
    @asynchronous
    def get(self):
        async_find = partial(
            self.find, 
                self.collection,
                on_success=self.on_success_get,
                on_error=self.on_error_get
        )

        self.loop.spawn_callback(async_find)

    def on_success_get(self, response):
        self.set_status(200)
        self.finish(dumps(response, cls=BsonEncoder))

    def on_error_get(self, error):
        self.set_status(500)
        self.finish("Error obtaining workers")
    
            



