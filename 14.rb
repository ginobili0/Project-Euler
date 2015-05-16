def collatz_length(x)
	return x if x <= 1

	count = 1
	while x > 1
		if x % 2 == 0
			x = x / 2
			count += 1
		else
			x = 3 * x + 1
			count += 1
		end
	end
	count
end

start = 1
longest_chain = 0

1.upto(1000000) do |n|
	l = collatz_length(n)
	start, longest_chain = n, l if l > longest_chain
end

puts start
puts longest_chain