from math import ceil


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        min_speed, max_speed = 1, max(piles)
        min_rate = 0
        while min_speed <= max_speed:
            mid = (min_speed+max_speed) // 2
            rate = mid
            total = sum([ceil(num/rate) for num in piles])
            if total <= h: # Try smaller speed
                min_rate = mid
                max_speed = mid - 1
            else: # Try higher speed
                min_speed = mid + 1
        return min_rate
if __name__ == "__main__":
    solution = Solution()
    print(solution.minEatingSpeed(piles=[25,10,23,4], h=4))