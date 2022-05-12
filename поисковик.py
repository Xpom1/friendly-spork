# Парсер новых предметов
import json
import requests
import time

predmeti = []
a = set((json.loads(requests.get("https://market.csgo.com/api/v2/prices/class_instance/RUB.json").text.replace('null', '0'))).get('items').keys())
while True:
    time.sleep(10)
    b = set((json.loads(requests.get("https://market.csgo.com/api/v2/prices/class_instance/RUB.json").text.replace('null', '0'))).get('items').keys())
    if len(list(b - a)) > 0:
        q = list(b - a)
        predmeti = q.copy()
    a = b.copy()
    b.clear()
    print(predmeti)