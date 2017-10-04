# this program is meant to test values for their type, 
# then return a message based on some other parameter

# here is a list of given variables:

sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

# line 23 allows a user to change current variable under examination

current_variable = sS

# and here is the rest of the code:

current_data_type = type(current_variable)

if current_data_type is int:
	if current_variable >= 100:
		print "That's a big number!"
	else: print "That's a small number."

elif current_data_type is str:
	if len(current_variable) >= 50:
		print "That's a long sentence."
	else:
		print "That's a short sentence."

elif isinstance(current_variable, list):
	if len(current_variable) >= 10:
		print "That's a big list!"
	else: print "That's a short list."