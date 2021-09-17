import json
import csv

student_fields = ['first_name', 'last_name', 'email', 'age', 'address', 'gender']

STUDENTS = []

TEST_STUDENTS = [
    ['Mary', 'D', 'mail@mail.com', '19', 'Huston', 'F'],
    ['John', 'S', 'new_mail@mail.com', '21', 'London', 'M'],
    ['Andy', 'H', 'more_mail@mail.com', 'sexteen', 'Brighton', 'M']
]

def add_student():
    student = {}
    for field in student_fields:
        student[field] = input('Enter {}\t'.format(field))
        if field == 'age':
            try:
                int(student['age'])
            except:
                student['age'] = input('Enter age as number\t')
    STUDENTS.append(student)

def calculate_avg_age():
    try:
        total_age = 0
        for student in STUDENTS:
            total_age += int(student['age'])
        avgerage_age = total_age / len(STUDENTS)
        print('Average age is {}'.format(avgerage_age))
    except ValueError:
        print('Cannot calculate average age')
    except Exception as e:
        print(str(e))

def print_student(student):
    b = []
    for st in student_fields:          
        b.append(len(st))
        max_str = max(b) * 2        # distance between column1 and column2 in print
    for field in student:
        a = field.replace('_', ' ')
        print(a.capitalize(), ' '* (max_str - len(a)), student[field])
    print('\n')  

def print_strudents_list():
    for student in STUDENTS:
        print_student(student)

def load_students():
    for test_student in TEST_STUDENTS:
        STUDENTS.append(dict(zip(student_fields, test_student)))

def dump_csv():
    with open('data/student_data.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=student_fields)
        writer.writeheader()
        for student in STUDENTS:
            writer.writerow(student)

def load_from_csv(file_path='student_data.csv'):
    with open('data/student_data.csv', 'r') as file:
        STUDENTS.extend(csv.DictReader(file))

def dump_students():
    with open('data/student_data.json', 'w') as file:
        json.dump(STUDENTS, file)

def load_from_json(file_path='data/student_data.json'):
    with open(file_path, 'r') as read_file:
        STUDENTS.extend(json.load(read_file))

ACTIONS = {
    'add': add_student,
    'avg_age': calculate_avg_age,
    'load': load_students,
    'print': print_strudents_list,
    'dump_json': dump_students,
    'dump_csv': dump_csv,
    'load_json': load_from_json,
    'load_csv': load_from_csv
}

while True:
    action = input('Desired action:\t')
    if action in ACTIONS:
        ACTIONS[action]()
    else:
        break