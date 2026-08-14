class Solution:
    def findMin(self, nums: list[int]) -> int:
        start, end = 0, len(nums)-1
        min_num = nums[0]
        while start <= end:
            mid = (start + end) // 2
            # Left sorted portion
            if nums[mid] > nums[end]:
                start = mid+1
            else:
                end = mid-1
            if nums[mid] < min_num:
                min_num = nums[mid]
        return min_num

if __name__ == "__main__":
    solution = Solution()
    print(solution.findMin(nums=[2,3,4,5,1]))