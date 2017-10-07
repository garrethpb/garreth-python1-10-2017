name = ["Garreth", "Dax", "Gray", "Brian", "Lauren"]
favorite_animal = ["horse", "cat", "fox", "rhino", "dog"]

def create_dict(arr1, arr2):
	new_dict = {}
	zipped = zip(arr1, arr2)
	new_dict = dict(zipped)
	return new_dict

new_dict2 = create_dict(name, favorite_animal)

for x in name:
	print new_dict2[x]

