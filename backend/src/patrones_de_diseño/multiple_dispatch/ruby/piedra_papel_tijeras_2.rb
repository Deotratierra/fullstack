#!/usr/bin/ruby

require_relative "objs"

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
	def compete(item)
		return $outcome[ [self.class.name,
		                 item.class.name] ]
    end

    def to_s; return self.class.name; end;

    def self.descendants
        ObjectSpace.each_object(Class).select { |klass| klass < self }
    end
end

class Paper < Item; end;
class Scissors < Item; end;
class Rock < Item; end;

# Variable global
$outcome = {
  [Paper, Rock] => Outcome.WIN,
  [Paper, Scissors] => Outcome.LOSE,
  [Paper, Paper] => Outcome.DRAW,
  [Scissors, Paper] => Outcome.WIN,
  [Scissors, Rock] => Outcome.LOSE,
  [Scissors, Scissors] => Outcome.DRAW,
  [Rock, Scissors] => Outcome.WIN,
  [Rock, Paper] => Outcome.LOSE,
  [Rock, Rock] => Outcome.DRAW,
}

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
