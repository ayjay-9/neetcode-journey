class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n

if __name__ == "__main__":
    solution = Solution()
    print(solution.myPow(x=2.00000, n=5))
    print(solution.myPow(x=1.10000, n=10))
    print(solution.myPow(x=2.00000, n=-3))