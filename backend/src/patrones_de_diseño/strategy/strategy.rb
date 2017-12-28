#!/bin/ruby

class Contexto
    def initialize(estrategia)
        @_estrategia = estrategia
    end

    def ejecutar()
        @_estrategia.algoritmo()
    end
end

class Estrategia
    # Implementamos un método abstracto
    def initialize()
        if !defined? self.algoritmo()
            raise TypeError, "You must declare algoritmo() " +
                "method in #{self.class.name}"
        end
    end
end


class EstrategiaConcretaA < Estrategia
    def algoritmo  # Cambia el nombre y no funciona
        puts "Algoritmo de #{self.class.name}"
    end
end

class EstrategiaConcretaB < Estrategia
    def algoritmo
        puts "Algoritmo de #{self.class.name}"
    end
end

if __FILE__ == $0
    estrategia_concreta_A = EstrategiaConcretaA.new
    contexto = Contexto.new(estrategia_concreta_A)
    contexto.ejecutar
end

