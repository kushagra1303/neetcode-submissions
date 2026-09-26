class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        lp , rp = 0, len(height) - 1
        leftMax, rightMax = height[lp], height[rp]

        res = 0

        while lp < rp:
            if leftMax < rightMax:
                lp += 1
                leftMax = max(leftMax, height[lp])
                res += leftMax - height[lp]
            
            else:
                rp -= 1
                rightMax = max(rightMax,height[rp])
                res += rightMax - height[rp]
        
        return res
            
