# part I

def draw_stars(list):
	for x in list:
		print "*" * x

list = [10, 27, 1, 2]

draw_stars(list)


# part II

def draw_stars2(list):
	for x in list:
		if isinstance(x, int):
			print "*" * x
		elif isinstance(x, str):
			length = len(x)
			letter = x[0]
			print letter * length

list = [4, "Springer", 9, "Gonzalez", 3, "Maybin"]

draw_stars2(list)




