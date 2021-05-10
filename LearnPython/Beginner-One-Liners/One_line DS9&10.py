import numpy as np
## Data: row is costomer shopping basket
## row = [course 1, course 2, ebook 1, ebook 2]
## value 1 indicates that an item was bought.

basket = np.array([
    [0,1,1,0],
    [0,0,0,1],
    [1,1,0,0],
    [0,1,1,1],
    [1,1,1,0],
    [0,1,1,0],
    [1,1,0,1],
    [1,1,1,1]
])

print(basket[:,2:])
# check if position 3 and 4 is equal 1
print(np.all(basket[:,2:],axis=1))

print(sum(np.all(basket[:,2:],axis=1)))

print(sum(np.all(basket[:,2:],axis=1))/basket.shape[0])

co_purchases = [(i,j,np.sum(basket[:,i]+basket[:,j]==2))
                for i in range(4) for j in range(i+1,4)]
print(co_purchases)
print(max(co_purchases,key=lambda x:x[2]))