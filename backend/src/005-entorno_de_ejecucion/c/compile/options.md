## Opciones de compilación
Podemos indicarle opciones al compilador para cambiar la forma en la que trabaja con el código.

______________________________________

### Optimización

#### GCC
El parámetro de optimización a la hora de compilar se indica con la opción `-O` (letra mayúscula). Este permite un rendimiento mayor del código. El parámetro por defecto es `O0` (sin optimización). Existen como mínimo 7 niveles optimización:
- `-O0`: Sin optimización.
- `-O` / `-O1`: Optimiza pero sin tomar mucho tiempo.
- `-O2`: Optimiza más agresivamente.
- `-O3`: Optimiza más agresivamente.
- `-Ofast` / `-O3 -ffast-math`: La optimización `-ffast-math` activa optimizaciones de números decimales que no cumplen con los estándares. Esto permite al compilador suponer que los números decimales son infinitamente precisos y operaciones computadas en ellos siguir las reglas estandar del álgebra real.
- `Os`: Optimiza el tamaño del código. Esto actualmente puede mejorar la velocidad en algunos casos, debido a un comportamiento de caché más inteligente.
- `Og`: Optimiza pero sin gastar tanto tiempo como para interferir en el proceso de prueba del código (útil para debug).

______________________________________

> Fuentes:
> - https://stackoverflow.com/questions/1778538/how-many-gcc-optimization-levels-are-there