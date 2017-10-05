# challenge: create a function called odd_even that iterates between 1 and 2000.
# As the loop iterates, print whether the number is odd or even.
# Output should look like this:
# Number is 1. This is an odd number.
# Number is 2. This is an even number.
# etc...


def odd_even():
	for odd_even in range (1, 1000, 1):
		if odd_even % 2 == 0:
			print "The number is ", odd_even, ".","This is an even number."
		else:
			print "The number is", odd_even, ".", "This is an odd number."
	
odd_even()