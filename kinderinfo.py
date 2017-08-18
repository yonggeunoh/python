# -*- coding: utf-8 -*-
# -*- coding: cp949 -*-
"""
Created on Mon Jul 10 17:55:16 2017

@author: 1310615
"""
import pandas as pd
import json
import requests

import xlwt
#from pandas import DataFrame
#from selenium import webdriver
#import urllib
#import BeautifulSoup

#pathWebDriver = '.\\webdriver\\'
#driver = webdriver.Chrome(pathWebDriver + "chromedriver")
#driver.implicitly_wait(10)
#driver.get('http://e-childschoolinfo.moe.go.kr/kinderMt/combineFind.do')
#driver.find_element_by_id

#html = 'http://e-childschoolinfo.moe.go.kr/kinderMt/combineFind.do'
#soup = BeautifulSoup.BeautifulSoup(html)
#print soup.prettify()

path = u".\\child\\"

childDf = pd.read_excel(path +u"childapi.xlsx",sheetname =u"URL")

childDf.columns

childDf.shape


data = None
for idx, row  in childDf.iloc[:1].iterrows():
    print row.URL
    data = json.loads(requests.get(row.URL).text)

    

print data["kinderInfo"][0]["addr"]


kindata = json.loads(data['kinderInfo'].text)

for i in dict.keys():
    dict[i]
    print i['addr'], i['clcnt3'], i['clcnt4'], i['clcnt5'], i['edate'], i['establish'], i['hpaddr'], i['key'], i['kindername'], i['mixclcnt'], i['mixppcnt'], i['odate'], i['officeedu'], i['opertime'], i['ppcnt3'], i['ppcnt4'], i['ppcnt5'], i['shclcnt'], i['shppcnt'], i['subofficeedu'], i['telno']
    


import xlwt
 
workbook = xlwt.Workbook(encoding='utf-8', cell_overwrite_ok=True)

sheetname = 'shteet1'
worksheet = workbook.add_sheet(sheetname) #시트 생성

worksheet.write(1,1,u"열기")
worksheet.write(1,2,u"읽기")
worksheet.write(1,3,u"쓰기")
worksheet.write(1,4,u"저장하기")
 

filename = path + 'testfile.xls' 
workbook.save(filename) #엑셀 파일 저장 및 생성



 


