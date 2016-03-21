#coding:utf-8

from python_baike_Spider import html_downloader,url_manger,html_output,html_parser

class SpiderMain():
    def __init__(self):
        self.urls = url_manger.UrlManger()
        self.downloader = html_downloader.HtmlDownload()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_output.HtmlOutput()

    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d:%s'%(count,new_url)
                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 100:
                    break

                count = count + 1
            except:
                print 'craw failed'

        self.outputer.output_html()




if __name__ == '__main__':
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)


'''
一般的爬虫架构分为三大模块，URL管理器，网页下载器(urllib2)和网页解析器(beautifulsoup)
'''
