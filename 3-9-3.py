# -*- coding: UTF-8
#総当たり戦の表をつくる
#同じ対戦組み合わせを省くには？

team = ['A','B','C','D','E' ]
opps = ['A','B','C','D','E' ]
for t1 in team :
    opps.remove(t1 )
    for t2 in opps:
        print( t1, 'vs', t2 )
