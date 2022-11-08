# amazon-tracking-price

## 概要
登録したamazonの商品ページURLを定期的にスクレイピングして価格を追跡するアプリです。

> **Warning**
> 
> まだ未完成です

## 環境構築
> **Warning**
> 
> Macbook Air M1での動作環境になります。
> 
> 他のPC環境の場合、そのまま入力するだけでは動作しない場合がございます。

任意のフォルダで`git clone`後以下のコマンドを流してください。

1. `docker-compose up -d`
2. `docker compose exec web python manage.py makemigrations`
3. `docker compose exec web python manage.py migrate`
4. `docker compose exec web python manage.py createsuperuser`
5. `docker compose exec web sh`で仮想環境に入り、６を実行。
6. 
```
$ apt-get update
$ apt-get install firefox-esr-l10n-ja
```
> **Warning**
> 
> `firefox-esr-l10n-ja`のバージョンに注意してください。
> 
> 当方のバージョンは`102.4.0esr-1~deb11u1`です。
> 
> バージョンが異なる場合は`geckodriver`のバージョンを対応させる必要があります。
7. `docker-compose restart`
8. http://localhost:8810 にアクセス
