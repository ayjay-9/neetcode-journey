from math import floor, ceil


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Median = ceil((N+1) / 2)th position
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        l, r = 0, len(nums1)-1
        size, pos, median = r+1, (l+r) / 2, 0
        if pos.is_integer(): # Median pos is an integer number
            median = nums1[int(pos)]
        else: # Median pos is a float, median is the average of the two middle numbers
            median = (nums1[floor(pos)] + nums1[ceil(pos)]) / 2
        return median

if __name__ == "__main__":
    solution = Solution()
    print(solution.findMedianSortedArrays(nums1=[1,2], nums2=[3]))
    print(solution.findMedianSortedArrays(nums1=[1,3], nums2=[2,4]))