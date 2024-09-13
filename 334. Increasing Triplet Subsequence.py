'''
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
'''
from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        '''
        #Brute
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for j in range(j+1,n):
                    if nums[i] < nums[j] and nums[j] < nums[k]:
                        return  True
                    
        return False

        #Better
        for i in range(1,n-1):
            min_ = min(nums[:j])
            max_ = max(nums[j+1:])
            if min_ < nums[j] < max_:
                return True
            
        return False
       
        #Optimized Better
        n = len(nums)
        min_ = [nums[0] * n]
        max_ = [nums[-1] * n]
        
        curr_min = nums[0]
        for i in range(1,n):
            if nums[i] < curr_min:
                curr_min = nums[i]
                
            min_[i] = curr_min
            
                
        curr_max = nums[-1]
        for i in range(n-2,-1,-1):
            if nums[i] > curr_max:
                curr_max = nums[i]
                
            max_[i] = curr_max
            
        for i in range(1,n-1):
            if min_[i-1] < nums[i] and max_[i+1] > nums[i]:
                return True
            
        return False
         '''
        #Optimal
        if len(nums) < 2:
            return False

        min_ = float('inf')
        second_min = float('inf')

        for num in nums:
            if num <= min_:
                min_ = num

            elif num <= second_min:
                second_min = num

            else:
                return True

        return False