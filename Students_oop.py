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

	def __str__(self):
		return '{} {} {} {} {} {}'.format(
		self.first_name, self.last_name, self.email, 
		self.age, self.address, self.gender
		)		

	def print_student(self):
		print(self.first_name)
		print(self.last_name)
		print(self.email)
		print(self.age)
		print(self.address)
		print(self.gender)

	def to_dict(self):
		student_dict = {}
		for field in ['first_name', 'last_name', 'email', 'age', 'address', 'gender']:
			student_dict[field] = getattr(self, field, '')
		return student_dict

	def from_dict(self):
		pass


class Group:

	def __init__(self, students_list, name_group = 'Group A'):
		self.students_list = students_list
		self.name_group = name_group

	def print_students_list(self):
		for student in self.students_list:
			student.print_student()
			print(self.name_group)

	def add_student(self):
		self.students_list.append(Student(
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
		with open('data/student_data.csv', 'w') as file:
			writer = csv.DictWriter(file, fieldnames=
			['first_name', 'last_name', 'email', 'age', 'address', 'gender'])
			writer.writeheader()
			for student in self.students_list:
				row = student.to_dict()
				writer.writerow(row)

	def load_from_csv(self):
		studs_test = []
		with open('data/student_data.csv', 'r') as file:
			studs = []
			studs.extend(csv.DictReader(file))
			for st in studs:
				st = Student(
					st['first_name'], 
					st['last_name'], 
					st['email'], 
					st['age'], 
					st['address'], 
					st['gender']
					)
				studs_test.append(st)
		return print(studs_test)

	def dump_students_json(self):
		row = []
		with open('data/student_data.json', 'w') as file:
			for student in self.students_list:
				row.append(student.to_dict())		
			json.dump(row, file)

	def load_from_json(self):
		studs = []
		with open('data/student_data.json', 'r') as read_file:
			studs.extend(json.load(read_file))
			print(studs)

	def load_students(self, value):
#		list_load = []
		for st in value:
			st = Student(
				st[0],
				st[1],
				st[2],
				st[3],
				st[4],
				st[5]
				)
			self.append(st)

stud = Student('Mary', 'D', 'mail@mail.com', '19', 'Huston', 'F')
stud2 = Student('John', 'S', 'new_mail@mail.com', '21', 'London', 'M')
stud4 = Student('Andy', 'H', 'more_mail@mail.com', '29', 'Brighton', 'M')
studs = [stud, stud2, stud4]
group = Group(studs)

studs_load = []
#Group.add_student(group)
#Group.print_students_list(group)
#Group.calculate_avg_age(group)
#Group.dump_csv(group)
#Group.load_from_csv(studs_load)
#Group.dump_students_json(group)
#Group.load_from_json(studs_load)

stud_list = [
['Joma', 'I', 'some_mail@mail.com', '28', 'Texas', 'M'],
['Calvin', 'C', 'calvinmail@mail.com', '36', 'Washington', 'M'],
['Sandra', 'B', 'sandramail@mail.com', '40', 'Paris', 'F']
]

Group.load_students(studs, stud_list)
group = Group(studs)
Group.print_students_list(group)