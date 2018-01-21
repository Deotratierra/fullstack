#!/usr/bin/env bats

# ==========================================
# Unittesting con Bats

# Instalación
' :
git clone https://github.com/sstephenson/bats.git
cd bats
./install.sh /usr/local
'

# Uso:
# bats unittesting.sh

# ==========================================

# Comprobar resultados
@test "Suma usando bc" {
    result="$(echo 2+2 | bc)"
    [ "$result" -eq 4 ]
}

@test "Suma usando dc" {
    result="$(echo 2 2+p | dc)"
    [ "$result" -eq 4 ]
}

# Correr comandos
@test "Comprobar sistema operativo" {
    run uname -s
    [ "$status" -eq 0 ]     # Obtener estado
    [ "$output" = "Linux" ] # Obtener salida

}

# Saltar tests
@test "Un test que no quiero ejecutar por ahora" {
  skip    # <--  Indicamos que queremos saltarlo
  run foo
  [ "$status" -eq 0 ]
}


# Fuente:
# https://github.com/sstephenson/bats