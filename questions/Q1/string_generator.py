from random import randint, choice
from string import ascii_letters
from sys import maxsize, argv

"""
	Utility file to generate test data.
"""

def generate_string():
	"""
		Method to generate random strings for sorting
	"""
	ret_string = ''
	num = str(randint(0, maxsize))
	if randint(1, 2) % 2 == 0: 
		rand_string = ''.join(choice(ascii_letters) for i in range(randint(1, 999 - len(num))))
		ret_string = '{} {}\n'.format(num, rand_string)
	else: 
		rand_string = ''.join(choice(ascii_letters) for i in range(randint(1, 1000 - len(num))))
		ret_string = '{}{}\n'.format(num, rand_string) 
	return ret_string

def generate_file(num_lines): 
	"""
		Method to populate test file.
	"""
	str_list = []
	for i in range(1, num_lines):
		str_list.append(generate_string())
	with open('testdata.txt', 'w') as f: 
		f.writelines(str_list)


if __name__ == '__main__':
	generate_file(int(argv[1]))