import requests
from django.conf import settings

def send_line_notification(post):
    """
    LINE通知を送信する関数
    """
    access_token = settings.LINE_CHANNEL_ACCESS_TOKEN
    group_id = settings.LINE_GROUP_ID

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    message = f"新しい不足シフトが登録されました！\n\n日付: {post.date}\n時間: {post.starttime.strftime('%H:%M')}~{post.endtime.strftime('%H:%M')}"
    
    data = {
        "to": group_id,
        "messages": [
            {"type": "text", "text": message},
        ],
    }

    try:
        response = requests.post(
            "https://api.line.me/v2/bot/message/push", headers=headers, json=data
        )
        response.raise_for_status()  # エラーがあれば例外を発生させる
    except requests.exceptions.RequestException as e:
        # エラー処理をログ出力などで行う
        print(f"LINE通知の送信に失敗しました: {e}")
