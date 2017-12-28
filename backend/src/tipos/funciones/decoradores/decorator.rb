#!/usr/bin/ruby

# En Ruby podemos jugar con los trozos de código
# pues las sentencias end van creando bloques
# con los cuales podemos trabajar:

def bloque
    puts "Llamo al bloque por primera vez"
    yield
    puts "Llamo al bloque por segunda vez"
    yield
end

bloque {
    puts "Y me cuelo en el lugar del yield"
}

# Dentro del bloque, que parece una función
# podemos colar trozos de código.

# Incluso podemos acceder a variables
# definidas en el bloque que se ejecutarán
# en el código que le pasamos mediante yields

def metodo
    yield("Hola", "Adios")
end

metodo{ |x, y|
    puts x + " ¿Qué tal? " + y
}

# Los bloques no son objetos, pero pueden
# convertirse en ellos gracias a la clase Proc

