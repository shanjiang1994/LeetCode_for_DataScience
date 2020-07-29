'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

nums = [1,2,3,1,2,3]
k = 2


def containsNearbyDuplicate(nums, k):
    dct = {}
    for i in range(len(nums)):
        # this if statement make sure exist j that let nums[i]=nums[j] and their index are distence enough(at least k position)
        if nums[i] in dct and dct[nums[i]] >= i - k: 
            print(True) 
        dct[nums[i]] = i
    print(False)

containsNearbyDuplicate(nums,k)



# dct
# key value
# 1	   3
# 2	   4
# 3	   5
