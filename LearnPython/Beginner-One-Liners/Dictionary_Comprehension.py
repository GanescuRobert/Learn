women = ['Alice','Ann','Liz']
men = ['Bob','Frank','Pete']

pairs = {w:m for w,m in zip(women,men)}
print (pairs)

# Ex 1
print({str(i):i for i in [*range(10)]})

# Ex 2
fruits = ['apple','mango','banana','cherry']
print({fruit:len(fruit) for fruit in fruits if 'a' in fruit})

# Ex 3
#print({fruit : fruit.capitalized() for fruit in fruits})

# Ex 4
print ({f:i for i,f in enumerate(fruits)})

# Ex 5
print({str(i):i for i in range(5)})
