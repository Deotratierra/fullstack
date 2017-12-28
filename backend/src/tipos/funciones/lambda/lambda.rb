#!/bin/ruby

#####     FUNCIONES LAMBDA     #####

def funcion_normal(x); x**2; end;
puts funcion_normal(4)

# ----------------------------------

funcion_lambda = lambda{ |x| x**2 }
puts funcion_lambda.call(4)

# Hay otras formas de crear y llamar lambdas
lambda_simple = ->(x){ x**2 }
puts lambda_simple.call(4)
puts lambda_simple[4]     # Más fácil
puts lambda_simple.(4)    # Anarquía sintática
puts lambda_simple === 4  # Stop please

