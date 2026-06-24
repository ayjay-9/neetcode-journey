from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # I'll need the number and the count
        groups = defaultdict(int)  # Number: 0 by default

        for num in sorted(nums):
            groups[num] += 1

        return list(sorted(groups, key=groups.get, reverse=True)[0:k])

if __name__ == "__main__":
    print(Solution().topKFrequent([1,2,2,3,3,3], 2))