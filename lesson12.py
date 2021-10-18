import datetime


class Student:

  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

  def __str__(self):
    return f'{self.first_name} {self.last_name}'


class LessonCell:
  def __init__(self, student, mark):
    self.student = student
    self.mark = mark
    if self.mark == '':
      self.mark = 'Absent'

  def __str__(self):
    return f'{self.student} {self.mark}'


class Lesson:

  CELLS = []

  def __init__(self, students, date=datetime.date.today()):
    self.date = date
    Lesson.CELLS.append(self.date)
    for student in students:
      Lesson.CELLS.append(LessonCell(student, input('Enter mark of student:\t')))

  def __str__(self):
    return f'{self.date}'

  def cells_print(self):
    for cell in Lesson.CELLS:
      print(cell)


student1 = Student('Vasyl', 'Petrov')
student2 = Student('Vasyl', 'Ivanov')
student3 = Student('Vasyl', 'Sidorov')
students = [student1, student2, student3]

Math = Lesson(students)
Math.cells_print()