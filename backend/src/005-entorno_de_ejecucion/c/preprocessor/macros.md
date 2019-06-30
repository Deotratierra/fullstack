## Macros comunes en los compiladores

### `_DEBUG` y `NDEBUG`
En la mayoría de compiladores, cuando compilamos un archivo pasando la opción de línea de comandos `-D` (Unix) o `/D` (Windows), estamos inidicando que la compilacion se está haciendo en modo de *debugging*. Esto puede ser bastante útil para incluir salidas por consola que sirvan de ayuda. Cuando pasemos la opción, la directiva `_DEBUG` será definida, pero si no la pasamos `NDEBUG` será definida en su lugar:

```c
void f()
{
#ifdef _DEBUG
    printf("LLamando a la función f()\n");
#endif
    // Código sin salida por pantalla...
}
```

### `__cplusplus`

Esta macros es definida por la mayoría de compiladores C/C++ cuando están compilando un archivo con la extensión `.cpp`. Esto permite escribir código que se adapta automáticamente al ser compilado para C p C++.

```c
void f()
{
#ifdef __cplusplus
    // Código para C++...
#else
    // Código para C...
#endif
}
```

