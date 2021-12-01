'''
Кожен новий метод чи атрибут має отримати щонайменше один тест. 
Якщо у методі є розгалуження (оператор if) - мають бути протестовані усі гілки.

+Додати поле description (опис) для Task. Значення за замовчанням - '' (пустий рядок)
+У Dashboard додати можливість сортування за Task title
+У Dashboard додати можливість пошуку задачі за словом, що входить у Task description
У Dashboard додати можливість вивести список активних задач 
(done == False), які містять задане слово у description
'''
class Task:

	def __init__(self, title, priority, description='', done='False'):
		self.title = title
		self.description = description
		self._priority = priority
		self.done = done


	def __str__(self):
		return self.title

	@property
	def priority(self):
		return self._priority

	@priority.setter    
	def priority(self, value):
		if value in range(1, 11):
			self._priority = value
		else:
			raise ValueError('Priority value is out of range')

class Dashboard:

	def __init__(self):
		self.task_list = []

	def sort_by_title(self):
		return sorted(self.task_list,
			key=lambda task: task.title)

	def find_title(self):
		search_world = input('Enter world:')
		find_list = []
		for task in self.task_list:
			if search_world in task.title:
				find_list.append(task.title)
		if find_list == []:
			find_list = 'Dont find!'
		return find_list

	def find_description(self):
		search_world = input('Enter world:')
		find_list = []
		for task in self.task_list:
			if search_world in task.description:
				find_list.append(task.title)
		if find_list == []:
			find_list = 'Dont find!'
		return find_list


	def active_tasks(self):
		search_world = input('Enter world:')
		active_list = []
		for task in self.task_list:
			if search_world in task.description and task.done == 'False':
				active_list.append(task.title)
		if active_list == []:
			active_list = 'Dont find active task!'
		return active_list

