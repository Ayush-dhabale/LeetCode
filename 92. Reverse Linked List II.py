"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        '''
        #Brute
        temp =  head
        nums1 = []
        while temp:
            nums.append(temp.val)

        nums[left - 1:right] = nums[left - 1:right][::-1]

        head = Listnode(nums[0])
        temp = head
        for val in nums[1:]:
            temp.next = ListNode(val)
            temp = temp.next

        temp.next = None

        return head

        '''
        #Optimal
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        
        for i in range(left - 1):
            temp = temp.next

        start = temp
        curr  = tail =  temp.next
        prev = None

        for i in range(right - left + 1):
            next_node = curr.next 
            curr.next = prev
            prev = curr
            curr = next_node

        start.next = prev
        tail.next = curr
        

        return dummy.next