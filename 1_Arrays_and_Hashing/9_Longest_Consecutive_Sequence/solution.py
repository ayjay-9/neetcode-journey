class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        ordered_nums = sorted(set(nums))
        count = 1
        sequence = []

        # Edge Case 1: [], i.e no elements in the list
        if not ordered_nums:
            return 0

        # Edge Case 2: [0] or [1], i.e 1 element in the sorted set
        if len(ordered_nums) == 1:
            return count

        for i in range(len(ordered_nums) - 1):
            if (ordered_nums[i + 1] == ordered_nums[i] + 1):
                count = count + 1
            else:
                sequence.append(count)
                count = 1
                continue
            sequence.append(count) # If everything is in sequence
        return max(sequence)

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestConsecutive([0, 0]))