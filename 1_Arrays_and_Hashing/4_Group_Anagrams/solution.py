from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                # key = Ascii value of the string - Ascii valuie of 'a'
                key = ord(c) - ord('a')
                # key is the index that will be incremented to produce a frequency pattern (fingerprint)
                count[key] += 1
            # If strings have the same fingerprint/pattern, add them to the end of the list
            # count is converted to a tuple because tuples are immutable and can be used as dictionary keys
            groups[tuple(count)].append(s)

        return list(groups.values())

if __name__ == '__main__':
    solution = Solution()
    print(solution.groupAnagrams(["act","pots","tops","cat","stop","hat"])) # Should be True