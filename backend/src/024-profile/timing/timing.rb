#!/usr/bin/ruby

# ===================================================0

def fn_timer(func=nil, miliseconds=false, *args)
    start_time = Time.now
    puts args
    if block_given? # Soporte para bloques de código
    	yield
    else
        response = self.send(func, args)
    end
    end_time = Time.now
    msg = "Total time running #{func.to_s}(): "
    elapsed_time = end_time - start_time
    unit_time = "seconds"
    if (miliseconds)
    	elapsed_time *= 1000
    	unit_time = "miliseconds"
    end
    puts msg += "#{elapsed_time} #{unit_time}"
    return response
end

# =====================================================

def slow_function(*args)
   for _ in (0..10000)
       _+= 1
   end
end

# Calculamos una función
fn_timer(:slow_function, miliseconds=true)

# Calculamos un bloque de código
fn_timer do
	for _ in (0..10000)
       _+= 1
   end
end

# Fuente:
# https://www.skorks.com/2010/03/timing-ruby-code-it-is-easy-with-benchmark/