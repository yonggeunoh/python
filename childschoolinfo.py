# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 17:55:16 2017
@author: 1310615
"""
import pandas as pd
import json
import requests
#import xlwt
from pandas import DataFrame
path = u".\\child\\"

childDf = pd.read_excel(path +u"childschoolinfo.xlsx",sheetname =u"URL")

data = None
acntDf = DataFrame(columns=('addr' ,'clcnt3' ,'clcnt4' ,'clcnt5' ,'edate' ,'establish' ,'hpaddr'
                           ,'key' ,'kindername' ,'mixclcnt' ,'mixppcnt' ,'odate' ,'officeedu'
                           ,'opertime' ,'ppcnt3' ,'ppcnt4' ,'ppcnt5' ,'shclcnt' ,'shppcnt'
                           ,'subofficeedu' ,'telno'), index = None)

for idx, row  in childDf.iloc[:100].iterrows():
#for idx, row  in childDf.iterrows():
    data = json.loads(requests.get(row.URL).text)
    for kiDict in data["kinderInfo"]:
        acntDf = acntDf.append(pd.Series(kiDict),ignore_index=True)
   
acntDf.to_excel(path + 'kinderList.xls' )    


#workbook = xlwt.Workbook(encoding='utf-8')
#sheetname = 'sheet1'
#worksheet = workbook.add_sheet(sheetname, cell_overwrite_ok=True) #시트 생성
#for i in data["kinderInfo"]:
#    print i['addr'], i['clcnt3'], i['clcnt4'], i['clcnt5'], i['edate'], i['establish'], i['hpaddr'], i['key'], i['kindername'] , i['mixclcnt'], i['mixppcnt'], i['odate'], i['officeedu'], i['opertime'], i['ppcnt3'], i['ppcnt4'], i['ppcnt5'], i['shclcnt']    , i['shppcnt'], i['subofficeedu'], i['telno']
#
#    worksheet.write(1, 1,i['addr'])
#    worksheet.write(1, 2,i['clcnt3'])
#    worksheet.write(1, 3,i['clcnt4'])
#    worksheet.write(1, 4,i['clcnt5'])
#    worksheet.write(1, 5,i['edate'])
#    worksheet.write(1, 6,i['establish'])
#    worksheet.write(1, 7,i['hpaddr'])
#    worksheet.write(1, 8,i['key'])
#    worksheet.write(1, 9,i['kindername'])
#    worksheet.write(1,10,i['mixclcnt'])
#    worksheet.write(1,11,i['mixppcnt'])
#    worksheet.write(1,12,i['odate'])
#    worksheet.write(1,13,i['officeedu'])
#    worksheet.write(1,14,i['opertime'])
#    worksheet.write(1,15,i['ppcnt3'])
#    worksheet.write(1,16,i['ppcnt4'])
#    worksheet.write(1,17,i['ppcnt5'])
#    worksheet.write(1,18,i['shclcnt'])
#    worksheet.write(1,19,i['shppcnt'])
#    worksheet.write(1,20,i['subofficeedu'])
#    worksheet.write(1,21,i['telno'])
#
#filename = path + 'testfile.xls' 
#workbook.save(filename) #엑셀 파일 저장 및 생성


