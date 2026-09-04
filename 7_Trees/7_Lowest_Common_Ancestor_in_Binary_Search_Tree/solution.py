# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Faster to find ancestors of descendants on the same side of the tree
        # Descendant can be the ancestor of itself
        self.lca = root
        if (p.val < root.val < q.val) or (q.val < root.val < p.val): # LCA is the immediate root
            return self.lca

        def dfs(curr: TreeNode) -> TreeNode:
            if not curr:
                return None
            if p.val < curr.val and q.val < curr.val: # LCA is on left, recurse the left
                dfs(curr.left)
            if p.val > curr.val and q.val > curr.val: # LCA is on right, recurse right
                dfs(curr.right)

            if (p.val < curr.val < q.val) or (q.val < curr.val < p.val): # The lca is the root
                self.lca = curr
                return self.lca
            if p.val == curr.val:
                self.lca = p
                return self.lca
            if q.val == curr.val:
                self.lca = q
                return self.lca

            return dfs(curr.left) or dfs(curr.right)
        dfs(root)
        return self.lca


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
    root, p, q, q2 = build_tree([5,3,8,1,4,7,9,None,2]), build_tree([3]), build_tree([8]), build_tree([4])
    root2, q3 = build_tree([2,1,3]), build_tree([1])

    print(print_tree(root=root))
    print(f"Lowest common ancestor of '{print_tree(root=p)}' and '{print_tree(root=q)}' in "
          f"{print_tree(root=root)} = {print_tree(solution.lowestCommonAncestor(root=root,p=p,q=q))}", end="\n\n")

    print(f"Lowest common ancestor of '{print_tree(root=p)}' and '{print_tree(root=q2)}' in "
          f"{print_tree(root=root)} = {print_tree(solution.lowestCommonAncestor(root=root, p=p, q=q2))}", end="\n\n")

    print(f"Lowest common ancestor of '{print_tree(root=p)}' and '{print_tree(root=q3)}' in "
          f"{print_tree(root=root2)} = {print_tree(solution.lowestCommonAncestor(root=root2, p=p, q=q3))}", end="\n\n")