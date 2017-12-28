#!/bin/ruby

require "colorize"   # gem install colorize

# Consultar los colores posibles
print String.color_samples

# Consultar los estilos disponibles
print String.modes

puts "Texto verde".colorize(:color => :green)
puts "Texto verde claro".light_green
puts "Texto azul claro".light_blue

puts "Texto en negritas".bold
puts "Texto celeste en cursivas".italic.light_cyan
puts "Texto parpadeante en rojo".blink.red
puts "Texto magenta con fondo amarillo".colorize(:color => :magenta, :background => :light_yellow)

# Fuentes:
# https://github.com/fazibear/colorize
