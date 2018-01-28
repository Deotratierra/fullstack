## Sistemas de construcción en SublimeText
Esto nos permite compilar ejecutar el código rápidamente desde SublimeText. Un sistema de construcción es un conjunto de instrucciones que serán ejecutadas en consola para construir y/o correr código.

- Seleccionar sistema de construcción activado: `Tools` -> `Build System` -> `<Sistema>`
- Ejecutar el sistema activado: <kbd>Ctrl</kbd>+<kbd>B</kbd>
- Ejecutar variante: <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>B</kbd>

_____________________________________

### Crear sistema
Para crear un nuevo sistema de construcción vamos a `Tools` -> `Build System` -> `New Build System`. Cada sistema permite variantes que serán mostradas al pulsar <kbd>Ctrl</kbd>+<kbd>B</kbd> para el sistema activado.
Aquí se proveen algunos ejemplos para bash en Unix.

#### C
```json
{
 "cmd":["bash", "-c", "gcc -Wall '${file}' -o '${file_path}/${file_base_name}'"],
 "file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:? (.*)$",
 "working_dir": "${file_path}",
 "selector": "source.c",
 "variants":
 [
   {
     "name": "run",
     "cmd":["bash", "-c", "gcc '${file}' -o '${file_path}/${file_base_name}' && '${file_path}/${file_base_name}'"]
   }
 ]
}
```

#### C++
```json
{
 "cmd":["bash", "-c", "g++ -Wall '${file}' -o '${file_path}/${file_base_name}' && '${file_path}/${file_base_name}'"],
 "file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:? (.*)$",
 "working_dir": "${file_path}",
 "selector": "source.c, source.c++",
 "variants":
 [
   {
     "name": "Run",
     "cmd":["bash", "-c", "g++ -std=c++14 '${file}' -o '${file_path}/${file_base_name}' && '${file_path}/${file_base_name}'"]
   }
 ]
}
```

_______________________________________

> Fuentes:
> - https://stackoverflow.com/questions/37118573/compiling-program-as-c-14-in-sublime-text-3-as-default