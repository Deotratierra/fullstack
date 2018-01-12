#include <stdio.h>
#include <string>
#include <iostream>
#include <curl/curl.h>

/* Necesitamos instalar la biblioteca curl
   En Linux, ejecuta:
sudo aptitude install libcurl4-openssl-dev

Luego compila linkeando la biblioteca:
g++ get.cpp -o get -lcurl

Si todo ha ido bien, ejecuta el programa:
./get

*/


int main(void){
    char URL [] = "https://min-api.cryptocompare.com/stats";
    CURL *curl;
    CURLcode res;

    curl_global_init(CURL_GLOBAL_DEFAULT);

    // Primero creamos el contexto. CURL necesita un contexto desde
    // el cual ejecutamos las operaciones.
    curl = curl_easy_init();
    if(curl) {
        curl_easy_setopt(curl, CURLOPT_URL, URL);  // Establecemos operación

        /* Realizamos la llamada */
        res = curl_easy_perform(curl);
        /* Comprobamos errores */
        if(res != CURLE_OK)
            fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));

    /* Siempre limpiamos el contexto */
    curl_easy_cleanup(curl);
    } else { return 128; }

    curl_global_cleanup();

    std::cout << "\n";

    return 0;
}

/* Fuentes:
https://curl.haxx.se/libcurl/c/https.html
https://gist.github.com/alghanmi/c5d7b761b2c9ab199157
*/
