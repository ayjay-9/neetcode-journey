import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]

if __name__ == "__main__":
    solution = Solution()
    k, nums = 2, [2,3,1,5,4]
    k2, nums2 = 3, [2,3,1,1,5,5,4]
    print(solution.findKthLargest(nums=nums, k=k))
    print(solution.findKthLargest(nums=nums2, k=k2))