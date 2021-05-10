hi = 'hello world!'
file = 'hellow.txt'

with open(file, 'a') as f:
    f.write(hi)

print(hi, file=open(file, 'a'))

f = open(file, 'a');f.write(hi);f.close()

open(file,'a').write(hi)


