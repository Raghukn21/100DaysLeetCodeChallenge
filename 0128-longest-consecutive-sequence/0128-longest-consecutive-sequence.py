class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # Convert list to a set for O(1) lookups
        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:
            # Check if 'num' is the start of a sequence
            # If num - 1 exists, 'num' is NOT the start, so we skip it
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1
                
                # Count how many consecutive numbers follow
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1
                
                # Update the global maximum
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak