# -*- coding: UTF-8
#年齢層を分析するプログラムを作ってみる
#数字のみ判定のブロック内に３段階の判定を書く

text = input( '年齢は?' )
if text.isdigit():
    age = int( text )
    if age < 20 :
        print( '未成年' )
    elif age < 65 :
        print( '成人' )
    else:
        print( '高齢者' )
