# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prev, slow, nxt, index = None, head, head,  0
        while slow and slow.next:
            nxt = nxt.next
            if index == n: # Update the pointers
                prev.next = nxt
                slow.next = None # Break the link at the node to be removed
                break
            prev = slow
            slow = slow.next
            index += 1
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
    head1 = build_linked_list([5])
    print(print_list(head1))
    print(print_list(solution.removeNthFromEnd(head=head1, n=1)))