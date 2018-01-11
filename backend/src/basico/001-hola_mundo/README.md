## Inicializar un programa

___________________________

#### Python
```python
if __name__ == "__main__":
    ...
```

- Ejecutar: python3 archivo.py

___________________________

#### NodeJS
```javascript
if (require.main == module){
    ...
}
```

- Ejecutar: `node archivo.js`

___________________________

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

___________________________

#### Ruby
```ruby
if __FILE__ == $0
    ...
end
```

- Ejecutar: `ruby archivo.rb`

___________________________

#### Bash
```bash
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  ...
fi

```

- Ejecutar: `chmod +x archivo.sh && ./archivo.sh`

___________________________

#### C++ / C
```cpp

int main() {
    ...
}
```

- Compilar ejecutable:
    - C: `gcc <ruta_al_codigo.c> -o <salida_ejecutable>`
    - C++: `g++ <ruta_al_codigo.cpp> -o <salida_ejecutable>`

___________________________

#### LaTeX
```latex
\documentclass{article}
\usepackage[utf8]{inputenc}

\begin{document}
...
\end{document}
```

- Compilar:
    - PDF: `pdflatex <ruta_al_codigo.tex>`
    - HDVI: `latex <ruta_al_codigo.tex>`

_____________________________

#### Batch
- Ejecutar: `archivo` (sin la extensión)

_____________________________

#### Nasm (lenguaje ensamblador)
```nasm
section .text
    global _start
_start:
    ...
```

- Compilar
```bash
nasm -f elf64 -o hello.o hello_world.asm
ld -o hello hello.o
```

