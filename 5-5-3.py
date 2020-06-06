# -*- coding: UTF-8
#特定の文字列の出現数を調べてみる
#複数のキーワードの出現数の合計を求められるようにする

from pathlib import Path
terms = { 'for':0, 'if':0, 'else':0 }
path = Path()
for filepath in path.glob( '*.py' ):
    rfile = open( filepath,encoding='utf-8' )
    text = rfile.read()
    rfile.close()
    for term in terms:
        cnt = text.count( term )
        terms[term] += cnt
print( terms )
