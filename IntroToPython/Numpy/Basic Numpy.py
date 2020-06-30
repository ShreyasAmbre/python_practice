# Basic of Numpy, creating array using numpy
# numpy is faster then list because it store data in continous manner
# array() method is built-in in numpy yo create the numpy object, we can pass any array like object such as
# list & tuple
import numpy

# Basic Numpy Array
arr = numpy.array([12, "12", False, "Shreyas", 1.2])

for i in arr:
    print(i)
print(type(arr))

# 2-D & 3-D Array using Array
# Note:- 1-D as an element called 2-D
# Note:- 2-D as an element called 3-D
# arr2 = numpy.array([ [1-D Element],  [1-D Element] ])
arr2 = numpy.array([[2, 3, 5], [4, 6, 5]])
arr3 = numpy.array([[[12, 23, 15], [13, 16, 15]], [[1, 2, 3], [1, 2, 3]]])
print("2-D Array :- ")
print(arr2)

print("3-D Array :- ")
print(arr3)
print(arr.ndim)
print(arr2.ndim)
print(arr3.ndim)

