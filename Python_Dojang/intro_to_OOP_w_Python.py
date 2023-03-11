my_student = {
    'name': 'Rolf Smith',
    'grades': [70, 88, 90, 99],
    'average': None # something here
}

def average_grade(student):
    return sum(student['grades'])/len(student['grades'])

class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades
    
    def average(self):
        return sum(self.grades) / len(self.grades)

student_one = Student('Rolf Smith', [70, 88, 90, 99])
student_two = Student('Jose Anderson', [50, 60, 99, 100])

print(student_one.name)
print(student_one.__class__)
print(student_two.name)

print(student_one.average())
#print(student_one.grades())
#print(Student.average(student_one))

def average(student):
    return sum(student.grades) / len(student.grades)

print(average(student_one))
print(student_one.average())
print(Student.average(student_one))