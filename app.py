import re
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('onf/Lo48/NJxUwWrcoLlAMOXBeYA25ITIsfGe5jJJ0ZCEcFHqYYFQXgH1RAigpnZ3W8mxbLr7axZOh35HJ5CXae3AfanM1o3YAEHjNa1K42EFfVnrl9ywrsNf2KNSYybjtHRyKYzRaA0HK9uRbXa2QdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('066873c2ab34f0f9926ddd92fdf92cdd')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    print("Huan debug== Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

   message = event.message.text

   if re.match("你是誰",message):
       line_bot_api.reply_message(event.reply_token,TextSendMessage("才不告訴你勒~~"))
   else:
        line_bot_api.reply_message(event.reply_token,text="You said: "+TextSendMessage(message))
 
   

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
