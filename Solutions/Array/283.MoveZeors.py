'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

nums = [0,1,0,3,12]
def MoveZeros(nums):
    idx = 0
    n = len(nums)
    if n<=1:
        print(nums) # replace return 
    else:
        for i in range(n):
            # move non-zero element to the head
            if nums[i] != 0:
                nums[idx]=nums[i]
                idx+=1
            # so far the nums are assinged as [1,3,12,3,12] and idx pointed to nums[3]

        # assign remaining positions to zero
        for i in range(idx,n):
            nums[i]=0
        print(nums) # replace return 

MoveZeros(nums)