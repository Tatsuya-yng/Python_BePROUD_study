# -*- coding: UTF-8
#繰り返し文を２つ組合わせて九九の表を作る
#九九らしく表示する

for cnt1 in range( 1, 10 ) :
    for cnt2 in range( 1, 10 ) :
        print( cnt1, '✖︎', cnt2, '=',
               cnt1 * cnt2 )
