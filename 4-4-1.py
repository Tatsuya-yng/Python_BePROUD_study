# -*- coding: UTF-8
#戻り値を返す関数を作る
#関数の実行結果の値を返すreturn文

def add_charge( bill ) :
    return int( bill * 1.07 )

print( add_charge(40000))
