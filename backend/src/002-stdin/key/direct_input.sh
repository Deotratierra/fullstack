#!/bin/bash

# Leer una sóla tecla
stty -echo -icanon min 1
_KEY=$(dd count=1 bs=1 2>/dev/null)
echo "Has pulsado la tecla $_KEY"
stty echo icanon

# ==============================================

# Leer una sóla tecla de un menú de opciones
_key() {
IFS= read -r -s -n1 -d '' "${1:-_KEY}"
}


while :
do
  printf "\n\n\t$bar\n"
  printf "\t %d. %s\n" 1 "Haz algo" \
                       2 "Haz otra cosa" \
                       3 "Salir"
  printf "\t%s\n" "$bar"
  _key
  case $_KEY in
    1) printf "\n%s\n\n" Algo ;;
    2) printf "\n%s\n\n" "Otra cosa" ;;
    3) break ;;
    *) printf "\a\n%s\n\n" "Selección inválida, inténtalo de nuevo"
       continue
       ;;
  esac

  printf ">>> %s " "Presiona cualquier tecla para continuar"
  _key
done
