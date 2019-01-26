
import requests
import pandas as pd
from io import BytesIO



header_params = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'file.krx.co.kr',
    'Origin': 'http://marketdata.krx.co.kr',
    'Referer': 'http://marketdata.krx.co.kr/mdi',
    'Upgrade-Insecure-Requests': '1'
}

search_params = {
    'name': 'fileDown',
    'filetype':'csv',
    'url':'MKD/13/1303/13030401/mkd13030401',
    'search_gubun':'ALL',
    'bnd_kind':'on',
    'mkt_gubun':'1',
    'date_sch_type':'month',
    'from_year':'2009',
    'from_month':'01',
    'to_year':'2019',
    'to_month':'01',
    'fromdate':'20181225',
    'todate':'20190125'
}


conn = requests.Session()
search_params['period_strt_mm']='200901'
search_params['period_end_mm'] ='201812'


resgen = conn.get('http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx', params=search_params)
print(resgen.url)

resdata = requests.post('http://file.krx.co.kr/download.jspx', headers=header_params, data={'code': resgen.text})
print(resdata.url)

df = pd.read_csv(BytesIO(resdata.content))


