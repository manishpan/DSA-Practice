import numpy as np

x = [[1,2,3], [4,5,6], [7,1,0]]

ar = np.array(x)
print(ar)
print(ar.sum(axis=0))
print(ar.sum(axis=1))
print(ar.T)
for i in ar.flat:
    print(i)
print(ar.ndim)
print(ar.size)
print(ar.nbytes)

one = np.array([1,3,4,634,2])
print(one.argmax())  #returns index of max element
print(one.argmin())
print(one.argsort()) #returns indexes from which we can sort arrays

print(ar.argmin())  #returns 8
print(ar.argmax())  #returns 6
print(ar.argmin(axis=0))
print(ar.argmax(axis=1))
print(ar.argsort(axis=0))
print(ar.argsort(axis=1))

print(np.where(ar>5)) #returns indices (1d or 2d) where >5 returns a tuple of arrays
print(np.count_nonzero(ar))