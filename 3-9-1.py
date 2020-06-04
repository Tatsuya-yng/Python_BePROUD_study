# -*- coding: UTF-8
#総当たり戦の表をつくる
#単純にすべての組み合わせを並べる

team = [ 'A', 'B','C','D','E' ]
for t1 in team :
    for t2 in team :
        print(t1, 'vs', t2 )
