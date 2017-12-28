#!/bin/ruby

# ============================================

# La biblioteca estándar de Ruby tiene
# un módulo que implementa el patrón Singleton

require "singleton"

class MiClase
    include Singleton

    def initialize(); end;

    def metodo()
        puts "Método normal"
    end
end

# ============================================

if __FILE__ == $0
    c1 = MiClase.instance
    c2 = MiClase.instance
    puts c1 === c2

    c1.metodo
end

