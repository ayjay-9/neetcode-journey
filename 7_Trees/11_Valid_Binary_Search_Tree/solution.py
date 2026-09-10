from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        q = deque([(float('-inf'), root, float('inf'))])
        while q:
            low, node, high = q.popleft()

            if not low < node.val < high:
                return False

            if node.left:
                q.append((low, node.left, node.val))
            if node.right:
                q.append((node.val, node.right, high))
        return True

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
    root = build_tree([2,1,3])
    root2 = build_tree([1,2,3])
    root3 = build_tree([5,4,6,None,None,3,7])
    root4 = build_tree([0,-1000,1000,None,None,0])

    print(print_tree(root=root))
    print(solution.isValidBST(root=root), end="\n\n")

    print(print_tree(root=root2))
    print(solution.isValidBST(root=root2), end="\n\n")

    print(print_tree(root=root3))
    print(solution.isValidBST(root=root3), end="\n\n")

    print(print_tree(root=root4))
    print(solution.isValidBST(root=root4), end="\n\n")