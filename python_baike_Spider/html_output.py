#coding:utf-8

#输出器

import time

class HtmlOutput(object):

    def __init__(self):
        self.datas = []

    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        #生成文件
        file_name = 'output.txt'
        file_content = ''
        # 最终要写到文件里的内容
        file_content += '生成时间：' + time.asctime() + '\n'
        #title_divide = '--' * 20 + '\n'
        for data in self.datas:
            count = 1
            file_content += '\n' + "词条:" + data['title'].encode('utf-8') + data['summary'].encode('utf-8')
            count = count + 1
        f = open(file_name, 'w')
        f.write(file_content)
        f.close()

        '''
        fout = open('output.html','w')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>"%data['url'])
            fout.write("<td>%s</td>"%data['title'].encode('utf-8'))
            fout.write("<td>%s</td>"%data['summary'].encode('utf-8'))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()
        '''


