
import pandas as pd
import urllib as ul
import requests

path = "C:\\Users\\1310615\\Desktop\\망간 다운로드\\Jul-2016_Access.xlsx"

frameAgg = pd.read_excel(path, sheetname='AGG')

frameAgg['URL']="http://whois.kisa.or.kr/openapi/whois.jsp?query=" + frameAgg['IP_ADDRESS'] + "&key=2015062511270252553438&answer=json"

sjson = []
sADDR = []
sZIPCODE = []

for i in frameAgg['URL']:
    #print(requests.get(i).json()['whois'].get('korean'))
    #print(requests.get(i).json())
    #json.append(requests.get(i).json())
    #print(requests.get(i).json()['whois']['korean']['user']['netinfo']['addr'])

    if requests.get(i).json()['whois'].get('korean'):
        sADDR.append(requests.get(i).json()['whois']['korean']['user']['netinfo']['addr'])
        sZIPCODE.append(requests.get(i).json()['whois']['korean']['user']['netinfo']['zipCode'])
    else:
        sADDR.append(requests.get(i).json()['whois']['countryCode'])
        sZIPCODE.append(requests.get(i).json()['whois']['countryCode'])

frameAgg['ADDR'] = sADDR
frameAgg['ZIPCODE'] = sZIPCODE

frameAgg.drop('URL',inplace=True,axis=1)

frameAgg.to_excel("C:\\Users\\1310615\\Desktop\\망간 다운로드\\Jul-2016_AccessResult.xlsx")
