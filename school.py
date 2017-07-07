# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 13:40:56 2017
@author: 1310615
"""

import argparse
import pandas as pd
from pandas import DataFrame
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException




##Exception 클래스를 상속한 클래스를 만든다
#class CustomException(Exception):
#    #생성할때 value 값을 입력 받는다.
#    def __init__(self, value):
#        self.value = value
#     
#    #생성할때 받은 value 값을 확인 한다.
#    def __str__(self):
#        return self.value
#
##예외를 발생하는 함수
#def raise_exception(err_msg):
#    raise CustomException(err_msg)




def getParentPaid(args):

#    grade = { 'H':'HighSchool'  }
    grade = {'E':'ElementarySchool' ,'M':'MiddleSchool', 'H':'HighSchool' }
    schoolDf = None
    accountNatinalDf = None
    accountPrivateDf = None
    pathFile = '.\\file\\'
    pathWebDriver = '.\\webdriver\\'
    debugStr = 'ParentPaid Start !!'
        
    # 국공립학교 계정
    accountNatinalDf = DataFrame(columns=('학교명','구분', '공시년월','학부모부담수입','등록금'
                                ,'학교운영지원비', '수익자부담수입','급식비'
                                ,'방과후학교활동비', '현장체험학습비','청소년단체활동비'
                                ,'졸업앨범대금', '교과서대금','기숙사비','기타수익자부담수입'
                                ,'누리과정비','교복구입비','운동부운영비'), index=None  )
    # 사립학교 계정
    accountPrivateDf = DataFrame(columns=('학교명','구분', '공시년월','학부모부담수입' ,'등록금'
                                         ,'입학금' ,'수업료' ,'학교운영지원비' ,'수익자부담수입' 
                                         ,'급식비' ,'방과후학교활동비' ,'현장체험학습비' 
                                         ,'청소년단체활동비' ,'졸업앨범대금' ,'교과서대금'
                                         ,'기숙사비' ,'기타수익자부담수입' ,'누리과정비' 
                                         ,'교복구입비','운동부운영비'), index=None  )


    debugStr = '웹드라이버 선택(팬텀은 화면표시 없음)'
    if args.browser == 'c':
        driver = webdriver.Chrome(pathWebDriver + "chromedriver")
    elif args.browser == 'p':
        driver = webdriver.PhantomJS(pathWebDriver + "phantomjs-2.1.1-windows\\bin\\phantomjs")
    elif args.browser == 'i':
        driver = webdriver.Ie(pathWebDriver + "IEDriverServer_win32_2.45.0")
    else:
        driver = webdriver.Chrome(pathWebDriver + "chromedriver")

    debugStr = '학교등급 선택'
    for g in grade:
        debugStr = '학교정보 읽어오기'
        if g == 'E':
            debugStr = grade.get(g)
            schoolDf = pd.read_excel(pathFile  + "2-2) 초등학교 현황.xlsx")
        elif g == 'M':
            debugStr = grade.get(g)
            schoolDf = pd.read_excel(pathFile  + "2-3) 중학교 현황.xlsx")
        elif g == 'H':
            debugStr = grade.get(g)
            schoolDf = pd.read_excel(pathFile  + "2-4) 고등학교 현황.xlsx")
        else:
            pass

        schoolDf.columns = schoolDf.iloc[2,0:]
        schoolDf = schoolDf.drop(0,axis=0)
        schoolDf = schoolDf.drop(1,axis=0)
        schoolDf = schoolDf.drop(2,axis=0)

        debugStr = '학교 루프 시작'

#        for idx, row in schoolDf.ix[:5].iterrows():
        for idx, row in schoolDf.iterrows():

            schoolName = row['학교명'].strip()
            schoolURL = row['홈페이지'].strip()
            
            debugStr = '웹 호출'
            driver.implicitly_wait(5)
            driver.get('http://www.schoolinfo.go.kr')
            debugStr = '변수 초기화'
            countNational = 0
            countPrivate = 0
            schooltype = 'thead'
        
            try:
                driver.find_element_by_id("SEARCH_KEYWORD").send_keys("")
                driver.find_element_by_id("SEARCH_KEYWORD").send_keys(schoolName)
                driver.find_element_by_xpath("//button[@title='검색하기']").click()
                
                debugStr = '학교검색결과 더보기버튼'
                while 1:
                    try:
                        driver.find_element_by_id("btnMore")
                    except NoSuchElementException:
                        break
                    driver.find_element_by_id("btnMore").click()

                debugStr = '학교검색결과 색인'
                
#                driver.find_element_by_xpath("//h1[@class='School_Name']/a[contains(@href,"+schoolName+")]").click()
                driver.find_element_by_xpath("//a[@href='"+schoolURL+"']/parent::span/parent::li/parent::ul/parent::article/h1[@class='School_Name']/a").click()
                
                debugStr = '국공사립 구분확인'
                establish = driver.find_element_by_xpath("//ul[@class='School_Data']/li[2]").text[5:]
                
                debugStr = '상세정보 클릭'
                driver.find_element_by_link_text('상세정보').click()
            
                debugStr = '예결산서 클릭'
                if establish in ('국립','공립'):
                    schooltype = 'thead'
                    colNo01= '22'
                    colNo02= '23'
                    colNo03= '24'
                    colNo04= '25'
                    colNo05= '26'
                    colNo06= '27'
                    colNo07= '28'
                    colNo08= '29'
                    colNo09= '30'
                    colNo10= '31'
                    colNo11= '32'
                    colNo12= '33'
                    colNo13= '34'
                    colNo14= '35'
                    colNo15= '36'
                    driver.find_element_by_link_text('학교회계 예·결산서').click()
                    
                elif establish == '사립':
                    schooltype = 'tbody'
                    colNo01= '23'
                    colNo02= '24'
                    colNo03= '25'
                    colNo04= '26'
                    colNo05= '27'
                    colNo06= '28'
                    colNo07= '29'
                    colNo08= '30'
                    colNo09= '31'
                    colNo10= '32'
                    colNo11= '33'
                    colNo12= '34'
                    colNo13= '35'
                    colNo14= '36'
                    colNo15= '37'
                    colNo16= '38'
                    colNo17= '39'
                    driver.find_element_by_link_text('사립학교 교비회계 예·결산서').click()
                    
                else:
                    pass
        #            raise_exception(schoolName + " pass !!!")
            
                debugStr = 'iframe 해제'
                driver.switch_to_frame(driver.find_element_by_xpath("//iframe"))
        
                debugStr = '자세히보기 클릭'
                driver.find_element_by_id("btnDetail").click()
        
                debugStr = '공시년월 목록 선택'
                select = Select(driver.find_element_by_id('select_trans_dt'))
                
                debugStr = '공시년월별 자세히 보기 루프'
                for index in range(len(select.options)):
                    debugStr = '공시년월별 자세히 보기 루프 select_by_index'
                    select = Select(driver.find_element_by_id('select_trans_dt'))
                    select.select_by_index(index)
        
                    debugStr = '공시년월별 자세히 보기 루프 existDetail'
                    existDetail = driver.find_element_by_xpath("//div[@id='btnDetail']/a")
                    if existDetail.is_displayed():
                        debugStr = '공시년월별 자세히 보기 루프 existDetail.click()'
                        existDetail.click()
                    
                    debugStr = '공시년월별 자세히 보기 루프 cell'
                    cell = []
                    cell.append(schoolName)
                    cell.append(establish)
                    cell.append(driver.find_element_by_xpath("//select[@id='select_trans_dt']/option[@selected='']").text)
                    cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr["+ colNo01 +"]/td").text)
                    cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr["+ colNo02 +"]/td").text)
                    cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr["+ colNo03 +"]/td").text)
                    cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr["+ colNo04 +"]/td").text)
                    cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr["+ colNo05 +"]/td").text)
                    cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr["+ colNo06 +"]/td").text)
                    cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr["+ colNo07 +"]/td").text)
                    cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr["+ colNo08 +"]/td").text)
                    cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr["+ colNo09 +"]/td").text)
                    cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr["+ colNo10 +"]/td").text)
                    cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr["+ colNo11 +"]/td").text)
                    cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr["+ colNo12 +"]/td").text)
                    cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr["+ colNo13 +"]/td").text)
                    cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr["+ colNo14 +"]/td").text)
                    cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr["+ colNo15 +"]/td").text)
                    if establish == '사립':
                        cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr["+ colNo16 +"]/td").text)
                        cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr["+ colNo17 +"]/td").text)
                    
                            
                    # 파일 쓰기 
                    if establish in ('국립','공립'):
                        accountNatinalDf.loc[countNational] = cell
                        countNational += 1
                    elif establish == '사립':
                        accountPrivateDf.loc[countPrivate] = cell
                        countPrivate += 1
                    
            except NoSuchElementException:
                print(schoolName + " NoSuchElementException !!!" + debugStr)
                pass
            except StaleElementReferenceException:
                print(schoolName + " StaleElementReferenceException !!!" + debugStr)
                pass
            
            
        
        
        # 파일 저장 
        accountNatinalDf.to_excel('.\\'+grade.get(g)+'National.xlsx',  header=True, index=True)
        accountPrivateDf.to_excel('.\\'+grade.get(g)+'Private.xlsx',  header=True, index=True)
        


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--browser', choices=['i', 'c', 'p'], default='c', help="Select Brower. \n i=IE, c=Chrome, p=PhantomJS")
    args, unparsed = parser.parse_known_args()
    getParentPaid(args)
