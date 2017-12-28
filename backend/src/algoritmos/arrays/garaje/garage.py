#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def garage(initial, final):
    steps = 0
    len_initial = len(initial)
    while initial != final:
        zero = initial.index(0) # Buscamos el índice del 0
        if zero != final.index(0): # Si el 0 no está en el índice final
            car_to_move = final[zero] # cogemos el coche de la posición final del 0
            pos = initial.index(car_to_move) # extraemos su posición
            initial[zero], initial[pos] = initial[pos], initial[zero] # y lo cambiamos por el 0
        else:  # Si ya lo está, buscamos otro número
            for i in range(len_initial):
                if initial[i] != final[i]: # Si el número no está en su posición final
                    initial[zero], initial[i] = initial[i], initial[zero] # lo cambiamos por el 0
                    break
        steps += 1
        #print(initial)  # Descomentar para verlo paso a paso
    return steps

if __name__ == "__main__":
    initial = [1, 2, 3, 0, 4]
    final =   [0, 3, 2, 1, 4]
    print("initial:", initial)
    print("final:", final)
    print(garage(initial, final))