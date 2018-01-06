## Inicializar un programa
Para hacerlo de forma controlada, es recomendable usar la siguiente sintaxis en el fichero que ejecutamos:

#### Python
```python
if __name__ == "__main__":
    ...
```

#### NodeJS
```javascript
if (require.main == module){
    ...
}
```

#### HTML
- Javascript puro:
```html
<script>
window.onload = function() {
    ...
}
</script>
```

- JQuery:
```html
<script>
$(window).ready(function() { 
   ... 
});
</script>
```

#### Ruby
```ruby
if __FILE__ == $0
    ...
end
```

#### Bash
```bash
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    ...
fi

```

#### C++ / C
```cpp

int main() {
    ...
}
```

#### LaTeX
```latex
\documentclass{article}
\usepackage[utf8]{inputenc}

\begin{document}
...
\end{document}
```

_____________________________

## Compilar

#### C++
`g++ <ruta_al_codigo.cpp> -o <salida_ejecutable>`

#### C
`gcc <ruta_al_codigo.c> -o <salida_ejecutable>`

#### LaTeX
`pdflatex <ruta_al_codigo.tex>` ó `latex <ruta_al_codigo.tex>`