#!/bin/ruby


def bubble_sort(array)
    n = array.length
    intercambiado = true
    while (intercambiado)
        intercambiado = false
        (1..n-1).step(1) do |i|
            if (array[i - 1] > array[i])
                array[i - 1], array[i] = array[i], array[i - 1]
                intercambiado = true
            end
        end
    end
    return array

end

if __FILE__ == $0
    array = [1, 5, 65, 23, 57, 1232, -1, -5, -2, 242, 100,
             4, 423, 2, 564, 9, 0, 10, 43, 64, 32, 1, 999]
    print(array, "\n")
    array = bubble_sort(array)
    print(array, "\n")
end
