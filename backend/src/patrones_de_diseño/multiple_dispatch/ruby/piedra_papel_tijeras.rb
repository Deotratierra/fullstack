#!/usr/bin/ruby

class Outcome
	def initialize(value, name)
		@value = value
		@name = name
	end

	# Sobrecarga de operadores
	def to_s; return @name; end;

	def ==(other)
		return @value == other.value
	end

	# Métodos de clase
	def self.WIN; Outcome.new(0, "win"); end;
	def self.LOSE; Outcome.new(1, "lose"); end;
	def self.DRAW; Outcome.new(2, "draw"); end;
end


class Item
	def to_s; self.class.name; end;

	# Método para obtener las clases hijas
    def self.descendants
        ObjectSpace.each_object(Class).select { |klass| klass < self }
    end
end


class Paper < Item
	def compete(item)
		return item.evalPaper(self)
	end

	def evalPaper(item)
		return Outcome.DRAW
	end

	def evalScissors(item)
		return Outcome.WIN
	end

	def evalRock(item)
		return Outcome.LOSE
	end
end

class Scissors < Item
	def compete(item)
		return item.evalScissors(self)
	end

	def evalPaper(item)
		return Outcome.LOSE
	end

	def evalScissors(item)
		return Outcome.DRAW
	end

	def evalRock(item)
		return Outcome.WIN
	end
end

class Rock < Item
	def compete(item)
		return item.evalRock(self)
	end

	def evalPaper(item)
		return Outcome.WIN
	end

	def evalScissors(item)
		return Outcome.LOSE
	end

	def evalRock(item)
		return Outcome.DRAW
	end
end


def match(item1, item2)
	puts( "%s <--> %s: %s" % [
		item1, item2, item1.compete(item2)] )
end

def itemPairGen(n)
	response = []
	items = Item.descendants()
	for i in (1..n) do
        response.push( [items.sample.new,
                        items.sample.new] )
    end
    return response
end

for item1, item2 in itemPairGen(20) do
	match(item1, item2)
end
