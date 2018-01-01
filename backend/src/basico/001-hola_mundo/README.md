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


_____________________________

## Compilar

#### C++
`g++ <ruta_al_codigo> -o <salida_ejecutable>`

#### C

`gcc <ruta_al_codigo> -o <salida_ejecutable>`