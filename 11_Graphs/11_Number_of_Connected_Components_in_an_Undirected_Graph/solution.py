class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        conMap = {i: [] for i in range(n)}
        for ai, bi in edges:
            conMap[ai].append(bi)
            conMap[bi].append(ai)  # undirected -> record both directions

        visit = set()

        def dfs(node): # If faced with runtime error, it's because of Stack Overflow, replace recursive logic with stack, like q=deque() loop
            if node in visit:
                return
            visit.add(node)
            for neighbor in conMap[node]:
                dfs(neighbor)

        count = 0
        for node in range(n):
            if node not in visit:
                count += 1  # found the root of a brand-new component
                dfs(node)  # mark everything reachable from it
        return count

if __name__ == "__main__":
    solution = Solution()

    n, edges = 5, [[0,1],[1,2],[3,4]]
    n2, edges2 = 5, [[0,1],[1,2],[2,3],[3,4]]

    print(f"{edges} == {solution.countComponents(n=n, edges=edges)}")
    print(f"{edges2} == {solution.countComponents(n=n2, edges=edges2)}")
