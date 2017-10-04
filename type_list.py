# This program is meant to take lists and print a message
# for each element in the list, based on each element's data type.
# The input is always a list.
# further instructions:
# 1. Test each element's data type.
# 2. If element is string, concatenate it onto a new string.
# 3. If element is a number, add it to a running sum.
# 4. At the end, print the string, the number, and an 
# analysis of what the list contains.
# 5. if list contains one data type, print that. 
# Otherwise, print "mixed".

# the following lists were given:

mixed_list = ['Novice coders say ', 19, 'hello ', 98.98, 'world.']
integers_only = [1, 2, 3, 4, 5]
strings_only = ["Guitar, ", "mandolin, ", "ukulele"]

def list_type(lst):
	new_string = ''
	running_sum = 0

	for value in lst:
		if isinstance(value, int) or isinstance(value, float):
			running_sum += value
		elif isinstance(value, str):
			new_string += value

	if new_string and running_sum:
		print "This list is mixed"
		print "String: ", new_string
		print "Total: ", running_sum

	elif new_string:
		print "This list is a string."
		print "String: ", new_string

	else:
		print "The list is made of integers."
		print "Total: ", running_sum

print list_type(mixed_list)
print list_type(integers_only)
print list_type(strings_only)