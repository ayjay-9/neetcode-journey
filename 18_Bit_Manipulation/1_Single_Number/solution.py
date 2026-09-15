from collections import Counter


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans

if __name__ == "__main__":
    solution = Solution()
    print(solution.singleNumber(nums=[3,2,3]))
    print(solution.singleNumber(nums=[7,6,6,7,8]))