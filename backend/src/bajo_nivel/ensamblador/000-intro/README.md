## Antes de empezar con lenguaje ensamblador
Aquí se incluye información básica antes de empezar a desarrollar con lenguaje ensamblador, para que el comienzo no resulte muy complicado.

### Entorno de trabajo
Lo primero es asegurarnos que estamos en una máquina con una arquitectura compatible con `x86_64` y un sistema operativo Linux. Para otras arquitecturas no estoy seguro de que funcionen todos los ejemplos pero si son de la familia de X80 no debería haber muchos problemas en la mayoría.

#### Compilador
Luego instalamos el compilador: `sudo apt-get install nasm`

[Nasm](https://es.wikipedia.org/wiki/Netwide_Assembler) produce código objeto (con extensión `.o`), el cual no es directamente ejecutable. Para sacar el ejecutable usamos el [enlazador](https://es.wikipedia.org/wiki/Enlazador) `ld` en sistemas Unix:

```
nasm -f elf64 -o archivo.o archivo.asm
ld -o ejecutable archivo.o
```

### Comprensión básica del proceso
Si no has visto ensamblador en tu vida recomiendo [esta lectura](http://www.rinconsolidario.org/eps/asm8086/CAP0.html).