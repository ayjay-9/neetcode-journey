class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # nums[i] + nums[j] + nums[k] == 0; (i != j, i !=k, j != k)
        trips = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            seen = set()
            for j in range(i + 1, len(nums)):
                target = -(nums[i] + nums[j])
                if target in seen:
                    triplet = [nums[i], target, nums[j]]
                    if triplet not in trips:
                        trips.append(triplet)
                seen.add(nums[j])
        return trips

if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([3,0,-2,-1,1,2]))