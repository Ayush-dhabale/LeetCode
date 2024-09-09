'''
You are given two integers m and n, which represent the dimensions of a matrix.

You are also given the head of a linked list of integers.

Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.

Return the generated matrix.

 

Example 1:


Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
Explanation: The diagram above shows how the values are printed in the matrix.
Note that the remaining spaces in the matrix are filled with -1.
Example 2:


Input: m = 1, n = 4, head = [0,1,2]
Output: [[0,1,2,-1]]
Explanation: The diagram above shows how the values are printed from left to right in the matrix.
The last space in the matrix is set to -1.
 

Constraints:

1 <= m, n <= 105
1 <= m * n <= 105
The number of nodes in the list is in the range [1, m * n].
0 <= Node.val <= 1000
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        mat = [[-1] * n for _ in range(m)]
        left = 0
        right = n - 1
        top = 0
        bottom = m - 1
        temp = head

        while right >= left and bottom >= top and temp:

            #Right
            for i in range(left, right+ 1):
                if temp:
                    mat[top][i] = temp.val
                    temp = temp.next
                else:
                    break

            top += 1

            #Down

            for i in range(top,bottom+1):
                if temp:
                    mat[i][right] = temp.val
                    temp = temp.next
                else:
                    break
            right -= 1

            #Left
            if top <= bottom:
                for i in range(right,left -1, -1):
                    if temp:
                        mat[bottom][i] = temp.val
                        temp = temp.next

                    else:
                        break

                bottom -= 1

            #Up
            if right >= left:
                for i in range(bottom,top - 1, -1):
                    if temp:
                        mat[i][left] = temp.val
                        temp = temp.next

                    else:
                        break

                left += 1

        return mat