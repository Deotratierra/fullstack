#!/usr/bin/ruby

# Abrir un archivo para escritura
File.open("ejemplo.txt", "w") do |archivo|
    # Escribir en un archivo
    archivo.write("Contenido del archivo\n")
end

# Abrir un archivo para lectura
File.open("ejemplo.txt", "r") do |archivo|
    # Leer un archivo
    archivo.each_line do |linea|
        puts linea
    end
end
