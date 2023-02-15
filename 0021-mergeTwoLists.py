# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        sentinel = ListNode(-1)
        new_head = sentinel
        while list1 and list2:
            if list1.val <= list2.val:
                new_head.next = list1
                list1 = list1.next
            else:
                new_head.next = list2
                list2 = list2.next
            new_head = new_head.next
        if list1:
            new_head.next = list1
        elif list2:
            new_head.next = list2
        return sentinel.next
