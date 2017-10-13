arr = [1,3,5,7,9,13]

def return_greater():
	counter = 0
	for i in range(0, len(arr)):
		if arr[i] > arr[1]:
			print arr[i]
			counter = counter + 1
	print counter

print return_greater()
