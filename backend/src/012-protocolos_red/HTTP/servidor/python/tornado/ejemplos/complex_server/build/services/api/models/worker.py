#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Worker Models"""

from services.api.models import BaseModel

class WorkerModel(BaseModel):
    def __init__(self, fields):
        super(WorkerModel, self).__init__(fields)

