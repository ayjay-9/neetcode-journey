from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        l_index = 0
        r_index = l_index+1
        l, r = s[l_index], s[r_index]
        seen = set()
        freq = defaultdict(int)
        for i in range(len(s)):
            if not l in seen:
                seen.add(l)

            if not r in seen:
                seen.add(r)
                if r_index != len(s)-1:
                    r_index += 1
                    r = s[r_index]

            if r in seen:
                substring = "".join(seen)
                freq[substring] = len(substring)
                if l_index != len(s)-1:
                    l_index += 1
                if r_index != len(s)-1:
                    r_index = l_index+1
                l, r = s[l_index], s[r_index]
                seen = set()
        return max(freq.values())

if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcde"))