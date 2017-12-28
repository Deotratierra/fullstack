#!/usr/bin/ruby

num1, num2 = 3, 5

# Ruby es muy simple!

#def mayor(a, b)  <----- Así también funciona
def mayor a, b
    if a > b    # Así tambien ----> if (a > b)
        a
    else
        b
    end
end

puts mayor num1, num2
#puts mayor(num1, num2) <----- Así también

