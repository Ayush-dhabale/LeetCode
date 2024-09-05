"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
 

Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        '''
        #brute
        lesser = []
        greater = []
        temp = head
        while temp:
            if temp.val >= x:
                greater.append(temp.val)
                
            else:
                lesser.append(temp.val)
                
            less_head = ListNode(lesser[0])
            temp = less_head
            for val in lesser[1:0] + greater:
                temp.next = ListNode(val)
                temp = temp.next
                
            temp.next = None
            
            return less_head
       
        '''
        
        #Optimal
        if not head or not head.next:
            return head
        
        less_h = ListNode(0)
        greater_h = ListNode(0)

        #Pointer
        less = less_h
        great = greater_h
        curr = head

        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next

            else:
                great.next = curr
                great = great.next

            curr = curr.next


        #Combine
        great.next = None
        less.next = greater_h.next

        return less_h.next