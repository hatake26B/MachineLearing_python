import numpy as np

#create a rank 1 array
a = np.array([0,1,2])
print(type(a))

#This will print the dimension of the array
print(a.shape)
print(a[0])
print(a[1])
print(a[2])

#change an element of the array
a[0]=5
print(a)

#create a rank 2 array
b = np.array([[0,1,2],[3,4,5]])
print(b.shape)
print(b)
print(b[0,0],b[0,1],b[1,0])

#creating Numpy array
c = np.zeros((3,3))
print(c)

#creating 2*2 array of all ones
d = np.ones((2,2))
print(d)

#creating 3x3 constant array
e = np.full((3,3),7)
print(e)

#create a 3x3 array filled with random values
f = np.random.random((3,3))
print(f)

#create a 3x3 identity matrix
g = np.eye(3)
print(g)

#convert list to array
h = np.array([2,3,1,0])
print(h)

#arange() will create arrays with regularly incrementing values
i= np.arange(20)
print(i)

#note mix of tuple and lists
j = np.array([[0,1,2,0],[0,0,0],(1+1j,3.,2.)])
print(j)

#create an array of range with float data type
k = np.arange(1,8,dtype=float)
print(k)

#linspace() will create arrays with a specified number of items 
#which are spces eually between the specified beginning and end values
l = np.linspace(2.,4.,5)
print(l)

#indices() will create a set of arrays stacked as a one-higher
#dimensioned arrary,one per dimension with each representing variation
#in that dimension
m = np.indices((2,2))
print(m) 




