x = 10
for i in range(5):
    if x%2==0:
        print(i)
    x-=1

# Method 1

exec('x=10\nfor i in range(5):\n\tif x%2==0:\n\t\tprint(i)\n\tx-=1')