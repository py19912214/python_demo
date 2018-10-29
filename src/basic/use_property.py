class Student(object):

    @property
    def score(self):
        return self._score

    @property
    def name(self):
        return 'panpan'
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
s = Student()
s.score = 60
print('s.score =', s.score)
# 代码会报错
s.score = 1000
print('s.name =', s.name)
