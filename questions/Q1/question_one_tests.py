import unittest
from functools import cmp_to_key
from question_one import CustomString

class TestCustomString(unittest.TestCase): 
	def test_compare(self):
		data = [CustomString(10, 'Apples', '10Apples'), CustomString(11, 'Apples', '11Apples'), CustomString(5, 'Chicken', '5 Chicken'), CustomString(5, 'Chicken Wings', '5 Chicken Wings'), CustomString(1, 'Zoo', '1 Zoo')]
		sorted_data = ['1 Zoo', '5 Chicken', '5 Chicken Wings', '10Apples', '11Apples']
		data = [str(x) for x in sorted(data, key=cmp_to_key(CustomString.compare))]
		self.assertEqual(data, sorted_data)

if __name__ == '__main__':
	unittest.main()