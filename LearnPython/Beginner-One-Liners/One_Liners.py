
arr1 = [3, 1, 42, 32]
arr2 = [*range(10)]

employees = {'Alice': 100000,
            'Bob': 99817,
            'Carol': 122908,
            'Frank': 88123,
            'Eve': 93121}

filename = 'One_Liners.py'

txt = ['lambda functions are anonymous functions.',
        'anonymous functions dPont have a name.', 'functions are objects in']

letters_amazon = '''
We spent several years building our own database engine,
Amazon Aurora, a fully-managed MySQL an PostgresSQL-compatible
service with the same or better durability and availability as
the commercial engines, but at one-tenth of the cost. We were
not surprised when this worked.
'''

price = [
        [9.9, 9.8, 9.8, 9.4, 9.5, 9.7],
        [9.5, 9.4, 9.4, 9.3, 9.2, 9.1],
        [8.4, 7.9, 7.9, 8.1, 9.0, 8.0],
        [7.1, 5.9, 4.8, 4.8, 4.7, 3.9]]

visitors = ['Firefox', 'corrupted', 'Chrome', 'corrupted',
            'Safari', 'corrupted', 'Safari', 'corrupted',
            'Chrome', 'corrupted', 'Firefox', 'corrupted']

cardiac_cycle = [62, 60, 62, 64, 68, 77, 80, 76, 71, 66, 61, 60, 62]

companies = {'CoolCompany' :{'Alice':33, 'Bob':28, 'Frank':29},
            'CheapCompany' : {'Ann':4, 'Lee':9,'Chrisi':7},
            'SosoCompany': {'Esther':38,'Cole':8, 'Paris':18}
            }

text = \
'''Call me Ishmael. Some years ago—never mind how long precisely — having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery
part of the world. It is a way I have of driving off the spleen and regulating
the circulation. - Moby Dick'''

column_names = ['name','salary','job']
db_rows = [('Alice',180000,'data scientist'),
            ('Bob',99000,'mid-level manager'),
            ('Frank',87000,'CEO')]

lst = [{1,2,3},{1,4},{1,3,5}]

l = [{'a': 0}, {'b': 1}, {'c': 2}, {'d': 3}, {'e': 4}, {'a': 4}]

l2 = ['n','o','h','t','y','p']

l3 = ['x','y','v','w']
#l3 = ['aaaa','b','cc','dddd','eee','fff']
###!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!###


def OL_quick_sort(arr):
    q = lambda arr: q([x for x in arr[1:] if x <=arr[0]]) + [arr[0]] + q([x for x in arr if x>arr[0]]) if arr else []
    print(q(arr))


def OL_pow_list_values(arr):
    print([x**2 for x in arr])


def over100k(employees):
    top_earners = []
    for key, value in employees.items():
        if value >= 100000:
            top_earners.append((key, value))
    print(top_earners)


def OL_over100k(employees):
    print([(k, v) for k, v in employees.items() if v >= 100000])


def open_file(file):
    f = open(file)
    lines = []
    for l in f:
        lines.append(l)
    print(lines)


def OL_open_file(file):
    print([l.strip() for l in open(file)])


def OL_conditionate_word_in_seq(txt):
    print(list(map(lambda seq: (True, seq) if 'anonymous' in seq else (False, seq), txt)))


def OL_find_word_in_seq(txt, key_word):
    print([word for word in txt.split() if key_word in word])


def OL_return_subseq_where_WIS(txt, key_word):
    def ans(t, k): return t[t.find(k)-20:t.find(k)+20] if k in t else -1
    print(ans(txt, key_word))


def OL_price_avg(price_list):
    import statistics as s
    sample = s.mean([s.mean(line) for line in price_list])
    print(sample)


def corrupted(visitors):
    for i in range(len(visitors)):
        if i % 2 == 1:
            visitors[i] = visitors[i-1]
    print(visitors)


def OL_corrupted(visitors):
    visitors[1::2] = visitors[::2]
    print(visitors)


def OL_expected_cycles(cardiac_cycle):
    import matplotlib.pyplot as plt

    expected_cycles = cardiac_cycle[1:-2] * 10

    plt.plot(expected_cycles)
    plt.show()


def OL_evaluate_employees_of_companies(companies):
    print([x for x in companies if any(y < 9 for y in companies[x].values())])

def OL_3size_word(text):
    print([[word for word in line.split()]for line in text.split('\n')])

def OL_zip_lists_to_dict(column_names,db_rows):
    db = [dict(zip(column_names,data)) for data in db_rows]
    print(db)


def half_to_square():
    output = []
    for i in range(10):
        if i < 5:
            output.append(i**2)
        else:
            output.append(0)
    print(output)


def OL_half_to_square():
    print([x**2 if x < 5 else 0 for x in range(10)])


def OL_Set_union(lst):
    print('Union:',set().union(*lst))
    print('Intersection:',lst[0].intersection(*lst))
    print('Difference:',lst[0].difference(*lst[1:]))


# Method 1:
def OL_M1_Merge_Dict(l):
    d= {k:v for x in l for k,v in x.items()}
    print(d)
# Method 2:
def Naive_M2_Merge_Dict(l):
    d = {}
    for dictionary in l:
        for k,v in dictionary.items():
            d[k]=v
    print(d)
# Method 3:
def Explicit_M3_Merge_Dict(l):
    d={}
    for dictionary in l:
        d.update(dictionary)
    print(d)
#Method 4:
def Unpack_Naive_M4_Merge_Dict(l):
    d = {**l[0],**l[1],**l[2],**l[3],**l[4]}
    print(d)
#Method 5:
from collections import ChainMap
def ChainMap_M5_Merge_Dict(l):
    d = dict(ChainMap(*l))


def Join_Reverse_Order(l2):
    print('-'.join(l2[::-1]))
    print(''.join(reversed(l2)))

#Method 1: zip
def Join_M1_List_Pairs(l3):
    out = [x+y for x,y in zip(l3[::2],l3[1::2])]
    print(out)
#Method 2: iterator
def Join_M2_List_Pairs(l3):
    it = iter(l3)
    out = [ x+ next(it,'') for x in it]
    print(out)
#Method 3: indexing
def Join_M3_List_Pairs(l3):
    out = [l3[i]+l3[i+1] for i in range(0,len(l3),2)]
    print(out)
###!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!###


# OL_quick_sort(arr1)

# OL_pow_list_values(arr2)

# over100k(employees)
# OL_over100k(employees)

# open_file(filename)
# OL_open_file(filename)

# OL_conditionate_word_in_seq(txt)
# OL_find_word_in_seq(letters_amazon,'SQL')
# OL_return_subseq_where_WIS(letters_amazon,'SQL')

#OL_price_avg(price)


#corrupted(visitors)
#OL_corrupted(visitors)

#OL_expected_cycles(cardiac_cycle)

#OL_evaluate_employees_of_companies(companies)

#OL_3size_word(text)

#OL_zip_lists_to_dict(column_names,db_rows)

#half_to_square()
#OL_half_to_square()

#OL_Set_union(lst)

#OL_M1_Merge_Dict(l)
#Naive_M2_Merge_Dict(l)
#Explicit_M3_Merge_Dict(l)
#Unpack_Naive_M4_Merge_Dict(l)
#ChainMap_M5_Merge_Dict(l)

#Join_Reverse_Order(l2)

Join_M1_List_Pairs(l3)
Join_M2_List_Pairs(l3)
Join_M3_List_Pairs(l3)