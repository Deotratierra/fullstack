## Clases en Cython
Para soportar programación orientada a objetos, Cython permite escribir clases de Python igual que lo hacemos en Python.

### Extensión de tipos
Sin embargo, basado en lo que Python llama un "tipo empotrado" ("built-in type"), Cython soporta una segunda forma de clase: las **extensiones de tipos**, a veces denominadas *`cdef classes`* debido a las palabras usadas para su declaración.

#### Ventajas y desventajas
Están algo más restringidas que las clases de Python, pero son generalmente más eficientes en memoria y rápidas. La diferencia principal es que usan una estructura (`struct`) de C para almacenar sus campos y métodos en lugar que un diccionario (`dict`) de Python. Esto les permite almacenar tipos de C arbitrarios en sus campos sin requerir una envoltura de Python para ello, además de acceso a los campos y métodos directamente a nivel de C sin pasar por un dicccionario de Python.

#### Gestionando los miembros
Los miembros de una clase `cdef` se declaran en el cuerpo de la clase, dónde se colocan los atributos de clase de las clases de Python clásicas, antes del cnstructor.

Por defecto los mimebros no son accesibles desde fuera, pues están definidos como privados (`private`). Para leerlos únicamente debemos indicar `readonly` al definirlos, antes del nombre de la variable. Para leerlos y escribirlos en tiempo de ejecución debemos indicar `public`.

#### Herencia

Las clases de Python normales pueden heredar de las clases `cdef`, pero no al revés. Cython requiere conocer la jerarquía completa de herencia para diseñar sus estructuras de C y las restringe a **una sóla herencia**. Las clases normales de Python, por otra parte, pueden heredar de cualquier cantidad de clases y extensiones de tipos, ya sean de código Cython o de puro Python.

