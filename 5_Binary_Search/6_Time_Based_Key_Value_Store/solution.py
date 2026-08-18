from collections import defaultdict


class TimeMap:

    def __init__(self):
        # Timestamp is strictly increasing
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        start, end = 0, len(self.map[key])-1
        max_time, answer = float("inf"), ""
        while start <= end:
            mid = (start + end) // 2
            timestamp_prev = self.map[key][mid][1]
            if timestamp < timestamp_prev:
                end = mid-1
            else:
                start = mid+1
            if timestamp_prev <= timestamp:
                answer = self.map[key][mid][0]
        return answer if answer else ""

if __name__ == "__main__":
    timeMap = TimeMap()
    timeMap.set("alice", "happy", 1)
    timeMap.set("alice", "sad", 3)
    timeMap.set("alice", "happy", 5)
    timeMap.set("alice", "sad", 7)
    timeMap.set("alice", "sad", 10)
    print(timeMap.get("alice", 1))
