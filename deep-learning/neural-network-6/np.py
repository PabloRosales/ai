import numpy as np

vector1 = np.array([0, 1, 2])
vector2 = np.array([2, 1, 0])
matrix1 = np.array([vector1, vector2])
matrix2 = np.zeros((2, 3))
matrix3 = np.random.rand(2, 3)

print(vector1)
print(vector2)
print(matrix1)
print(matrix2)
print(matrix3)
print(vector1 * vector2)
print(matrix1 * vector1)
print(matrix1 * matrix2)
print(matrix1 * matrix3)
print(matrix2 * matrix3)
print(vector1 * 0.0)
print(matrix1 * 0.0)