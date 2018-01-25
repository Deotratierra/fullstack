## Enlazado de bibliotecas en C/C++
La forma de enlazar los archivos en tiempo de compilación puede ser **estática** o **dinámica**.

> Para aprender con un ejemplo paso a paso ver el archivo `test.sh`.

### Enlazado estático
La forma estática es la que se utiliza desde el primer momento que se empieza a programar: hemos creado varios archivos `.c` y queremos utilizar funciones de otro archivo dentro del archivo principal, con el objetivo de dividir el código en partes y no trabajar desde el mismo archivo.

El resultado es que todos los archivos .c se compilan en varios archivo .o y luego todos se unen para formar un archivo ejecutable. Este ejecutable contendrá todas las funciones y símbolos de todos los archivos fuente.

> En Unix las bibliotecas estáticas suelen llamarse `libnombre.a`.

### Enlazado dinámico
También tenemos la posibilidad de enlazar dinámicamente los objetos dentro del ejecutable, lo cual otorga ventajas:

- No tenemos que meterlo todo dentro del ejecutable, el cual puede crecer mucho.
- No tenemos por qué compilarlo todo siempre en tiempo de desarrollo.
- Una mejor modularización de nuestro código.
- Nos permite reutilizar código en forma de bibliotecas, código que puede ser reutilizado en varios proyectos (nuestros y de otras personas).
- Si arreglamos un bug en una biblioteca, todos los programas que la utilicen se beneficiarán del cambio.
- Nos permite utilizar bibliotecas implementadas por otras personas.
- Permite ocultar parte de nuestro código y distribuir complementos binarios.
- Damos facilidades para utilizar nuestras bibliotecas a otros desarrolladores, abstrayéndolos de lo que no necesitan conocer para utilizarlas.
- Permite la creación de plugins para nuestras aplicaciones.

> En Unix las bibliotecas dinámicas suelen llamarse `libnombre.so`.