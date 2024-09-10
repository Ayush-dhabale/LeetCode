'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
 

Constraints:

0 <= num <= 231 - 1
 

Follow up: Could you do it without any loop/recursion in O(1) runtime?
'''
class Solution:
    def addDigits(self, num: int) -> int:
        '''
        #Brute
        while num >= 10:  
            digit_sum = 0
            while num > 0:
                digit_sum += num % 10  
                um //= 10  
            num = digit_sum  
        return num

        #Better
        if num < 10:  
            return num
        digit_sum = sum(int(digit) for digit in str(num))  
        return self.addDigits(digit_sum)  
        
        '''
        #Optimal
        if not num:
            return 0
        return 1 + (num - 1) % 9