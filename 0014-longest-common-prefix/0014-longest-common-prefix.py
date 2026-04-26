class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # Take the first string as a reference
        for i in range(len(strs[0])):
            char = strs[0][i]
            
            # Check this character against all other strings
            for j in range(1, len(strs)):
                # If we've reached the end of a string or found a mismatch
                if i == len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]
        
        return strs[0]