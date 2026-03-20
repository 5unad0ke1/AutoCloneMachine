import os
import requests
from dotenv import load_dotenv

load_dotenv()

class WebhookAPI:

    WEBHOOK_URL = os.getenv("WEBHOOK_URL")
    AVATAR_URL = os.getenv("AVATAR_URL")

    @staticmethod
    def send_message(message: str):
        payload = {
                "username": "白カラスちゃん",
                "avatar_url" : WebhookAPI.AVATAR_URL,
                "content": "# 通知だよ～みて～\n```" + message + "```"
                }
        
        result = requests.post(WebhookAPI.WEBHOOK_URL, json=payload)
        if result.status_code == 204:
            print("✅ 通知成功")
        else:
            print(f"⚠️ 通知失敗: {result.status_code}, {result.text}")
    
    @staticmethod
    def send_test():
        WebhookAPI.send_message("🔔 Pythonから通知テスト！")
