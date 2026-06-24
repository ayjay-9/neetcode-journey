class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_set = set()
        for i in range(0, len(nums) - 1):
            for j in range(1, len(nums)):
                if (i != j) and (nums[i] + nums[j]) == target:
                    new_set.add(i)
                    new_set.add(j)

        return list(new_set)

