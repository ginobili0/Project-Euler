n = 20

until (11..20).all? { |x| n % x == 0 }
	n += 20
end

puts num
