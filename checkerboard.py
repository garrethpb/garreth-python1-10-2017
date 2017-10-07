def checkerboard():

	for i in range(0, 10):
		if i % 2 == 0:
			print "* " * 10
		else:
			print " *" * 10

print checkerboard()