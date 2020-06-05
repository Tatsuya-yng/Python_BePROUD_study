# -*- coding: UTF-8
#スケジュール表のための日付一覧を作る
#二週間分の日付けの一覧を作る

from datetime import date, timedelta
start = date( 2020,1,1 )
for d in range(366):
    cur = start + timedelta( days=d )
    print( cur )
