from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # Initialize the crs: prerequisite map
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visit = set()
        finished = set()
        order = []
        def dfs(crs):
            if crs in visit:
                return False
            if crs in finished:
                return True

            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visit.remove(crs)
            finished.add(crs)
            order.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs): return []
        return list(order)

if __name__ == "__main__":
    solution = Solution()
    numCourses, prerequisites = 3, [[1,0]]
    numCourses2, prerequisites2 = 3, [[0,1],[1,2],[2,0]]

    print(f"{prerequisites} -> {numCourses} == {solution.findOrder(numCourses=numCourses, prerequisites=prerequisites)}")
    print(f"{prerequisites2} -> {numCourses2} == {solution.findOrder(numCourses=numCourses2, prerequisites=prerequisites2)}")