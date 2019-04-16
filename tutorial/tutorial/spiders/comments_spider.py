import scrapy


class CommentsSpider(scrapy.Spider):
    name = "comments"


    pre_url = 'http://liuyan.people.com.cn/threads/content?tid='
    start_urls = []

    f = open('tutorial/spiders/tid.txt')
    for line in f.readlines():
        tid = line[: -1]
        url = pre_url + tid
        start_urls.append(url)


    def parse(self, response):
        yield {
            'text':  response.css('p.zoom::text').get()
	}
