"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        #Brute
        nums.sort()
        longest = 1
        current_streak = 1
    
    
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]: 
                continue
            elif nums[i] == nums[i - 1] + 1: 
                current_streak += 1
            else:  
                longest = max(longest, current_streak)
                current_streak = 1
    
        return max(longest, current_streak)
        
        '''
        #Optimal
        nums_set = set(nums)
        max_ = 0

        for num in nums:
            if num - 1 not in nums_set:
                current = 1

                while num + 1 in nums_set:
                    num += 1
                    current += 1

                max_ = max(max_,current)

        return max_