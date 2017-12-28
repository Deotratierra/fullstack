## Número máximo de hilos
Limitado al número de CPUs del sistema.

________________________

### Python
```python
import multiprocessing
multiprocessing.cpu_count()
```

________________________

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