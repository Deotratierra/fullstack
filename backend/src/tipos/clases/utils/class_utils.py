#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Obtener todos los métodos no especiales de una clase
method_list = [func for func in dir(Foo) \
                   if callable(getattr(Foo, func)) and not func.startswith("__")]
