def palindrome?(x)
	x = x.to_s
	return true if x == x.reverse
	false
end

def divisible?(x)
	999.downto(100).each { |y| return true if x % y == 0 && (x / y).to_s.length == 3 }
	false
end

999999.downto(100000).each do |x|
	if palindrome?(x) && divisible?(x)
		puts x
		break
	end
end

