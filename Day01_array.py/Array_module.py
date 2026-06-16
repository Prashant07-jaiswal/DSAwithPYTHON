from array import *

arr = array('i', [])
n = int(input("Enter the size of the array: "))

for i in range(0,n):
    arr.append(int(input("Enter the next element: ")))

for x in arr:
    print(x,end=" ")


# val = array('i', [1,2,3,4,5,6]) 

# val.insert(1, 10)

# val.append(20)

# val.reverse()

# val.pop()

# val.pop(4)

# val.remove(20)

# val[4] = 1

# rev = val[::-1]

# copy_array = array(rev.typecode, (x for x in rev))

# for i in range(0, len(copy_array)):
#     print(copy_array[i], end=" ")
# print('\n')
# for i in range(0, len(rev)):
#     print(rev[i], end=" ")
# print('\n')
# for i in range(0, len(val)):
#     print(val[i], end=" ")
# print("\n")
# for x in val:
#     print(x, end=" ")