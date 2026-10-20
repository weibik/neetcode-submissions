class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [0] * len(nums)
        left = [1] * len(nums)
        right = [1] * len(nums)

        for i in range(1, length):
            left[i] = left[i-1] * nums[i-1]

        for i in range(length - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        for i in range(length):
            res[i] = left[i] * right[i]
        

        return res