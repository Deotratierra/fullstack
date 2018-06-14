<?php

$datos = ["a", "b", "c"];

// ------------------------------------------------------

// Obtener el tipo de una variable

echo gettype($datos), "\n";   // array

// ------------------------------------------------------


// Mostrar información estructurada de conjuntos de datos

/* Esta función admite un número indefinido de parámetros,
    por lo que podemos imprimir varias estructuras a la vez.
*/

var_dump($datos);
/*
    array(3) {
      [0]=>
      string(1) "a"
      [1]=>
      string(1) "b"
      [2]=>
      string(1) "c"
    }
*/

// ------------------------------------------------------

// Imprimir información legible de una variable

print_r($datos);
/*
    Array
    (
        [0] => a
        [1] => b
        [2] => c
    )
*/

// ------------------------------------------------------

// Obtener información estructurada sobre una variable

var_export($datos);
echo "\n";

/*
    array (
      0 => 'a',
      1 => 'b',
      2 => 'c',
    )
*/

/* Fuentes:
http://php.net/manual/es/function.var-dump.php
*/

?>
