num = 2**1000
num = num.to_s
num_arr = num.split("")
sum = 0
num_arr.each { |x| sum += x.to_i }
puts sum