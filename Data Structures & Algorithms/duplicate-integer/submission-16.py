class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen: set[int] = set()

        for val in nums:
            if val in seen:
                return True
            seen.add(val)
        return False
    