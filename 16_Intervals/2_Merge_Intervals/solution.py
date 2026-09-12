class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return [[]]

        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda item: item[0])
        merged = [intervals[0]]
        for i in range(1,len(intervals)):
            curr, prev = intervals[i], merged[-1]
            if curr[0] <= prev[1]: # If current start time is less than prev end time
                merged[-1] = [prev[0], max(curr[1], prev[1])] # Extend the duration
            else:
                merged.append(curr)
        return merged

if __name__ == "__main__":
    solution = Solution()

    i1, i2, i3, i4 = [[1, 3], [1, 5], [6, 7]], [[1,2], [2,3]], [[1,3], [8,10], [15,18], [2,6]], [[1,4],[5,6]]
    i5 = [[1,4],[0,4]]

    print(f"{i1} -> {solution.merge(intervals=i1)}")
    print(f"{i2} -> {solution.merge(intervals=i2)}")
    print(f"{i3} -> {solution.merge(intervals=i3)}")
    print(f"{i4} -> {solution.merge(intervals=i4)}")
    print(f"{i5} -> {solution.merge(intervals=i5)}")