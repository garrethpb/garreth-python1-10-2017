astros_infielders = [
	{'first_name' : 'Yuli', 'last_name' : 'Gurriel'},
	{'first_name' : 'Jose', 'last_name' : 'Altuve'},
	{'first_name' : 'Carlos', 'last_name' : 'Correa'},
	{'first_name' : 'Alex', 'last_name' : 'Bregman'}
]

astros = {
'Outfielders': [
	{'first_name' : 'George', 'last_name' : 'Springer'},
	{'first_name' : 'Marwin', 'last_name' : 'Gonzalez'},
	{'first_name' : 'JJ', 'last_name' : 'Reddick'}
],

'Infielders': [
	{'first_name' : 'Yuli', 'last_name' : 'Gurriel'},
	{'first_name' : 'Jose', 'last_name' : 'Altuve'},
	{'first_name' : 'Carlos', 'last_name' : 'Correa'},
	{'first_name' : 'Alex', 'last_name' : 'Bregman'}
]
}

def outputInfielders(arr):
    for i in arr:
        print i['first_name'],i['last_name']

def outputAstros(astros):
	for i in astros:
		counter = 0
		print i 
		for player in astros[i]:
			counter += 1
			first_name = player['first_name']
			last_name = player['last_name']
			length = len(first_name) + len(last_name)
			print '{} - {} {} - {}'.format(counter, first_name, last_name, length)

outputInfielders(astros_infielders)
outputAstros(astros)
