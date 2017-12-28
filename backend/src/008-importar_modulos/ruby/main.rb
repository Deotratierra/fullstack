#!/usr/bin/ruby

# ---------  IMPORTAR EN EL MISMO DIRECTORIO  -----------------

# require_relative permite importar módulos relativos al archivo
# donde se ha declarado esta sentencia
require_relative "modulo"

# ---------  IMPORTAR DE OTROS DIRECTORIOS  -------------------
require "./directorio/modulo" # Así también --> "./directorio/modulo.rb"
# Sin require_relative tenemos que escribir "./" antes del nombre
# si el módulo se encuentra en el mismo directorio


=begin
Otra forma de importar es usar  -->  load "./modulo"
En este caso, el modulo volverá a cargarse,
si han ocurrido cambios en su interior podremos
acceder a ellos
=end

if __FILE__ == $0  # Equivalente en python -> if __name__ == "__main__":
    funcion
    funcion_otro_directorio
end

=begin
Fuentes:
https://stackoverflow.com/questions/3672586/what-is-the-difference-between-require-relative-and-require-in-ruby
=end
