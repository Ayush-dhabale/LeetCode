'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        #Brute
        result = []
        n = len(nums)
        for i in range(n):
            product = 1
            for j in range(n):
                if i != j:
                    product *= nums[j]
                    
            result.append(product)
            
        return product
    
        #Better
        before = [1]*len(nums)
        after = [1]*len(nums)

        for i in range(1,len(nums)):
            before[i] = before[i-1]* nums[i-1]

        for i in range(len(nums)-2,-1,-1):
            after[i] = after[i+1]*nums[i+1] 

        result = [before[i]*after[i] for i in range(len(nums))]

        return result
        '''
        
        #Optimal
        n = len(nums)
        result = [1] * n
    
    
        before_product = 1
        for i in range(n):
            result[i] = prefix_product
            prefix_product *= nums[i]
    
    
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix_product
            suffix_product *= nums[i]
            
        return result
        
        