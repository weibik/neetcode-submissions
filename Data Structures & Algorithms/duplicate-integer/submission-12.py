class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}

        for val in nums:
            if val in hash_map:
                return True
            hash_map[val] = False
        return False
    