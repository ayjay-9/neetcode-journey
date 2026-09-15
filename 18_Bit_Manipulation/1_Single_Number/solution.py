from collections import Counter


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        freq = Counter(nums)
        freq = sorted(freq.items(), key=lambda item: item[1])
        return freq[0][0]

if __name__ == "__main__":
    solution = Solution()
    print(solution.singleNumber(nums=[3,2,3]))
    print(solution.singleNumber(nums=[7,6,6,7,8]))