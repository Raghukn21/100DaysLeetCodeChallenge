class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # Frequency map for characters in the current window
        max_length = 0
        max_freq = 0  # Count of the most frequent character in the current window
        left = 0
        
        for right in range(len(s)):
            # Update frequency of the incoming character
            count[s[right]] = count.get(s[right], 0) + 1
            
            # Update max_freq - this is the "anchor" of our window
            max_freq = max(max_freq, count[s[right]])
            
            # Check if the current window is valid
            # (Length of window - frequency of most common char)
            while (right - left + 1) - max_freq > k:
                # If invalid, shrink from the left
                count[s[left]] -= 1
                left += 1
                # Note: We don't strictly need to update max_freq here 
                # because the result only improves if max_freq increases.
            
            # Update the global maximum length found
            max_length = max(max_length, right - left + 1)
            
        return max_length