# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> ListNode:
        # General Reorder [0, n-1, 1, n-2, 2, n-3, ...]
        # Find the middle of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next # This will stop at the middle when fast gets to the end
            fast = fast.next.next

        # Reverse the second half of the list, node after middle (where slow stopped)
        second = slow.next # starts at the node immediately after middle
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Merge both halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        return head

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
    head1 = build_linked_list([2, 4, 6, 8])
    print(print_list(head1))
    print(print_list(solution.reorderList(head1)))
    head2 = build_linked_list([2, 4, 6, 8, 10])
    print(print_list(head2))
    print(print_list(solution.reorderList(head2)))