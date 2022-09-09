#part-2.
#NUmphy by using array.
from numpy import *

"""arr=array([1,2,3,4,5,6]);
print(arr.dtype)
arrs=array([1,2,3,4,5,6],float);
print(arr.dtype)
print(arrs)

ars=linspace(0,15,14)
print(ars)
p=arange(1,10,2)
print(p)

s=logspace(1,40,6)
print(s)

a=zeros(5,int)
print(a)

b=ones(5,int)
print(b)
"""
#copying the value from one array to another array using numpy.
"""ar=array([1,2,3,4,5])
ar=ar+3
print(ar)
ar1=array([2,3,4,5,4])
ars=ar+ar1;
print(ars)
print(sin(ar))
print(cos(ar))
print(tan(ar))
print(sqrt(ar))
print(sum(ar))
print(max(ar))
print(concatenate([ar,ar1]))
print(sort(ar))"""
#aliasing.:-return only single array.
""""ars=array([1,2,3,4])
arrs=ars;
print(ars)
print(arrs)
#Shallow copy.:-The array is dependent to each other another array.
ar=array([1,32,34,2,3])
arr=ar.view()
ar[1]=3
print(ar)
print(arr)
print(id(ar))
print(id(arr))
#Deep copy:-The array is not dependent to each other.
ar=array([12,3,4,4])
arrs=ar.copy();
ar[1]=2;
print(ar)
print(arrs)"""

#2-d array.
"""arr1=array([

    [1,2,3,4],[1,2,3,4]

])"""
"""print(arr1)
print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
arr2=arr1.flatten()
print(arr2)
#create 3d array.
arr3=arr1.reshape(2,2,4)
print(arr3)
print(arr3.ndim)"""
#create a matrix.
"""print(arr1)
m=matrix(arr1)
print(m)
zm=matrix('1 2 3 4 ; 1 2 3 4')
print(zm)"""
n=matrix('1 2 3 ; 3 4 3; 1 2 3 ; 3 4 3')
"""print(n)
print(diagonal(n))
print(n.min())
print(n.max())
print(n.sum())
"""
#m=matrix('1 2 3 ; 3 4 3; 1 2 3; 3 4 3');
#s=n*m
print(n)