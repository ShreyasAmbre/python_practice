import numpy

# How to fetch element using index value in 2-D Array
arr = numpy.array([[2, 3, 5], [4, 6, 5]])
print("2nd Dimension 3rd Element :- ", arr[1, 2])
print("1st Dimension 2nd Element :- ", arr[0, 1])

arr2 = numpy.array([[[12, 23, 15], [13, 16, 15]], [[1, 2, 3], [1, 2, 3]]])
print("1st Dimension 2nd Array 3rd  Element :- ", arr2[0, 1, 2])
