# Numpy Array Methods
import numpy

arr = numpy.array([[2.1, 3.1, 5.1], [4.1, 6.1, 5.1]], dtype='f')

print(arr.ndim)
print(arr.dtype)

# WE can change the datatype of arr using astype()
print(arr.astype(dtype='i'))  # this we give integer array rather than previous float array

# copy() and view()
x = arr.copy()
print(x)

#  view() :- Make a view, change the original array, and display both arrays:
arr1 = numpy.array([1, 2, 3, 4, 5])
x = arr1.view()
arr1[0] = 42
print(arr1)
print(x)

#  shape()
print(arr.shape)  # give output :- (dimension, elements)

