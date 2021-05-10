import numpy as np
alice =[99,101,103]
bob = [110,108,105]
tim = [90,88,85]

salaries = np.array([alice,bob,tim])

taxation = np.array([[0.2,0.25,0.22],
                    [0.4,0.5,0.5],
                    [0.1,0.2,0.1]])
print(salaries)
print(taxation)
print(salaries*taxation)
print(salaries- salaries*taxation)
print(np.max(salaries-salaries*taxation))