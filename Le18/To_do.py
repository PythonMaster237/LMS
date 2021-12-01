import unittest

from unittest.mock import patch, Mock

from Less18 import Task, Dashboard

class TestTask(unittest.TestCase):

	def test_task_object(self):
		task = Task('Task1', '2')
		self.assertEqual(task.description, '')

	@patch('builtins.input', return_value='Buy')
	def test_find_correct_title(self, mock_input):
		task1 = Task('Buy something', '2')
		task2 = Task('Sell something', '3')
		dashboard = Dashboard()
		dashboard.task_list.extend([task1, task2])
		self.assertEqual(dashboard.find_title(), [task1.title])

	@patch('builtins.input', return_value='Tr')
	def test_find_wrong_title(self, mock_input):
		task1 = Task('Buy something', '2')
		task2 = Task('Sell something', '3')
		dashboard = Dashboard()
		dashboard.task_list.extend([task1, task2])
		self.assertEqual(dashboard.find_title(), 'Dont find!')

	def test_sort_by_title(self):
		task1 = Task('B something', '2')
		task2 = Task('A something', '3')
		task3 = Task('C something', '1')
		dashboard = Dashboard()
		dashboard.task_list.extend([task1, task2, task3])
		self.assertEqual(dashboard.sort_by_title(), 
							[task2, task1, task3])	

	@patch('builtins.input', return_value='Buy')
	def test_find_correct_description(self, mock_input):
		task1 = Task('Buy something', '2')
		task1.description = 'Buy'
		task2 = Task('Sell something', '3')
		task2.description = 'Sell'
		task3 = Task('C something', '1')
		task3.description = 'Buy'
		dashboard = Dashboard()
		dashboard.task_list.extend([task1, task2, task3])
		self.assertEqual(dashboard.find_description(), 
			[task1.title, task3.title])

	@patch('builtins.input', return_value='Rt')
	def test_find_wrong_description(self, mock_input):
		task1 = Task('Buy something', '2')
		task1.description = 'Buy'
		task2 = Task('Sell something', '3')
		task2.description = 'Sell'
		task3 = Task('C something', '1')
		task3.description = 'Buy'
		dashboard = Dashboard()
		dashboard.task_list.extend([task1, task2, task3])
		self.assertEqual(dashboard.find_description(), 
			'Dont find!')

	@patch('builtins.input', return_value='Today')
	def test_correct_active_tasks(self, mock_input):
		task1 = Task('Buy something', '2', 'Tomorrow')
		task2 = Task('Sell something', '3', 'Today')
		task3 = Task('C something', '1', 'Today')
		dashboard = Dashboard()
		dashboard.task_list.extend([task1, task2, task3])
		self.assertEqual(dashboard.active_tasks(),
			[task2.title, task3.title])

	@patch('builtins.input', return_value='Yesterday')
	def test_wrong_active_tasks(self, mock_input):
		task1 = Task('Buy something', '2', 'Tomorrow', 'Done')
		task2 = Task('Sell something', '3', 'Today', 'Done')
		task3 = Task('C something', '1', 'Today', 'Done')
		dashboard = Dashboard()
		dashboard.task_list.extend([task1, task2, task3])
		self.assertEqual(dashboard.active_tasks(),
			'Dont find active task!')


if __name__ == '__main__':
	unittest.main()

