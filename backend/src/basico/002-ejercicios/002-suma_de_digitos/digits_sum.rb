#!/usr/bin/ruby

num1, num2 = 4511, 369301;

def digits_sum(number)
    response, total = "", 0
    while (number != 0)
        rest = number % 10
        response += rest.to_s
        total += rest
        number /= 10
        if (number > 0)
            response += " + "
        end           
    end
    response += " = %d" % total
    return response
end

puts digits_sum(num1)
puts digits_sum(num2)
