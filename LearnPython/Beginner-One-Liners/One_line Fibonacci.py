from functools import reduce
n = 10

fibs = reduce(lambda x, y: x+[x[-2]+x[-1]],\
                [0]*(n-2),\
                [0, 1])
print(fibs)