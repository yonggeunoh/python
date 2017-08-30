# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 08:52:21 2017
@author: 1310615
"""

import os
import sys
import logging
import argparse
import pandas as pd
from pandas import DataFrame as df
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from datetime import datetime

def getKinderInfo(args):

    pathList = u'.\\'
    pathResult= u'.\\'
    pathWebDriver = u'D:\\app\\python\\webdriver\\'

    if not os.path.exists(pathResult):
        os.makedirs(pathResult)

    if not os.path.exists(pathList):
        os.makedirs(pathList)

    currtime = datetime.today().strftime("%Y%m%d%H%M%S")
    logging.basicConfig(filename = u'.\\kindergartenLog'+ currtime +'.log'
                      , level = logging.WARN
                      , format = '%(asctime)s %(message)s'
                      , datefmt = '%Y/%m/%d %I:%M:%S %p'
                      , mode='w')
    logger = logging.getLogger(u"crumbs")
    logger.setLevel(logging.ERROR)


    logger.info(u'웹드라이버 선택(팬텀은 화면표시 없음)')
    if args.browser == 'c':
        driver = webdriver.Chrome(pathWebDriver + "chromedriver")
    elif args.browser == 'p':
        driver = webdriver.PhantomJS(pathWebDriver + "phantomjs-2.1.1-windows\\bin\\phantomjs")
    elif args.browser == 'i':
        driver = webdriver.Ie(pathWebDriver + "IEDriverServer_win32_2.45.0")
    else:
        driver = webdriver.Chrome(pathWebDriver + "chromedriver")

    driver.implicitly_wait(5)

    # 유치원 목록
    kindeListDf = pd.read_excel(pathList  + u"kindergartenList.xlsx")

    # 유치원 결산자료 목록
    kinderDf = df(columns=(
        # 유치원 정보
         u'주소',u'설립구분',u'유치원명',u'공시년월',u'원아수3세',u'원아수4세',u'원아수5세이상'
        # 교육과정 교육비용
        ,u'교육과정기본수업료3세',u'교육과정기본수업료4세',u'교육과정기본수업료5세',u'교육과정기본수업료주기'
        ,u'교육과정기본간식비3세',u'교육과정기본간식비4세',u'교육과정기본간식비5세',u'교육과정기본간식비주기'
        ,u'교육과정기본급식비3세',u'교육과정기본급식비4세',u'교육과정기본급식비5세',u'교육과정기본급식비주기'
        ,u'교육과정기본교재비및재료비3세',u'교육과정기본교재비및재료비4세',u'교육과정기본교재비및재료비5세',u'교육과정기본교재비및재료비주기'
        ,u'교육과정기본합계(월)3세',u'교육과정기본합계(월)4세',u'교육과정기본합계(월)5세'
        ,u'교육과정선택입학금3세',u'교육과정선택입학금4세',u'교육과정선택입학금5세',u'교육과정선택입학금주기'
        ,u'교육과정선택원복비3세',u'교육과정선택원복비4세',u'교육과정선택원복비5세',u'교육과정선택원복비주기'
        ,u'교육과정선택현장학습비3세',u'교육과정선택현장학습비4세',u'교육과정선택현장학습비5세',u'교육과정선택현장학습비주기'
        ,u'교육과정선택차량운영비3세',u'교육과정선택차량운영비4세',u'교육과정선택차량운영비5세',u'교육과정선택차량운영비주기'
        ,u'교육과정선택가방비3세',u'교육과정선택가방비4세',u'교육과정선택가방비5세',u'교육과정선택가방비주기'
        ,u'교육과정선택졸업및수료앨범비3세',u'교육과정선택졸업및수료앨범비4세',u'교육과정선택졸업및수료앨범비5세',u'교육과정선택졸업및수료앨범비주기'
        ,u'교육과정선택기타경비3세',u'교육과정선택기타경비4세',u'교육과정선택기타경비5세',u'교육과정선택기타경비주기'
        # 방과후과정 교육비용
        ,u'방과후과정기본수업료3세',u'방과후과정기본수업료4세',u'방과후과정기본수업료5세',u'방과후과정기본수업료주기'
        ,u'방과후과정기본간식비3세',u'방과후과정기본간식비4세',u'방과후과정기본간식비5세',u'방과후과정기본간식비주기'
        ,u'방과후과정기본급식비3세',u'방과후과정기본급식비4세',u'방과후과정기본급식비5세',u'방과후과정기본급식비주기'
        ,u'방과후과정기본교재비재료비3세',u'방과후과정기본교재비재료비4세',u'방과후과정기본교재비재료비5세',u'방과후과정기본교재비재료비주기'
        ,u'방과후과정기본합계(월)3세',u'방과후과정기본합계(월)4세',u'방과후과정기본합계(월)5세'
        ,u'방과후과정선택현장학습비3세',u'방과후과정선택현장학습비4세',u'방과후과정선택현장학습비5세',u'방과후과정선택현장학습비주기'
        ,u'방과후과정선택차량운영비3세',u'방과후과정선택차량운영비4세',u'방과후과정선택차량운영비5세',u'방과후과정선택차량운영비주기'
        ), index=None)

    cityNo = args.city
#    cityNo = args.city.decode('cp949').encode('utf-8')

    print cityNo , type(cityNo)
    
    cityDf = kindeListDf[u'city'].drop_duplicates()
    if  cityNo == u'a':
        cityDf = kindeListDf[u'city'].drop_duplicates()
    else:
        cityDf = kindeListDf[u'city'][kindeListDf.city == int(cityNo)].drop_duplicates()


    for city in cityDf:
        kcity = ''
#        for idx, row in kindeListDf.loc[(kindeListDf[u'city'] == int(city))].iterrows():
        for idx, row in kindeListDf.loc[(kindeListDf[u'city'] == int(city) )].iloc[:3].iterrows():

            kname = row[u'kindername'].strip()
            kaddr = row[u'addr'].strip()
            kcity = row[u'cityname'].strip()

            print kcity + ' 처리'
            
            try:

                driver.get('http://e-childschoolinfo.moe.go.kr/kinderMt/combineFind.do')
                driver.find_element_by_xpath("//select[@id='combineSidoList']/option[text()='"+kcity+u"']").click()
                driver.find_element_by_id('organName').send_keys('')
                driver.find_element_by_id('organName').send_keys(kname)
                driver.find_element_by_xpath("//form[@id='combineSearch']//a[text()='검색']").click()
                driver.find_element_by_xpath("//td[text()='"+kaddr +"']/../td/a").click()
                driver.find_element_by_xpath("//a[text()='교육·보육비용']").click()

                select = Select(driver.find_element_by_id('select-time'))
                optionSize = len(select.options)

                # latest = y 가장 최신 예결산 자료만 입수
                if args.latest == 'y':
                    optionSize = 1
                else:
                    optionSize = len(select.options)

                logger.info(kname + u'공시년월 최근것 만 입수 ' + args.latest )


                for index in range(optionSize):
                    select = Select(driver.find_element_by_id('select-time'))
                    select.select_by_index(index)
                    openYYMM = driver.find_element_by_xpath("//select[@id='select-time']/option[@selected='selected']").text

                    logger.info(  kname + ' ' + openYYMM + u' 처리')
                    print kcity + ' ' + kname + ' ' + kaddr + ' ' + openYYMM + u' 처리'


                    cell = []

                    cell.append(kaddr)
                    cell.append(row[u'establish'].strip())
                    cell.append(kname)
                    cell.append(openYYMM)
#                    cell.append(str(row[u'ppcnt3']).strip())
#                    cell.append(str(row[u'ppcnt4']).strip())
#                    cell.append(str(row[u'ppcnt5']).strip())
                    cell.append(row[u'ppcnt3'])
                    cell.append(row[u'ppcnt4'])
                    cell.append(row[u'ppcnt5'])

                    # 교육과정 교육비용 기본경비
                    four = [u'1',u'2',u'3',u'4']
                    curri_basic = [u'수업료',u'간식비',u'급식비',u'교재비 및 재료비']
                    for i in curri_basic:
                        for j in four:
                            cell.append(driver.find_element_by_xpath(u"//caption[text()='교육과정 교육비용']/..//th[text()='"+i+u"']/../td["+j+u"]").text.strip())

                    cell.append(driver.find_element_by_xpath(u"//caption[text()='교육과정 교육비용']/..//th[text()='합계(월)']/../td[1]").text.strip())
                    cell.append(driver.find_element_by_xpath(u"//caption[text()='교육과정 교육비용']/..//th[text()='합계(월)']/../td[2]").text.strip())
                    cell.append(driver.find_element_by_xpath(u"//caption[text()='교육과정 교육비용']/..//th[text()='합계(월)']/../td[3]").text.strip())


                    # 교육과정 교육비용 선택경비
                    curri_option = [u'입학금',u'원복비',u'현장학습비',u'차량운영비',u'가방비',u'졸업및 수료앨범비',u'기타경비']

                    for i in curri_option:
                        col = ''
                        try:
                            driver.find_element_by_xpath(u"//caption[text()='교육과정 교육비용']/..//th[text()='"+i+u"']/../td[1]").text.strip()
                            for j in four:
                                col = ''
                                try:
                                    col = driver.find_element_by_xpath(u"//caption[text()='교육과정 교육비용']/..//th[text()='"+i+u"']/../td["+j+u"]").text.strip()
                                except NoSuchElementException as e:
                                    print i + j + u'없음'
                                    pass
                                cell.append(col)
                        except NoSuchElementException as e:
                            cell.append(col)
                            cell.append(col)
                            cell.append(col)
                            cell.append(col)

                    # 방과후 과정 교육비용 기본경비

                    afterschool_basic = [u'수업료',u'간식비',u'급식비',u'교재비 및 재료비']
                    for i in afterschool_basic:
                        for j in four:
                            cell.append(driver.find_element_by_xpath(u"//caption[text()='방과후 과정 교육비용']/..//th[text()='"+i+u"']/../td["+j+u"]").text.strip())

                    cell.append(driver.find_element_by_xpath(u"//caption[text()='방과후 과정 교육비용']/..//th[text()='합계(월)']/../td[1]").text.strip())
                    cell.append(driver.find_element_by_xpath(u"//caption[text()='방과후 과정 교육비용']/..//th[text()='합계(월)']/../td[2]").text.strip())
                    cell.append(driver.find_element_by_xpath(u"//caption[text()='방과후 과정 교육비용']/..//th[text()='합계(월)']/../td[3]").text.strip())

                    # 방과후 과정 교육비용 선택경비
                    afterschool_option = [u'현장학습비',u'차량운영비']
                    for i in afterschool_option:
                        col = ''
                        try:
                            driver.find_element_by_xpath(u"//caption[text()='방과후 과정 교육비용']/..//th[text()='"+i+u"']/../td[1]").text.strip()
                            for j in four:
                                col = ''
                                try:
                                    col = driver.find_element_by_xpath(u"//caption[text()='방과후 과정 교육비용']/..//th[text()='"+i+u"']/../td["+j+u"]").text.strip()
                                except NoSuchElementException as e:
                                    print i + j + u'없음'
                                    pass
                                cell.append(col)
                        except NoSuchElementException as e:
                            cell.append(col)
                            cell.append(col)
                            cell.append(col)
                            cell.append(col)

                    # Raw 저장
                    kinderDf.loc[len(kinderDf)] = cell

            except Exception as e:
                logger.error( kname + ' ' + kaddr + u" 정보취득 실패 !! " + str(e))
                pass

        kinderDf.to_excel(pathResult + u'유치원_' + kcity + currtime +'.xlsx',  header=True, index=True)
        kinderDf.drop(kinderDf.index, inplace=True)
        #
    driver.close()
    driver.quit()
    #

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')

    parser = argparse.ArgumentParser(description=u'description: 유치원 알리미 Web Crawler'
                                   , formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-b', '--browser', choices=['i', 'c', 'p'], default=u'p'
                      , help=u'''사용할 인터넷 브라우저 선택(p는 백그라운드실행)\ni = IE, c = Chrome, p = PhantomJS''')
    parser.add_argument('-l', '--latest', choices=['y', 'n'], default=u'n'
                      , help=u'''가장 최신 자료만 취득''')
    parser.add_argument('-c', '--city', default=u'a'
                      , help=u'''시도명''')
    args, unparsed = parser.parse_known_args()
    getKinderInfo(args)
