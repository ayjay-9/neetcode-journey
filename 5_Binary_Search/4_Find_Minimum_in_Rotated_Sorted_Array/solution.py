class Solution:
    def findMin(self, nums: list[int]) -> int:
        return min(nums)

if __name__ == "__main__":
    solution = Solution()
    print(solution.findMin(nums=[3,4,5,6,1,2]))