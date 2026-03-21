class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZeroIndex = 0
        
        for cur in range(len(nums)):
            if nums[cur] != 0:
                # Swap the non-zero element with the element at lastNonZeroIndex
                nums[lastNonZeroIndex], nums[cur] = nums[cur], nums[lastNonZeroIndex]
                lastNonZeroIndex += 1