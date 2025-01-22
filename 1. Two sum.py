'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        '''

        #Brute
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if (nums[i] + nums[j]) == target:
                    return [i,j]        
                
        #Better
        nums_index = [(num,i) for i, num in enumerate(nums)]
        
        nums_index.sort()
        
        high, low = n- 1, 0
        
        while high > low:
            if nums_index[low][0] + nums_index[high][0] > target:
                high -= 1
                
            elif nums_index[low][0] + nums_index[high][0] < target:
                low += 1
                
            else:
                return [nums_index[low][1], nums_index[high][1]]
        
        '''
            
        #Optimal
        map_ = {}
        
        for i, num in enumerate(nums):
            if target - num in map_:
                return [i, map_[target - num]]
            
            map_[num] = i

        