#!/usr/bin/ruby

class Pareja
    def initialize(n1, n2)
        @n1 = n1
        @n2 = n2
    end

    attr_reader :n1, :n2  # Atributos públicos

    def to_s      # Representación como string   (puts, print)
    	return "Pareja(#{@n1}, #{@n2})"
    end

    # ================================================
    #           SOBRECARGA DE OPERADORES

    def int_to_self(other)
        if ( other.instance_of?(Integer) || other.instance_of?(Float) )
            return Pareja.new(other, other)
        else
        	if ( !other.instance_of?(Pareja) )
                raise NotImplementedError
        	end
        	return other
        end
    end

    #   Aritméticos

    def +(other)
    	other = self.int_to_self(other)
    	[@n1 + other.n1, @n2 + other.n2]
    end

    def -(other)
        other = self.int_to_self(other)
        [@n1 - other.n1, @n2 - other.n2]
    end

    def *(other)
    	other = self.int_to_self(other)
    	[@n1 * other.n1, @n2 * other.n2]
    end

    def coerce(other)  # Para que funione n + Pareja(x, y)
        [self, other]
    end

    # ------------------------------------------------

    # De comparación

    def <(other)
    	other = self.int_to_self(other)
    	(@n1 + @n2) < (other.n1 + other.n2)
    end

    def <=(other)
    	other = self.int_to_self(other)
    	(@n1 + @n2) <= (other.n1 + other.n2)
    end

    def ==(other)
    	other = self.int_to_self(other)
    	@n1  == other.n1 && @n2 == other.n2
    end

    def !=(other)
        other = self.int_to_self(other)
        @n1 != other.n1 || @n2 != other.n2
    end

    def >(other)
    	other = self.int_to_self(other)
    	(@n1 + @n2) > (other.n1 + other.n2)
    end

    def >=(other)
    	other = self.int_to_self(other)
    	(@n1 + @n2) >= (other.n1 + other.n2)
    end

end


# =============================== #
###       Inicialización        ###

pareja1 = Pareja.new(3, 5)     # initialize
pareja2 = Pareja.new(2, 7)



# =============================== #
###       Representación        ###

puts pareja1                   # to_s

# =============================== #
###  Sobrecarga de operadores   ###

# Aŕitméticos

suma = pareja1 + pareja2           # +  
suma2 = pareja1 + 1

suma3 = 3 + pareja1                # coerce -> +

resta = pareja1 - pareja2          # -
resta2 = pareja1 - 2
resta3 = 4 - pareja1               # coerce -> -


multiplicacion = pareja1 * pareja2 # *
multiplicacion2 = pareja1 * 3
multiplicacion3 = 3 * pareja1      # coerce -> *

# ----------------------------------------------

# De comparación
menor_que =       pareja1 <  pareja2    # <
menor_igual_que = pareja1 <= pareja2    # <=
igual =           pareja1 == pareja2    # ==
distinto =        pareja1 != pareja2    # !=
mayor_que =       pareja1 >  pareja2    # >
mayor_igual_que = pareja1 >= pareja2    # >=


=begin
Fuentes:
https://cdaddr.com/programming/ruby-to_s-vs-to_str/
https://stackoverflow.com/questions/43383145/ruby-overload-operator-behaviour-for-some-cases-only
https://stackoverflow.com/questions/2799571/in-ruby-how-does-coerce-actually-work
=end