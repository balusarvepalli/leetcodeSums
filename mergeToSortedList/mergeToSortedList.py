class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if not list1: return list2
        if not list2: return list2
        #listNode is to made the current node.
        current = ListNode(0)
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1: current.next = list1
        if list2: current.next = list2
            
        return current.next