# -*- coding: UTF-8
#数値が入力されたら計算する
#数字の時は計算する

text = input( '入力せよ' )
if text.isdigit():
    print( int( text ) * 1.08 )
