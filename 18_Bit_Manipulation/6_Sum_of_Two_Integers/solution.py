class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF # Simulate a 32-bit signed integer (32 binary 1's), range: -2,147,483,648 to 2,147,483,647
        max_int = 0x7FFFFFFF # 2,147,483,647

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        return a if a <= max_int else ~(a ^ mask)

if __name__ == "__main__":
    solution = Solution()
    print(solution.getSum(a=-1, b=1))
    print(solution.getSum(a=4, b=7))