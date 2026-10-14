class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        buckets = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1

        # nums = [2,2, 5,5,3,3,3], k = 2
        # {2:2, 5:2, 3:3}

        for key, val in count.items():
            buckets[val].append(key)
        # [[], [], [2, 5], [3], [], [], [], []]

        result = []
        for freq in range(len(nums), 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
