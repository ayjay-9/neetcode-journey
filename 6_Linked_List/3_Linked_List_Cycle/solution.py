# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        curr, nxt = head, head
        while curr:
            if nxt.next:
                if nxt.next.next is None:
                    break
                else:
                    nxt = nxt.next.next
            else:
                break
            curr = curr.next
            if nxt == curr:
                return True
        return False

def build_linked_list(values):
    head = None
    curr = None
    for val in values:
        node = ListNode(val)
        if head is None:
            head = node
            curr = node
        else:
            curr.next = node
            curr = node
    return head

def print_list(head) -> list:
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values

if __name__ == "__main__":
    solution = Solution()
    head = build_linked_list([1, 2, 3, 4])
    print(print_list(head))
    print(solution.hasCycle(head))