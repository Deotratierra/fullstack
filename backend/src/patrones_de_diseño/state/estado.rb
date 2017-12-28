#!/bin/ruby

class Contexto
    # Mantiene una instancia de una subclase
    # EstadoConcreto que define el estado actual
    def initialize(estado)
        @_estado = estado
    end

    attr_reader :_estado

    def peticion
        @_estado.manejar()
    end
end

class Estado
	# Interfaz para encapsular el comportamiento
	# asociado a un estado particular del contexto
    def initialize()
        if !defined? self.manejar()
            raise TypeError, "Debes declarar el método " +
                "manejar() en #{self.class.name}"
        end
    end
end

class EstadoConcretoA < Estado
    def manejar
        puts "Manejador de #{self.class.name}"
    end
end

class EstadoConcretoB < Estado
    def manejar
        puts "Manejador de #{self.class.name}"
    end
end

if __FILE__ == $0
    estado_concreto_A = EstadoConcretoA.new
    contexto = Contexto.new(estado_concreto_A)
    contexto.peticion
end
