#mapreduce demo
from functools import reduce
def f(x):
    return x * x
def add(x, y):
    return x+y;
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
temp=list(r);
print(temp)
print(reduce(add, temp))

def normalize(name):
    return name.capitalize();
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)