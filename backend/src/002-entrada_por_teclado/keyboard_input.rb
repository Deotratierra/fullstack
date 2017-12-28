#! /usr/bin/ruby

=begin (Esto es un comentario de varias líneas)

Con la función gets en ruby, podemos obtener las entradas por teclado,
pero lo hace en la línea inferior a la petición "Escribe tu nombre: ",
así que creamos la función prompt para solucionarlo de forma simple:

https://stackoverflow.com/questions/2889720/one-liner-in-ruby-for-displaying-a-prompt-getting-input-and-assigning-to-a-var
=end

def prompt(*args)
    print(*args)
    gets
end

name = prompt "Escribe tu nombre: " # Esto recoge "tuNombre/n", recoge la pulsación ENTER
name = name.chomp # Con chomp le quitamos el salto de línea

puts "Bienvenid@ al curso, %s." % name # El formateo de Python!

=begin   
También podría formatearse el saludo anterior así:

puts "Bienvenid@ al curso, #{name}."

De hecho, es mas intuitivo en este caso.
=end

