#!/usr/bin/ruby

def longest_non_repeat(s)
	start, maxlen = [0, 0]
	used_char = {}
	s.split("").each_with_index do |char, i|
        if ( used_char.key?(char) && start <= used_char[char] )
        	start = used_char[char] + 1
        else
        	maxlen = [maxlen, i-start+1].max
        end
        used_char[char] = i
	end
	return maxlen
end


a = "abcabcdefbb"
p(a)
p(longest_non_repeat(a)) # 6