class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Assuming all letters are in lowercase
        track_letters = [0] * 26
        
        # Both strings are equal so they hjave the same lengths
        for i in range(len(s)):
            track_letters[ ord(s[i]) - ord('a') ] += 1
            track_letters[ ord(t[i]) - ord('a') ] -= 1

        for val in track_letters:
            if val != 0:
                # i.e if the value does not reset, then it is not p[resent in the two strings
                return False
        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.is_anagram("racecar", "carrace")) # Should be true
    print(solution.is_anagram("jar", "jam")) # Should be false
