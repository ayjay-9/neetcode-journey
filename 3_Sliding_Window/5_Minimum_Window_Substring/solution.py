from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # No substring will be found
        if len(s) < len(t):
            return ""

        chars = [0]*52 # Lower and uppercase
        # Set the frequency for chars in t
        for i in range(len(t)):
            if t[i].islower():
                chars[ ord(t[i]) - ord('a') ] += 1
            else:
                chars[ord(t[i]) - ord('A') + 26 ] += 1

        left, window_len = 0, 0
        indices = []
        starting_index = 0
        for right in range(len(s)):
            # chars_check = chars
            substring = s[left:right+1]
            window_len = max(window_len, right-left+1)
            if substring[right].islower(): # Lowercase
                if chars[ord(substring[right]) - ord('a')]  >= 1:
                    indices.append(right)
                    chars[ord(substring[right]) - ord('a')] -= 1
            else: # Uppercase
                if chars[ord(substring[right]) - ord('A') + 26]  >= 1:
                    indices.append(right)
                    chars[ord(substring[right]) - ord('A') + 26] -= 1
        return s[min(indices):max(indices)+1]



if __name__ == "__main__":
    solution = Solution()
    print(solution.minWindow("OUZODYXAZV", "XYZ"))