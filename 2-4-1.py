# -*- coding: UTF-8
#数値が入力されていない時に警告する
#else節を追加してみる

text = input( '入力せよ' )
if text.isdigit():
    print( int( text ) * 1.08 )
else:
    print( '数字ではない' )
