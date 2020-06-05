# -*- coding: UTF-8
#スケジュール表のための日付一覧を作る
#日付け一覧に曜日も表示する

from datetime import date, timedelta
youbi = '月火水木金土日'
start = date(2018,6,18)
for d in range(14) :
    cur = start + timedelta( days=d )
    wd = cur.weekday()
    print( cur, youbi[wd] )
