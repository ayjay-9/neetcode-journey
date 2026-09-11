# Definition for a Node.
from collections import deque


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return None
        oldToNew = {}

        def dfs(node: Node) -> Node:
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
        return dfs(node)

def build_graph(adj_list: list[list[int]]) -> Node | None:
    if not adj_list:
        return None

    nodes = {i + 1: Node(i + 1) for i in range(len(adj_list))}

    for val, neighbor_vals in enumerate(adj_list, start=1):
        nodes[val].neighbors = [nodes[nv] for nv in neighbor_vals]

    return nodes[1]


def print_graph(node: Node) -> None:
    if node is None:
        print("(empty graph)")
        return

    visited = {node.val: node}
    q = deque([node])

    while q:
        cur = q.popleft()
        neighbor_vals = [n.val for n in cur.neighbors]
        print(f"{cur.val}: {neighbor_vals}")
        for n in cur.neighbors:
            if n.val not in visited:
                visited[n.val] = n
                q.append(n)

if __name__ == "__main__":
    solution = Solution()
    adj_list, adj_list2, adj_list3 = [[2],[1,3],[2]], [[]], []
    graph, graph2, graph3 = build_graph(adj_list), build_graph(adj_list2), build_graph(adj_list3)

    print_graph(graph)
    print()
    print(f"{print_graph(solution.cloneGraph(node=graph))}", end="\n\n\n")

    print_graph(graph2)
    print()
    print(f"{print_graph(solution.cloneGraph(node=graph2))}", end="\n\n\n")

    print_graph(graph3)
    print(f"{print_graph(solution.cloneGraph(node=graph3))}", end="\n\n")
