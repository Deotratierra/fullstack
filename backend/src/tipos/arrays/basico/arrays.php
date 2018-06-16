<?php

/* Los arreglos en PHP son pares de claves-valor.*/

// Definición en todas las versiones de PHP
$arreglo = array(
    0 => "hola",
);

// Definición a partir de PHP 5.4
$arreglo = [
    0 => "hola",
];

// Acceso a los valores por claves
echo $arreglo[0], "\n";   // hola

// -----------------------------------------------------------------

/* Amoldamiento de claves

  La clave puede ser una cadena o un entero, aunque se producen los
    siguientes amoldamientos de claves si es de otro tipo:
    - Una cadena que contenga un entero válido será convertido a entero,
       por ejemplo "5" será convertido a entero pero "05" se mantendrá
       como una cadena.
    - Un número de punto flotante será convertido a entero desechando
       su parte decimal.
    - Un booleano será convertido a entero siendo true -> 1 y false -> 0.
    - Un valor nulo (null) será amoldado a una cadena vacía ("").
    - Los arreglos y los objetos no podrán ser utilizados como claves,
       produciendo una advertencia "Illegal offset type".
 */
$array_amoldado = array(
    1    => "a",
    "1"  => "b",
    1.5  => "c",
    true => "d",
);
                            // array(1) {
var_dump($array_amoldado);  //   [1]=> string(1) "d"
                            // }


// -----------------------------------------------------------------

/* Arrays indexados (sin clave explícita)

  A diferencia de otros lenguajes de programación,
    PHP no distingue entre arrays indexados o asociativos,
    así que un array indexado es un array asociativo con
    claves como enteros empezando por el 0.
  Podemos establecer un array indexado sin establecer explícitamente
    las claves numéricas:
*/

$arreglo_indexado_implicito = [
	"hola", "que tal", "muy bien", "gracias"
];

echo $arreglo_indexado_implicito[2], "\n";  // muy bien

/* Si establecemos una clave numérica explícita, las siguientes
    continuarán el contador:
*/

$arreglo_indexado_pseudoimplicito = array(
    "hola",
    "que tal",
    15 => "muy bien",
    "gracias"
);

echo $arreglo_indexado_pseudoimplicito[16], "\n";  // gracias

// -----------------------------------------------------------------

/* Recorrer un arreglo

  Para recorrer un arreglo fácilmente utilizamos la función foreach(),
   la cual sólo sirve para arreglos.
*/

$arreglo_a_recorrer = array("violeta", "azul", "magenta");

// Recorrer los valores
foreach ($arreglo_a_recorrer as $color) {
    echo "¿Te gusta el color $color?\n";
}

// Recorrer pares de claves-valor
foreach($arreglo_a_recorrer as $clave => $valor) {
    echo "La clave número $clave corresponde al valor $valor\n";
}

// -----------------------------------------------------------------

// Contar los elementos de un arreglo

echo count($arreglo_a_recorrer), "\n";

// -----------------------------------------------------------------

// Ordenar los elementos de un arreglo

sort($arreglo_a_recorrer);
print_r($arreglo_a_recorrer);

// -----------------------------------------------------------------

// Comprobar si una variable es un arreglo

echo is_array($arreglo), "\n";  // 1

// -----------------------------------------------------------------

// Concatenar dos arreglos

$array_concatenado = array_merge($arreglo, $arreglo_a_recorrer);

// -----------------------------------------------------------------

?>
