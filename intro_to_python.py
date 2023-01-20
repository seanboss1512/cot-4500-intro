open('requirements.txt','r')
import numpy as np
array0 = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
for i in range(0, 3):
    for j in range(0, 3):
        if i == j:
            array0[i][j] = 1
        else:
            array0[i][j] = 0
print(array0)
for i in range(0, 3):
        for j in range(0, 3):
            if i == j:
                array0[i][j] = 1
            else:
                array0[i][j] += 3
print("\n")
print(array0)
array0 = np.delete(array0, 2, 1)
print("\n")
print(array0)
