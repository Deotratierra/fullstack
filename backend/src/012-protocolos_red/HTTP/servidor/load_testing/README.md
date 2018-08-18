## Pruebas de carga sobre servidores web

### [ab (Apache HTTP server benchmarking tool)](https://httpd.apache.org/docs/2.4/programs/ab.html)
Este programa nos permite ejecutar tests de carga sobre un servidor web en ejecución.

Suponiendo que tenemos un servidor web corriendo en `localhost:8765`, ejecutaríamos: `ab -n 10000 -c 100 -g grafica.data http://localhost:8765/`