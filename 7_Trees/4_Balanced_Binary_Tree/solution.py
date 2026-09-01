# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # Height(Left) - Height(Right) = [-1,0,1]
        self.res = True
        if not root:
            return self.res
        def dfs(curr: TreeNode) -> int:
            if not curr:
                return 0 # left and right subtrees are naturally 0
            # Find the heights of the subtrees
            left, right = dfs(curr.left), dfs(curr.right)
            if abs(left - right) > 1:
                self.res = False
            return 1 + max(left,right) # Return the height
        dfs(root)
        return self.res

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
    root = build_tree([[1,2,3,None,None,4]])
    root2 = build_tree([1,2,3,None,None,4,None,5])
    root3 = build_tree([])

    print(print_tree(root))
    print(solution.isBalanced(root))

    print(print_tree(root2))
    print(solution.isBalanced(root2))

    print(print_tree(root3))
    print(solution.isBalanced(root3))
