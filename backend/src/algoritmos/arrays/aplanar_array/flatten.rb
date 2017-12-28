#!/bin/ruby

a = ["elem1"]
b = [2, 1, [3, [4, 5], 6], 7, [8]]

def flatten(l, source=nil)
    if ( !source.instance_of?(Array) ); source = []; end;
    for i in l do
        if ( i.instance_of?(Array) )
            source = flatten(i, source)
        else
            source.push(i)
        end
    end
    return source
end

print flatten(b, a)
