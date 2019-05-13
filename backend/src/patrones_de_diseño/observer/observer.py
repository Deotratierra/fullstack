#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Ejemplo de eventos simple, muy similar a la sintaxis
  ``on(eventName, func)`` de Javascript.
"""

class Event(object):
    pass

class Observable(object):

    def __init__(self):
        self.callbacks = {}

    def on(self, event_name, callback):
    	try:
    	    event_callbacks = self.callbacks[event_name]
    	except KeyError:
    		self.callbacks[event_name] = []
    		event_callbacks = self.callbacks[event_name]
    	self.callbacks[event_name].append(callback)        

    def fire(self, event_name, **attrs):
        e = Event()
        e.source = self
        for k, v in attrs.items():
            setattr(e, k, v)

        try:
            event_callbacks = self.callbacks[event_name]
        except KeyError:
            pass
        else:
	        for cb in event_callbacks:
	            cb(e)

"""python3 -i observer.py

>>> class Gallina(Observable):
...     def poner_huevo(self):
...         self.fire("poner_huevo")
... 
>>> gallina = Gallina()
>>> gallina.on("poner_huevo", lambda e: print("He puesto un huevo", e))

>>> gallina.poner_huevo()
He puesto un huevo <__main__.Event object at 0x7fd7c7077c18>
"""

# ----------------------------------------------------------------------

"""Ejemplo de evento usando un decorador."""

class event(object):
    def __init__(self, func):
        self.__doc__ = func.__doc__
        self._key = ' ' + func.__name__
    def __get__(self, obj, cls):
        try:
            return obj.__dict__[self._key]
        except KeyError:
            be = obj.__dict__[self._key] = boundevent()
            return be

class boundevent(object):
    def __init__(self):
        self._fns = []
    def __iadd__(self, fn):
        self._fns.append(fn)
        return self
    def __isub__(self, fn):
        self._fns.remove(fn)
        return self
    def __call__(self, *args, **kwargs):
        for f in self._fns[:]:
            f(*args, **kwargs)

# producer
class MyJob(object):
    @event
    def progress(pct):
        """Se ejecuta cuando cierto progreso del trabajo se ha completado.
        Se pasa como parámetro el porcentaje completado del trabajo."""

    def run(self):
        n = 10
        for i in range(n+1):
            self.progress(100.0 * i / n)

#consumer
"""python3 -i observer.py

>>> import sys
>>> job = MyJob()
>>> job.progress += lambda pct: sys.stdout.write("%.1f%% done\n" % pct)
>>> job.run()
0.0% done
10.0% done
20.0% done
30.0% done
40.0% done
50.0% done
60.0% done
70.0% done
80.0% done
90.0% done
100.0% done
"""

# Fuentes:
# https://stackoverflow.com/questions/1904351/python-observer-pattern-examples-tips
