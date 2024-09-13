'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','I','E','O','U']
        l = list(s)

        front = 0
        rare = len(l)- 1

        while rare > front:
            while rare > front and l[front] not in vowels:
                front +=1

            while rare > front and l[rare] not in vowels:
                rare -= 1

            l[front],l[rare] = l[rare],l[front]
            front += 1
            rare -= 1
        return ''.join(l)
        

        


        