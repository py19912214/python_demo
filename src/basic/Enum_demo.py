from enum import Enum, unique

class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
student=Student("pan",Gender.Male);
print(student.name)
print(student.gender.name,student.gender.value)