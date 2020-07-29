
'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
 

Constraints:

-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n

'''

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

def merge(nums1,m,nums2,n):

    while m>0 and n>0: #incase the position are stepped to 0
        if nums2[n-1]>=nums1[m-1]:
           nums1[m+n-1]=nums2[n-1]
           n-=1
        else: #nums1[m-1]>=nums2[n-1]
            nums1[m+n-1],nums1[m-1]= nums1[m-1],nums1[m+n-1] #it's okay we just let nums1[m+n-1] = nums1[m-1]
            m-=1

    # corner case
    if m==0 and n>0:
        nums1[:n] = nums2[:n]
    
    print(nums1)


# call the function
merge(nums1,m,nums2,n)



########################################################
# Methodology:                                         #
#    - two pointer                                     #
#    - start from the end to the front                 #
########################################################

# [1,2,3,0,0,0]
# [2,5,6]


# Normal case:
# --------------------------------------------
# while m>0 and n>0:
#     if nums1[m-1]<=nums2[n-1]?
        
#         nums1[1,2,3,0,0,0]   
#                   ↑(m-1)
#         nums2[2,5,6]
#                   ↑(n-1)
#         answer is True

#         Then we let nums1[m+n-1]=nums2[n-1], and n = n-1
#         nums1[1,2,3,0,0,6]
#                   ↑(m-1)
#         nums2[2,5,6]
#                 ↑(n-1)

#         so on and so forth until:

#     else nums1[m-1]>nums2[n-1]

#         nums1[1,2,3,0,5,6]
#              (m-1)↑ ↑(m+n-1)

#         nums2[2,5,6]
#               ↑(n-1) = 0 # n still > 0

#         move nums1[m-1] to the place nums1[m+n-1] and move m forward = m-1
        
#         nums1[1,2,0,3,5,6]
#                 ↑(m-1) 
#         nums2[2,5,6]
#               ↑(n-1) = 0 
#         # here is the previous loop we get:
#         nums1[1,2,2,3,5,6]
#         now n is zero, break the loop   


# Other cases that we need to concern
# --------------------------------------------
# [1,2,3,0,0,0]
# 3
# [2,5,6]
# 3
# --------------------------------------------
# [0,0,0,0,0]
# 0
# [1,2,3,4,5]
# 5
# --------------------------------------------
# so we need add this :
# if m==0 and n>0:
#             nums1[:n] = nums2[:n]