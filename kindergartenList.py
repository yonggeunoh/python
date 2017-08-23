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

childDf = pd.read_excel(path +u"kindergartenURL.xlsx",sheetname =u"URL")

data = None
acntDf = DataFrame(columns=('addr' ,'clcnt3' ,'clcnt4' ,'clcnt5' ,'edate' ,'establish' ,'hpaddr'
                           ,'key' ,'kindername' ,'mixclcnt' ,'mixppcnt' ,'odate' ,'officeedu'
                           ,'opertime' ,'ppcnt3' ,'ppcnt4' ,'ppcnt5' ,'shclcnt' ,'shppcnt'
                           ,'subofficeedu' ,'telno'
                           ,'city','district','cityname','districtname1','districtname2'
                           ), index = None)

#a = childDf.iloc[:100]
#b = childDf.iloc[100:200]
#c = childDf.iloc[200:]

for idx, row  in childDf.iloc[200:].iterrows():
#for idx, row  in childDf.iterrows():
    data = json.loads(requests.get(row.URL).text)
    for kiDict in data["kinderInfo"]:
        kiDict['city'] = row.city
        kiDict['district'] = row.district
        kiDict['cityname'] = row.cityname
        kiDict['districtname1'] = row.districtname1
        kiDict['districtname2'] = row.districtname2
        acntDf = acntDf.append(pd.Series(kiDict),ignore_index=True)
   
acntDf.to_excel(path + 'kindergartenList3.xlsx' )

