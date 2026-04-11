class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

if __name__ == "__main__":
    solution = Solution()
    print(solution.is_anagram("racecar", "carrace")) # Should be true
    print(solution.is_anagram("jar", "jam")) # Should be false
