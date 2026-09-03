# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def dfs(root):
            if not root:
                return "#"

            return (
                    "," + str(root.val) +
                    dfs(root.left) +
                    dfs(root.right)
            )

        return dfs(subRoot) in dfs(root) # E.g dfs(root) is (,1,2,4##,5##,3##) and dfs(subroot) is (,2,4##,5##)
        # So subroot is in root
        # Ex2: dfs(root) is (,1,2,4,6###,5##,3##) and dfs(subroot) is (,2,4##,5##)
def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        current = queue.popleft()
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    return root


def print_tree(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        current = queue.popleft()
        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


if __name__ == "__main__":
    solution = Solution()
    root = build_tree([1,2,3,4,5])
    subroot = build_tree([2,4,5])

    root2 = build_tree([1,2,3,4,5,None,None,6])
    subroot2 = build_tree([2,4,5])

    print(f"{print_tree(subroot)} is a subroot of {print_tree(root)} ? '{solution.isSubtree(root=root, subRoot=subroot)}'", end="\n\n")
    print(f"{print_tree(subroot2)} is a subroot of {print_tree(root2)} ? '{solution.isSubtree(root=root2, subRoot=subroot2)}'", end="\n\n")

