# assignment: Write a program that takes a list of strings
# and a given letter and returns a new list that 
# prints out only the strings that contain the letter.

# example input:
# string_list = ['hello', 'world', 'my', 'name', 'is', 'Garreth']
# char = 'o'
# example output:
# new_string_list = ['hello', 'world']

def find_characters(string_list, char):
	new_string_list = []

	for i in range(0, len(string_list)):

		if string_list[i].find(char) != -1:
			new_string_list.append(string_list[i])

	print new_string_list

string_list = ['hello', 'world', 'my', 'name', 'is', 'Garreth']
find_characters(string_list, 'o')

# Breakdown of this code:
# line 11: declare variable "find_characters", set up to pass 2 parameters,
# "string_list" and "char". "string_list" will hold the words I want to check,
# "char" is the letter to look for.

# line 12: define a new empty list called "new_string_list".

# line 14: set up for loop. 
# *"i" is essentially blank variable (same is used often in JS)
# *"in range" is standard syntax for iterating through a list in Py
# *"0" stands for the index - starting at the first member of the list
# *"len(string_list)" tell the loop how many times to go through:
# *as many times as there are members in the list.

# line 16:
# setting up an "if" statement to tell the function what to do.
# if the function finds the character "o" it knows to "flag it"
# (I don't know what the "-1" means)

# line 17:
# telling the function to add (append) every word that contains the character
# onto a new list, which will be called "new_string_list"

# line 19:
# getting the output - tells the computer to print the new string_list
# created by the program

# lines 21-22: defines the 2 arguments passed into the function