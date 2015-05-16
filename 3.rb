def prime?(n)
	(2..(n/2)).each { |x| return false if n % x == 0}
	true
end

n = 600851475143
result = []
prod_sum = 1
x = 2

while prod_sum < n
	if n % x == 0 && prime?(x)
		result << x
		prod_sum *= x
	end
	x += 1
end

puts result[-1]