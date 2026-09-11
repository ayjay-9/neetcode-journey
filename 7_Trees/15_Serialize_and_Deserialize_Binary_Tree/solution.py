# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Encodes a tree to a single string.
    def serialize(self, root: TreeNode) -> str:
        if not root:
            return "None"

        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None

        values = iter(data.split(','))

        def build():
            val = next(values)
            if val == "None":
                return None

            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node
        return build()


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
    root, root2 = build_tree([1,2,3, None, None, 5]), build_tree([])
    s_root, s_root2 = solution.serialize(root=root), solution.serialize(root=root2)
    d_root, d_root2 = solution.deserialize(data=s_root), solution.deserialize(data=s_root2)

    print(f"Serialized {print_tree(root)} = '{s_root}' -> Deserialized '{s_root}' = {print_tree(d_root)}", end="\n\n")
    print(f"Serialized {print_tree(root2)} = '{s_root2}' -> Deserialized '{s_root2}' = {print_tree(d_root2)}", end="\n\n")