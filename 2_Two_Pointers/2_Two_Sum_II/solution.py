class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # 1-Indexed Array [10, 20, 30] = [1, 2, 3] not [0, 1, 2]
        index1 = 1 # Start at first element
        index2 = len(numbers) # Start at last element

        # If sum > target, decrease right pointer, else increase left pointer
        for _ in range(len(numbers)):
            if numbers[index1-1] != numbers[index2-1]:
                if numbers[index1-1] + numbers[index2-1] == target:
                    return [index1, index2]
                elif numbers[index1-1] + numbers[index2-1] > target:
                    index2 -= 1
                else:
                    index1 += 1

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2,3,4], 6))