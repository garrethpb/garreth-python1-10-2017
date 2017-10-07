astros_infielders = {
	'first_base' : 'Yuli Gurriel',
	'second_base' : 'Jose Altuve',
	'third_base' : 'Alex Bregman',
	'shortstop' : 'Carlos Correa'
}

def make_tuple(arr):
	return [(k, v) for k, v in arr.iteritems()]

print make_tuple(astros_infielders)


#function output
#[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]
