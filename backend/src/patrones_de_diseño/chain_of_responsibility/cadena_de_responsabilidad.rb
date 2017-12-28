#!/bin/ruby

#####     Código servidor     #####

class Evento
    def initialize(nombre)
        @nombre = nombre
    end

    attr_reader :nombre
end

class Manejador
    # Base de la interfaz del manejador
    def initialize(sucesor=nil)
        @_sucesor = sucesor
    end

    def manejar(evento)
        # Obtenemos el método que manejará el evento
        manejador = "manejar_" + evento.nombre

        # Si el manejador posee el método que
        # puede manejar el evento...
        if self.public_methods.include? manejador.to_sym
            method(manejador).call(evento)

        # Este es un detalle de implementación y no es
        # estrictamente necesario, añade un soporte a todos
        # los manejadores (por ejemplo, cazar a todos los
        # eventos no soportados)
        elsif self.public_methods.include? "manejar_por_defecto".to_sym
            method("manejar_por_defecto").call(evento)

        # Pasa al próximo manejador en la cadena
        # si este existe
        elsif Manejador.method_defined? "_sucesor"
            @_sucesor.manejar(evento)
        end
    end

    attr_reader :_sucesor
end

# Manejadores concretos
class FinalDeCadena < Manejador
    def manejar_cierre(evento)
        puts "FinalDeCadena: #{evento.nombre}"
    end

    def manejar_por_defecto(evento)
        puts "Defecto: #{evento.nombre}"
    end
end

class MitadDeCadena < Manejador
    def manejar_hacer(evento)
        puts "MitadDeCadena: #{evento.nombre}"
    end
end

class PrincipioDeCadena < Manejador
    def manejar_accion(evento)
        puts "PrincipioDeCadena: #{evento.nombre}"
    end
end

# ===============================================

#####     Código cliente     #####

# Manejadores                            # Métodos soportados

final = FinalDeCadena.new                # [cierre, por_defecto]
mitad = MitadDeCadena.new(final)         # [cierre, por_defecto, hacer]
principio = PrincipioDeCadena.new(mitad) # [cierre, por_defecto, hacer, accion]

# ^^^^^^
# Construimos la cadena de forma que el principio
# pueda manejar todos los eventos soportados,
# ya que hereda de todos los manejadores

eventoHacer = Evento.new("hacer")
eventoAccion = Evento.new("accion")
eventoCierre = Evento.new("cierre")
eventoNulo = Evento.new("nulo")

if __FILE__ == $0
    puts

    # Pasamos los eventos al principio de la cadena
    puts "Debe imprimir PrincioDeCadena: accion"
    principio.manejar(eventoAccion)

    puts "\n-----------------------\n"

    puts "Debe imprimir MitadDeCadena: hacer"
    principio.manejar(eventoHacer)

    puts "\n-----------------------\n"

    puts "Debe imprimir FinalDeCadena: cierre"
    principio.manejar(eventoCierre)

    puts "\n-----------------------\n"

    puts "Debe imprimir Defecto: nulo"
    principio.manejar(eventoNulo)
end

