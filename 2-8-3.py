# -*- coding: UTF-8
#複数の比較式を組み合わせる
#not演算子を使ってFalseの時だけ実行する

text = input( '年齢は？' )
if not text.isdigit():
    print( '数値を入力して' )
