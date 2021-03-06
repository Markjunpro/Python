#-*-coding :utf-8 -*-
#/!usr/bin/bash python3

# this code is from python developers in wechat

import requests
import re
from  bs4 import BeautifulSoup 
import traceback

def getHTMLTText(url):
	try:
		r = requests.get(url)
		r.raise_for_status()
		r.encoding = r. apparent_encoding
		return r.text
	except:
		return ""

def getStockList(lst,stockURL):
	html = getHTMLTText(stockURL)
	soup = BeautifulSoup(html,'html.parser')
	a = soup.find_all('a')
	for i in a :
		try:
			href =i.attrs['href']
			lst.append(re.findall(r"[s][hz]\d{6}",href)[0])
		except:
			continue

def getStockInfo(lst,stockURL,fpath):
	conut = 0
	for stock in lst:
		url = stockURL + stock + ".html"
		html = getHTMLTText(url)
		try:
			if html=="":
				continue
				infoDict = {}
				soup = BeautifulSoup(html,'html.parser')
				stockInfo = soup.find('div',attrs={'class':'stock-bets'})

				name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
				infoDict.update({'股票名称':name.text.split()[0]})

				keyList = stockInfo.find_all('dt')
				valueList = stockInfo.find_all('dd')
				for i in range(len(keyList)):
					key = keyList[i].text
					val = valueList[i].text
					infoDict[key] = val

				with open(fpath,'a',encoding='utf-8') as f:
					f.write(str(infoDict)+'\n')
					count = count + 1
					print("\r当前进度{:.2f}%".format(count*100/len(lst)),end="")
		except:
			count = count +1
			print("\r当前进度{:.2f}%".format(count*100/len(lst)),end="")
			continue

def main():
	stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
	stock_info_url = 'http://gupiao.baidu.com/stock'
	output_file = '/home/username/python/BaiduStockInfo.txt'
	slist =[]
	getStockList(slist,stock_list_url)
	getStockInfo(slist,stock_info_url,output_file)

if __name__ == '__main__':
	main()
