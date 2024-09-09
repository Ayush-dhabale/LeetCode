'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        #Brute
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                 if nums[i] == nums[j] and abs(i - j) <= k:
                    return True
    
        return False
        
        #Better
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        
        
            if len(seen) > k:
                seen.remove(nums[i - k])
        return False
    
        '''
    
        #Optimal
                
        temp = {}
        i = 0

        while i < len(nums):
            if nums[i] in temp and abs(i-temp[nums[i]]) <= k:
                return True

            temp[nums[i]] = i
            i += 1
        return False

        
        