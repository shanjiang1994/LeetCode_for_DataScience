'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
'''


nums = [0,1,2,2,3,0,4,2]
val = 2

def removeElement(nums,val):
    pointer = 0
    n = len(nums)
    for i in range(n):
        if nums[i]!=val:
            nums[pointer] = nums[i]
            pointer+=1
    print(nums[:pointer]) # in leetcode we just write down return pointer


removeElement(nums,val)



# nums[0,1,2,2,3,0,4,2]
#      ↑ nums[pointer] = nums[i]= 0

#      nums[i]=0 and 0!=val
#      then let nums[pointer] = nums[i] -> 0:=0
#      pointer+=1 


# nums[0,1,2,2,3,0,4,2]
#        ↑ pointer = nums[i]= 1

#      nums[i]=1 and 1!=val
#      then let nums[pointer] = nums[i] -> 1:=1
#      pointer+=1 


# nums[0,1,2,2,3,0,4,2]
#          ↑ pointer = nums[i]= 2
#     nums[i]=2 and 2==val
#     then we dont do anything


# nums[0,1,2,2,3,0,4,2]
#  pointer ↑ ↑ nums[i]= 2

#     nums[i]=2 and 2==val
#     then we dont do anything


# nums[0,1,2,2,3,0,4,2]
#  pointer ↑   ↑ nums[i]=3

#      nums[i]=3 and 3!=val
#      then let nums[pointer] = nums[i] -> 2:=3
#      pointer+=1 

# nums[0,1,3,2,3,0,4,2]
#  pointer=3 ↑   ↑ nums[i]=0

#      nums[i]=0 and 0!=val
#      then let nums[pointer] = nums[i] -> 2:=0
#      pointer+=1 

# nums[0,1,3,0,3,0,4,2]
#    pointer=4 ↑   ↑ nums[i]=4

#      nums[i]=4 and 4!=val
#      then let nums[pointer] = nums[i] -> 3:=4
#      pointer+=1 

# nums[0,1,3,0,4,0,4,2]
#      pointer=5 ↑   ↑ nums[i]=2

#      nums[i]=2 and 2=val
#      then we dont do anything
# then we return first #pointer elements which are 0,1,3,0,4
