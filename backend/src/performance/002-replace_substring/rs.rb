

def rs()
    (0..Integer(ARGV[0])).step(1) do |_|
        string = "Salida de emergencia"
        pattern = "Salida"
        substitution = "Entrada"
        result = string.sub(pattern, substitution)
    end
end

if __FILE__ == $0
    rs()
end
