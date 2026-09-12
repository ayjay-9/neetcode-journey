import heapq
from collections import Counter, deque


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # [-cnt, idleTime]
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1 # Reduce the frequency of the letter since we've processed the task
                if cnt < 0:
                    q.append([cnt, time+n]) # Store the next available time it can be added back
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0]) # Push the reduced count to the heap
        return time

if __name__ == "__main__":
    solution = Solution()
    tasks, n = ["X","X","Y","Y"], 2
    tasks2, n2 = ["A","A","A","B","C"], 3

    print(solution.leastInterval(tasks=tasks, n=n))
    print(solution.leastInterval(tasks=tasks2, n=n2))