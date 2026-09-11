from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0
        self.max_area = 0

        def bfs(r:int, c:int):
            area = 0
            q = deque()
            visit.add((r,c))
            q.append((r,c))
            area += 1
            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    newr, newc = row+dr, col+dc
                    if (newr in range(rows) and
                        newc in range(cols) and
                        grid[newr][newc] == 1 and
                        (newr,newc) not in visit):
                        q.append((newr,newc))
                        visit.add((newr,newc))
                        area += 1
            self.max_area = max(self.max_area, area)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    bfs(r=r,c=c)
                    islands += 1 # Within each island, count the number of 1's and update the max_area
        return self.max_area

if __name__ == "__main__":
    solution = Solution()
    grid = [
        [0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [0, 1, 1, 0, 1],
        [0, 1, 0, 0, 1]
    ]
    print(solution.maxAreaOfIsland(grid=grid), end="\n\n")