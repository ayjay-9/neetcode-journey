from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # What is the highest occurring character?
        count = defaultdict(int)
        res, left, maxf = 0, 0, 0

        for right in range(len(s)):
            count[s[right]] += 1
            maxf = max(maxf, count[s[right]])

            if (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.characterReplacement("AAABABB", 1))