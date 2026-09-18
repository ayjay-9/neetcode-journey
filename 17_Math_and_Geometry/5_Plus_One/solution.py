class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = ""
        for n in digits:
            num += str(n)
        num = str(int(num)+1)
        res = []
        for n in num:
            res.append(int(n))
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.plusOne(digits=[1,2,3,4]))
    print(solution.plusOne(digits=[9,9,9]))
