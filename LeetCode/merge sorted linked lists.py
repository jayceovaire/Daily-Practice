class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            node_head = list1
            node_tail = self.mergeTwoLists(list1.next, list2)
        else:
            node_head = list2
            node_tail = self.mergeTwoLists(list1, list2.next)

        node_head.next = node_tail
        return node_head

