from functools import cmp_to_key
import sys
import os 

class CustomString(): 
	"""
		Custom Object to make sorting easier.
	"""
	def __init__(self, num, chars, raw_string): 
		self.num = num 
		self.chars = chars
		self.raw_string = raw_string

	def compare(self, to_compare):
		"""
			Custom comparator to compare by number and then word. 
			Done in the style of what one might see in Java...
			...because never have I ever needed to sort like this 
			other than for a class project.
		"""
		if self.num - to_compare.num == 0: 
			# numbers are equivalent
			if self.chars < to_compare.chars:
				return -1 
			elif self.chars > to_compare.chars:
				return 1 
			else: 
				return 0 
		else: 
			# numbers are not equivalent
			return self.num - to_compare.num
			

	def __str__(self):
		return self.raw_string

def file_processor(f): 
	"""
		Method to convert lines from text file to CustomString objects.
	"""
	data_objs = []
	with open(f, 'r') as data:
		for line in data: 
			raw_string = line
			number = int(''.join(filter(str.isdigit, raw_string)))
			chars = ''.join(filter(str.isalpha, raw_string))
			data_objs.append(CustomString(number, chars, raw_string))
	return data_objs

def save_sorted_data(data):
	with open('sorted.txt', 'w') as f:
		f.writelines([str(x) for x in data])

if __name__ == '__main__':
	data = file_processor(sys.argv[1])
	data = sorted(data, key=cmp_to_key(CustomString.compare))
	save_sorted_data(data)
