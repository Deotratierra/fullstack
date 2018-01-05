## Canales
Un stream es una especie de canal a través del cual fluyen los datos. Técnicamente, un stream es el enlace lógico utilizado por el programador para leer o escribir datos desde y hacia los dispositivos estándar conectados a la PC o a los archivos en disco. Normalmente, el dispositivo estándar para manipular entradas es el teclado, el dispositivo estándar de salida está asociado (generalmente) con la pantalla o monitor de despliegue de la PC y el dispositivo estándar para mensajes de error está asociado por defecto con la pantalla o monitor de despliegue.

### Modos de apertura en C y Python
| Modo | Descripción |
|------|-------------|
|  r   | Abre un archivo para lectura. Si no existe se produce una violación de segmento (C) o se lanza un FileNotFoundError (Python). |
|  w   | Abre un archivo para escritura. Si existe se borra el contenido pero si no existe se crear uno nuevo. |
|  a   | Abre un archivo para añadir nuevo contenido escribiendo a partir del ya creado. Si no existe se crea un nuevo archivo. |
|  r+  | Abre un archivo para lectura y escritura. Si no existe funciona igual que el modo de sólo lectura. |
|  w+  | Abre un archivo para lecttura y escritura. Si no existe funciona igual que el modo de sólo escritura. |
|  a+  | Abre un archivo para añadir nuevo contenido escribiendo a partir del ya creado y para lectura. Si no existe se crea un nuevo archivo. |
|  x   | Crea un archivo sólo si no existe, pero si existe se produce una violación de segmento (C) o se lanza un FileExistsError (Python). |
