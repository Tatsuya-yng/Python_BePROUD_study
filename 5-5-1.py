# -*- coding: UTF-8
#特定の文字列の出現数を調べてみる
#・フォルダ内のファイル一覧を取得する

from pathlib import Path
path = Path()
for filepath in path.glob( '*.py' ) :
    print( filepath )
