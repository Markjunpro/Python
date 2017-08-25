#!/usr/bin/python3
#-*-coding :utf-8 -*-

import warnings
warnings.filterwarnings("ignore")
import jieba  
import numpy
import codecs 
import re
import pandas as pd 
import matplotlib.pyplot as plt 
from urllib import request
from bs4 import BeautifulSoup as bs

import matplotlib
matplotlib.rcParams['figure.figsize']= (10.0,5.0)
from wordcloud import WordCloud

def getNowPlayingMovies_list():
	resp = request.urlopen('https://movie.douban.com/nowplaying/hangzhou/')
	html_date = resp.read().decode('utf-8')
	soup = bs(html_date,'html.parser')
	nowplaying_movies = soup.find_all('div',id='nowplaying')
	nowplaying_movies_list = nowplaying_movies[0].find_all('li',class_='list-item')
	nowplaying_list = []
	for item in nowplaying_movies_list:
		nowplaying_dict = {}
		nowplaying_dict['id'] = item['data-subject']
		for tag_img_item in item.find_all('img'):
			nowplaying_dict['name'] = tag_img_item['alt']
			nowplaying_list.append(nowplaying_dict)
	return nowplaying_list

def getCommentsByld(movield,pageNum):
	eachCommentList = [];
	if pageNum >0 :
		start = (pageNum-1)*20
	else:
		return False
	requrl = 'https://movie.douban.com/subject/' + movield + '/comments' + '?' + 'start='+str(start)+'&limit=20'
	print(requrl)
	resp = request.urlopen(requrl)
	html_date = resp.read().decode('utf-8')
	soup = bs(html_date,'html.parser')
	comment_div_lits = soup.find_all('div',class_='comment')
	for item in comment_div_lits:
		if item.find_all('p')[0].string is not None:
			eachCommentList.append(item.find_all('p')[0].string)
	return eachCommentList

def main():
	commentList =[]
	NowPlayingMovie_list = getNowPlayingMovies_list()
	for i in range(10):
		num = i+1
		commentList_temp = getCommentsByld(NowPlayingMovie_list[0]['id'],num)
		commentList.append(commentList_temp)

	comments = ''
	for k in range(len(commentList)):
		comments = comments + (str(commentList[k])).strip()

	pattern = re.compile(r'[\u4e00-\u9fa5]+')
	filterdate = re.findall(pattern,comments)
	clearned_comments = ''.join(filterdate)

	segment = jieba.lcut(clearned_comments)
	words_df = pd.DataFrame({'segment':segment})

	stopwords = pd.read_csv('stopwords.txt',index_col=False,quoting=3,sep="\t",names=['stopword'],encoding = 'utf-8')
	words_df = words_df[~words_df.segment.isin(stopwords.stopword)]

	word_stat = words_df.groupby(by=['segment'])['segment'].agg({"计数":numpy.size})
	word_df = word_stat.reset_index().sort_values(by=["计数"],ascending=False)

	wordcloud =WordCloud(font_path="simhei.ttf",background_color='white',max_font_size=80)
	word_frequence = {x[0]:x[1] for x in word_stat.head(1000).values}

	word_frequence_list=[]
	for key in word_frequence:
		temp = (key,word_frequence[key])
		word_frequence_list.append(temp)

	wordcloud = wordcloud.fit_words(word_frequence_list)
	plt.imshow(wordcloud)

if __name__ == '__main__':
	main()

