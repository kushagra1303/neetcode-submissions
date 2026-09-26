class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        ans = [0] * n

        for i in range(n):
            for j in range(i+1,n):
                if temp[j] > temp[i]:
                    ans[i] = j - i
                    break
        
        return ans
        