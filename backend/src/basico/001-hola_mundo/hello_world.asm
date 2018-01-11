;Comentarios en nasm

section .data ; La sección de datos es opcional
    msg db      "¡Hola mundo desde lenguaje ensamblador con Nasm para Linux x86_64!"

section .text ; Sección de código (obligatoria)
    global _start  ; Indicamos dónde comienza el programa
_start:
    mov     rax, 1    ; Introducimos en el registro la función sys_write() (ver *1)
    mov     rdi, 1    ; Primer parámetro de la función (forma de abrir la salida: stdout)
    mov     rsi, msg  ; Segundo parámetro (mensaje)
    mov     rdx, 67   ; Tercer parámetro (largo del mensaje)
    syscall           ; Lanzamos la llamada al sistema

    mov    rax, 60    ; Introducimos en el registro la función sys_exit()...
    mov    rdi, 0     ; ... con el código de salida 0
    syscall           ; Salimos del programa de forma controlada

; ===========================================================

; *1 -> Cuando realizamos una llamada al sistema usamos el registro rax
;       En este caso estamos llamando a la función sys_write()
;       Tabla de llamadas al sistema por números:
;       http://blog.rchapman.org/posts/Linux_System_Call_Table_for_x86_64/
;       Esta función toma 3 parámetros:
;           - descriptor de archivo: 0 stdin, 1 stdout, 2 stderr
;           - buffer: Contenido que queremos introducir en el archivo
;           - count: Número de bytes que tendrá el archivo

; =============================================================================

; Para ver más ir al apartado de bajo nivel donde se encuentra el directorio ensamblador/