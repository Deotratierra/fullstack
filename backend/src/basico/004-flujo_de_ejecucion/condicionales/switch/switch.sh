#!/sh/bin

: '
Las sentencias switch en Bash siguen la siguiente sintaxis:
    -------------------------------------------------------

    case EXPRESION in CASO_1) LISTA_DE_COMANDOS;;
    	              CASO_2_A|CASO_2_B) LISTA_DE_COMANDOS;;
    	              ...
    	              CASO_N) LISTA_DE_COMANDOS;;
    esac
    -------------------------------------------------------

Usamos | para separar entre varios casos. Para los casos
    que se cumplirán por defecto si no se cumple otra opción
    se suele usar *) al final.
'

# -----------------------------------------------------------

NUM=90

case $NUM in
  [1-6][0-9])
    MENSAJE="El número está entre 10 y 69."
    ;;
  [7-8][0-9])
    MENSAJE="Está entre 70 y 89."
    ;;
  9[0-9])
    MENSAJE="El número está entre 90 y 99."
    ;;
  1[0-9][0-9]*)
    MENSAJE="El número es mayor que 99."
    ;;
  *)
    MENSAJE="El número es menor de 10."
    ;;
esac

echo $MENSAJE
