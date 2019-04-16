f = open('tid.txt')

pre_url = 'http://liuyan.people.com.cn/threads/content?tid='
start_urls = []


f = open('tid.txt')
for line in f.readlines():
    tid = line[: -1]
    url = pre_url + tid
    start_urls.append(url)

print(start_urls)
