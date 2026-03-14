class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths are different, they can't be anagrams
        if len(s) != len(t):
            return False
            
        # Array to store the frequency of 26 lowercase English letters
        count = [0] * 26
        
        # Increment for characters in s, decrement for characters in t
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
            
        # If any count is not 0, there is a mismatch
        for c in count:
            if c != 0:
                return False
                
        return True
        