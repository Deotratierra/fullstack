#!/bin/ruby

class Shape
    def factory(type)
        if (type == "Circle"); return Circle.new; end;
        if (type == "Square"); return Square.new; end;
        puts "Bad shape creation: %s" % type
        raise NotImplementedError
    end

    # Método para obtener las clases hijas
    def self.descendants
        ObjectSpace.each_object(Class).select { |klass| klass < self }
    end
end

class Circle < Shape
    def draw; puts ("Circle.draw"); end;
    def erase; puts ("Circle.erase"); end;
end

class Square < Shape
	def draw; puts ("Square.draw"); end;
    def erase; puts ("Square.erase"); end;
end

def shapeNameGen(n)
	types = Shape.descendants()
	response = []

	for i in (1..n) do
		response.push(types.sample.to_s)
	end
	return response
end

S = Shape.new

for shape in shapeNameGen(7) do
	shape = S.factory(shape)
    shape.draw
    shape.erase
end

=begin
Fuentes:
http://www.eq8.eu/blogs/13-ruby-ancestors-descendants-and-other-annoying-relatives
=end