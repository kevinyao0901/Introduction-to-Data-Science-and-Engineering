import csv
import requests
from lxml import etree


fp = open('douban_top250.csv', 'w', newline='', encoding='utf-8')

writer = csv.writer(fp)
writer.writerow(('name', 'actor', 'information', 'date', 'star', 'evaluate', 'introduction'))

urls = ['https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(0, 250, 25)]
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.'}

for url in urls:
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath("//ol[@class='grid_view']/li")

    for info in infos:
        name = info.xpath(".//div[@class='info']//div[@class='hd']//a/span[1]/text()")[0]
        
        actor = info.xpath(".//div[@class='info']//div[@class='bd']//p[1]/text()")
        if actor:
            actor = actor[0].strip()
        else:
            actor = ''
        
        information = info.xpath(".//div[@class='info']//div[@class='bd']//p[2]/span/text()")
        if information:
            information = information[0]
        else:
            information = ''
        
        date = info.xpath(".//div[@class='info']//div[@class='bd']//p[2]/text()[last()]")
        if date:
            date = date[0].strip()
        else:
            date = ''
        
        star = info.xpath(".//div[@class='info']//div[@class='bd']//div[@class='star']//span[@class='rating_num']/text()")
        if star:
            star = star[0]
        else:
            star = ''
        
        evaluate = info.xpath(".//div[@class='info']//div[@class='bd']//div[@class='star']//span[4]/text()")
        if evaluate:
            evaluate = evaluate[0]
        else:
            evaluate = ''
        
        introduction = info.xpath(".//div[@class='info']//div[@class='bd']//p[@class='quote']/span/text()")
        if introduction:
            introduction = introduction[0].strip()
        else:
            introduction = ''

        writer.writerow((name, actor, information, date, star, evaluate, introduction))

fp.close()
print('爬取完成！')
