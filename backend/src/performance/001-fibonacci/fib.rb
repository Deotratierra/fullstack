
def fib(n)
    a, b = 0, 1
    (0..n).step(1) do |i|
        a, b = a + b, a
    end
    return a
end

if __FILE__ == $0
    arg = Integer(ARGV[0])
    fib(arg)
end
