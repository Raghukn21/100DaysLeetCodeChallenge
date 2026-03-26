class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Step 1: Initialize the sum of the first window
        # We use float('-inf') if we want to be safe, 
        # but sum(nums[:k]) is perfect here.
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Step 2: Slide the window
        for i in range(k, len(nums)):
            # Add the element entering the window, subtract the one leaving
            current_sum += nums[i] - nums[i - k]
            
            if current_sum > max_sum:
                max_sum = current_sum
        
        # Step 3: Calculate the average at the very end
        return max_sum / k