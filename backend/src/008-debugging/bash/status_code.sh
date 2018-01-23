#!/bin/sh

alert () {
    # uso: alert $? <"Mensaje con variables">
    #
    # Ejemplo:
    #     --------------------------------------------
    #     mail -s "$FROM intentando obtener $FILE" $TO
    #     alert $? "Mail de $LOG a $TO"
    #     --------------------------------------------
    #
    #     Salidas:
    #         Con error:
    #            WARNING: Mail de $LOG a $TO no se completó satisfactoriamente.
    #         Sin error:
    #             INFO: Mail de $LOG a $TO completado satisfactoriamente.

    if [ "$1" -ne 0 ]; then
        echo "WARNING: $2 no se completó satisfactoriamente." >&2
        exit $1
    else
        echo "INFO: $2 completado satisfactoriamente." >&2
    fi
}
