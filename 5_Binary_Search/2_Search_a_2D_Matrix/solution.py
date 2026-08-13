class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        outer_start, inner_start, outer_end, inner_end = 0, 0, len(matrix)-1, len(matrix[0])-1
        found = False
        while outer_start <= outer_end and inner_start <= inner_end:
            outer_mid = (outer_start + outer_end) // 2
            if target < matrix[outer_mid][inner_start]:
                outer_end -= 1
            elif target in matrix[outer_mid]:
                inner_mid = (inner_start + inner_end) // 2
                if target < matrix[outer_mid][inner_mid]:
                    inner_end = inner_mid
                else:
                    inner_start = inner_mid
                if target == matrix[outer_mid][inner_start]:
                    found = True
                    break
                inner_start += 1
            else:
                outer_start += 1
        return found

if __name__ == "__main__":
    solution = Solution()
    print(solution.searchMatrix(matrix=[[1,2,4,8],[10,11,12,13],[14,20,30,40]], target=4))