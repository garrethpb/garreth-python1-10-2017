# print odd numbers from 1 to 1000, using for loop
for print_odd in range(1, 1001, 2):
	print print_odd

# print multiples of 5 from 5 to 1000000
for print_fives in range(5, 1000000, 5):
	print print_fives

# sum all numbers in list a = [1, 2, 5, 10, 255, 3]
list_a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in list_a:
	sum += i
print sum

# find average of all numbers in list a = [1, 2, 5, 10, 255, 3]
print sum/len(list_a)

