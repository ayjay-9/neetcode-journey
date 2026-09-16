class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = (res << 1) | (n&1)
            n >>= 1
        return bin(res)

if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseBits(n=0b00000000000000000000000000010101))