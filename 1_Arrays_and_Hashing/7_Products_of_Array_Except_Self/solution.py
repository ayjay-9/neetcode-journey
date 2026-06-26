class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        products = [1] * len(nums)
        prefix, postfix = 1, 1

        for i in range(len(nums)):
            products[i] = prefix
            prefix *= nums[i]

        for j in range(len(nums) - 1, -1, -1):
            products[j] *= postfix
            postfix *= nums[j]
        return products