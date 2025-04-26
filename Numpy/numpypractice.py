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

print(np.zeros((3,4))) # 3 rows and 4 columns of zeros

matrix = np.ones([4,5],str)
print(matrix)

#np.eye() is function for creating a amtric and performing matric operations in NumPy 
#it returns 1 in the diagonal
matrix = np.eye(5)
print(matrix) 

#np.reshape() - reshaping the array and changning the dimensions

arr4 = np.arange(0,10)
print(arr4)
arr4_reshaped = arr4.reshape(2,5)
print(arr4_reshaped)
print(arr4_reshaped.reshape(5,2))

'''
numpy provides 
1. trigonometric functions
2. statistical functions
3. linear algebra functions
4. exponential and logarithmic functions
5. functions for arithimatic operations between arrays and matrics 
'''

print('Sine function', np.sin(0)) # sin(0) = 0
print(np.cos(90)) # sin(90) = 1 

print('Sine function', np.sin(0)) # sin(0) = 0
print('cos function',np.cos(90)) # sin(90) = 1 
print('tan function on array : \n',np.tan(arr4_reshaped)) # tan(45) = 1
np.exp(arr4_reshaped)
np.sqrt(arr4_reshaped)
print(np.log(2)) # by default log base is e
np.log10(arr4_reshaped)
print(np.sum(arr4_reshaped))

arr5 = np.arange(10,30)
arr5_reshaped = arr5.reshape(5,4)
arr5_reshaped1 = arr5_reshaped.reshape(4,5)
print(arr5_reshaped)  
print(arr5_reshaped1)  

np.matmul(arr5_reshaped,arr5_reshaped1) #matrix multiplication 


arr7 = np.arange(0,6)
arr8 = np.arange(6,12)
print(arr7 + arr8)
print(arr7 - arr8)
print(arr7 * arr8)
print(arr7 / arr8)
print(arr7 ** arr8)

numpy_array = np.array([1,2,3,4,5])
print(numpy_array)
print(numpy_array[::-1]) #revert a numpy array

arr5 = np.arange(10,30)
arr5_reshaped = arr5.reshape(5,4)
arr5_reshaped1 = arr5_reshaped.reshape(4,5)
print(arr5_reshaped)  
print(arr5_reshaped1)  

print(arr5_reshaped @ arr5_reshaped1) #element wise multiplication; dimentions has to be same
print(np.transpose(arr5_reshaped))
arr5_reshaped.T # transpose shortcut



