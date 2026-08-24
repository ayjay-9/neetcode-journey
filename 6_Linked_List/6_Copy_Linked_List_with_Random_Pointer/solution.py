# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def __init__(self):
        self.map = {}
    def copyRandomList(self, head: Node) -> Node:
        if head is None:
            return None
        if head in self.map:
            return self.map[head]

        copy = Node(head.val)
        self.map[head] = copy
        copy.next = self.copyRandomList(head.next)
        copy.random = self.map.get(head.random)
        return copy

def build_linked_list(values):
    if not values:
        return None
    nodes = []
    # First pass: create all nodes
    for val, random_index in values:
        nodes.append(Node(val))
    # Second pass: connect next and random pointers
    for i, item in enumerate(values):
        val, random_index = item
        if i + 1 < len(nodes):
            nodes[i].next = nodes[i + 1]
        if random_index is not None:
            nodes[i].random = nodes[random_index]
    return nodes[0]

def print_list(head) -> list:
    nodes = []
    index_map = {}
    curr = head
    index = 0
    # First pass: collect nodes and remember each node's index
    while curr is not None:
        nodes.append(curr)
        index_map[curr] = index
        curr = curr.next
        index += 1
    result = []
    # Second pass: convert nodes back into [val, random_index]
    for node in nodes:
        if node.random is None:
            random_index = None
        else:
            random_index = index_map[node.random]

        result.append([node.val, random_index])
    return result

if __name__ == "__main__":
    solution = Solution()
    head1 = build_linked_list([[3,None], [7,3], [4,0], [5,1]])
    print(print_list(head1))
    print(print_list(solution.copyRandomList(head=head1)))