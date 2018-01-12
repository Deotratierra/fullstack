#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Base API models"""

class BaseModel:
    """Base model to work with API data models"""
    def __init__(self, fields_dict):
        for key, value in fields_dict.items():
            setattr(self, key, value)
