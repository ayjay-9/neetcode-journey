import heapq


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.minHeap = nums

        heapq.heapify(self.minHeap) # Sorts in O(logn), but may have more than k elements
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

if __name__ == "__main__":
    kthlargest = KthLargest(k=3, nums=[1, 2, 3, 3])
    print(kthlargest.add(3))
    print(kthlargest.add(5))
    print(kthlargest.add(6))
    print(kthlargest.add(7))
    print(kthlargest.add(8))


