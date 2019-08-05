#-*- coding:utf-8 -*-
import requests
import re
import csv

def movie_info(url):
  #url = 'https://movie.douban.com/top250'#请求接口
  r = requests.get(url) #发送请求
  name = '<span class="title">([\u4e00-\u9fa5]+)</span>'
  rank=' <em class="">(.*?)</em>'
  country='&nbsp;/&nbsp;([\u4e00-\u9fa5]+)&nbsp;/&nbsp;'
  director='<p class="">(.*?)&nbsp;&nbsp;'
  time='<br>(.*?)&nbsp;/&nbsp'
  all=r.text
  movie_names=re.findall(name, all,re.S)
  movie_ranks = re.findall(rank, all,re.S)
  movie_countries = re.findall(country, all, re.S)
  text = re.sub('导演: ',"",all)  #把导演两个字替换掉
  movie_directors = re.findall(director, text, re.S)
  movie_times=re.findall(time, all, re.S)

  for rank,name,country,director,time in zip(movie_ranks,movie_names,movie_countries,movie_directors,movie_times):
          writer.writerow([rank,name,country,director,time])

if __name__ == '__main__':

    file = open('E:/python/scripts/movie.csv','w+',encoding='utf-8',newline='')
    writer = csv.writer(file)
    writer.writerow(['rank','name','country','director','time'])

    for i in range(0,250,25):
        url = 'https://movie.douban.com/top250?start={}&filter='.format(i)
        movie_info(url)