class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0

        l, r = 0, len(heights) - 1

        while l < r:
            min_h = min(heights[l], heights[r])
            width = r - l

            max_water = max(max_water, min_h * width)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_water