import numpy as np

'''
NumPy (Numerical Python) is a versatile Python library designed for numerical computations. It offers:

- Multidimensional Arrays: Efficiently manages large arrays and matrices.
- Mathematical Functions: Provides tools for operations like linear algebra, statistics, and Fourier transforms.
- Performance: Delivers faster computations compared to Python lists, thanks to its C-based implementation.
- Data Manipulation: Includes features for reshaping, slicing, and indexing arrays.
'''

arr_str = ["mercedes", "audi", "bmw", "toyota", "ford"]
arr_num = [1, 2, 4, 4, 5]
print(arr_num)

'''
Convert a list of strings to a numpy array
'''
numpy_array = np.array(arr_str)
print(numpy_array)
print(type(numpy_array))

numpy_array_num = np.array(arr_num)
print(numpy_array_num)
print(type(numpy_array_num))

matrix = np.array([[1,2,1],(2,1,2),[1,2,1]])
print(matrix)

#np.arange
arr2 = np.arange(start = 0, stop = 10, step = 2)
print(arr2)

#np.linspace
arr2 = np.linspace(0,99) # by default 50 evently spaced value will be geenrated. 
print(arr2)

arr3= np.linspace(0,99,10) #10 evenly spaced points between 0 and 99
print(arr3)
