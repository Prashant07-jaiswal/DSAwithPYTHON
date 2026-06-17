from array import *

#this is Reverse Traversal algorithen concept
def findleader(arr):
    #n stores size of array
    n = len(arr)
    if n == 0:
        return[]
    #max_so_far contain negative infinite value which always less than zero 
    #We use negative infinity as a safe "starting point" when we are trying to find the maximum value in a list of numbers.
    max_so_far = float('-inf')
    leader = array('i',[])
    
    #it start at last element(-1) and stop at (0)index which is first element and (-1) reffers the backstep from last 
    for i in range(n-1,-1,-1):
        if arr[i] >= max_so_far:
            leader.append(arr[i])
            max_so_far = arr[i]
    
    leader.reverse()
    return leader

print(findleader([16,17,4,3,5,2]))

