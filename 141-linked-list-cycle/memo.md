```python
#step3.py
slow = fast = head
while fast and fast.next:
```
例えば input = [0,0,0,0,0] みたいな場合に、fastは常にFalse判定されるのではないかとも思ったが、ListNodeのインスタンスであるから val == 0 でもFalseとならないことを知った。

上記のままでもエラーは起きないが、ここは
```python
while fast is None and fast.next is None
```
と書く方が可読性が高いコードになるのか気になった。