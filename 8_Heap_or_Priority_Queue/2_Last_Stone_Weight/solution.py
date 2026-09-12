import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # Continue running until len(stones) > 1
        maxHeap = [-weight for weight in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            high, low = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)
            if high != low:
                heapq.heappush(maxHeap, -(high-low))

        return (-1*maxHeap[0]) if maxHeap else 0

if __name__ == "__main__":
    solution = Solution()
    s, s2 = [2,3,6,2,4], [1,2]

    print(solution.lastStoneWeight(stones=s))
    print(solution.lastStoneWeight(stones=s2))
