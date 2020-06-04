import numpy as np
a=np.array([[1,2,3],[3,4,5],[5,6,7]])
print(a)
print("------------------")
print("Print Diagonals from left side")
i=0
for d1 in a:
    print(d1[i])
    i+=1
print("-----------------")
print("Print Diagonals from right side")
k=2
for d2 in a:
    print(d2[k])
    k-=1
