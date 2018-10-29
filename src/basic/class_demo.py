class Person(object):
    def printSupName(self):
        print("Person:panpan");
class Student(Person):
    def __init__(self, name,secondName):
        self.name = name
        self._secondName = secondName
    def printName(self):
        self.printSupName();
        print("Student:{0}".format(self.name));

student=Student("panyue","secondName1");
# 人为调用父类方法
student.printSupName();
#在子对象中调用父对象方法
student.printName();
print(student.name)
print(student._secondName)