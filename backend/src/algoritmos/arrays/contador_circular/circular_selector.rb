#!/usr/bin/ruby

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def circular_selector(int_list, skip)
    skip = skip - 1
    idx, response = 0, []
    len_list = int_list.length
    while (len_list > 0)
        idx = (skip + idx) % len_list
        response.push(int_list[idx])
        int_list.delete_at(idx)
        len_list -= 1
    end
    return response
end

print circular_selector(a, 3)
