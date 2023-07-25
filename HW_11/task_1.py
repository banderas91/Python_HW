# Создайте класс Матрица. Добавьте методы для: 
# вывода на печать, проверку на равенство, сложения, *умножения матриц

import numpy as np

class Matrix:
    
    def __init__(self, data):
        self._data = np.array(data)
        
    def __repr__(self):
        return repr(self._data)
    
    def __str__(self):
        return str(self._data)
    
    def __eq__(self, other):
        return np.array_equal(self._data, other._data)
    
    def __add__(self, other):
        if self._data.shape != other._data.shape:
            raise ValueError("Размеры матриц не совпадают")
        return Matrix(self._data + other._data)
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Matrix(self._data * other)
        elif isinstance(other, Matrix):
            if self._data.shape[1] != other._data.shape[0]:
                raise ValueError("Размеры матриц не совпадают")
            return Matrix(self._data @ other._data)
        else:
            raise TypeError("Умножение матрицы возможно только на число или другую матрицу")
        
# m1 = Matrix([[1, 2], [3, 4]])
# m2 = Matrix([[2, 3], [4, 5]])

# print(m1)
# print(m2)

# print(m1 == m2)

# m3 = m1 + m2
# print(m3)  


# m4 = m1 * 2
# print(m4)


# m5 = m1 * m2 
# print(m5)
