from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r: int, c: int):
            q = deque()
            visit.add((r,c)) # Show that you've visited the coordinates
            q.append((r,c)) # Enable the BFS/DFS since we're not using recursion
            while q:
                row, col = q.popleft() # If using DFS, use pop(), that's the only change for the entire solution
                directions = [[1,0], [-1,0], [0,1], [0,-1]] # [[Right], [Left], [Up], [Down]]
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r=r,c=c)
                    islands += 1
        return islands


if __name__ == "__main__":
    solution = Solution()
    grid = [
        ["0","1","1","1","0"],
        ["0","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]

    grid2 = [
        ["1", "1", "0", "0", "1"],
        ["1", "1", "0", "0", "1"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(solution.numIslands(grid=grid), end="\n\n")
    print(solution.numIslands(grid=grid2), end="\n\n")