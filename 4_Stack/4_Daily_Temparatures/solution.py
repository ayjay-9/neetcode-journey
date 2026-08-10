class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        days= [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                days[stackInd] = i - stackInd
            stack.append((t, i))
        return days


if __name__ == "__main__":
    solution = Solution()
    print(solution.dailyTemperatures(temperatures=[30,38,30,36,35,40,28]))