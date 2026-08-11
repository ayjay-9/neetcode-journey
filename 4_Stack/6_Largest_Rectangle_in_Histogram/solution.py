class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0
        stack = []  # stores pairs: (start_index, height)

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                index, popped_height = stack.pop()
                max_area = max(max_area, popped_height * (i - index))
                start = index
            stack.append((start, height))

        for index, height in stack:
            max_area = max(max_area, height * (len(heights) - index))
        return max_area

if __name__ == "__main__":
    solution = Solution()
    print(solution.largestRectangleArea(heights=[7,1,7,2,2,4]))