## Clases en Cython
Para soportar programación orientada a objetos, Cython permite escribir clases de Python igual que lo hacemos en Python.

#### Extensión de tipos
Sin embargo, basado en lo que Python llama un "tipo empotrado" ("built-in type"), Cython soporta una segunda forma de clase: las **extensiones de tipos**, a veces denominadas *`cdef classes`* debido a las palabras usadas para su declaración.

#### Ventajas y desventajas
Están algo más restringidas que las clases de Python, pero son generalmente más eficientes en memoria y rápidas. La diferencia principal es que usan una estructura (`struct`) de C para almacenar sus campos y métodos en lugar que un diccionario (`dict`) de Python. Esto les permite almacenar tipos de C arbitrarios en sus campos sin requerir una envoltura de Python para ello, además de acceso a los campos y métodos directamente a nivel de C sin pasar por un dicccionario de Python.

____________________________________________________

### Gestionando los miembros
Los miembros de una clase `cdef` se declaran en el cuerpo de la clase, dónde se colocan los atributos de clase de las clases de Python clásicas, antes del cnstructor.

Por defecto los mimebros no son accesibles desde fuera, pues están definidos como privados (`private`). Para leerlos únicamente debemos indicar `readonly` al definirlos, antes del tipo de la variable. Para leerlos y escribirlos en tiempo de ejecución debemos indicar `public`.

____________________________________________________

### Inicialización y limpieza a nivel C
El hecho de que tengamos una `struct` de C detrás de cada extensión de tipo tiene otras implicaciones, particularmente en la creación e inicialización de objetos.

#### Inicialización
Cuando Python llama a `__init__`, requiere el argumento `self` para ser una instancia valida de ese tipo extendido. Cuando `__init__` es llamado, este método típicamente inicializa los atributos en el argumento de la instancia (`self`). A nivel de C, antes de que `__init__` sea llamado, la `struct` de la instancia debe ser asignada (en memoria -> *allocated*) y todos los campos de la estructura deben estar en un estado válido, preparados para aceptar valores iniciales.

Cython agrega un método especial llamado `__cinit__` el cual es responsable de realiar las operaciones de asignación e inicialización a nivel de C. Para algunas clases no suele ser necesario escribir su método `__cinit__` y podemos inicializarlas con el constructor clásico `__init__`. Pero es posible que hubiera constructores alternativos e `__init__` fuera llamado varias veces durante la creación del objeto. En otras otras situaciones es posible que `__init__` fuera puenteado ignorando su comportamiento por completo.

Cython garantiza que llama a `__cinit__` exactamente una vez y antes de `__init__`, `__new__` y otros constructores alternativos de Python como los constructores de clase.

#### Limpieza de memoria
Cython también provee finalización a nivel de C mediante el método especial `__dealloc__`. La responsabilidad de este método es deshacer lo que `__cinit__` realizó durante la creación. Si está definido, Cython se asegura de llamar a `__dealloc__` una vez durante la finalización.

____________________________________________________

#### Herencia

Las clases de Python normales pueden heredar de las clases `cdef`, pero no al revés. Cython requiere conocer la jerarquía completa de herencia para diseñar sus estructuras de C y las restringe a **una sóla herencia** del tipo `cdef`. Las clases normales de Python, por otra parte, pueden heredar de cualquier cantidad de clases y extensiones de tipos, ya sean de código Cython o de puro Python.

____________________________________________________

> Fuentes:
> - http://cython.readthedocs.io/en/latest/src/userguide/extension_types.html
> - http://apprize.info/python/cython/5.html