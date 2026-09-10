# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return None
        res = [root.val]
        def dfs(curr: TreeNode) -> int:
            if not curr:
                return 0

            left_max, right_max = dfs(curr.left), dfs(curr.right)
            left_max, right_max = max(left_max, 0), max(right_max, 0)

            res[0] = max(res[0], curr.val+left_max+right_max)
            return curr.val + max(left_max, right_max)
        dfs(root)
        return res[0]

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
    root, root2 = build_tree([1,2,3]), build_tree([-15,10,20,None,None,15,5,-5])
    print(f"Max Path sum of {print_tree(root)} = {solution.maxPathSum(root=root)}", end="\n\n")
    print(f"Max Path sum of {print_tree(root2)} = {solution.maxPathSum(root=root2)}", end="\n\n")