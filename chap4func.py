# -*- coding: UTF-8
#関数を組合わせて使ってみよう
#モジュールを作る
#4-3-1.py+4-4-1.pyをコピー


def create_mail( recv, bill ) :
    tmp = '''{}様
PT企画の田中です。
今月の請求額は{}円です。
'''
    msg = tmp.format( recv, bill )
    print( msg )

def add_charge( bill ) :
    return int( bill * 1.07 )
