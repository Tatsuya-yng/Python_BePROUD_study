# -*- coding: UTF-8
#年齢層を分析するプログラムを作ってみる
#義務教育期間の判定を追加する

text = input( '年齢は？' )
if text.isdigit():
    age = int( text )
    if age < 20 :
        if age >= 6 and age <= 15 :
            print( '未成年(義務教育)' )
        else:
            print( '未成年' )
    elif age < 65 :
        print( '成人' )
    else:
        print( '高齢者' )
