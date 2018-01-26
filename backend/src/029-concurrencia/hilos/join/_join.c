#include <stdio.h>

/* ============================================================================
                                   UNIX
*/
#ifdef __unix__
#include <pthread.h>
#include <unistd.h>  // usleep()

void* imprime_100(void* num);

int main() {
    for (int i=1; i<6; i++) {
        pthread_t hilo_ID;  // Identificador del hilo

        int valor_retorno;  // Valor de retorno

        // Creamos un hilo
        pthread_create(&hilo_ID, NULL, &imprime_100, (void*)&i);

        /* La función pthread_join() bloquea hasta que un hilo completa
            su ejecución. Toma dos parámetros: el identificador del hilo
            a esperar que termine y un puntero a void* a una variable
            que recibirá el valor de retorno del hilo. Si no te importa este
            pásale NULL como segundo argumento */
        pthread_join(hilo_ID, (void*)&valor_retorno);

        usleep(500000);

        printf("\nHilo %d finalizado.\n", i);
    }

    return 0;
}

/**
 * Imprime 100 veces el número pasado como parámetro.
 * @param num Número a imprimir 100 veces.
 * @return       Retorna 0 si no sucede ningún error.
 */
void* imprime_100(void* num) {
    int _num = (*(int *) num);  // Casting de void* a int

    for (int i=0; i<100; i++) {
        printf("%d", _num);
    }
    return 0;
}

/* ============================================================================
                                  WINDOWS
*/

#elif defined(_WIN32)
#include <windows.h>

DWORD WINAPI imprime_100(LPVOID num);

int main() {
    for (int i=1; i<6; i++) {
        DWORD hilo_ID;             // Identificador del hilo
        HANDLE manejador_de_hilo;  // Manejador del hilo

        // Creamos un hilo
        manejador_de_hilo = CreateThread(NULL, 0, imprime_100, &i, 0, &hilo_ID);

        int ret;

        /* La función WaitForSingleObject() espera hasta que un objeto de sincronización
            pasado como argumento ha terminado o hasta que se produce una señal en este.
           Toma dos argumentos: el primero es una función a esperar y el segundo es
            un tiempo de expiración en milisegundos, pero también se le puede pasar 0
            para que este tiempo sea infinito:
            https://msdn.microsoft.com/en-us/library/windows/desktop/ms687032(v=vs.85).aspx
        */
        ret = WaitForSingleObject(
            manejador_de_hilo,
            0
        );

        Sleep(500);

        printf("\nHilo %d finalizado (ID = %d).\n", i, hilo_ID);

        if (CloseHandle(manejador_de_hilo) != 0) {
            printf("Manejador de hilo cerrado con éxito.\n");
        } else {
            printf("Ocurrió un error cerrando el manejador de hilo.\n");
        }
    }

    return 0;
}

/**
 * Imprime 100 veces el número pasado como parámetro.
 * @param num Número a imprimir 100 veces.
 * @return       Retorna 0 si no sucede ningún error.
 */
DWORD WINAPI imprime_100(LPVOID num) {
    int _num =  *(DWORD*)num;  // Casting de void* a int

    for (int i=0; i<100; i++)
        { printf("%d", _num);
    }
    return 0;
}

// ============================================================================

#endif

/* Fuentes:
LINUX:
Programación avanzada en Linux - Mark Mitchell, Jeffrey Oldham y Alex Samuel
https://stackoverflow.com/questions/21091000/how-to-get-thread-id-of-a-pthread-in-linux-c-program

WINDOWS:
https://msdn.microsoft.com/en-us/library/windows/desktop/ms687032(v=vs.85).aspx
*/
