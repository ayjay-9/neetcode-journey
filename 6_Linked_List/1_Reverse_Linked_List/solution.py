# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


def build_linked_list(values):
    head = None
    current = None
    for value in values:
        node = ListNode(value)
        if head is None:
            head = node
            current = node
        else:
            current.next = node
            current = node
    return head


def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)


if __name__ == "__main__":
    solution = Solution()
    head = build_linked_list([0, 1, 2, 3])
    print_linked_list(head)
    reversed_head = solution.reverseList(head)
    print_linked_list(reversed_head)
