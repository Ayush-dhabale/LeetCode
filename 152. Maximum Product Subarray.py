'''
Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
'''
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        #Brute
        n = len(nums)
        max_ = float('-inf')
        for i in range(n):
            product = 1
            for j in range(i,n):
                product *= nums[j]
                max_ = max(max_,product)
                
        return max_
        
        '''
        #Optimal
        n = len(nums)
        prod1 = prod2 = 1
        max_ = float('-inf')

        for i in range(n):
            if prod1 == 0:
                prod1 = 1

            if prod2 == 0:
                prod2 = 1

            prod1 *= nums[i]
            prod2 *= nums[n- i - 1]

            max_ = max(max_,max(prod1,prod2))

        return max_ 