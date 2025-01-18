'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 

Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
'''
from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        #Brute
        result = []
        for num in nums1:
            if num in nums2:
                result.append(num)
                nums2.remove(num)  # Remove one occurrence from nums2
        return result
       
       #Better
        freq_map = Counter(nums1)  # Frequency map for nums1
        result = []
    
        for num in nums2:
            if freq_map[num] > 0:
                result.append(num)
                freq_map[num] -= 1  # Decrease the count in the map
    
        return result
        '''
        #Optimal
        
        nums1.sort()
        nums2.sort()
        result = []
        i, j = 0, 0
    
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
    
        return result
