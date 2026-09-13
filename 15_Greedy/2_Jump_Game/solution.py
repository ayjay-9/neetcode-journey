class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= len(nums):
                return True # Early return
        return True


if __name__ == "__main__":
    solution = Solution()
    nums, nums2, nums3, nums4, nums5 = [1,2,0,1,0], [1,2,1,0,1], [5,4,0,2,0,1,0,1,0], [2,3,1,1,4], [2,5,0,0]

    print(solution.canJump(nums=nums))
    print(solution.canJump(nums=nums2))
    print(solution.canJump(nums=nums3))
    print(solution.canJump(nums=nums4))
    print(solution.canJump(nums=nums5))