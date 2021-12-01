import unittest

from lesson22 import linear_shift, circular_shift, nested_parentheses

class TestTask(unittest.TestCase):

	def test_linear_shift(self):
		test_list = [1, 2, 3, 4]
		list_linear = linear_shift(test_list, 3)
		self.assertEqual(list_linear, [0, 0, 0, 1])

	def test_circular_shift(self):
		test_list = [1, 2, 3, 4]
		list_circular = circular_shift(test_list, 2)
		self.assertEqual(list_circular, [3, 4, 1, 2])

	def test_nested_parentheses(self):
		incoming1 = "((())(())())"
		incoming2 = "())"
		self.assertTrue(nested_parentheses(incoming1))
		self.assertFalse(nested_parentheses(incoming2))

if __name__ == '__main__':
	unittest.main()