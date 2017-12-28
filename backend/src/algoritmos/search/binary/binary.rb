#!/bin/ruby

def binary_search(array, query)
    lo, hi = 0, array.length - 1
    while (lo <= hi)
        mid = lo + (hi - lo) / 2
        val = array[mid]
        if (val == query)
            return mid
        elsif (val < query)
            lo = mid + 1
        else
            hi = mid - 1
        end
    end
    return nil
end


def main
    array = [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6]
    print array, "\n"
    print "Encontrado ", 5, " en el índice: ", binary_search(array, 5), "\n"
    print "Encontrado ", -1, " en el índice: ", binary_search(array, -1), "\n"
end


if __FILE__ == $0
    main()
end