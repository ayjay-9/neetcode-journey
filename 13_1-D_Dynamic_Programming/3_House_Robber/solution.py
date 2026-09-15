class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 2:
            return nums[1]
        total, i = 0, 0
        while i < len(nums):
            if i+1 < len(nums):
                if nums[i+1] > nums[i]:
                    total += nums[i+1]
                    i += 3
                else:
                    total += nums[i]
                    i += 2
        return total

if __name__ == "__main__":
    solution = Solution()
    print(solution.rob(nums=[1,1,3,3]))
    print(solution.rob(nums=[2,9,8,3,6]))