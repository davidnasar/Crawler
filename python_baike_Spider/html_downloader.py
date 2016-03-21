#coding:utf-8

import urllib2
#下载器

class HtmlDownload(object):

    def download(self,url):
        if url is None:
            return None
        response = urllib2.urlopen(url)

        if response.getcode() != 200:
            return None

        return response.read()


