'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
'''
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        #brute
        n = len(nums)
        len_ = float('inf')
        
        for i in range(n):
            for j in range(i,n):
                sum_ = 0
                for k in range(i,j+1):
                    sum_ += nums[k]
                    
                if sum_ >= target:
                    len_ = min(len_, j - i + 1)
                    
                    
        return len
    
        #Better
        n = len(nums)
        len_ = float('inf')
        
        for i in range(n):
            sum_ = 0
            for j in range(i,n):
                sum_ += nums[j]
                if sum_ >= target:
                    len_ = min(len_,j - i + 1)
                    break
                    
        return len_
                    
        '''
        #Optimal
        n = len(nums)
        low = 0
        min_len = float('inf')
        sum_ = 0

        for high in range(n):
            sum_ += nums[high]

            while sum_ >= target:
                min_len = min(min_len,high - low + 1)
                sum_ -= nums[low]
                low += 1

        return min_len if min_len != float('inf') else 0