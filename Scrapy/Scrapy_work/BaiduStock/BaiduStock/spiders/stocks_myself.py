# -*- coding: utf-8 -*-
import scrapy
import re


class StocksSpider(scrapy.Spider):
    name = 'baiduStock'
    
    start_urls = ['http://quote.eastmoney.com/stocklist.html']

    def parse(self, response):
    	for href in response.css('a::attr(href)').extract():
    		try:
    			stock = re.findall(r"[s][h/z]\d{6}",href)[0]
    			url = 'https://gupiao.baidu.com/stock/'+stock+'.html'
    			yield scrapy.Request(url,callback=self.parse_stock)
    		except:
    			continue
    def parse_stock(self,response):
    	infoDict ={}
    	stockInfo = response.css('.stock-bets')
    	name = stockInfo.css('.bets-name').extract()[0]
    	keyList = stockInfo('dt').extract()
    	valueList = stockInfo.css('dd').extract()
    	for i in range(len(keyList)):
    		key = re.findall(r'>.*</dt>',keyList[i])[0][1:-5]
    		try:
    			value = re.findall(r'\d+\.?*<dd>',valueList[i])[0][0:-5]
    		except:
    			val = '--'
    		infoDict[key] = value

    	infoDict.update(
    		{'stock-name':re.findall('\s.*\(',name)[0].split()[0]+\
    			re.findall('\>.\<',name)[0][1:-1]
    		}
    		)
    	yield infoDict
