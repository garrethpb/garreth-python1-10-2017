# assignment: Write a function that compares two lists
# and prints a message depending on whether or not they are identical
# If lists are identical, print: "These lists are the same."
# If lists are not identical, print: "These lists are not the same."

# here are a few tests cases (comment out the ones you are not testing):

# list_one = [1, 2, 3, 4, 5]
# list_two = [1, 2, 3, 4, 5]

# list_one = [1, 2, 3, 4, 5]
# list_two = [1, 2, 3, 4, 6]

list_one = ['broccoli', 'carrots', 'brussels sprouts', 'arugula']
list_two = ['broccoli', 'carrots', 'brussels sprouts', 'zucchini']

def compare_lists(list_one, list_two):
	if list_one == list_two:
		print "These lists are the same."
	else:
		print "These lists are not the same."

print compare_lists(list_one, list_two)

