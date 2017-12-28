#!/usr/bin/ruby

def garage(initial, final)
    steps = 0
    len_initial = initial.length
    while initial != final do
        zero = initial.index(0)
        if zero != final.index(0)
            car_to_move = final[zero]
            pos = initial.index(car_to_move)
            initial[zero], initial[pos] = [initial[pos], initial[zero]]
        else
            for i in (0..len_initial)
                if initial[i] != final[i]
                    initial[zero], initial[i] = [initial[i], initial[zero]]
                    break
                end
            end
        end
        steps += 1
        #print initial, "\n"
    end
    return steps

end


if (__FILE__ == $0)
    initial = [1, 2, 3, 0, 4]
    final =   [0, 3, 2, 1, 4]
    print "initial: ", initial, "\n"
    print "final: ", final, "\n"
    p garage(initial, final)
end