import numpy as np
A=np.array([1,2,3,4,5,6,7,8,9])
print(A[:]) #Slice from 0th element to last element
print(A[2:6]) #Slice from 3rd element 6th element
print(A[:-6])#Slice from 0th element to last 6th element(excluded)
print(A[::-1]) #reversing order

B=np.array([[1,2,3,4],[2,3,4,5],[3,5,8,9]])
print(B)
print(B[:2, :4])#2 rows and 4 column
print(B[:1,])# only first rows and all coulmns
print(B[:, 2]) #all rows and second coulmn
print(B[:, 2:5])# all rows and column from 2 to 5
