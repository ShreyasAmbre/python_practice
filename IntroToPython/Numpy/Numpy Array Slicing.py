# 2-D Array Slicing
import numpy
arr = numpy.array([[2, 3, 5, 6, 4, 2, 8], [4, 6, 5, 6, 3, 4, 5]])
print(arr[1, 0:2])
print(arr[0, 0:])
# Below From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
print(arr[0:2, 1:4])