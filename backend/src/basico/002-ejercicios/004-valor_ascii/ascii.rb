#!/usr/bin/ruby

if (__FILE__ == $0)
    caracter = "a"
    caracter_en_ascii = caracter.ord
    puts "El caracter '%s' en ASCII ---> %d" % [caracter, caracter_en_ascii]

    numero = 98
    numero_en_caracter = numero.chr
    puts "El número %d en caracter ---> %s" % [numero, numero_en_caracter]
end
