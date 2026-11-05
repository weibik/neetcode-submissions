class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        for i in range(0, len(nums) - 2):
            if nums[0] > 0:
                break

            if (i > 0 and nums[i] == nums[i - 1]):
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]

                if current_sum < 0:
                    l += 1
                elif current_sum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while (nums[l] == nums[l - 1] and l < r):
                        l += 1

        return res