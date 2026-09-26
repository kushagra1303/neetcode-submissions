class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lp,rp = 0, len(heights) - 1
        maxWater = 0

        while lp < rp:
            w = rp - lp
            h = min(heights[lp],heights[rp])
            area = w * h

            maxWater = max(maxWater,area)

            if heights[lp] > heights[rp]:
                rp -= 1
            else:
                lp += 1
        return maxWater
        