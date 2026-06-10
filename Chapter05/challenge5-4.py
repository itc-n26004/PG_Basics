furits = {'height' : '173',
          'favoritecolor' : 'blue',
          'favoritemusic' : 'ミュージック'}
print(furits)

#ユーザーに入力してもらう
Key = input('favoritemusic')

#入力されたキーに対応するバリューを取得して表示
print(furits[Key])
