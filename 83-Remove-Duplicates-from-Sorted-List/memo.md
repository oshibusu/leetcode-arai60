
### 解法
- 例えば[1,1,1,2,2,2,3,4,5]みたいなinputがある時に、head.nextを1→2→3→4→5という流れになるように付け替えなければいけない

### コメント集

- nodchipさんのcurrentという単語は、previousやnextと対比することによって意味を持つ単語だから、currentを使うのは自然ではない、というコメントを発見。
確かにそう思う。
https://github.com/atomina1/Arai60_review/pull/2/files#r1890232755

- "先頭のノードがあればそこから全部たどれるので、linked list 全体と先頭のノードをそれほど区別せずに扱っています。それで混乱するということかと思います。"
これが最初わかっていなかったから、step1で解法を思いつくのに時間がかかった。
https://github.com/atomina1/Arai60_review/pull/2/files#r1891034401