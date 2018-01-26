#include <stdio.h>

#ifdef __unix__
#include <pthread.h>
#include <unistd.h>

/* Los atributos de los hilos proveen un mecanismo para ajustar con precisión
    el comportamiento de hilos individuales. La función pthread_create(), como
    segundo argumento, puede tomar un puntero a un objeto de atributos de hilo.
    Si pasas NULL, se configura con los atributos del hilo actual, sin embargo,
    puedes crear y personalizar un objeto de atributos de hilo para especificar
    otros valores.
   Para especificar atributos de hilo personalizados, sigue los siguientes pasos:
       1. Crea un objeto pthread_attr_init. La manera más fácil es declarando
           una variable de este tipo.
       2. Llama a la función pthread_attr_init(), pasando un puntero al objeto.
           Esto inicializa los atributos a sus valores por defecto.
       3. Modifica el atributo objeto para contener los valores de atributos deseados.
       4. Pasa un puntero al objeto atributo cuando llames a la función pthread_create().
       5. LLama a la función pthread_attr_destroy para liberar el objeto de atributos.
           La variable pthread_attr_t no es desasignada en memoria, puede ser
           reinicializada con pthread_attr_init().

   Para la mayoría de las tareas de programación en Linux sólo interesa un atributo de
    hilo (los atros atributos son primariamente especializados para programación
    especializada en tiempo real). Este atributo es el estado "detach" (despegado) del
    hilo.
   Un hilo puede crearse como un hilo "joinable" (articulable, que se puede esperar)
    o un hilo despegado:
      - Los recursos de un hilo articulable, como los de un proceso,
          no son liberados automáticamente cuando este termina. En su lugar, el estado de
          salida se cuelga dentro del sistema (algo así como un proceso zombie) hasta que
          otro hilo llama a pthread_join() para obtener su valor de retorno y, sólo en ese
          momento, sus recursos son liberados.
      - Los recursos de un hilo despegado son liberados automáticamente cuando este
          termina, por lo tanto, otro hilo no puede sincronizarse con su finalización
          usando pthread_join() ni obtener su valor de retorno.
*/

void* imprime_100(void* num);

int main() {
    pthread_t hilo_despegado; // Identificador del hilo
    pthread_attr_t attr;      // Objeto de atributos del hilo
    int parametro = 5;

    // Inicializa el objeto de atributos de hilo:
    pthread_attr_init(&attr);

    /* Para establecer el estado  despegado en un objeto de atributos de hilo,
        usa la función pthread_attr_setdetachstate. El primer argumento es un puntero
        al objeto de atributos del hilo y el segundo es el estado despegado deseado.
        Debido a que el estado articulado es el estado por defecto, es necesario llamar
        a este función sólo para crear estados despegados. Pasa la variable
        PTHREAD_CREATE_DETACHED como segundo argumento. */
    pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_DETACHED);

    // Pasamos el objeto de atributos del hilo como segundo argumento
    pthread_create(&hilo_despegado, &attr, &imprime_100, (void*)&parametro);

    // Destruimos el objeto de atributos del hilo
    pthread_attr_destroy(&attr);

    usleep(500000);
    printf("\n");

    return 0;
}

void* imprime_100(void* num) {
    int _num = (*(int *) num);

    for (int i=0; i<100; i++) {
        printf("%d", _num);
    }
    return 0;
}

#endif
