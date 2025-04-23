# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        else:
            return None
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
    
'''
while A:
    B
    if C
        break
else:
    return Y

こういう書き方ができるのが美しいと思った。同様の書き方で、for文でno break occuredの時でも、else clauseがexcuteされる。
whileではA(loop's condition)がfalseになったらelse clauseは当然executeされない
forでは、for文が回り切ったら、else clauseはexecuteされない

書いてみて思ったが、
while
'''