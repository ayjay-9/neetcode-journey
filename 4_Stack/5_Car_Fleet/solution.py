class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)

if __name__ == "__main__":
    solution = Solution()
    print(solution.carFleet(target = 10, position = [4,1,0,7], speed = [2,2,1,1]))