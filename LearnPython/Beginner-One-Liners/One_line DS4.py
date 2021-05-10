import numpy as np
inst = np.array([
    [232,'@instagram'],
    [133,"@selenagomez"],
    [59,'@victoriassecret'],
    [120,'@cristiano'],
    [111,'@beyonce'],
    [77,'@nike']
    ])

#my one liner
accounts = [account[1] for account in inst if int(account[0]) > 100]
print(accounts)

#video one liner

superstars = inst[inst[:,0].astype(float)>100, 1]
print (superstars)