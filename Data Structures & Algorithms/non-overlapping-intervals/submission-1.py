class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda  x:x[1])
        ans = -1
        prev = intervals[0]

        for interval in intervals:
            if prev[1] > interval[0]:
                ans += 1
            else:
                prev = interval
        return ans
        