#include <stdio.h>
#include <stdlib.h>

int main() {
    char numero[]="0x3076";

    // Conversión de un número hexadecimal a decimal
    unsigned long en_decimal = strtol(numero, NULL, 16);
    printf("%lu\n", en_decimal);

    return 0;
}