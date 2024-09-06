"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        '''
        #Brute
        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next
    

        left, right = 0, len(nodes) - 1
        while left < right:
            nodes[left].next = nodes[right]
            left += 1
            if left == right:
                break
            nodes[right].next = nodes[left]
            right -= 1
    
    
            nodes[left].next = None
        
        '''
        #Optimal
        
        slow , fast = head , head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        curr = slow
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        first ,second = head , prev

        while second.next:
            temp1 , temp2 = first.next , second.next

            first.next = second
            second.next = temp1
            first , second = temp1 , temp2


            