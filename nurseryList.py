# -*- coding: utf-8 -*-
"""
Created on Sun Sep 03 16:17:29 2017

@author: Yong-geun
"""
import xml.etree.ElementTree as ET
import pandas as pd
import json
import requests
#import xlwt
from pandas import DataFrame
path = u".\\"

#nurseryDf = pd.read_excel(path +u"kindergartenURL.xlsx",sheetname =u"URL")

apicall ='http://api.childcare.go.kr/mediate/rest/cpmsapi030/cpmsapi030/request?key=0dda6a90d7534ffeb263d9510ae8609e&arcode='


apicode =[ u'11110',u'11140',u'11170',u'11200',u'11215',u'11230',u'11260',u'11290',u'11305'
        ,u'11320',u'11350',u'11380',u'11410',u'11440',u'11470',u'11500',u'11530',u'11545'
        ,u'11560',u'11590',u'11620',u'11650',u'11680',u'11710',u'11740',u'26110',u'26140'
        ,u'26170',u'26200',u'26230',u'26260',u'26290',u'26320',u'26350',u'26380',u'26410'
        ,u'26440',u'26470',u'26500',u'26530',u'26710',u'27110',u'27140',u'27170',u'27200'
        ,u'27230',u'27260',u'27290',u'27710',u'28110',u'28140',u'28170',u'28185',u'28200'
        ,u'28237',u'28245',u'28260',u'28710',u'28720',u'29110',u'29140',u'29155',u'29170'
        ,u'29200',u'30110',u'30140',u'30170',u'30200',u'30230',u'31110',u'31140',u'31170'
        ,u'31200',u'31710',u'36110',u'41110',u'41111',u'41113',u'41115',u'41117',u'41130'
        ,u'41131',u'41133',u'41135',u'41150',u'41170',u'41171',u'41173',u'41190',u'41210'
        ,u'41220',u'41250',u'41270',u'41271',u'41273',u'41280',u'41281',u'41285',u'41287'
        ,u'41290',u'41310',u'41360',u'41370',u'41390',u'41410',u'41430',u'41450',u'41460'
        ,u'41461',u'41463',u'41465',u'41480',u'41500',u'41550',u'41570',u'41590',u'41610'
        ,u'41630',u'41650',u'41670',u'41800',u'41820',u'41830',u'42110',u'42130',u'42150'
        ,u'42170',u'42190',u'42210',u'42230',u'42720',u'42730',u'42750',u'42760',u'42770'
        ,u'42780',u'42790',u'42800',u'42810',u'42820',u'42830',u'43110',u'43111',u'43112'
        ,u'43113',u'43114',u'43130',u'43150',u'43720',u'43730',u'43740',u'43745',u'43750'
        ,u'43760',u'43770',u'43800',u'44130',u'44131',u'44133',u'44150',u'44180',u'44200'
        ,u'44210',u'44230',u'44250',u'44270',u'44710',u'44760',u'44770',u'44790',u'44800'
        ,u'44810',u'44825',u'45110',u'45111',u'45113',u'45130',u'45140',u'45180',u'45190'
        ,u'45210',u'45710',u'45720',u'45730',u'45740',u'45750',u'45770',u'45790',u'45800'
        ,u'46110',u'46130',u'46150',u'46170',u'46230',u'46710',u'46720',u'46730',u'46770'
        ,u'46780',u'46790',u'46800',u'46810',u'46820',u'46830',u'46840',u'46860',u'46870'
        ,u'46880',u'46890',u'46900',u'46910',u'47110',u'47111',u'47113',u'47130',u'47150'
        ,u'47170',u'47190',u'47210',u'47230',u'47250',u'47280',u'47290',u'47720',u'47730'
        ,u'47750',u'47760',u'47770',u'47820',u'47830',u'47840',u'47850',u'47900',u'47920'
        ,u'47930',u'47940',u'48120',u'48121',u'48123',u'48125',u'48127',u'48129',u'48170'
        ,u'48220',u'48240',u'48250',u'48270',u'48310',u'48330',u'48720',u'48730',u'48740'
        ,u'48820',u'48840',u'48850',u'48860',u'48870',u'48880',u'48890',u'50110',u'50130' ]

root = None
for code in apicode[:1]:
    url = apicall + code
    xml_data = requests.get(url).text.encode('utf-8')
    root = ET.parse(xml_data)
print root.tag
print root.attrib



aa =root.find('response/item/crname')


for child in root:
    print child.tag, child.attrib


for country in root.findall('crname'):
    rank = country.find('rank').text
    name = country.get('name')
    print name, rank


data = None
acntDf = DataFrame(columns=(u'sidoname' ,u'sigunname' ,u'stcode' ,u'crname'
                        ,u'crtypename' ,u'crstatusname' ,u'zipcode' ,u'craddr'
                        ,u'crtelno' ,u'crfaxno' ,u'crhome' ,u'nrtrroomcnt'
                        ,u'nrtrroomsize' ,u'plgrdco' ,u'chcrtescnt' ,u'crcapat'
                        ,u'crchcnt' ,u'la' ,u'lo' ,u'crcargbname' ,u'crcnfmdt'
                        ,u'crpausebegindt' ,u'crpauseenddt' ,u'crabldt' ,u'crspec' ), index = None)


for idx, row  in nurseryDf.iloc[:3].iterrows():

    data = json.loads(requests.get(row.URL).text)
    for ndict in data["nurseryInfo"]:
        acntDf = acntDf.append(pd.Series(ndict),ignore_index=True)
   
acntDf.to_excel(path + 'nurseryList.xlsx' )
