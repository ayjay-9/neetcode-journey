class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Window size is fixed as the length of s1
        left = 0
        check = sorted(list(s1))
        for right in range(len(s1)-1, len(s2)):
            sublist = sorted(list(s2[left:right+1]))
            if check == sublist:
                return True
            else:
                left += 1
        return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.checkInclusion("abc", "lecaabee"))