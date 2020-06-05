# -*- coding: UTF-8
#テキストファイルを読み込んで加工する
#読み込んだ文字列を置換する

rfile = open( 'sample.txt',encoding='utf-8' )
text = rfile.read()
rfile.close()
text = text.replace( '.','~♪' )
print( text )
