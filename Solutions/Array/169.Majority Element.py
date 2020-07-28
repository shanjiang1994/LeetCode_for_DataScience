    
'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''

nums =[2,2,1,1,1,2,2]
    
    
def majorityElement(nums):
    dct = {}
    for i in range(len(nums)):
        if nums[i] in dct:
            dct[nums[i]]+=1
        else: 
            dct[nums[i]]=1
    
    max_val = max(dct.values())

    for i in dct:
        if dct[i] == max_val:
            print(i) 


majorityElement(nums)