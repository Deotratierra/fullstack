## Número máximo de hilos
Limitado al número de CPUs del sistema.

________________________

### Python
```python
import multiprocessing
multiprocessing.cpu_count()
```

________________________

### C
```c
#include <stdio.h>
#include <sys/sysinfo.h>

int main() {
    printf("Número de procesadores\n");
    printf("  Configurados: %2d\n", get_nprocs_conf());
    printf("  Disponibles: %3d\n", get_nprocs());

    return 0;
}
```

### C++
```cpp
#include <thread>
std::thread::hardware_concurrency()
```

________________________

### Javascript/NodeJS
```js
os.cpus().length
```

________________________

### Bash
```bash
cat /proc/cpuinfo | grep processor | wc -l
```

________________________