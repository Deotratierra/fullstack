## Bomba al enemigo
Dada una matriz de 2 dimensiones, cada celda es un muro (`M`), un enemigo (`E`)o está vacía (`-`). Tiramos una bomba la cual mata a todos los enemigos que se encuentren en la línea horizontal o en vertical con respecto al lugar donde la tiramos, pero la explosión no atraviesa los muros. Sólo podemos poner la bomba en lugares vacíos.

Devuelve el número máximo de enemigos que podemos matar. Por ejemplo, dada la siguiente matriz:

```
- E - E
E M - E
- - E -
```

Si pondemos una bomba en (3, 2) mata a 2 enemigos:

```
- E x E
E M o x
- - x -
```

__________________________

#### Leyenda
- `E`: enemigo
- `-`: espacio vacío
- `M`: muro
- `o`: bomba
- `x`: alcance de la explosión

> Fuente:
> - https://github.com/keon/algorithms/blob/master/matrix/bomb_enemy.py
