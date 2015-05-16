sum = 0
square_sum = 0

(1..100).each do |x| 
	square_sum += x ** 2
	sum += x
end

puts sum**2 - square_sum

