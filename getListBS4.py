import requests
import bs4
from IPython.html.nbconvert.handlers import respond_zip
from docutils.nodes import target



#-*- coding: utf-8 -*-

import requests
import bs4

kyobo_url= "http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf"
tvo_url= "http://tvo.kr/xe/index.php?mid=download1"
target_url = kyobo_url
print(target_url)

#베스트셀러 순위별로 책 링크 가져오기
response = requests.get( 'http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf' )
soup = bs4.BeautifulSoup(response.text)
book_page_urls = [a.attrs.get('href') for a in soup.select('div.title a[href^="http://www.kyobobook.co.kr/product/detailViewKor.laf"]')]


#책별로 데이터 가져오기
for book_page_url in book_page_urls:
    response = requests.get( book_page_url )
    soup = bs4.BeautifulSoup(response.text)

    title = soup.select( 'h1.title strong' )[0].get_text().strip()
    author = soup.select( 'span.name  a' )[0].get_text()
    print (title + '/' + author  )