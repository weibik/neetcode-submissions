class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, val in enumerate(nums):
            hash_map[val] = i
        
        for i, val in enumerate(nums):
            comp = target - val
            if comp in hash_map and hash_map[comp] != i:
                return [i, hash_map[comp]]

# 4, 5, 3 target 7
# {4:0, 5:1, 3:2}

