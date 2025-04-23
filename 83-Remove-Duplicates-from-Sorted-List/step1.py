# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        current = head
        while current is not None and current.next is not None:
            if current.val == current.next.val: 
                current.next = current.next.next
            else:
                current = current.next
        return head

'''
current.nextを付け替えていくというところを思いつくのにかなり時間がかかった。
時間がかかった理由としては、どこを出力すればいいかよくわかっていなかったため。

この問題を解いて、よりLinked Listの構造への理解が深まったように思う。
どのような出力が欲しいのか、というところから逆算して考えなければいけないなと思った。(今回であれば、Linked Listの先頭のNode)
何度かエラーが出た。elseのところの文を忘れてしまったり。whileが永遠に回ってしまうのは防がないといけない、という意識が自分に足りていない。

'''