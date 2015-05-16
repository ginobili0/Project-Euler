def prime?(n)
	(2..n/2).each{ |x| return false if n % x == 0 }
	true
end

sum = 5
(4...2000000).each{ |x| sum += x if prime?(x) }

puts sum