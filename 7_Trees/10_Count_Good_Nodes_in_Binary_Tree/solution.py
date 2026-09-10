from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        if not root:
            return self.count
        else:
            self.prev = root.val

        def dfs(curr: TreeNode):
            # After backtracking, reset the prev to the former greatest
            if not curr:
                return

            old_val = self.prev

            if curr.val >= self.prev:
                self.count += 1
                self.prev = curr.val

            dfs(curr.left)
            dfs(curr.right)

            self.prev = old_val

        dfs(root)
        return self.count

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
    root = build_tree([2,1,1,3,None,1,5])
    root2 = build_tree([1,2,-1,3,4])
    root3 = build_tree([3,3,None,4,2])
    root4 = build_tree([2,None,4,10,8,None,None,4])

    print(print_tree(root=root))
    print(solution.goodNodes(root=root), end="\n\n")

    print(print_tree(root=root2))
    print(solution.goodNodes(root=root2), end="\n\n")

    print(print_tree(root=root3))
    print(solution.goodNodes(root=root3), end="\n\n")

    print(print_tree(root=root4))
    print(solution.goodNodes(root=root4), end="\n\n")