'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

 

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 4, denominator = 333
Output: "0.(012)"
 

Constraints:

-231 <= numerator, denominator <= 231 - 1
denominator != 0
'''
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        frac = []

        if (numerator < 0) ^ (denominator < 0):
            frac.append("-")

        numerator,denominator = abs(numerator), abs(denominator)
        int_p = numerator // denominator
        frac.append(str(int_p))

        remainder = numerator % denominator
        
        if remainder == 0:
            return ''.join(frac)

        frac.append('.')
        map_ = {}
        pos = len(frac)
        while remainder != 0:
            if remainder in map_:
                frac.insert(map_[remainder],"(")
                frac.append(")")
                break

            map_[remainder] = pos
            pos += 1
            remainder *= 10
            frac.append(str(remainder // denominator))
            remainder %= denominator

        return ''.join(frac)