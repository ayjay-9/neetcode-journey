from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        q = deque([root])
        right = []
        # I need to track both left and right, and once right is no longer visible, add left
        while q:
            level_size = len(q)
            for i in range(level_size):
                node = q.popleft()
                if i == level_size-1:
                    right.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return right

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
    root = build_tree([1,2,3,None,4,None,5])
    root2 = build_tree([1,2,3,4,None,None,None,5])
    root3 = build_tree([])

    print(print_tree(root=root))
    print(solution.rightSideView(root=root), end="\n\n")

    print(print_tree(root=root2))
    print(solution.rightSideView(root=root2), end="\n\n")

    print(print_tree(root=root3))
    print(solution.rightSideView(root=root3))