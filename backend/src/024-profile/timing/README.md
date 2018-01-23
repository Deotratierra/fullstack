## Análisis de rendimiento
Para analizar la velocidad de los algoritmos se fuerza el tamaño del problema al que se aplica. Pongamos que tenemos el siguiente algoritmo (Javascript):

```
for (i=0; i <= N; i++) {
    console.log(i)
}
```

Cada una de las iteraciones del bucle anterior comparten como criterio de agrupación su [*comportamiento asintótico*](https://es.wikipedia.org/wiki/As%C3%ADntota), es decir, que la diferencia entre dos iteraciones cualquiera del conjunto de todas tiende a cero.

Al conjunto de todas las operaciones dentro del algoritmo que estamos analizando se le denomina `O` (puedes encontrar una declaración más formal en la fuente). Puesto que en el bucle anterior todas las iteraciones tienden a tardar lo mismo, decimos que el **orden de complejidad** (magnitud que expresa el rendimiento) del mismo es `O(N)`, donde `N`, como se puede apreciar, es el número de iteraciones que realiza.

>Fuentes:
- http://www.lab.dit.upm.es/~lprg/material/apuntes/o/
