#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main application router"""

import os
from functools import partial
from json import dumps
from bson.objectid import ObjectId

from tornado.web import asynchronous
from tornado.gen import coroutine


from base_handlers import BaseAPIRequestHandler
from services.api.models import WorkerModel
from bson_utils import BsonEncoder

class APIWorkersRequestHandler(BaseAPIRequestHandler):
    @property
    def collection(self):
        return self.db["main"]["workers"]

    #        =========     SAVE WORKERS     =========
    @asynchronous
    def post(self):
        # Get arguments
        args = self.request_arguments

        # Verify them
        self.verify_dict(args, str, lenght=3,
                         on_error=self.on_error_post)

        # Insert in database
        find_queries = [{"title": args["title"]},
                        {"address": args["address"]}]

        async_insert =  partial(
            self.insert_one_if_not_exists,
                self.collection, find_queries,
                args, on_success=self.on_success_post,
                on_exists=self.on_exists_post,
                on_error=self.on_error_post
        )
        self.loop.spawn_callback(async_insert)

    def on_success_post(self):
        self.set_status(200)
        try:
            self.finish("The worker have been successfully added.")
        except RuntimeError as error:
            pass

    def on_exists_post(self):
        self.set_status(202, reason="exists")
        try:
            self.finish("The worker already exists!")
        except RuntimeError:
            pass

    def on_error_post(self, error):
        self.set_status(500, reason=str(error))
        self.finish(dumps(error))

    # ==========================================================

    #        =========     GET WORKERS     =========
    @asynchronous
    def get(self):
        async_find = partial(
            self.find,
                self.collection,
                on_success=self.on_success_get,
                on_error=self.on_error_get,
                on_any=self.on_any_get
        )

        self.loop.spawn_callback(async_find)

    def on_success_get(self, response):
        self.set_status(200)
        self.finish(dumps(response, cls=BsonEncoder))

    def on_error_get(self, error):
        self.set_status(500, reason=str(error))
        self.finish("Error obtaining workers")

    def on_any_get(self):
        self.set_status(200)
        self.finish(dumps([]))

    # ==========================================================

    #        =========     DELETE WORKERS     =========
    @asynchronous
    def delete(self):
        try:
            delete_query = {"_id": ObjectId(self.get_argument("_id"))}
        except Exception as error:
            self.on_error_delete(str(error))
        else:
            async_delete = partial(
                self.delete_all,
                    self.collection, delete_query,
                    on_success=self.on_success_delete,
                    on_error=self.on_error_delete
            )
            self.loop.spawn_callback(async_delete)

    def on_success_delete(self):
        self.set_status(200)
        self.finish("Worker removed successfully")

    def on_error_delete(self, error):
        self.set_status(500, reason=str(error))
        self.finish("Error removing worker. Please, try again.")
    # ==========================================================

    #        =========     EDIT WORKERS     =========
    @asynchronous
    def patch(self):
        # Get arguments
        args = self.request_arguments

        # Verify them
        self.verify_dict(args, str, lenght=4,
                         on_error=self.on_error_patch)

        find_query = {"_id": ObjectId(args["_id"])}
        del args["_id"]

        async_replace = partial(
            self.replace_if_exists,
                self.collection, find_query, args,
                on_success=self.on_success_patch,
                on_error=self.on_error_patch
        )
        self.loop.spawn_callback(async_replace)


    def on_success_patch(self):
        self.set_status(200)
        self.finish("Worker edited successfully")

    def on_error_patch(self, error):
        self.set_status(500, reason=str(error))
        self.finish("Error editing worker. Please, try again.")

    # ==========================================================
