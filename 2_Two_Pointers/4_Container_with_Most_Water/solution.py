class Solution:
    def maxArea(self, heights: list[int]) -> int:
        # 1. Calculate Area
        # 2. Move pointer
        max_area = 0
        l_index, r_index = 0, len(heights)-1
        l_pointer, r_pointer = heights[0], heights[r_index]
        for i in range(len(heights)-1):
            if l_index == r_index:
                break
            area = (r_index - l_index) * min(l_pointer, r_pointer)
            if area > max_area:
                max_area = area
            # Move pointer with smaller value
            if l_pointer > r_pointer:
                r_index -= 1
                r_pointer = heights[r_index]
            else:
                l_index += 1
                l_pointer = heights[l_index]
        return max_area

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea([1,7,2,5,12,3,500,500,7,8,4,7,3,6]))