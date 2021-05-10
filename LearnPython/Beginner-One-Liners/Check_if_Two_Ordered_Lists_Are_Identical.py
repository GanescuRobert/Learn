# 1. Simple Comparison
def method_1(l1, l2):
    return l1 == l2

# 2. Simple For Loop
def method_2(l1, l2):
    for i in range(min(len(l1), len(l2))):
        if l1[i] != l2[i]:
            return False
    return len(l1) == len(l2)

# 3. Zip + For Loop
def method_3(l1, l2):
    for x, y in zip(l1, l2):
        if x != y:
            return False
    return len(l1) == len(l2)

# 4. Sum + Zip + Len
def method_4(l1, l2):
    for x, y in zip(l1, l2):
        num_equl = sum(x == y for x, y in zip(l1, l2))
        return num_equl == len(l1) == len(l2)


# 5. map() + reduce() = len()
from functools import reduce
def method_5(l1, l2):
    equal = map(lambda x, y: x == y, l1, l2)
    result = reduce(lambda x, y: x and y, equal)
    return result and len(l1) == len(l2)

# 6. map() + all()
def method_6(l1, l2):
    result = all(map(lambda x, y: x == y, l1, l2))
    return result and len(l1)==len(l2)

l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3]

print(method_1(l1, l2))
print(method_2(l1, l2))
print(method_3(l1, l2))
print(method_4(l1, l2))
print(method_5(l1, l2))
print(method_6(l1, l2))
