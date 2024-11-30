# シフト管理アプリケーション

## 概要
シフト管理アプリケーションは、アルバイトスタッフや管理者が簡単にシフトを管理できるウェブアプリケーションです。シフトの提出、承認、スケジュールの確認が行えます。

---

## 主な機能
- **不足シフトの一覧表示**: 不足シフトを日付順に並べ、過去のものは表示しないように設定
- **不足シフトの登録機能**: カレンダーから日付の選択が行え、簡単に不足シフトの登録が可能
- **埋まったシフトの一覧表示**: 不足シフトに交代者が現れた場合、交代希望者が二重で交代を申請できないようにボタンを押せなくした。URLからアクセスしてもアクセスできないようにした。

---

## 使用技術
- **フレームワーク**: Django
- **データベース**: SQLite
- **フロントエンド**: HTML, CSS, JavaScript
- **バックエンド**: Python
---

## 起動方法
1. リポジトリをクローン:
    ```bash
    git clone https://github.com/your-username/shift-management-app.git
    cd shift-management-app
    ```

2. 仮想環境を作成して有効化:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
    ```

3. 必要なパッケージをインストール:
    ```bash
    pip install -r requirements.txt
    ```

4. マイグレーションを実行:
    ```bash
    python manage.py migrate
    ```

5. サーバーを起動:
    ```bash
    python manage.py runserver
    ```

6. ブラウザでアクセス:  
   `http://127.0.0.1:8000/`

---

## 今後の展望
- **カレンダー表示機能の作成**
- - ****: Django
