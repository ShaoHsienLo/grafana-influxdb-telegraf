import paho.mqtt.client as mqtt
import random
import json
import datetime
import time

# 設置日期時間的格式
ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S'

# 連線設定
# 初始化地端程式
# client = mqtt.Client(transport='websockets')
client = mqtt.Client()

# 設定登入帳號密碼
client.username_pw_set("iii", "iii05076416")

# 設定連線資訊(IP, Port, 連線時間)
client.connect("192.168.1.85", 1883, 60)

while True:
    # 發布的內容
    # 需包含：
    # 1. time: timestamp
    # 2. tags: topic
    # 3. field: current, score
    payload = {
        'timestamp': datetime.datetime.now().timestamp(),
        'topic': 'sensors',
        'current': round(random.uniform(0, 10), 2),
        'score': round(random.uniform(50, 100), 0)
    }
    print(json.dumps(payload))
    # 要發布的主題和內容
    client.publish("mytopic", json.dumps(payload))
    time.sleep(1)
