class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        if not nums:
            return 0
        for num in range(len(nums)):
            if num not in nums:
                return num
        return max(nums)+1

if __name__ == "__main__":
    solution = Solution()
    print(solution.missingNumber(nums=[1,2,3]))
    print(solution.missingNumber(nums=[0,2]))