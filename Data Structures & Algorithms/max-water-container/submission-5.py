class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lp,rp = 0, len(heights) - 1
        maxWater = 0

        while lp < rp:
            width = rp - lp
            height = min(heights[lp],heights[rp])
            area = width * height

            maxWater = max(maxWater,area)

            if heights[lp] < heights[rp]:
                lp += 1
            else:
                rp -= 1
        
        return maxWater