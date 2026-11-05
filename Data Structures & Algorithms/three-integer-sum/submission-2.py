class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        last_index = len(nums) - 1
        nums = sorted(nums)

        if nums[0] > 0:
            return []

        for i in range(0, len(nums) - 2):
            l = i + 1
            r = last_index

            if (i > 0 and nums[i] == nums[i - 1]):
                continue

            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                if current_sum < 0:
                    l += 1
                    while (nums[l] == nums[l - 1] and l < r):
                        l += 1
                elif current_sum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while (nums[l] == nums[l - 1] and l < r):
                        l += 1

        return res