from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visit = set()

        def dfs(crs):
            if crs in visit:  # Cycle detected
                return False
            if preMap[crs] == []:  # Course has no prerequisites and can be completed
                return True

            visit.add(crs)  # Since it's not already there
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visit.remove(crs)  # Avoid visiting same one again
            preMap[crs] = []  # Course can be completed
            return True  # So return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True

if __name__ == "__main__":
    solution = Solution()
    numCourses, prerequisites = 2, [[0,1]]
    numCourses2, prerequisites2 = 2, [[0,1], [1,0]]

    print(f"{prerequisites} -> {numCourses} == {solution.canFinish(numCourses=numCourses, prerequisites=prerequisites)}")
    print(f"{prerequisites2} -> {numCourses2} == {solution.canFinish(numCourses=numCourses2, prerequisites=prerequisites2)}")