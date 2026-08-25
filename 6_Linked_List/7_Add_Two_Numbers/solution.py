# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_head, l2_head, list1, list2, total = l1, l2, [], [], 0
        num1, num2, list1_copy, list2_copy = "", "", [], []
        while l1_head:
            list1.append(l1_head.val)
            l1_head = l1_head.next

        while l2_head:
            list2.append(l2_head.val)
            l2_head = l2_head.next

        if list1:
            for i in range(len(list1)-1, -1, -1):
                list1_copy.append(list1[i])
        if list2:
            for i in range(len(list2)-1, -1, -1):
                list2_copy.append(list2[i])

        if list1_copy and list2_copy:
            for num in list1_copy:
                num1 += str(num)
            for num in list2_copy:
                num2 += str(num)
            total = int(num1) + int(num2)

        dummy, str_list = ListNode(0), str(total)
        sum_list = dummy
        if total >= 0:
            for i in range(len(str_list)-1, -1, -1):
                sum_list.next = ListNode(int(str_list[i]))
                sum_list = sum_list.next
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


def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)


if __name__ == "__main__":
    solution = Solution()
    l1 = build_linked_list([0])
    l2 = build_linked_list([0])
    print(print_linked_list(solution.addTwoNumbers(l1, l2)))
