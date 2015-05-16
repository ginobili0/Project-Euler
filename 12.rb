sum = 0
tri_number[n] = (0..n + 1).each{ |x| sum += x }

puts tri_number[7]