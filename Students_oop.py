import json
import csv

class Student:

	def __init__(self, first_name, last_name, email, age, address, gender):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.age = age
		self.address = address
		self.gender = gender

	def print_student(self):
		print(self.first_name)
		print(self.last_name)
		print(self.email)
		print(self.age)
		print(self.address)
		print(self.gender)


class Group:

	def __init__(self, students_list, name_group = 'Group A'):
		self.students_list = students_list
		self.name_group = name_group

	def print_students_list(self):
		for student in self.students_list:
			Student.print_student(student)
			print(self.name_group)

	def add_student(self):
		studs.append(Student(
					input('First name:\t'), 
					input('Second name:\t'),
					input('email:\t'), 
					input('age:\t'), 
					input('address:\t'), 
					input('gender:\t')
					))

	def calculate_avg_age(self):
		total_age = 0
		try:
			for student in self.students_list:
				if hasattr(student, 'age'):
					total_age += int(student.age)
			avr_age = total_age/len(self.students_list)
			print('Average age is {}'.format(avr_age))
		except ValueError:
			print('Cannot calculate average age')
		except Exception as e:
			print(str(e))

	def dump_csv(self):
		pass

	def load_from_csv(self):
		pass

	def dump_students(self):
		pass

	def load_from_json(self):
		pass

	def load_students(self):
		pass

stud = Student('Mary', 'D', 'mail@mail.com', '19', 'Huston', 'F')
stud2 = Student('John', 'S', 'new_mail@mail.com', '21', 'London', 'M')
stud4 = Student('Andy', 'H', 'more_mail@mail.com', '29', 'Brighton', 'M')
studs = [stud, stud2, stud4]

group = Group(studs)

#Group.add_student(Student)
#Group.print_students_list(group)
#Group.calculate_avg_age(group)

#Group.dump_csv(group)
#Group.dump_students(group)