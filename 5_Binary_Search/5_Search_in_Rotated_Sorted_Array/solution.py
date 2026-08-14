from operator import index


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.search(nums=[3,5,6,0,1,2], target=6))