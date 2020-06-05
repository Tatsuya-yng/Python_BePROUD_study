# -*- coding: UTF-8
#関数の中で変数を使う
#メール定型文の受信者名に任意の文字列を差し込む

def create_mail( recv, bill ) :
    tmp = '''{}様
PT企画の田中です。
今月の請求額は{}円です。
'''
    msg = tmp.format( recv, bill )
    print( msg )

create_mail( '山本',40000)
