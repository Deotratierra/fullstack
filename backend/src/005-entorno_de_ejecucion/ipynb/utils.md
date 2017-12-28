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

### Compartir notebooks online
- [Nbviewer](http://nbviewer.jupyter.org/)




