## Versionado
Con versionado me refiero a ir aumentando la versión de un programa cuando hacemos un commit en un repositorio. En los sistemas de versionado se suele llamar a los 3 espacios de la versión: *major*, *minor* y *micro*.

Por ejemplo, si nuestro programa tiene actualmente la versión 0.7.230, para actualizar la versión debo cambiar manualmente en todos los archivos el número, lo cual es un proceso engorroso. Esto podemos suplirlo con un simple script. Así puedo ejecutar `./version micro` o `./version minor` y el versionado se realizará automáticamente en todos los archivos necesarios.

El script que puedes ver desarrollado en este directorio se compone básicamente de dos nodos: la versión original (una línea en un archivo) y la versión de salida, la cual debe replicarse en varios archivos. El proceso de extraer y depositar las versiones se realiza con lectura/escritura de archivos mediante expresiones regulares.

____________________________________________

### Uso

- Aumentar versión (`major` / `minor` / `micro`):
    + Python: `python3 vss.py major`

- Disminuir versión (`unmajor` / `unminor` / `unmicro`):
    + Python: `python3 vss.py unminor`

____________________________________________

### Obtener nueva versión en Bash
Si necesitamos obtener la nueva versión en un script:

```bash
NEW_VERSION=$(python3 vss.py micro 2>&1)
echo $NEW_VERSION
```
