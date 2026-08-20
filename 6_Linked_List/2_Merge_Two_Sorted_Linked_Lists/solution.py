# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        h1, h2 = list1, list2
        merged_list = ListNode()
        tail = merged_list
        while h1 or h2:
            if h1:
                if h2:
                    if h1.val <= h2.val:
                        tail.next = ListNode(h1.val)
                        h1 = h1.next
                    else:
                        tail.next = ListNode(h2.val)
                        h2 = h2.next
                else:
                    tail.next = ListNode(h1.val)
                    h1 = h1.next
            else:
                if h2:
                    tail.next = ListNode(h2.val)
                    h2 = h2.next
            tail = tail.next
        return merged_list.next

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
    list1 = build_linked_list([1,2,4])
    list2 = build_linked_list([1,3,5])
    print(print_list(list1))
    print(print_list(list2))
    merged_list = solution.mergeTwoLists(list1, list2)
    print(print_list(merged_list))