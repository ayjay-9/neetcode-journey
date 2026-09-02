# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        self.equal = True # Default is no root, so no children
        # If both don't have a root
        if not p and not q:
            return self.equal
        # If either doesn't have a root, then they are unequal
        if (p and not q) or (not p and q):
            return False
        # Check if subtrees on left and right are the same
        def dfs(p_curr: TreeNode, q_curr: TreeNode) -> bool:
            if not p_curr and not q_curr: # If both are Null, they are equal
                self.equal = True
                return self.equal
            if (not p_curr and q_curr) or (p_curr and not q_curr): # If either one of them is Null, they are not equal
                self.equal = False
                return self.equal
            if p_curr.val != q_curr.val: # If Nodes don't have the same number, they are not equal
                self.equal = False
                return self.equal

            left, right = dfs(p_curr.left, q_curr.left), dfs(p_curr.right, q_curr.right)

            if not left or not right:
                self.equal = False

            return p_curr.val == q_curr.val
        dfs(p, q)
        return self.equal

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
    # p1 = build_tree([1,2,3])
    # q1 = build_tree([1,2,3])
    #
    # p2 = build_tree([4,7])
    # q2 = build_tree([4,None,7])
    #
    # p3 = build_tree([1,2,3])
    # q3 = build_tree([1,3,2])
    #
    # print(f"{print_tree(p1)} == {print_tree(q1)} ? '{solution.isSameTree(p=p1,q=q1)}'", end="\n\n")
    #
    # print(f"{print_tree(p2)} == {print_tree(q2)} ? '{solution.isSameTree(p=p2,q=q2)}'", end="\n\n")
    #
    # print(f"{print_tree(p3)} == {print_tree(q3)} ? '{solution.isSameTree(p=p3,q=q3)}'")

