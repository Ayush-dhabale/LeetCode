'''
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

 

Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
'''
import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        factors = [2,3,5]
        i = 0
        count = {1}


        while i < n:
            current_ugly = heapq.heappop(heap)
            if i == n - 1:
                return current_ugly

            for factor in factors:
                new_ugly = current_ugly * factor
                if new_ugly not in count:
                    heapq.heappush(heap,new_ugly)
                    count.add(new_ugly)
            i += 1
