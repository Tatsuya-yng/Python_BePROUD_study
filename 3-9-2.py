# -*- coding: UTF-8
#総当たり戦の表をつくる
#同じチーム同士の対戦を除く

team = [ 'A','B','C','D','E' ]
for t1 in team :
    for t2 in team :
        if t1 != t2 :
            print( t1, 'vs', t2 )
