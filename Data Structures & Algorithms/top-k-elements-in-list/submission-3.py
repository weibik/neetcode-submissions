from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(lambda: 0)

        for num in nums:
            hash_map[num] += 1

        result = sorted(hash_map, key=hash_map.get, reverse=True)[:k]
        return result