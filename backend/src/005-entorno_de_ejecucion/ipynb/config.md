### Configuración de IpythonNotebook

#### Ejecutar IPython notebook en un entorno virtual

- Primero instalamos ipykernel: `pip3 install ipykernel`
- Luego añadimos el kernel del entorno virtual al notebook: 
```sh
python3 -m ipykernel install --user --name=<nombre_del_entorno>
```

Cuando entremos al notebook, vamos a `Kernel -> Change kernel` y elegimos nuestro entorno virtual.

#### Añadir kernel Javascript a IPython
```sh
cd /usr/local/share/jupyter/kernels
sudo git clone https://github.com/minrk/jskernel
```

>Fuente: https://github.com/minrk/jskernel


#### Acceso a los kernels de IPython (en Linux)

`cd /usr/local/share/jupyter/kernels`

>Fuente: http://jupyter.readthedocs.io/en/latest/projects/jupyter-directories.html