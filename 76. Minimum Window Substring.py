"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        #Brute
        from collections import Counter
        n = len(s)
        t_map = Counter(t)
        min_len = float('inf')
        min_win = ""
        
        for i in range(n):
            for j in range(i,n):
                curr_win = s[i:j+1]
                curr_win_map = Counter(curr_win)
                
                for char in t_map:
                    if curr_win_map.get(char,0) < t_map[char]:
                        break
                    
                else:
                    min_len = min(min_len, j - i + 1)
                    min_win = curr_win
                    
        return min_win if min_len !=  float('inf') else ""
        

    
        #Better
        from collections import Counter
        min_len = float('inf')
        start = -1
        n = len(s)
        m = len(t)
        
        
        for i in range(n):
            t_map = Counter(t)
            count 
            
            for j in range(n):
                if t_map[s[j]] > 0:
                    count += 1
                    t_map[s[j]] -= 1
                    
                if count == m:
                    min_len = min(min_len, j - i + 1)
                    start = i
                    
        return s[start:min_len + 1] if min_len != float('inf') else ""
    
        '''
        
        #Optimal
        from collections import Counter
        min_len = float('inf')
        start = -1
        n = len(s)
        m = len(t)
        t_map = Counter(t)
        low = high = 0
        count = 0
        
        while high < n:
            if t_map[s[high]] > 0:
                count += 1
            t_map[s[high]] -= 1
                
            while count == m:
                if min_len < high - low + 1:
                    min_len = high - low + 1
                    start = low
                        
                t_map[s[low]] += 1
                    
                if t_map[s[low]] > 0:
                    count -= 1
                    
                low += 1
                    
            high += 1
                
        return s[start:start + min_len] if start != -1 else ""