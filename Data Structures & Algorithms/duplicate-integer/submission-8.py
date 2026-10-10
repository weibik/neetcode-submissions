class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        values = []

        for val in nums:
            if val in values:
                return True
            values.append(val)
        return False
    