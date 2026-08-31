# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        groupPrev = dummy = ListNode(0, head)
        while True:
            # walk k steps to find the group's last node; if we fall off, we're done
            kth = groupPrev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            groupNext = kth.next  # first node of the *next* group (exclusive boundary)

            # reverse [groupPrev.next .. kth]
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # reconnect
            newTail = groupPrev.next  # old head is now the tail
            groupPrev.next = kth  # kth is the new head of this group
            groupPrev = newTail  # tail becomes prev for the next

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
    while head is not None:
        values.append(head.val)
        head = head.next
    return values

if __name__ == "__main__":
    solution = Solution()
    head = build_linked_list([1,2,3,4,5,6])
    print(print_linked_list(head))
    print(print_linked_list(solution.reverseKGroup(head=head, k=3)))