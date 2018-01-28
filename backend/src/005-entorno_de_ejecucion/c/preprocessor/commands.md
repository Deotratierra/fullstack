## Preprocesar en C/C++

### gcc
> En los siguientes ejemplos `archivo.ext` se refiere tanto a `archivo.c` como `archivo.cpp`.

- Para obtener el código preprocesado de un archivo ya sea C++ o C, basta con ejecutar `cpp archivo.ext > archivo.i`, por ejemplo: `cpp main.c > main.i`.
    - También se puede usar: `cc -E archivo.ext > ejemplo1.i`

- Para traducir a ensamblador desde `.i` ejecutar: `cc -S archivo.i`. Obtendremos `archivo.s`.
    - Directamente desde `.c` o `.cpp`: `cc -S archivo.ext`

- Para ensamblar para conseguir código de máquina (código objeto): `as -o archivo.o archivo.s`. Obtendremos `archivo.o`.
    - También se puede usar: `cc -c archivo.s`.

- Para enlazar todos los archivos objeto en un ejecutable: `cc -o ejecutable archivo1.o archivo2.o archivo3.o`.

_____________________________________________

### Utilidades (Linux)
- Desensamblar código objeto o archivos ejecutables: `objdump -d archivo`.
- Obtener las funciones de un archivo de código objeto o ejecutable: `nm archivo`