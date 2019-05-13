#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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