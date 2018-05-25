## Testing en Golang
Si has visto proyectos Golang por ahí, habrás notado que los tests para cada archivo se encuentra en la misma carpeta. Para cada archivo `main.go` habrá un archivo de tests llamado `main_test.go`. Así es como se organizan los tests en Golang.

- Ejecutar los tests: `go test`. Opciones:
    + `-v`: añade verbosidad.
    + `-i`: instalar dependencias de los tests.
    + `-json`: convertir la salida a formato JSON.
    + `-parallel n`: ejecuta los tests con un número `n` de CPUs en paralelo.