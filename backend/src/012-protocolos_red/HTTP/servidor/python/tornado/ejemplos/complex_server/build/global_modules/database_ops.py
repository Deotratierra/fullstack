#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Common database operations"""

from tornado.web import asynchronous

class MotorOps:
    """Class to performs common async database operations

    Include it as parent of a RequestHandler and call """

    # =========   COMMON OPERATIONS   =========

    # DELETE
    async def delete_all(self, collection, delete_query,
                         on_success=None, on_not_exists=None,
                         on_error=None):
        """Delete all document in collection matching a query.

        :param collection:: Collection where do insert
        :type collection: <class 'motor_tornado.MotorCollection'>

        :param find_delete_query: Dictionary or list of dictionaries
            to find documents in database and delete it if exists.
        :type find_delete_query: list/dict

        :param on_success: Callback if the delete success
            (optional, default == None)
        :type on_success: function

        :param on_not_exists: Callback if the requested element/s not
            exists in database (optional, default == None)
        :type on_not_exists: function

        :param on_error: Callback if a error happens during the process
            (optional, default == None)
        :type on_error: function
        """
        try:
            response = await collection.delete_many(delete_query)
            print(response.deleted_count)
            if response.deleted_count == 0:
                if on_not_exists: on_not_exists()
            else:
                if on_success: on_success() # <pymongo.results.DeleteResult object at 0x7fc7b69a60c8>
        except Exception as error:
            self.logger.database.error("DELETE_ALL ERROR: %s", error)
            if on_error: on_error(str(error))

    # FIND
    async def find(self, collection, limit=None,
                   on_success=None, on_any=None, on_error=None):
        """Find all documents in a collection o limiting
        the number of them. If isn't limited, returns an async
        iterator.

        https://motor.readthedocs.io/en/stable/tutorial-tornado.html#querying-for-more-than-one-document

        Example call:
        ----------------------------------------------------------
        async_find = partial(
            self.find,
                self.collection,
                on_success=self.on_success_get,
                on_error=self.on_error_get,
                on_any=self.on_any_get
        )
        self.loop.spawn_callback(async_find)
        ----------------------------------------------------------

        Example callback:
        ----------------------------------------------------------
        def on_success_get(self, response):
            self.set_status(200)
            self.finish(dumps(response, cls=BsonEncoder))
        ----------------------------------------------------------


        :param collection: Collection to find in
        :type colection: <class 'motor_tornado.MotorCollection'>

        :param limit: Number of documents to return, all by default
            (optional, default == None)
        :type limit: int

        :param on_success: Callback if the search success and exists
            documents. Returns response as first param.
            (optional, default == None)
        :type on_success: function

        :parm on_any: Callback if the search success and not exists
            any document in the collection (optional, default == None)
        :type on_any: function

        :param on_error: Callback if the search fails. Returns error
            as first param.
            (optional, default == None)
        :type on_error: function
        """
        response = []
        try:
            if limit:
                count = 0
                async for document in collection.find():
                    response.append(document)
                    count += 1
                    if count >= limit: break
            else:
                async for document in collection.find():
                    response.append(document)
        except Exception as error:
            self.logger.database.error("FIND_ALL ERROR: %s", error)
            if on_error: on_error(error)
        else:
            if len(response) == 0:
                msg = "FIND_ALL returns any documents"
                self.logger.database.debug(msg)
                if on_any: on_any()
            else:
                msg = "FIND_ALL returns next documents: %s"
                self.logger.database.debug(msg, response)
                if on_success: on_success(response)

    # INSERT
    async def insert_one_if_not_exists(self, collection,
                                find_query, insert_query,
                                on_success=None, on_exists=None,
                                on_error=None):
        """Insert a document in a collection if it doesn't
        already exists --> collection.find_one(find_query) == None
        You can pass a list of queries to find a document,
        and only be inserted if any of these return a document.

        Example call:
        ---------------------------------------------------------
        async_insert =  partial(
            self.insert_one_if_not_exists,
                self.collection, find_queries,
                worker.__dict__, on_success=self.on_success_post,
                on_exists=self.on_exists_post, on_error=self.on_error_post
        )

        self.loop.spawn_callback(async_insert)
        ---------------------------------------------------------

        :param collection: Collection where do insert
        :type collection: <class 'motor_tornado.MotorCollection'>

        :param find_query: Dictionary or list of dictionaries
            to find documents in database. If any of these exists,
            the insertion will be done.
        :type find_query: list/dict

        :param insert_query: Dictionary with the keys and values
            to insert in the database.
        :type insert_query: dict

        :param on_success: Callback if the insert query is done.
            Returns result of the query as first param.
            (optional, default == None)
        :type on_success: function

        :param on_error: Callback if the insert query fails.
            Returns the error of the insert as first param.
            (optional, default == None)
        :type on_error: function

        :param on_exists: Callback if the document already exists
            on database. (optional, default == None)
        :type on_exists: function
        """
        async def do_find():
            if isinstance(find_query, list):
                documents = []
                for query in find_query:
                    result = await collection.find_one(query)
                    documents.append(result)
                document = True if all(documents) == True else False
            else:
                document = await collection.find_one(find_query)
            return document

        async def do_insert():
            result = await collection.insert_one(insert_query)
            self.logger.database.debug("INSERT: %s", result.inserted_id)
            return result

        try:
            found = await do_find()
        except Exception as error:
            self.logger.database.error("FIND_ONE ERROR: %s", error)
            if on_error:  on_error(str(error))

        if not found:
            try:
                result = await do_insert()
            except Exception as error:
                self.logger.database.error("INSERT_ONE ERROR: %s", error)
                if on_error:  on_error(str(error))
            else:
                if on_success:  on_success()
        else:
            msg = "The query was found, document not inserted"
            self.logger.database.debug(msg)
            if on_exists: on_exists()

    # UPDATE
    async def replace_if_exists(self, collection, find_query, document_replacer,
                          on_success=None, return_replaced=False,
                          on_error=None, on_not_exists=None):
        """Replace a document in a collection if exists.
        >>> collection.find_one(find_query) != None

        Example call:
            ----------------------------------------
            async_replace = partial(
                self.replace_if_exists,
                    self.collection, find_query, args,
                    on_success=self.on_success_patch,
                    on_error=self.on_error_patch
            )
            self.loop.spawn_callback(async_replace)
            ---------------------------------------

        Example callback:
            ---------------------------------------
            def on_error_patch(self, error):
                self.set_status(500, reason=str(error))
                self.finish("Error editing. Please, try again.")
            ---------------------------------------

        :param collection: Collection where do update
        :type collection: <class 'motor_tornado.MotorCollection'>

        :param find_query: Dictionary to find  a document in database.
            If exists, it will be replaced.
        :type find_query: dict

        :param document_replacer: Document in form of dictionary
            which will replace the document.
        :type document_replacer: dict

        :param on_success: Callback if the replace query is done.
            Returns the new document if param return_replaced == True.
            (optional, default == None)
        :type on_success: function

        :param return_replaced: Returns the new document in
            on_success callback if True, otherwise, the callback
            returns anything (optional, default == False)
        :type return_replaced: bool

        :param on_error: Callback if the update query fails.
            Returns the error of the insert as first param.
            (optional, default == None)
        :type on_error: function

        :param on_not_exists: Callback if the document not exists
            on database. (optional, default == None)
        :type on_not_exists: function
        """
        async def do_find(query):
            try:
                document = await collection.find_one(query)
            except Exception as e:
                print(e)
            return document

        async def do_replace(_id):
            result = await collection.replace_one({"_id": _id},
                                                  document_replacer)
            return result

        try:
            document = await do_find(find_query)
        except Exception as error:
            self.logger.database.error("FIND_ONE ERROR: %s", error)
            if on_error: on_error(error)
        else:
            if document:
                try:
                    result = await do_replace(document["_id"])
                except Exception as error:
                    if on_error: on_error(error)
                else:
                    self.logger.database.debug("REPLACE_ONE: %s", result.upserted_id)
                    if on_success:
                        if return_replaced:
                            try:
                                new_document = await do_find(document["_id"])
                            except Exception as error:
                                if on_error: on_error(error)
                                self.logger.database.error("FIND_ONE ERROR: %s", error)
                            else:
                                on_success(new_document)
                        else:
                            on_success()
            else:
                msg = "Document not found, so could not been replaced."
                self.logger.database.debug(msg)
                if on_not_exists: on_not_exists()


