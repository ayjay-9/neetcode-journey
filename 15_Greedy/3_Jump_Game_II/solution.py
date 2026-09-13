class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = current_end = max_reach = 0
        for i in range(len(nums) - 1):
            max_reach = max(max_reach, i + nums[i])
            if i == current_end:  # exhausted this jump's range — must jump now
                jumps += 1
                current_end = max_reach
        return jumps # minimum number of jumps


if __name__ == "__main__":
    solution = Solution()
    nums, nums2 = [2,4,1,1,1,1], [2,1,2,1,0]

    print(solution.jump(nums=nums))
    print(solution.jump(nums=nums2))