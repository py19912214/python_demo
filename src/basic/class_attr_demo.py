from types import MethodType

class Student():
    name='pan'
    def __init__(self, name):
        self.name = name
student2=Student("pan");
student1=Student("yue");
print(student1.name)
# 如果删除实例的name属性
# 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
del student1.name
print(student1.name)
# 调用类的属性
print(Student.name)
#正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：
student1.studentAge=123;
print(student1.studentAge)
# 动态绑定方法
def printAge(self,age):
    self.age=age;
    print('打印年龄:'+str(age))
print(hasattr(student1, 'printAge'));
student1.printAge = MethodType(printAge, student1) # 给实例绑定一个方法
student1.printAge(123123)
print(student1.age)
# 结束
print(hasattr(student1,'printAge'));
#动态绑定的方法 只归实例所有 其他实例都没有的
print(hasattr(student2,'printAge'));
# 如果想所有的实例都可以方法那只有
# 方法第一个参数一定要加self不然是不生效的
def printScore(self,score):
    print('打印积分:'+str(score))
Student.printScore = printScore;
student1.printScore(123123123)
# 设置一个类只能添加name跟age属性其他属性不允许添加
class Person():
    __slots__ = ('name', 'age')
person=Person();
person.name='asdasd';
print(person.name)
#如下代码会报错。因为不允许添加其他不认识的属性
# person.score='asdasd';
# print(person.score)