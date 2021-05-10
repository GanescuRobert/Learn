

# 18
l1 = list(map(
    lambda x: x[0],
    ['red', 'green', 'blue']))

#17
l2 = list(map(
    lambda x, y: str(x)+' ' + y + 's',
    [0, 2, 2], ['apple', 'orange', 'banana']))

#16
l3 = ' friend with '.join(['Alice', 'Bob', 'Alex', 'Fillip'])

#15
l4 = list(filter(
    lambda x: True if x > 17 else False,
    [1, 15, 17, 18, 25]))

#14
l5 = '      \n \t           42          \t '.strip()

#13
l6 = sorted([8, 3, 2, 42, 5])

#12
l7 = sorted([8, 3, 2, 42, 5], key=lambda x: 0 if x == 42 else x)

#11
l8 = list(zip(['Alice', 'Anna'], ['Bob', 'Jon', 'Frank']))

#10
l9 = list(zip(*[('Alice', 'Bob'), ('Anna', 'Jon')]))

#9
l10 = list(enumerate(['Alice', 'Bob', 'Jon']))

#8
# python -m http.server 8888 turn on a server -> windows shell

#7
import antigravity  # comics

#6
import this  # The Zen of Python, by Tim Peters

#5
a, b = 'Alice', 'Jane'
print(a, b)
a, b = b, a
print(a, b)

#4
def f(x, y, z):
    return x+y*z
print(f(*[1, 3, 4]))
#3
print(f(**{'z': 4, 'x': 1, 'y': 3}))

#2
a, *b = [*range(8)]
print(a, b)

#1
x= {'Alice':18}
y= {'Bob':27,'Ann':22}
z={**x,**y}

print(z)


print('l1:', l1)
print('l2:', l2)
print('l3:', l3)
print('l4:', l4)
print('l5:', l5)
print('l6:', l6)
print('l7:', l7)
print('l8:', l8)
print('l9:', l9)
print('l10:', l10)
