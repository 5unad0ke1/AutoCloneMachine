import requests

class WebhookAPI:

    WEBHOOK_URL = "https://discord.com/api/webhooks/1433807224970412172/LPO-ysGm6-oYaXCXP5wRAyIcML1mLLvgV9Ezn2PSR0kjjL2O8T5gnYwwpFjJS1ed7o3a"
    AVATAR_URL = "https://cdn.discordapp.com/attachments/1414959083542286341/1433809515580751942/easy-peasy_7qpGEDcJol.png?ex=69060aab&is=6904b92b&hm=6a132bd11250883cc4d3f3c9919cea2e2dcef6da87b3a21d6cd2f10f997fa04e&"

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
