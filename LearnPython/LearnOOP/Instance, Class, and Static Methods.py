import math


class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


obj = MyClass()
print(obj.method())

print(MyClass.method(obj))
print(obj.classmethod())
print(obj.staticmethod())

print(MyClass.staticmethod())
print(MyClass.classmethod())
# print(MyClass.method())

'''
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return 'Pizza(%r)' % self.ingredients

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])


print(Pizza(['cheese', 'tomatoes']))

print(Pizza(['mozzarella', 'tomatoes']))
print(Pizza(['mozzarella', 'tomatoes', 'ham', 'mushrooms']))
print(Pizza(['mozzarella'] * 4))

print(Pizza.margherita())
print(Pizza.prosciutto())

'''


class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi
