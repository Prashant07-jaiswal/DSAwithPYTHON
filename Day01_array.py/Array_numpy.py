from numpy import *

arr = array([1,2,3,4])

#numpy gives feature to create heterogenous array.
arr_hetero = array([1,2,3.0,'a'])

#It create array in a airthmetic progression.
#It divide 1-10 elements into 5 equal parts.
arr = linspace(1, 10, 5)

#It create array from 10 with distance 2. 
arr = arange(10,20,2)

#it create array of all 0 element of size 10.
val = zeros(10)

#it create array of given(3) element of given size(8).
val = full(8, 3)

#zero dimension array.
zero = array(10)
print(zero)

#one dimension array
one = array([1,2,3])

#two dimension array
two = array([[1,2,3], [4,5,6]])

#three dimension array
three = array([[[1,2],[3,4]],[[5,6],[7,8]]])

for x in three:
    print(x, end=" ")
print('\n')
for x in two:
    print(x, end=" ")
print('\n')
for x in one:
    print(x, end=" ")
print('\n')
for x in val:
    print(x, end=" ")
print('\n')
for x in arr_hetero:
    print(x, end=" ")
print('\n')
for x in arr:
    print(x, end=" ")