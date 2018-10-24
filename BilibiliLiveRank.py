# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 10:49:36 2018

@author: fuwen
"""
import requests,re,time,json,datetime,pytz

url = 'https://api.live.bilibili.com/room/v1/Area/getRoomList?actionKey=appkey&appkey=1d8b6e7d45233436&area_id=0&build=5322000&cate_id=0&device=android&mobi_app=android&page=1&page_size=30&parent_area_id=0&platform=android&sort_type=online&ts=1540134793&sign=fdf7bdac2e163385c2f1b410d5df7fa8'
with open('BilibiliLiveRank.csv','a') as f :
    f.writelines(['name',',','type',',','value',',','date','\n'])

while True:
    LiveJson = requests.get(url).text
    LiveRoomList = json.loads(LiveJson)['data']
    now_time = datetime.datetime.fromtimestamp(int(time.time()), pytz.timezone('Asia/Shanghai')).strftime('%m月%d日 %H时%M分')
    now = now_time.encode(encoding='UTF-8',errors='strict').decode('UTF-8')
    for LiveRoom in LiveRoomList:
        area = LiveRoom['area_v2_parent_name'] +'-'+ LiveRoom['area_name']
        uname = LiveRoom['uname']
        online = LiveRoom['online']
        with open('BilibiliLiveRank.csv','a') as f:
            f.writelines([uname,',',area,',',str(online),',',now,'\n'])
    print(now,uname)
    time.sleep(60)
