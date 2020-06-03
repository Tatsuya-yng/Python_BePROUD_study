# -*- coding: UTF-8
#条件分岐の中に条件分岐をかく
#２つのif文を組み合わせる

text = input( '年齢は?' )
if text.isdigit():
    age = int( text )
    if age < 20 :
        print( '未成年' )
