import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        split_string = s[::-1].lower().split(" ")
        reversed_string = ''.join(split_string)
        reversed_string = re.sub(r"\W", "", reversed_string)
        s = re.sub(r"\W", "", s).lower()
        print(s, reversed_string)
        return s == reversed_string

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("tab a cat"))