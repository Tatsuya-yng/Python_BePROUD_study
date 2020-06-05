# -*- coding: UTF-8
#テキストファイルを読み込んで加工する
#テキストファイルを読み込んで内容を確認する

rfile = open( 'sample.txt',encoding='utf-8' )
text = rfile.read()
rfile.close()
print( text )
