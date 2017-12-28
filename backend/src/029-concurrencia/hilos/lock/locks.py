#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading

lock = threading.Lock()

def WC(persona):
    lock.acquire()
    print("%s haciendo sus necesidades" % persona)
    lock.release()

if __name__ == "__main__":
    hombre = threading.Thread(target=WC, args=["hombre"])
    anciano = threading.Thread(target=WC, args=["anciano"])

    hombre.start()
    anciano.start()

    hombre.join()
    anciano.join()
