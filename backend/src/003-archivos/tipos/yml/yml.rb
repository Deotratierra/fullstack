#!/usr/bin/ruby

require "yaml"

# Insertar datos en un archivo .yml

data = {
    "primero" => 1,
    "segundo" => {"hola" => "adios"}
}

File.open("data.yml", "w") do |f|
    f.write(YAML.dump(data))
end


# ====================================================

# Leer datos de un archivo .yml

File.open("fichero.yml", "r") do |f|
    puts YAML.load(f.read)
end

# Fuente:
# https://ruby-doc.org/stdlib-2.1.0/libdoc/yaml/rdoc/YAML.html
