import math


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # Map point to their euclidian distance
        coorMap = {}
        for x,y in points:
            coorMap[(x,y)] = self.euclideanDistance([x,y], [0,0])
        coorMap = sorted(coorMap.items(), reverse=True, key=lambda item: item[1])
        res = [list(key[0]) for key in coorMap]
        while len(res) > k:
            res.remove(res[0])
        return res[0:]

    def euclideanDistance(self, coordinate1: list[int], coordinate2: list[int]) -> float:
        x = (coordinate1[0] - coordinate2[0])
        y = (coordinate1[1] - coordinate2[1])
        res = math.sqrt((x*x) + (y*y))
        return res

if __name__ == "__main__":
    solution = Solution()
    points, k = [[0,2],[2,2]], 1
    points2, k2 = [[0,2],[2,0],[2,2]], 2
    points3, k3 = [[1,3],[-2,2],[2,-2]], 2

    # print(solution.kClosest(points=points, k=k))
    # print(solution.kClosest(points=points2, k=k2))
    print(solution.kClosest(points=points3, k=k3))