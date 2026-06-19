def twoSum(nums, target):

    #Hash map algorithm is basically provided dict to store named value 
    hashmap = {} # number : index

    #Enumerate returns index of a element iterate to i and value to n. 
    for i,n in enumerate(nums):
        
        #the difference of target and element of array 
        diff = target - n

        #it checks diff as a key name in hashmap 
        if diff in hashmap:

            #it returns indecies of diff key name and element(n) that substracted from target.
            return (hashmap[diff], i)
        
        #it added n as a key name and i as a value in hashmap.
        hashmap[n] = i

print(twoSum([3,2,4], target = 6))