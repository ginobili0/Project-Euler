
fib = [1, 2]
upto = 4000000

while fib[-2] + fib[-1] < upto
	fib << fib[-2] + fib[-1]
end

sum = 0
fib.each { |x| sum += x if x.even?}

puts sum