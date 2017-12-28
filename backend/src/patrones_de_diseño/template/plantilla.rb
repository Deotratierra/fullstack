#!/bin/ruby

class Operacion
	# Define una operación en dos pasos
    # abstractos que cada subclase concretará
    def initialize
        metodos_abstractos = [
            "self.suboperacion_1",
            "self.suboperacion_2"
        ]

        for metodo in metodos_abstractos do
            if !defined? metodo.to_sym
            	raise TypeError, "Debes declarar los métodos " +
                    "abstractos de la clase padre Operacion " +
                    "en #{self.class.name}"
            end
        end
    end

    def ejecutar
        self.suboperacion_1
        self.suboperacion_2
    end
end


class OperacionConcreta < Operacion
    # Implementa las operaciones
    # para seguir los pasos del algoritmo
    # específicos para esta subclase */
    def suboperacion_1
        puts("Primer paso en la operación")
    end

    def suboperacion_2
        puts("Segundo paso en la operación")
    end
end

if __FILE__ == $0
    operacion_concreta = OperacionConcreta.new
    operacion_concreta.ejecutar()
end