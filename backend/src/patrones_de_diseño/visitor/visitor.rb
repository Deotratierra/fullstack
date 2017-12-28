#!/bin/ruby

class NoModificable; end;

# Las superclases de Flor no pueden ser modificadas
class Flor < NoModificable
    def aceptar(visitante)
        visitante.visitar(self)
    end
    def polinizar(polinizador)
        puts("#{self} polinizado por #{polinizador}")
    end
    def depredar(depredador)
        puts("#{self} depredado por #{depredador}")
    end

    # Sobrecarga de salida como cadena
    def to_s; self.class.name; end;

    # Método para obtener las clases hijas
    def self.descendants
        ObjectSpace.each_object(Class).select { |klass| klass < self }
    end
end

class Gladiolo < Flor; end;
class Tulipan < Flor; end;
class Crisantemo < Flor; end;

class Visitante
	def to_s; self.class.name; end;
end

class Insecto < Visitante; end;
class Polinizador < Insecto; end;
class Depredador < Insecto; end;

class Abeja < Polinizador
    def visitar(flor)
        flor.polinizar(self)
    end
end

class Mosquito < Polinizador
    def visitar(flor)
        flor.polinizar(self)
    end
end

class Gusano < Depredador
    def visitar(flor)
        flor.depredar(self)
    end
end


def flowerGen(n)
    response = []
    flores = Flor.descendants()
    for _ in (0..n) do
        response.push(flores.sample().new)
    end
    return response
end


abeja = Abeja.new
mosquito = Mosquito.new
gusano = Gusano.new

for flor in flowerGen(10) do
	flor.aceptar(abeja)
    flor.aceptar(mosquito)
    flor.aceptar(gusano)
end
