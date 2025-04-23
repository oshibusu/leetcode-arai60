# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        check1 = check2 = head 
        while check1 and check1.next:
            if check1.next.next == check2.next:
                return True
            check1 = check1.next.next
            check2 = check2.next
        return False
    

'''
メモリ計算量O(n)の解法も思いついたが、それじゃないやり方があると思って考えていたが思い付かず、結局答えを見てしまった。
'''