unsorted = [33, 2, 3, 45, 6, 54, 33]


q = lambda l:\
    q([x for x in l[1:] if x <= l[0]]) + \
    l[0:1]+ \
    q([x for x in l[1:] if x > l[0]]) \
    if l else []


print(q(unsorted))
# 2,3,6,33,33,45,54
