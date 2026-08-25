class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # Floyd's Algorithm to detect cycles
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            index = nums[fast]
            fast = nums[index]
            if slow == fast: # First intersection
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2: # Index of start of loop
                return slow or slow2

if __name__ == "__main__":
    solution = Solution()
    print(solution.findDuplicate(nums=[1,2,3,2,2]))
