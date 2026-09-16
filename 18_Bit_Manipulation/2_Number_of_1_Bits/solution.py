class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n%2
            n = n >> 1
        return count

if __name__ == "__main__":
    solution = Solution()
    print(solution.hammingWeight(n=23))
    print(solution.hammingWeight(n=2147483645))