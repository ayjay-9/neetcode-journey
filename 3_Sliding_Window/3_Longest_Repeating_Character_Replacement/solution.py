from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        copy = list(s)
        # What is the highest occurring character?
        freq = defaultdict(int)
        for i in range(len(copy)):
            freq[copy[i]] += 1
        most_freq = max(freq, key=freq.get)
        # To reduce the number of replacements, replace the other k characters with the most freq character
        replacements, left, right, max_len = 0, 0, 1, 0
        substring = ""
        for _ in range(len(s)):
            # Length of substring
            max_len = max(max_len, len(substring))
            if replacements < k:
                # Replace Characters
                if copy[left] != most_freq:
                    copy[left] = most_freq
                    replacements += 1
                    if left != len(s)-1:
                        left += 1
                    substring = "".join(copy)[left:right + 1]
                if copy[right] != most_freq:
                    copy[right] = most_freq
                    replacements += 1
                    if right != len(s)-1:
                        right += 1
                    substring = "".join(copy)[left:right + 1]
                else:
                    if right != len(s)-1:
                        right += 1
                    substring = "".join(copy)[left:right+1]
            else:
                if right != len(s) - 1:
                    right += 1
                substring = "".join(copy)[left:right + 1]
        return max_len


if __name__ == "__main__":
    solution = Solution()
    print(solution.characterReplacement("AAAA", 0))