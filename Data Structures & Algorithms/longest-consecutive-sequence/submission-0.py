class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        set_of_nums = set(nums)

        if len(set_of_nums) == 1:
            return 1

        for num in set_of_nums:
            if (num - 1) not in set_of_nums:
                current_length = 0
                while (num + current_length) in set_of_nums:
                    current_length += 1
                max_length = max(current_length, max_length)

        return max_length