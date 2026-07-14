class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) < 3:
            return 0

        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        water = 0

        while left < right:
            if left_max <= right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]

        return water

if __name__ == "__main__":
    solution = Solution()
    print(solution.trap([0,2,0,3,1,0,1,3,2,1]))