class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        if not intervals:
            return True # There can't be any conflict on a free schedule

        intervals.sort(key=lambda item:item.start) # Sort by start time
        for i in range(1, len(intervals)):
             if intervals[i].start < intervals[i-1].end:
                 return False
        return True

if __name__ == "__main__":
    solution = Solution()
    intervals = [Interval(0,30), Interval(5,10), Interval(15,20)]
    intervals2 = [Interval(5,8), Interval(9,15)]
    print(solution.canAttendMeetings(intervals=intervals))
    print(solution.canAttendMeetings(intervals=intervals2))
