import logging
import requests
from django.conf import settings

logger = logging.getLogger(__name__)

LINE_API_URL = "https://api.line.me/v2/bot/message/push"
LINE_MESSAGE_TEMPLATE = """
新しい不足シフトが登録されました！

日付: {date}
時間: {starttime}~{endtime}
"""

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

    message = LINE_MESSAGE_TEMPLATE.format(
        date=post.date, starttime=post.starttime, endtime=post.endtime
    )
     
    data = {
        "to": group_id,
        "messages": [
            {"type": "text", "text": message},
        ],
    }

    try:
        response = requests.post(
            LINE_API_URL, headers=headers, json=data
        )
        response.raise_for_status()  # エラーがあれば例外を発生させる
    except requests.exceptions.RequestException as e:
        # エラー処理
        logger.error(f"LINE通知の送信に失敗しました: {e}")
