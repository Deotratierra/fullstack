#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Base Routers"""

class SubRouter:
    """Base router. For use, insert
    in child class a property with the
    routes and pass the prefix"""
    def __init__(self, prefix):
        self.prefix = prefix

    @property
    def routes(self):
        """Return routes builded"""
        return self._build_routes()

    def _build_routes(self):
        """Admin routes builder"""
        builder = []
        for route in self.ROUTES:
            route = self.prefix + route[0], route[1]
            builder.append(route)
        return builder
