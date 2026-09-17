class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            carry = (a&b) << 1
            a ^= b
            b = carry
        return a

if __name__ == "__main__":
    solution = Solution()
    print(solution.getSum(a=1, b=1))
    print(solution.getSum(a=4, b=7))