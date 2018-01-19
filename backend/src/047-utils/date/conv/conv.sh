#!/bin/bash

# =================================================

# Convierte una cantidad de segundos pasada como
# argumento a XX:XX:XX (horas:minutos:segundos)
function convert_secs() {
  ((h=${1}/3600))
  ((m=(${1}%3600)/60))
  ((s=${1}%60))
  printf "%02d:%02d:%02d\n" $h $m $s
}

convert_secs 7200  # 02:00:00

# =================================================


