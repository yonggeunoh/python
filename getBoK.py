import requests
from bs4 import BeautifulSoup

# url = "http://www.bok.or.kr/broadcast.action?menuNaviId=561" # 공지사항
url = "http://www.bok.or.kr/contents/total/ko/boardNewRptList.action?menuNaviId=500" # 최신자료
url = "http://tvo.kr/xe/index.php?mid=download1"
r = requests.get(url)
soup = BeautifulSoup(r.text)

HEADER = ('', 'id', 'title', '', 'date', 'hits')

for tr in soup.select("#contentArea .brdList tbody tr"):
    parsed = [td.text.strip() for td in tr.select("td")]
    cols = dict(zip(HEADER, parsed))
    print('{} {} {}'.format(cols['title'], cols['date'], cols['hits']))