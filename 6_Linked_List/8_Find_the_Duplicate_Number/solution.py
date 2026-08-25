class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        nums = sorted(nums)
        l, r = 0, 1
        while l <= r:
            if nums[l] != nums[r]:
                l += 1
                r += 1
            else:
                return nums[l]

if __name__ == "__main__":
    solution = Solution()
    print(solution.findDuplicate(nums=[1,2,3,2,2]))
