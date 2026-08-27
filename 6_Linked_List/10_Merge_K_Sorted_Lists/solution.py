# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        if not lists or len(lists) < 1:
            return None

        values = []
        for head in lists:
            while head is not None:
                values.append(head.val)
                head = head.next
        values.sort()

        dummy = ListNode()
        tail = dummy
        for value in values:
            tail.next = ListNode(value)
            tail = tail.next
        return dummy.next


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


def print_linked_lists(head):
    all_lists = []
    for head in lists:
        values = []
        while head is not None:
            values.append(head.val)
            head = head.next
        all_lists.append(values)
    return all_lists

def print_linked_list(head):
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values

if __name__ == "__main__":
    solution = Solution()
    list1 = build_linked_list([1,2,4])
    list2 = build_linked_list([1,3,5])
    list3 = build_linked_list([3,6])
    lists = [list1, list2, list3]
    print(print_linked_lists(lists))
    print(print_linked_list(solution.mergeKLists(lists)))