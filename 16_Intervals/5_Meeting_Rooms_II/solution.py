class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        if not intervals:
            return 0 # There can't be any conflict on a free schedule

        start, end = sorted([i.start for i in intervals]), sorted([i.end for i in intervals])
        res, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                s+=1
                count+=1
            else:
                e+=1
                count-=1
            res = max(res, count)
        return res

if __name__ == "__main__":
    solution = Solution()
    intervals = [Interval(0,40), Interval(5,10), Interval(15,20)]
    intervals2 = [Interval(4,9)]
    intervals3 = [Interval(1,10), Interval(2,3), Interval(4,5), Interval(6,7), Interval(8,9)]
    intervals4 = [Interval(1, 5), Interval(2, 6), Interval(3, 7), Interval(4, 8), Interval(5, 9)]
    print(solution.minMeetingRooms(intervals=intervals))
    # print(solution.minMeetingRooms(intervals=intervals2))
    # print(solution.minMeetingRooms(intervals=intervals3))
    # print(solution.minMeetingRooms(intervals=intervals4))
