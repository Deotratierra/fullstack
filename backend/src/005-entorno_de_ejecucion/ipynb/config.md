### Configuración de IpythonNotebook

#### Ejecutar IPython notebook en un entorno virtual

- Primero instalamos ipykernel: `pip3 install ipykernel`
- Luego añadimos el kernel del entorno virtual al notebook:
```sh
python3 -m ipykernel install --user --name=<nombre_del_entorno>
```

Cuando entremos al notebook, vamos a `Kernel -> Change kernel` y elegimos nuestro entorno virtual.

_________________________

#### [Añadir nuevos kernels](https://github.com/mondeja/fullstack/tree/master/backend/src/005-entorno_de_ejecucion/ipynb/kernels.md)


