# mysql_ju_nicegui
MySQLとjupyterlabとniceguiをセットにしたdocker-composeです

## 使い方
niceguiのアクセス方法
```
localhost:80
```
- main.pyにniceguiのコードを書いて保存すると、localhost:80がブラウザで自動更新されてアプリのGUIが見れます。
アプリの作り方は、公式ページhttps://nicegui.io/をご参照ください。

###　フォルダ構成
```
mysql_ju_nicegui
├── db => (MySQLのデータ保存場所)
├── work => （jupyterlabのコードを保存する場所）
├── main.py => （ここに、niceguiのコードを書いてください。）
└── docker-compose.yml
```
- ターミナルで下記のコードを実行
```
git clone https://github.com/keikois/mysql_ju_nicegui.git
```
```
cd mysql_ju_nicegui
```
```
docker-compose up -d
```

- localhost:8888でjupyterlabが起動
- localhost:8080でphpMyAdminが起動
- localhost:80でniceguiが起動

- docker-compose down　でdocker-composeを終了できます。

## git cloneが終ったら
git cloneが終ったら、リモートリポジトリを削除するコマンドを使ってください。

Git のリモートリポジトリを削除するコマンド
```
git remote rm origin 
```
Gitのリモートリポジトリを確認するコマンド
- 何も書かれていないことを確認してください。
```
git remote -v 
```
