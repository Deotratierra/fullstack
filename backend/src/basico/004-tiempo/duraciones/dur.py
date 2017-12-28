#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import timedelta
# https://docs.python.org/2/library/datetime.html#timedelta-objects

# Establecer duraciones
un_minuto = timedelta(minutes=1)
diez_minutos = un_minuto * 10

# Convertir entre duraciones
diez_minutos_en_segundos = diez_minutos.seconds
print(diez_minutos_en_segundos) # 600

# Representación como string
print(diez_minutos)  # 0:10:00

# Obtener los segundos totales de la duración
print(un_minuto.total_seconds())  # 60.0
