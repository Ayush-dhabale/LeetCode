"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Brute
        '''
        temp = head
        nums = []
        while temp:
            if temp.val not in nums:
                nums.append(temp.val)
                
        head = ListNode(nums[0])
        temp = head
        for val in nums[1:]:
            temp.next = ListNode(val)
            temp = temp.next
            
        return head
        
        '''
        
        #Optimal
            
        if not head:
            return head
        
        curr = head

        while curr:
            if curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next

            else:
                curr = curr.next
        
        return head