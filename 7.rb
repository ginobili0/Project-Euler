def prime?(n)
	(2..n/2).each{ |x| return false if n % x == 0 }
	true
end

def nth_prime(n)
	count = 2
	i = 4
	while true
		count += 1 if prime?(i)
		break if count == n
		i += 1
	end
	return i
end

puts nth_prime(10001)

