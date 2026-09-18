class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        strToNum = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }
        # Build the numbers
        n1, n2 = 0, 0
        for i in range(len(num1)):
            n1 *= 10
            n1 += strToNum[num1[i]]
        for i in range(len(num2)):
            n2 *= 10
            n2 += strToNum[num2[i]]

        # Multiply
        mul = n1*n2
        res = []
        numToStr = {
            0: "0",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
        }
        # Append digits to list
        while mul:
            res.append(numToStr[mul%10])
            mul //= 10

        ans = ""
        for num in range(len(res)-1, -1, -1):
            ans += res[num]
        return ans if ans else "0"

if __name__ == "__main__":
    solution = Solution()
    print(solution.multiply(num1="3", num2="4"))
    print(solution.multiply(num1="111", num2="222"))
    print(solution.multiply(num1="0", num2="0"))