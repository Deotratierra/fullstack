#!/usr/bin/ruby

# INICIALIZACIÓN

lista1 = Array.new
lista2 = Array.new(3) # Array de 3 elementos nil
lista3 = Array.new(3, "hola") # Array de 3 elementos "hola"
lista4 = Array.new(5) {
    |e| e = e * 2   # Array de números de 0 a 8 cada 2
}
lista5 = Array.[](1, 2, 3, 4, 5)
lista6 = Array[1, 2, 3, 4, 5]
lista7 = Array(1..5)

# Crear un array de strings (olvídate de espacios en las cadenas)
lista8 = %w{ que_tal saludos adiós }

# ------------------------------------------------

# MODIFICACIÓN Y ACCESO A SUS ELEMENTOS

puts lista2.length  # 5
puts lista2.size    # 5
puts "#{lista3}"    # ["hola", "hola", "hola"]
puts "#{lista4}"    # [0, 2, 4, 6, 8]

puts (lista5 == lista6) # true
puts "#{lista7}"    # [1, 2, 3, 4, 5]

# Ordenar una lista
puts "#{lista8.sort}"

puts lista7.last  # 5  <--- Obtener el último elemento
puts lista7.first # 1  <--- Obtener el primer elemento

# Obtener un elemento por su índice
puts lista7[2]      # 3
puts lista7[2] == lista7.at(2) # true

lista3.fetch(100, "oops") # oops  <--- Con valor por defecto si no existe

# Obtener los n primeros elementos
puts "#{lista5.take(2)}" # [1, 2]

# Obtener los n últimos elementos
puts "#{lista5.drop(2)}" # [3, 4, 5]

# Comprobar si un array está vacío
puts lista1.empty? # true
puts lista2.empty? # false

# Comprobar si un elemento existe en el array
puts lista4.include?(4) # true

# Añadir un elemento al final del array
lista2 << 20
lista2.push(10)

# Añadir un elemento al principio del array
lista2.unshift(0)

# Añadir elementos en el índice indicado
lista2.insert(3, "uno", "dos")

puts "#{lista2}" # [0, nil, nil, "uno", "dos", nil, 20, 10]


# Eliminar un elemento
lista8.delete("saludos")

puts lista2.pop  # 10 <--- Obteniéndolo

lista2.delete_at(1) # <---De un índice

lista2.delete("uno") # <--- Por referencia
puts "#{lista2}" # [0, nil, "dos", nil, 20]

# Recorrer un array
lista8.each do |saludo|
    puts "##### " + saludo + " #####"
end

# ---------------------------------------

# Iterar string caracter por caracter
"hola".split("").each do |char|
	print(char)
end

for char in "hola".split("")
	print(char)
end

# Enumerando
"hola".split("").each_with_index do |char, i|
	print(char, i)
end

# =================================================

=begin 
Existen muchísimas más formas de interactuar
con los arrays en ruby. Para profundizar:
https://ruby-doc.org/core-2.2.0/Array.html
=end


