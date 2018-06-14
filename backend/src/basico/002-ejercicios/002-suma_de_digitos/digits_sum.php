<?php

function digits_sum($number) {
    $response = "";
    $total = 0;
    while ($number != 0) {
        $rest = $number % 10;
        $response += (string)$rest;
        $total += $rest;
        $number = (int)($number/10);
        if ($number > 0) {
            $response += " + ";  // Las cadenas se pueden concatenar
                                 // mediante el operador de suma +
        }
    }
    $response += " = " + (string)$total;
    return $response;
}

$num1 = 2345;
$num2 = 326205;

echo digits_sum($num1), "\n";
echo digits_sum($num2), "\n";

?>