class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start, end = 0, len(nums)-1
        found = False

        while start <= end:
            mid = (end + start) // 2
            if target < nums[mid]:
                end = mid
            else:
                start = mid
            if target == nums[start]:
                found = True
                break
            start += 1

        if found:
            return start
        else:
            return -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.search(nums=[-1,0,2,4,6,8], target=-1))