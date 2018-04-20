#coding=utf-8

import requests 

url = "http://open.douyucdn.cn/api/RoomApi/live"
rsp = requests.get(url).json()
for room in rsp["data"]:
	print room["room_id"],room["room_name"]











