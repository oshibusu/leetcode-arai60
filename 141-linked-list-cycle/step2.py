# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        check1 = check2 = head 
        while check1 and check1.next:
            check1 = check1.next.next
            check2 = check2.next
            if check1 == check2:
                return True
        return False