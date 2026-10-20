class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i, j = 1, len(nums) - 2
        index = 0
        res = [0] * len(nums)
        left = [1] * len(nums)
        right = [1] * len(nums)


        while i < len(nums):
            left[i] = left[i-1] * nums[i-1]
            i += 1

        while j >= 0:
            right[j] = right[j + 1] * nums[j + 1]
            j -= 1

        while index < len(nums):
            res[index] = left[index] * right[index]
            index += 1
        return res