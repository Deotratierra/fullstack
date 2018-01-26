#include <stdio.h>

#ifdef __unix__
/*
Compilación:
gcc create.c -o create -lpthread
*/
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>      // exit()

/* La función pthread_exit() termina el hilo en ejecución y hace al valor pasado como
    parámetro, disponible a cualquier proceso que esté esperando por su terminación.
    http://pubs.opengroup.org/onlinepubs/9699919799/functions/pthread_exit.html
*/

void* contador(void* max);

int main() {
    pthread_t hilo_contador_ID;
    long parametro_contador = 0, ret;
    int ok;

    ok = pthread_create(&hilo_contador_ID, NULL, &contador, (void*)&parametro_contador);
    if (ok != 0) {
        printf("Ocurrió un error creando el hilo.\n");
        exit(1);
    }

    pthread_join(hilo_contador_ID, (void*)&ret);

    printf("Valor de retorno: %d\n", ret);

    if (ret == 0) {
        printf("El contador ha llegado hasta %d correctamente.\n", parametro_contador);
    } else {
        printf("Ha ocurrido un error en el contador.\n");
    }

    return 0;
}

/**
 * Función que cuenta desde 1 hasta el número pasado como argumento
 * @param max Número hasta el cual llegará el contador
 * @return    Devuelve -1 si pasamos 0 ó un valor negativo, si no devuelve 0.
 */
void* contador(void* max) {
	long _max = (*(int*) max);
    if (_max < 1) {
        printf("El límite de segundos del contador no puede ser %d\n", _max);
        /* Con la variable PTHREAD_CANCELED devolvemos el mismo valor
            que si el hio hubiera sido cancelado desde el exterior: -1 */
        pthread_exit(PTHREAD_CANCELED);
    }

	for (int i=1; i<_max+1; i++){
		printf("%d ", i);
		usleep(1000000);
	}
	printf("\n");
	pthread_exit(0);

	/* Podríamos devolver unc cadena tal que:
	    ---------------------------------------------
        char *ret;

	    if ((ret = (char*) malloc(20)) == NULL) {
	        perror("malloc() error");
	        exit(2);
	    }
	    strcpy(ret, "This is a test");
	    pthread_exit(ret);
	    ---------------------------------------------
	https://www.ibm.com/support/knowledgecenter/en/SSLTBW_2.2.0/com.ibm.zos.v2r2.bpxbd00/ptexit.htm
	*/
}

#endif

/* Fuentes:
Programación avanzada en Linux - Mark Mitchell, Jeffrey Oldham y Alex Samuel
http://profesores.elo.utfsm.cl/~agv/elo330/2s08/lectures/POSIX_Threads.html
https://stackoverflow.com/questions/18117376/warning-return-makes-pointer-from-integer-without-a-cast-but-returns-integer-as
https://stackoverflow.com/questions/3844678/pthread-exit-vs-return
https://www.ibm.com/support/knowledgecenter/en/SSLTBW_2.2.0/com.ibm.zos.v2r2.bpxbd00/ptexit.htm
*/