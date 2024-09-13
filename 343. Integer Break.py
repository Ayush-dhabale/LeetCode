'''
Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.

 

Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
 

Constraints:

2 <= n <= 58
'''
class Solution:
    def integerBreak(self, n: int) -> int:
        '''
        if n < 4:
            return n - 1

        res = 1

        while n > 4:

            res *= 3
            n -= 3

        return res * n
        '''
        #DP
        dp = [0] * (n+1)
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        dp[2], dp[3] = 2, 3
        for i in range(4, n+1):
            dp[i] = max(dp[2] * dp[i - 2], dp[3] * dp[i - 3])
        
        return dp[-1]
        
        