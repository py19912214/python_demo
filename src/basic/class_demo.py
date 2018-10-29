class Person(object):
    def printSupName(self):
        print("Person:panpan");
class Student(Person):
    def __init__(self, name,privateName):
        self.name = name
        # 私有变量
        self.__privateName = privateName
    def getPrivateName(self):
        return self.__privateName;
    def printName(self):
        self.printSupName();
        print("Student:{0}".format(self.name));

student=Student("panyue","secondName1");
# 人为调用父类方法
student.printSupName();
#在子对象中调用父对象方法
student.printName();
print(student.name)
# 打印私有变量 会报错
# print(student.__privateName)
# 打印私有变量 不会报错但是这个是版本不一样 结果不一样 不建议采纳这种做
print(student._Student__privateName)
print(type(student))
print(isinstance(student,Person))
person=Person();
print(isinstance(person,Student))
print(isinstance(person,Person))