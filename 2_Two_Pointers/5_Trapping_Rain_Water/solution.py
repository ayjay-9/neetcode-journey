class Solution:
    def trap(self, height: list[int]) -> int:
        # Distance between l_pointer and r_pointer should be at least 2
        l_index = 0
        r_index = l_index+2
        max_vol, vol, temp = 0, 0, 0

        # if r_height >= l_height, that is the total volume... Move both pointers
        # else move the right pointer 1 place
        for i in range(r_index-1, len(height)-1):
            l_pointer, r_pointer = height[l_index], height[r_index]
            if l_pointer <= r_pointer:
                vol = min(l_pointer, r_pointer) - height[i]
            else:
                vol = l_pointer - height[i]
            if vol > 0:
                temp += vol
            if r_pointer >= l_pointer:
                max_vol += temp # don't update/reset unless there is an equal or higher height
                temp = 0
                l_index = r_index - 1
                r_index = l_index+2
            else:
                r_index += 1
        return max_vol

if __name__ == "__main__":
    solution = Solution()
    print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))