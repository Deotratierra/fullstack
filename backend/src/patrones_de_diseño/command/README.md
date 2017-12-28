## Patrón comando
El patrón comando se usa para encapsular y empaquetar toda la información necesaria para invocar un método o una petición. Hace más fáil construir colas, loguear o deshacer operaciones. De muchas formas puede considerarse como una transacción o un reemplazo orientado a objetos de los callbacks.

### Ejemplos de uso
#### Editor de textos
Imagina que tenemos un editor de textos que soporta características como **negritas**, *cursivas*, etc... así como realizar operaciones de deshacer (<kbd>Ctrl</kbd> + <kbd>Z</kbd>). Para ello, debemos guardar en memoria un historial con las últimas operaciones realizadas.

Usando el patrón comando, cada opción de formateo del texto es representada por un comando concreto. Cuando llega un comando al editor, este se guarda en una cola de ejecución y se ejecutan todos los comandos en cola a través del método `ejecutar()` de cada uno. Cada comando ejecutado se guarda en un historial. Si llega un evento de deshacer, se saca el último comando del historial y se llama al método `deshacer()` del comando.