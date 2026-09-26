"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
            
        intervals.sort(key = lambda x:x.start)
        ans = -1
        prev = intervals[0]

        for interval in intervals:
            if prev.end > interval.start:
                ans += 1
            else:
                prev = interval
        
        return ans == 0
