
class Solution:
    def has_duplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)

if __name__ == '__main__':
    solution = Solution()
    print(solution.has_duplicate([1, 2, 3, 1, 4])) # Should be True
    print(solution.has_duplicate([1, 2, 3, 4, 5])) # Should be False