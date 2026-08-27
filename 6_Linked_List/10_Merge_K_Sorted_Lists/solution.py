# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        if not lists or len(lists) < 1:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedLists.append(self.mergeLists(l1,l2))
            lists = mergedLists
        return lists[0]

    def mergeLists(self, l1, l2) -> ListNode:
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
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