import requests
import json

##定义存放tid值的文件
f = open('tid.txt', 'w+')

##基本信息
url = 'http://liuyan.people.com.cn/threads/queryThreadsList'
payload = {'fid': 539, 'lastItem': 5867215}   #修改fid的值即可获取相应的城市留言
header_info = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'Host': 'liuyan.people.com.cn',
    'Origin': 'http://liuyan.people.com.cn',
    'Connection': 'keep-alive',
    'Referer': 'http://liuyan.people.com.cn/threads/list?fid=539',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
}

##获取数据
def load_data():
    r = requests.post(url, data=payload, headers=header_info)
    data = json.loads(r.text)
    return data

lastItem = 5867215


##默认获取20*10条数据
for _ in range(20):
    i = 0
    payload['lastItem'] = lastItem
    data = load_data()
    for line in data['responseData']:
        i = i + 1
        f.write(str(line['tid']) + '\n')
        if i == 10 :
            lastItem = line['tid']
            break
