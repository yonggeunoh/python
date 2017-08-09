# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 13:40:56 2017
@author: 1310615
"""

import sys
import os
import argparse
import pandas as pd
import logging
from pandas import DataFrame
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
#from selenium.common.exceptions import StaleElementReferenceException
#from selenium.common.exceptions import ElementNotVisibleException

def getParentPaid(args):

    reload(sys)
    sys.setdefaultencoding('utf-8')

    driver = None
    schoolDf = None
    schoolDfempty = None
    acctDf = None
    pathFile = '.\\'
    pathWebDriver = '.\\webdriver\\'
    pathResult = '.\\result\\'
    pathLog = '.\\log\\'

    if not os.path.exists(pathResult):
        os.makedirs(pathResult)
    if not os.path.exists(pathLog):
        os.makedirs(pathLog)

    logging.basicConfig(filename = pathLog + 'schoolinfo'+datetime.today().strftime("%Y%m%d%H%M%S") +'.log'
                      , level = logging.CRITICAL
                      , format = '%(asctime)s %(message)s'
                      , datefmt = '%Y/%m/%d %I:%M:%S %p')
    logger = logging.getLogger("crumbs")
    logger.setLevel(logging.ERROR)

    logger.info('ParentPaid Start !!')
    grade = { 'e':u'초등학교'
            , 'm':u'중학교'
            , 'h':u'고등학교'
            , 'u':u'대학교'
            , 'g':u'대학원'
            , 's':u'특수학교'
            , 'o':u'기타' }

    gList = list(grade.keys())

    if args.grade == 'a':
        gList = gList
    else:
        del gList
        gList= list(args.grade)

    logger.info(u'웹드라이버 선택(팬텀은 화면표시 없음)')
    if args.browser == 'c':
        driver = webdriver.Chrome(pathWebDriver + "chromedriver")
    elif args.browser == 'p':
        driver = webdriver.PhantomJS(pathWebDriver + "phantomjs-2.1.1-windows\\bin\\phantomjs")
    elif args.browser == 'i':
        driver = webdriver.Ie(pathWebDriver + "IEDriverServer_win32_2.45.0")
    else:
        driver = webdriver.Chrome(pathWebDriver + "chromedriver")

    logger.info(u'학교등급 선택')
    for g in gList:
        schoolDf = schoolDfempty

        print(grade.get(g) + u"처리")

        logger.info(grade.get(g) + u'학교목록 읽어오기')
        if g == 'e':
            schoolDf = pd.read_excel(pathFile  + u"2-2) 초등학교 현황.xlsx")
            schoolDf.columns = schoolDf.iloc[2,0:]
            schoolDf = schoolDf.drop([0,1,2],axis=0)
        elif g == 'm':
            schoolDf = pd.read_excel(pathFile  + u"2-3) 중학교 현황.xlsx")
            schoolDf.columns = schoolDf.iloc[2,0:]
            schoolDf = schoolDf.drop([0,1,2],axis=0)
        elif g == 'h':
            schoolDf = pd.read_excel(pathFile  + u"2-4) 고등학교 현황.xlsx")
            schoolDf.columns = schoolDf.iloc[2,0:]
            schoolDf = schoolDf.drop([0,1,2],axis=0)
        elif g == 'u':
            schoolDf = pd.read_excel(pathFile  + u"1-1) 대학 현황.xlsx")
            schoolDf.columns = schoolDf.iloc[4,0:]
            schoolDf.rename(columns={u"학교명(국문)":u"학교명"}, inplace = True)
            schoolDf = schoolDf.drop([0,1,2,3,4],axis=0)
        elif g == 'g':
            schoolDf = pd.read_excel(pathFile  + u"1-2) 대학원 현황.xlsx")
            schoolDf.columns = schoolDf.iloc[4,0:]
            schoolDf.rename(columns={u"학교명(국문)":u"학교명"}, inplace = True)
            schoolDf = schoolDf.drop([0,1,2,3,4],axis=0)
        elif g == 's':
            schoolDf = pd.read_excel(pathFile  + u"2-5) 특수학교 및 기타학교 현황.xlsx", sheetname =u"특수학교")
            schoolDf.columns = schoolDf.iloc[2,0:]
            schoolDf = schoolDf.drop([0,1,2],axis=0)
        elif g == 'o':
            schoolDf = pd.read_excel(pathFile  + u"2-5) 특수학교 및 기타학교 현황.xlsx", sheetname =u"기타학교")
            schoolDf.columns = schoolDf.iloc[3,0:]
            schoolDf = schoolDf.drop([0,1,2,3],axis=0)
        else:
            pass

        logger.info(u'변수 초기화')

        # 계정
        acctDf = DataFrame(columns=(u'학교명'
                                  , u'학교구분'
                                  , u'공시년월'
                                  , u'학부모부담수입'
                                  , u'등록금'
                                  , u'입학금'
                                  , u'수업료'
                                  , u'학교운영지원비'
                                  , u'수익자부담수입'
                                  , u'급식비'
                                  , u'방과후학교활동비'
                                  , u'현장체험학습비'
                                  , u'청소년단체활동비'
                                  , u'졸업앨범대금'
                                  , u'교과서대금'
                                  , u'기숙사비'
                                  , u'기타수익자부담수입'
                                  , u'누리과정비'
                                  , u'교복구입비'
                                  , u'운동부운영비')
                             , index = None)

        # City Loop BEGIN
        for city in schoolDf[u'시도'].drop_duplicates():
            print(city + u'처리')
            countPrvt = 1

            # School Loop BEGIN
            for idx, row in schoolDf.loc[(schoolDf[u'시도'] == city)].iterrows():

                logurl = ''
                
                try:
                    logger.info(u'웹 호출')
                    driver.implicitly_wait(3)
                    driver.get('http://www.schoolinfo.go.kr')

                    sname = row[u'학교명'].strip()
                    url = 'http://' + row[u'홈페이지'].strip().replace('http://','').rstrip('/')
                    city = row[u'시도'].strip()

                    logurl = sname + " " + url
                    print(logurl)

                    logger.info(sname + ': Loop Start')

                    driver.find_element_by_id("SEARCH_KEYWORD").send_keys("")
                    driver.find_element_by_id("SEARCH_KEYWORD").send_keys(sname)
                    driver.find_element_by_xpath(u"//button[@title='검색하기']").click()

                    logger.info(sname + ': btnMore')
                    while 1:
                        try:
                            driver.find_element_by_id("btnMore")
                        except Exception as e:
                            logger.info(sname + ": btnMore Break")
                            break
                        driver.find_element_by_id("btnMore").click()

                    logger.info(sname + u'학교검색결과 색인')
                    if 'url' == 'urlX' :
                        driver.find_element_by_xpath("//a[@href='"+url+"']/parent::span/parent::li/parent::ul/parent::article/h1[@class='School_Name']/a").click()
                    else:
                        driver.find_element_by_xpath("//p[@class='School_Division']/span[1][text()='"+city+"']/parent::p/../h1/a").click()

                    logger.info(sname + u'국공사립 구분확인')
                    establish = driver.find_element_by_xpath("//ul[@class='School_Data']/li[2]").text[5:]

                    logger.info(sname + u'상세정보 클릭')
                    driver.find_element_by_link_text(u'상세정보').click()

                    logger.info(sname + u'예결산서 클릭')

                    if establish in (u'국립',u'공립'):
                        driver.find_element_by_link_text(u'학교회계 예·결산서').click()
                    elif establish == u'사립':
                        driver.find_element_by_link_text(u'사립학교 교비회계 예·결산서').click()
                    else:
                        pass

                    logger.info(sname + u'iframe 해제')
                    driver.switch_to_frame(driver.find_element_by_xpath("//iframe"))

                    logger.info(sname + u'자세히보기 클릭')
                    driver.find_element_by_id("btnDetail").click()

                    logger.info(sname + u'공시년월 목록 선택')
                    select = Select(driver.find_element_by_id('select_trans_dt'))

                    # latest = y 가장 최신 예결산 자료만 입수
                    if args.latest == 'y':
                        optionSize = 1
                    else:
                        optionSize = len(select.options)

                    logger.info(sname + u'공시년월 최근것 만 입수 ' + args.latest )
                    for index in range(optionSize):

                        logger.info(sname + u'공시년월 select_trans_dt')
                        select = Select(driver.find_element_by_id('select_trans_dt'))
                        
                        logger.info(sname + u'공시년월 select_trans_dt option')
                        select.select_by_index(index)
                        
                        logger.info(sname + u'공시년월 select_by_index')
                        openYYMM = driver.find_element_by_xpath("//select[@id='select_trans_dt']/option[@selected='']").text

                        logger.info(sname + u'공시년월별 자세히 보기 openYYMM : ' + openYYMM)
                        existDetail = driver.find_element_by_xpath("//div[@id='btnDetail']/a")

                        if existDetail.is_displayed():
                            existDetail.click()

                        cell = []
                        print(sname + " " + openYYMM)

                        openMM = openYYMM[6:]

                        tableNo = ''
                        if openMM == '05월':
                            # 5월은 세입예산에서 추출
                            tableNo = ''
                        elif openMM == '09월':
                            # 9월은 세입결산에서 추출
                            tableNo = '3'
                        else:
                            pass

                        logger.info(sname + u'공시년월별 자세히 보기 tableNo : ' + openMM + 'exceldetail' + tableNo)

                        cell.append(sname)
                        cell.append(establish)
                        cell.append(openYYMM)

                        for col in acctDf.columns:
                            if col in (u'학교명',u'학교구분',u'공시년월'):
                                pass
                            else:
                                cellString = ''
                                try:
                                    cellString = driver.find_element_by_xpath("//div[@id='exceldetail"+tableNo+"']//th[text()='" + col + "']/../td").text
                                except NoSuchElementException as e:
                                    pass
                                cell.append(cellString)
                                '''
                                # Y.Oh : Exception handling can cause slowing down program.
                                cellString = driver.find_element_by_xpath("//div[@id='exceldetail"+tableNo+"']//th[text()='" + col + "']/../td").text
                                if len(cellString) > 0:
                                    cell.append(cellString)
                                else:
                                    cell.append('')
                                '''
                        acctDf.loc[countPrvt] = cell
                        countPrvt += 1
                    # openYYMM Loop END

                except NoSuchElementException as e:
                    print(logurl + u' 없음')
                    logger.exception(u'NoSuchElementException : ' + logurl)
                    pass
                except Exception as e:
                    logger.exception(sname + ' ' + str(e))
                    pass
                # School Loop END

            logger.info(sname + u': 파일 저장(' + grade.get(g) +u')')
            acctDf.to_excel(pathResult + grade.get(g) + city  + u'.xlsx',  header=True, index=True)
            acctDf.drop(acctDf.index, inplace=True)
            # City Loop END

        # Grade Loop END

    driver.close()
    driver.quit()
    # getParentPaid END

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=u'description: 학교알리미 Web Crawler'
                                   , formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-b', '--browser', choices=['i', 'c', 'p'], default='c'
                      , help=u'''사용할 인터넷 브라우저 선택(p는 백그라운드실행)\ni = IE, c = Chrome, p = PhantomJS''')
    parser.add_argument('-l', '--latest', choices=['y', 'n'], default='n'
                      , help=u'''가장 최신 자료만 취득''')
    parser.add_argument('-g', '--grade', choices=['e', 'm', 'h', 'u', 'g', 's', 'o','a'], default='a'
                      , help=u'''학교등급 선택\n  e = 초등학교\n, m = 중학교\n, h = 고등학교\n, u = 대학교\n, g = 대학원\n, s = 특수학교\n, o = 기타학교\n, a = 전학급''')
    args, unparsed = parser.parse_known_args()
    getParentPaid(args)
