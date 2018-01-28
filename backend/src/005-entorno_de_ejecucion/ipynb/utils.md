## Utilidades IPythonNotebook

### Tutoriales
- [El completo sistema de Display](http://nbviewer.jupyter.org/github/ipython/ipython/blob/2.x/examples/Notebook/Display%20System.ipynb#LaTeX)

______________________________

### Comandos útiles

#### Eliminar scroll por defecto en las salidas
```js
%%javascript
IPython.OutputArea.prototype._should_scroll = function(lines) {
    return false;
}
```


________________________________

### Notebooks online
- Para ejecutar notebooks en la nube: https://try.jupyter.org/
- Para correr notebooks en la nube gratis desde un repositorio de Github podemos usar [Binder](https://mybinder.org/). Para configurar las dependencias, seguir [este tutorial](http://mybinder.readthedocs.io/en/latest/using.html#preparing-a-repository-for-binder).
- Para visualizar notebooks estáticos (también es posible en Github) la web más famosa es [Nbviewer](http://nbviewer.jupyter.org/).






