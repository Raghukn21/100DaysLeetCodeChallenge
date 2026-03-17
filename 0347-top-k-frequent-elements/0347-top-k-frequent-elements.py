class Solution:
    def topKFrequent(self, nums, k):
        # Step 1: Count the frequency of each element
        count_map = {}
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
            
        # Step 2: Create buckets where index = frequency
        freq_buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, count in count_map.items():
            freq_buckets[count].append(num)
            
        # Step 3: Iterate backwards to get the top k frequent elements
        result = []
        for i in range(len(freq_buckets) - 1, 0, -1):
            for num in freq_buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result