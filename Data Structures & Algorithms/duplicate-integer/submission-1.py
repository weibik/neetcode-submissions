from collections import defaultdict 


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         hash_map = defaultdict(lambda: 0)

         for num in nums:
            hash_map[num] += 1
            if hash_map[num] > 1:
                return True

         return False