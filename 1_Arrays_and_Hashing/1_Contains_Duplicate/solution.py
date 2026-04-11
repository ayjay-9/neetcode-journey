
class Solution:
    def has_duplicate(self, nums: list[int]) -> bool:
        already_seen = set()
        for num in nums:
            if num in already_seen:
                return True
            already_seen.add(num)
        return False

if __name__ == '__main__':
    solution = Solution()
    print(solution.has_duplicate([1, 2, 3, 1, 4])) # Should be True
    print(solution.has_duplicate([1, 2, 3, 4, 5])) # Should be False