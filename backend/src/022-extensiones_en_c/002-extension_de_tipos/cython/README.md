## Extendiendo tipos (clases) en Cython
#### [Referencia](http://cython.readthedocs.io/en/latest/src/userguide/extension_types.html)

La palabra clave `cdef` también puede ser colocada delante de una definición de clase para crear un tipo extendido. Un tipo extendido es similar a una clase de Python pero sus atributos deben ser tener tipado y son almacenados en un eficiente struct de C.

Podemos extender tipos usando la declaración `cdef class` y declarando sus atributos dentro del cuerpo de la clase (donde se colocan los atributos de clase).

> [Ejemplo de extensión de tipos en Python](https://github.com/mondeja/fullstack/tree/master/backend/src/022-extensiones_en_c/002-extension_por_tipos/cython) (cy)

Por defecto, los atributos declarados en una clase Cython son privados. Para acceder a ellos mediante la sintaxis `clase.atributo` debemos anteponer la palabra `static` al declararlos.

_______________________________________________________
