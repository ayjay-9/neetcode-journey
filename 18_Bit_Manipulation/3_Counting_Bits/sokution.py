class Solution:
    def countBits(self, n: int) -> list[int]:
        res = []
        for bit in range(n+1):
            count = 0
            while bit:
                bit &= bit-1
                count += 1
            res.append(count)
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.countBits(n=4))