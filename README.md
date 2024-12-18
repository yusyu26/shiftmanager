# シフト管理アプリケーション

## 概要
シフト管理アプリケーションは、不足シフトの現在の状況、簡単に不足シフトの登録、不足シフトへの参加申請を可能にするWebアプリケーションです。

---

## 主な機能
- **不足シフトの一覧表示**: 不足シフトを日付順に並べ、過去のものは表示しないように設定
- **不足シフトの登録機能**: カレンダーから日付の選択が行え、簡単に不足シフトの登録が可能
- **埋まったシフトの一覧表示**: 不足シフトに交代者が現れた場合こちらのリストに移動。埋まったシフトに対して交代を申請できないようにボタンを押せなくした。また、URLからアクセスしてもアクセスできないようにした。

---

## 使用技術
- **フレームワーク**: Django
- **データベース**: PostgreSQL
- **フロントエンド**: HTML, CSS, JavaScript
- **バックエンド**: Python
---


## 今後の展望
- **カレンダー表示機能の作成**
- **LINE通知機能の作成**
