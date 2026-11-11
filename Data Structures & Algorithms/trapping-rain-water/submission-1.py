class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        left_best, right_best = height[l], height[r]
        total = 0

        while l < r:
            if left_best < right_best:
                l += 1
                left_best = max(left_best, height[l])
                total += left_best - height[l]
            else:
                r -= 1
                right_best = max(right_best, height[r])
                total += right_best - height[r]

        return total