class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        max_num = []
        left = 0
        window = []
        for right in range(k-1, len(nums)):
            window = nums[left:right+1]
            max_num.append(max(window))
            left += 1
        return max_num

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSlidingWindow([1,2,1,0,4,2,6], 3))