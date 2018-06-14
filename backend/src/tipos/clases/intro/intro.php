<?php

// Clases en PHP

// Definición de clases
class Clase {
    // Declaración de propiedades
    public $propiedad = "hola";

    // Declaración del constructor
    function __construct(){
        echo "¡La clase ha sido instanciada!\n";
    }

    // Declaración de métodos
    public function metodo() {
        // Acceso a las propiedades desde métodos
        echo $this->propiedad, " (desde el método)", "\n";
    }
}

// Instanciación de un objeto
$c = new Clase();

// Acceso a las propiedades públicas desde la instancia
echo $c->propiedad, "\n";  // hola

// Llamada a los métodos del objeto
$c->metodo();              // hola (desde el método)

// Llamada estática a los métodos del objeto
Clase::metodo();    // PHP Fatal error:  Uncaught Error:
                    // Using $this when not in object context

?>
