# -*- coding: UTF-8
#テキストファイルを読み込んで加工する
#置換後の文字列を保存する

rfile = open( 'sample.txt',encoding='utf-8' )
text = rfile.read()
rfile.close()
text = text.replace( '. ', '~♪' )
print( text )
wfile = open( 'output.txt' ,mode='w',encoding='utf-8')
wfile.write( text )
wfile.close()
