"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort by start values
        intervals.sort(key=lambda x: x.start)

        # now the list is sorted, we can check for overlaps
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
                
        return True
            

