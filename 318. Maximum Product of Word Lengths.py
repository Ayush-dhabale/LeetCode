'''
Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

 

Example 1:

Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".
Example 3:

Input: words = ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.
 

Constraints:

2 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i] consists only of lowercase English letters.
'''
from typing import List
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        bitmask = []
        for word in words:
            mask = 0
            for char in word:
                mask |= 1 << (ord(char) - ord('a'))
            bitmask.append((mask, len(word)))
    
        max_ = 0
        for i in range(n):
            for j in range(i + 1, n):
                if bitmask[i][0] & bitmask[j][0] == 0:  
                    max_ = max(max_, bitmask[i][1] * bitmask[j][1])
        
        return max_
