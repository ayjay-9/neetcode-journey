class Solution:
    def countBits(self, n: int) -> list[int]:
        res = []
        for bit in range(n+1):
            res.append(bin(bit).count('1')) # O(1) extra space
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.countBits(n=4))