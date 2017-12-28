#!/bin/bash

# ===============================================

###   Medir tiempo dentro de un script   ###

ns_start=`date +%s%N`
start=`date +%s`

sleep 3

ns_end=`date +%s%N`
end=`date +%s`
let ns_total=$ns_end-$ns_start
let total=$end-$start

echo "Tiempo de ejecución: $ns_total nanosegudos, $total segundos"

# ===============================================

###   Medir tiempo de comandos   ###

time sleep 3

# ===============================================
