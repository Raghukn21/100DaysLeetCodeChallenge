class Solution:
    def findMin(self, nums: list[int]) -> int:
        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            
            # If mid element is greater than the rightmost element, 
            # the minimum must be in the right half.
            if nums[mid] > nums[high]:
                low = mid + 1
            # Otherwise, the minimum is in the left half (including mid).
            else:
                high = mid
                
        # After the loop, low == high, pointing to the minimum element.
        return nums[low]