## Debugging con Python
#### [Referencia](https://docs.python.org/3/library/pdb.html#pdb.Pdb)
Gracias a la biblioteca estándar `pdb` de Python podemos debuggear fácilmente el código, inspeccionándolo línea por línea a través de un script basado en comandos.

Para usarlo debemos importarla al principio del código:
```
import pdb; pdb.set_trace()
```

Al correr el script de nuevo, se ejecutará a través del debugger y veremos la ejecución detenida en la primera línea de código después de la importación, junto al número de línea donde se encuentra.

### Comandos
Los siguientes comandos pueden usarse escribiendo únicamente la primera letra.

- `break <num>`: Inserta un breakpoint donde se detendrá la ejecución en la línea provista por el número pasado como argumento.
- `clear <num>`: Borrar todos los breakpoints si no pasamos un número. Si pasamos un número se borra el breakpoint referido al número (el primero es 1).
- `continue`: El programa se ejecuta hasta encontrar un breakpoint.
- `list <num>`: Muestra las 11 líneas del código adyacentes a la actual. Se puede indicar un número para determinar el número de línas.
- `ll`: Muestra todo el código fuente de la función o frame actual.
- `next`: Ejecuta la siguiente línea de código.
- `p <variable>`: Inspecciona el valor de una variable ejecutada (`print`). Escribe `pp` para usar `prettyprint`
