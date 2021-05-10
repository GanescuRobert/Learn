###############################
# Method 1: Single-Line Def
###############################
def f1(x): return str(x*3)+'!'
print(f1(1))
print(f1('python'))
###############################
# Method 2: Lambda Function
###############################
f2 = lambda x: str(x*3)+'!'
print(f2(1))
print(f2('python'))
###############################
# Method 3: exec()
###############################
f3 = "def f(x):\n   return str(x*3) + '!'"
exec(f3 +'\nprint(f(1))')
exec(f3 +"\nprint(f('python'))")
