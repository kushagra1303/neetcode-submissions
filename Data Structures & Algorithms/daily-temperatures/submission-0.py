class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = []
        n = len(temp)
        for i in range(n):
            count = 0
            for j in range(i+1,n):
                count += 1
                if temp[i]<temp[j]:
                    res.append(count)
                    break
            else:
                res.append(0)
        return res
        