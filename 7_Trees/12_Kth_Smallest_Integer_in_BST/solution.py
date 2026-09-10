from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
           return None

        q = deque([root])
        stack = [root.val]
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    stack.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    stack.append(node.right.val)
        stack.sort()
        return stack[k-1]

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
    root, k = build_tree([2,1,3]), 1
    root2, k2 = build_tree([4,3,5,2,None]), 4
    # root3 = build_tree([5,4,6,None,None,3,7])
    # root4 = build_tree([0,-1000,1000,None,None,0])

    print(print_tree(root=root))
    print(solution.kthSmallest(root=root, k=k), end="\n\n")

    print(print_tree(root=root2))
    print(solution.kthSmallest(root=root2, k=k2), end="\n\n")

    # print(print_tree(root=root3))
    # print(solution.isValidBST(root=root3), end="\n\n")
    #
    # print(print_tree(root=root4))
    # print(solution.isValidBST(root=root4), end="\n\n")