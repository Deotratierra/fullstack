## Distribución de procesos por el Kernel de Linux
El kernel se encarga de que los procesos se dividan el tiempo del CPU en pedacitos llamados ciclos y automáticamente cambia de un proceso a otro, dando la ilusión de que están corriendo todos al mismo tiempo.

La información del estado de los procesos es almacenada en Bloques de Control de Procesos (PCBs). Todos estos bloques son almacenados en las tablas de procesos del kernel. A cada proceso le asigna una identificación (PID), la cual es utilizada para localizarla dentro de la tabla de procesos del kernel. Todos los procesos, excepto el init que es generado por el propio kernel al arrancar el sistema, tienen un proceso padre.

### Ejecutar procesos
Cada ve que se arranca un programa se ejecuta un nuevo proceso, a no ser que indiquemos lo contrario. El método por el cual un programa crea un nuevo proceso es llamado *forking* (ramificar). Este crea un duplicado exacto del proceso, incluyendo código ejecutable, la información, el estado de las variables...

Podemos evitar esto usando el comando `exec`. Este reemplaza el programa que se está ejecutando por el programa que indicamos que ejecute. Por ejemplo, si ejecutamos `exec nano`, se abrirá el editor *nano*, pero al salir del mismo se cerrará también la consola. Otra forma de evitarlo es [enviando procesos a segundo plano](https://github.com/mondeja/fullstack/tree/master/backend/src/029-concurrencia/procesos/os_control/_proc.sh).

### Monitorear procesos
El PCB de cada proceso guarda mucha información, la mayoría sólo relevante para el kernel. Algunos de los campos de información más importantes son:
- ID del proceso (PID): Es un entero único que se utiliza para no perder de vista los procesos. Se distribuyen de forma incremental, por eso el init siempre lleva el número 1. El número más grande posible es el 32767, (número más grande que puede ser representado por 2 bytes de memoria).
- IDs de usuario y grupo efectivos.
- IDs de usuario y grupo reales.
- ID del proceso padre (PPID).
- Estado del proceso.
- Estado de la señal.

#### Comando `top`
Este comando muestra una tabla que se actualiza cada 3 segundos con la siguiente información:

`top - 17:14:10 up 38 min,  2 users,  load average: 0,01, 0,05, 0,13`
Hora del sistema, tiempo encendido, número de usuarios y carga media en intervalos de 5, 10 y 15 minutos.

`Tasks: 201 total,   1 running, 200 sleeping,   0 stopped,   0 zombie`

Tareas por procesos: ejecutándose, durmiendo, detenidas y [zombies](https://es.wikipedia.org/wiki/Proceso_zombie).

`%Cpu(s):  0,3 us,  0,2 sy,  0,0 ni, 99,3 id,  0,2 wa,  0,0 hi,  0,0 si,  0,0 st`

Rendimiento de las CPUs en porcentaje: usuario (us), kernel (sy), procesos de baja prioridad (ni), procesos inactivos (id), en espera (wa), interrupiones de hardware (hi), interrupiones de software (si) y tiempo robado por la máquina anfitriona al sistema virtualizado (st - steal time, solo relevante en sistemas virtualizados).

`KiB Mem :  8074076 total,  5665892 free,  1280632 used,  1127552 buff/cache`

Memoria física: total, libre, en uso y de buffer.

`KiB Swap:  7811068 total,  7811068 free,        0 used.  6404516 avail Mem`

Memoria virtual: total, libre, en uso y disponible.

```
PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
930 root      20   0  520776  46656  34896 S   1,0  0,6   0:03.58 dockerd
2239 mondeja   20   0 1133400 284896  48084 S   0,7  3,5   0:40.93 sublime_text
2254 mondeja   20   0  773192  64612  52804 S   0,3  0,8   0:08.05 konsole
```

Columnas de procesos: identificador del proceso (PID), usuario (USER), prioridad (PR, si es rt está ejecutando en tiempo real), asignación de prioridad (NI), memoria virtual utilizada por el proceso (VIRT), memoria física que utiliza el proceso (RES), memoria compartida (SHR), estado del proceso (S), porcentaje de CPU utilizado desde la última actualización (%CPU), porcentaje de memoria física utilizada desde la última actualización (%MEM), tiempo que lleva el proceso desde su inicio (TIME+), comando de inicio del proceso (COMMAND).

> Existe un programa parecido a top pero más rápido y con una interfaz mejor: `htop`. Para instalarlo: `sudo apt-get install htop`. [Lista de softwares de monitoriación del sistema](http://www.upubuntu.com/2012/06/list-of-best-system-monitoring.html).


### Prioridad de procesos
El kernel utiliza un sistema de asignación de enteros a los procesos para administrar el tiempo de CPU de cada proceso. Cada proceso tiene dos valores de prioridad: estático y dinámico. La prioridad dinámica la calcula el kernel en base a la prioridad estática para distribuir adecuademente el tiempo de CPU entre procesos. A la prioridad se le denomina *niceness*

Las prioridades (estáticas) se definen por un valor numérico que tienen un rango desde `-20` (mayor prioridad) hasta `20` (menor prioridad).

#### Establecer prioridad de procesos
Los procesos heredan su prioridad de su proceso padre (por defecto 0). Para iniciar un comando con un *niceness* diferente al de su proceso padre, debemos utilizar el comando `nice`. Sólo los superusuarios pueden establecer prioridades negativas a los procesos.

- Lanzar un comando con cierta prioridad: `nice -n <numero_de_prioridad> <comando>`
- Cambiar la prioridad de un proceso en ejecución: `renice <numero_de_prioridad> -p <PID>`



> Fuentes:
> - Administración de sistemas GNU/Linux - Antonio Perpinan
> - https://geekytheory.com/funcionamiento-del-comando-top-en-linux
> - https://unix.stackexchange.com/questions/18918/in-linux-top-command-what-are-us-sy-ni-id-wa-hi-si-and-st-for-cpu-usage
> - http://persoal.citius.usc.es/tf.pena/ASR/Tema_3html/node4.html