# -*- coding: utf-8 -*-


import pandas as pd
import requests
import json

statDf = pd.read_excel("statlist.xlsx")

host='http://ecos.bok.or.kr/api/StatisticItemList/'
key ='[OpenAPI인증키]'
condition ='/json/kr/1/1000/'

#statcode ='010Y002'#010Y002 043Y062
df = pd.DataFrame()

#df = pd.DataFrame(json.loads(requests.get(host+key+condition + '010Y002').text)['StatisticItemList']['row'])
#url=host+key+condition + '010Y002'
df.to_excel("statresult.xlsx")

for statcode in statDf['통계코드']:
    try:
        response = json.loads(requests.get(host+key+condition + statcode).text)
        df = df.append(pd.DataFrame(response['StatisticItemList']['row']))
    except Exception as e:
        print(statcode  + str(e))
        pass

df.to_excel("statresult.xlsx")


#rdf = pd.DataFrame(response['StatisticItemList']['row'])



# 
#f = csv.writer(open("statresult.csv", "w"))
#
#f.writerow(['STAT_CODE','STAT_NAME','GRP_NAME','ITEM_CODE','ITEM_NAME','CYCLE','START_TIME','END_TIME','DATA_CNT'])
#
#for x in response['StatisticItemList']['row']:
#    f.writerow([x["STAT_CODE"], x["STAT_NAME"], x["GRP_NAME"], 
#                x["ITEM_CODE"], x["ITEM_NAME"], x["CYCLE"],     
#                x["START_TIME"], x["END_TIME"], x["DATA_CNT"]])


