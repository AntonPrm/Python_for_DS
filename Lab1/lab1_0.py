import numpy as np

file_name = 'matrix.csv'

#matrix creation
#x = np.random.randint(100, size=(10,10))
#np.savetxt(delimiter=',', fname=file_name,fmt='%1.1i', X=x)

#read file
y = np. loadtxt(delimiter=',', fname=file_name)
print(y)

#max and min
matrix_min = np.min(y)
matrix_max = np.max(y)

#coordinates max and min
c_min = np.where(y==matrix_min)
print('Min = ', c_min)
c_max = np.where(y==matrix_max)
print('Max = ', c_max)

#change
y[c_max] = matrix_min
y[c_min] = matrix_max
print('result:\n', y)
