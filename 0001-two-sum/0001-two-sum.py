class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # hash_map stores: { value: index }
        hash_map = {}
        
        for i, n in enumerate(nums):
            # Calculate the "complement" needed to reach the target
            complement = target - n
            
            # Check if we've already seen this complement in the map
            if complement in hash_map:
                # If found, return the index of the complement and current index
                return [hash_map[complement], i]
            
            # Otherwise, add the current number and its index to the map
            hash_map[n] = i
            
        return []