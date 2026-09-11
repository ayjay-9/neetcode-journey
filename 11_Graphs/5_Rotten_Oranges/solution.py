from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # All fruits must get rotten, else return -1
        if not grid:
            return -1

        rows, cols = len(grid), len(grid[0])
        fruits = 0
        self.rotten = 0
        visit = set()
        q = deque()
        self.minutes = 0 # Then track how long it will take rotten to equal fruits

        # Find the total number of fruits and rotten fruits
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    fruits += 1
                if grid[r][c] == 2:
                    self.rotten += 1 # Should be equal to fruits at the end
                    visit.add((r,c)) # Pre-add the coordinates of the rotten fruits, so they can rot others in parallel
                    q.append((r,c))

        while q:
            size = len(q)
            converted = False
            for _ in range(size):
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    newr, newc = row+dr, col+dc
                    if (newr in range(rows) and
                        newc in range(cols) and
                        grid[newr][newc] == 1 and
                        (newr,newc) not in visit):
                        grid[newr][newc] = 2 # The horizontally and vertically adjacent fruits become rotten
                        q.append((newr,newc))
                        visit.add((newr,newc))
                        self.rotten += 1
                        converted = True
            if converted:
                self.minutes += 1

        if self.rotten != fruits:
            return -1
        else:
            return self.minutes

if __name__ == "__main__":
    solution = Solution()
    grid, grid2 = [[1,1,0],[0,1,1],[0,1,2]], [[1,0,1],[0,2,0],[1,0,1]]

    print(f"{grid} takes {solution.orangesRotting(grid=grid)} minutes for all fruits to get rotten", end="\n\n")
    print(f"{grid2} takes {solution.orangesRotting(grid=grid2)} minutes for all fruits to get rotten", end="\n\n")