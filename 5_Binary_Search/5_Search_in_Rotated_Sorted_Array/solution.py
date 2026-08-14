from operator import index


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start, end = 0, len(nums)-1

        while start <= end:
            mid = (start+end) // 2
            if target == nums[mid]:
                return mid
            # Left sorted portion
            if nums[start] <= nums[mid]:
                if target > nums[mid] or target < nums[start]: # Go to right portion
                    start = mid+1
                else: # Eliminate right portion
                    end = mid-1
            else: # Right sorted portion
                if target < nums[mid] or target > nums[end]: # Go to left portion
                    end = mid-1
                else:
                    start = mid+1
        return -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.search(nums=[3,4,5,6,1,2], target=1))