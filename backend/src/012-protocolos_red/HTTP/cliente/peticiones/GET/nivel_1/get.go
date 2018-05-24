package main

import (
	"fmt"
	"net/http"  // https://golang.org/pkg/net/http/
	"time"
)

var urls = []string{
	"https://github.com/mondeja",
	"http://golang.org/",
	"http://matt.aimonetti.net/",
}

type HttpResponse struct {
	url      string
	response *http.Response
	err      error
}


/* Los canales (chan) son un tipo por el cual puedes enviar
    y recibir valores con el operador de canal <-.
              (Los datos viajan en la dirección de la flecha)

   ch <- v    // Envia v al canal ch
   v := <-ch  // Recibe desde ch y asigna a la variable v.
*/

func AsyncHttpGets(urls []string) []*HttpResponse {
	ch := make(chan *HttpResponse, len(urls))
	responses := []*HttpResponse{}
	for _, url := range urls {
		go func(url string) {                 // Usando la sintaxis go func() ejecutamos
			fmt.Printf("Fetching %s \n", url) // corrutinas de forma asíncrona.
			resp, err := http.Get(url)        // La función Get() de la biblioteca http
			resp.Body.Close()
			if err != nil {
	            fmt.Printf("Error fetching %s \n%s", url, err)
            }
			ch <- &HttpResponse{url, resp, err}
		}(url)
	}

	for {
		select {
		case r := <-ch:                            // Si una respuesta viene
			fmt.Printf("%s was fetched\n", r.url)  // avisamos que ha llegado
			responses = append(responses, r)
			if len(responses) == len(urls) {       // Si tenemos todas las
				return responses                   // respuestas las devolvemos
			}                                      // cerrando así el ciclo.
		case <-time.After(28 * time.Millisecond):  // Cada 28 milisegundos
			fmt.Printf(".")                        // mostramos un caracter "."
		}
	}

	return responses
}

func main() {
	results := AsyncHttpGets(urls)
	for _, result := range results {
		fmt.Printf("%s status: %s\n", result.url,
			result.response.Status)
	}
}

// Original: https://gist.github.com/mattetti/3798173

/* Fuentes para ampliar:
https://tour.golang.org/concurrency/2
https://gobyexample.com/goroutines
https://medium.com/@nate510/don-t-use-go-s-default-http-client-4804cb19f779
*/
