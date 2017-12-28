#!/usr/bin/ruby

class Base;
    def initialize()
        if !defined? self.abstracto()
            raise TypeError, "Debes declarar el método " +
                "abstracto() en #{self.class.name}"
        end
    end
end;

class Ejemplo < Base  # Herencia
    @@propiedad = "Soy una propiedad"

    def self.propiedad
    	@@propiedad
    end

    # Constructor
    def initialize
    	@_atributo = "Soy un atributo"
    	@_atributo_leible = "Soy un atributo leible"
    	@_atributo_sobrescribible = "Soy un atributo sobreescribible"
    end

	# Atributo leible y editable
	attr_accessor :_atributo

	attr_reader :_atributo_leible # Sólo leíble

	attr_writer :_atributo_sobrescribible # Sólo editable

    # Método público por defecto
	def normal; puts "Soy un método normal"; end;

	# Método de clase
	def self.de_clase
		return Ejemplo.new
	end

    def abstracto
        puts "Mira en la clase padre."
        puts "Cambiame el nombre en #{self.class.name} y verás lo que pasa."
    end

    # Método para obtener las clases hijas
    def self.descendants
        ObjectSpace.each_object(Class).select { |klass| klass < self }
    end


	protected
	    def protegido
	    	"Método protegido"
	    end

    private
        def privado;
        	"Método privado"
        end
end

# Constructor
ej = Ejemplo.new

# Acceso a propiedades
puts Ejemplo.propiedad  # Soy una propiedad

puts ej._atributo # Soy un atributo

#puts ej._atributo_sobrescribible  # ERROR --> undefined method `_atributo_sobrescribible

# Método normal
ej.normal()  # Soy un método normal

# Método de clase
puts Ejemplo.de_clase  # #<Ejemplo:<dirección_en_memoria>>

# Método abstracto
puts ej.abstracto  # # Mira en la clase padre.
                   # Cambiame el nombre en Ejemplo y verás lo que pasa.

# Método protegido
#puts ej.protegido  # ERROR --> protected method `protegido' called

# Método privado
#puts ej.privado  # ERROR --> private method `privado' called

# ====================================

# Obtener las subclases
ej.descendants()


=begin

#####     RANGOS DE ACCESO     #####

- Los métodos públicos pueden ser invocados
por cualquiera, no tienen control de acceso.
Los métodos son públicos por defecto, excepto
initialize(), que siempre es privado.
- Los métodos protegidos sólo pueden ser
invocados por objetos de la clase que los define
o sus subclases. Su acceso se mantiene dentro
de la familia.
- Los métodos privados sólo pueden ser llamados
en la clase que los definen y dentro de los
descendientes directos.

=end
