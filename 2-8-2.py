# -*- coding: UTF-8
#複数の比較式を組み合わせる
#幼児と高齢者だけを対象にする

text = input( '年齢は?' )
age = int( text )
if age <= 5 or age >= 65 :
    print( '幼児と高齢者' )
