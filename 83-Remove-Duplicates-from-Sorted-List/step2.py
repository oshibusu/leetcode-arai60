# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current is not None and current.next is not None:
            while current.next is not None and current.val == current.next.val:
                current.next = current.next.next
            current = current.next
        return head

'''
他の方の解法やコメントを読んで、どこをどうすれば綺麗になるのか考える。
odaさんのコメントを見てよりシンプルな書き方を見つけたのでそれを試してみた
'NoneType' object has no attribute valというエラーが出てしまった。while文の中のwhile文できちんと、current.next is not Noneであることを確認するべき。
このwhile分の作業は、group, filter, concatであるとのこと。
'''