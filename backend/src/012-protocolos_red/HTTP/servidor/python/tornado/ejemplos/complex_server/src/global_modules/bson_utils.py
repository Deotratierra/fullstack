#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Bson encoder to work with MongoDB"""

import json
from bson.objectid import ObjectId

class BsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        else:
            return obj

def bsonDecoder(dct):
    for k, v in dct.items():
        if '_id' in k:
            try:
                dct['_id'] = ObjectId(dct['_id'])
            except:
                pass
        return dct