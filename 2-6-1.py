# -*- coding: UTF-8
#3段階以上に分岐させる
#elif節の書き方を覚える

text = input( '年齢は？' )
age = int( text )
if age < 20 :
    print( '未成年' )
elif age < 65 :
    print( '成人' )
else:
    print( '高齢者' )
