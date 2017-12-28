#!/usr/bin/ruby

sentencias = [
    "abcdefGHIJKLMNopqrstuvwxyz",
    "abcdefGHIJKLwNopqrstuvwxyz",
    "Texto de ejemplo",
    "The quick brown fox jumps over the lazy dog",
]

$abecedario_ingles = "abcdefghijklmnopqrstuvwxyz" # Variable global

def pangrama(string)
    letras = []
    for letra in string.split(//) do  # Creamos un array de la cadena
        letra = letra.downcase        # La letra en minúscula
        if !(letras.include? letra)   # Si la letra no está en nuestra lista 
            if ($abecedario_ingles.include? letra) # y está en el abecedario
               letras.push(letra)     # La agregamos a la lista
            end
        end
    end
    if ($abecedario_ingles.length == letras.length)
        return true
    end
    return false
end


for s in sentencias do
    puts pangrama(s)
end
