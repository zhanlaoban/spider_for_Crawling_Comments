# spider_for_Crawling_Comments
基于Scrapy的爬虫，爬取 地方领导留言网 “http://liuyan.people.com.cn" 中的留言内容。

# Environment：
```pip install scrapy```

# Usage:
1. 找到你想要爬取的有关某个城市的留言，这里以北京市为例：http://liuyan.people.com.cn/threads/list?fid=539
2. 记下fid为539，写入get_tid.py中的fid值处；可以修改get_tid.py中最外层for循环中的循环次数，这里默认为20；默认爬取20*10条数据，10是不可控的
3. 运行以下命令：  
```python get_tid.py```  
在当前文件夹下得到tid.txt
4. 将上面得到的tid.txt拷贝到tutorial/tutorial/spiders下，与comments_spider.py处于同一目录下
5. 到根目录下，运行以下命令：  
```scrapy crawl comments -o commmets.csv```  
即可得到名为comments.csv的留言内容

# YOU CAN CONTACT ME IF YOU HAVE ANY QUESTIONS ABOUT THIS REPO.
