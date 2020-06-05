# -*- coding: UTF-8
#関数を組合わせて使ってみよう
#データの数だけ関数を呼び出す

import chap4func
data = [
{'name':'山本','bill':40000,'crg':True},
{'name':'吉田','bill':25000,'crg':False}
]
for rec in data:
    bill = rec['bill']
    if rec['crg'] :
        bill = chap4func.add_charge(bill)
    chap4func.create_mail(rec['name'],bill)

