class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Start at beginning, multiply every other thing in list, append to new list
        products = []

        for i in range(0, len(nums)):
            product = 1
            for j in range(0, len(nums)):
                if j != i:
                    product *= nums[j]
            products.append(product)

        return products