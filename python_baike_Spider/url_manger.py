#coding:utf-8

#url管理器,管理器需要维护两个列表，一个是待爬取的URL,一个是爬取过的Url

class UrlManger(object):

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    #向管理器中添加新的Url
    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

     #添加新的URL
    def add_new_urls(self,urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    #判断管理器中是否含有新的Url
    def has_new_url(self):
        return len(self.new_urls) != 0

    #获取一个新的待爬取的URL
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url



