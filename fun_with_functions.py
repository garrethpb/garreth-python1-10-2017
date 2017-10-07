# challenge: create a function called odd_even that iterates between 1 and 2000.
# As the loop iterates, print whether the number is odd or even.
# Output should look like this:
# Number is 1. This is an odd number.
# Number is 2. This is an even number.
# etc...


def odd_even():
	for i in range (1, 1000):
		if i % 2 == 0:
			print "The number is " + str(i) + "." + "This is an even number."
		else:
			print "The number is" + str(i) + "." + "This is an odd number."
	
odd_even()


a = [2,4,10,16]

def multiply(arr):
	new_array = []
	for i in arr:
		i = i * 5
		new_array.append(i)
	print new_array

multiply(a)


