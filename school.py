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

    schoolDf = None
    acctPblcDf = None
    acctPrvtDf = None
    driver = None
    pathFile = '.\\file\\'
    pathWebDriver = '.\\webdriver\\'
    debugLog = 'ParentPaid Start !!'
    
    
    grade = {'e':'ElementarySchool' ,'m':'MiddleSchool'    , 'h':'HighSchool'
            ,'u':'University'       ,'g':'GraduateSchool'
            ,'k':'Kindergarden'     ,'s':'SpecialSchool'   ,'o':'Others' }
    

    # 국공립학교 계정
    acctPblcDf = DataFrame(columns=('학교명','구분', '공시년월','학부모부담수입','등록금'
                                   ,'학교운영지원비', '수익자부담수입','급식비'
                                   ,'방과후학교활동비', '현장체험학습비','청소년단체활동비'
                                   ,'졸업앨범대금', '교과서대금','기숙사비','기타수익자부담수입'
                                   ,'누리과정비','교복구입비','운동부운영비'), index=None  )
    # 사립학교 계정
    acctPrvtDf = DataFrame(columns=('학교명','구분', '공시년월','학부모부담수입' ,'등록금'
                                   ,'입학금' ,'수업료' ,'학교운영지원비' ,'수익자부담수입'
                                   ,'급식비' ,'방과후학교활동비' ,'현장체험학습비'
                                   ,'청소년단체활동비' ,'졸업앨범대금' ,'교과서대금'
                                   ,'기숙사비' ,'기타수익자부담수입' ,'누리과정비'
                                   ,'교복구입비','운동부운영비'), index=None  )


    debugLog = '웹드라이버 선택(팬텀은 화면표시 없음)'
    if args.browser == 'C':
        driver = webdriver.Chrome(pathWebDriver + "chromedriver")
    elif args.browser == 'P':
        driver = webdriver.PhantomJS(pathWebDriver + "phantomjs-2.1.1-windows\\bin\\phantomjs")
    elif args.browser == 'I':
        driver = webdriver.Ie(pathWebDriver + "IEDriverServer_win32_2.45.0")
    else:
        driver = webdriver.Chrome(pathWebDriver + "chromedriver")

    debugLog = '학교등급 선택'
    for g in grade:
#    for g in ('E','M','H'):
        debugLog = '학교정보 읽어오기'
        if g == 'e':
            schoolDf = pd.read_excel(pathFile  + "2-2) 초등학교 현황.xlsx")
            schoolDf.columns = schoolDf.iloc[2,0:]
            schoolDf = schoolDf.drop([0,1,2],axis=0)
        elif g == 'm':
            schoolDf = pd.read_excel(pathFile  + "2-3) 중학교 현황.xlsx")
            schoolDf.columns = schoolDf.iloc[2,0:]
            schoolDf = schoolDf.drop([0,1,2],axis=0)
        elif g == 'h':
            schoolDf = pd.read_excel(pathFile  + "2-4) 고등학교 현황.xlsx")
            schoolDf.columns = schoolDf.iloc[2,0:]
            schoolDf = schoolDf.drop([0,1,2],axis=0)
        elif g == 's':
            schoolDf = pd.read_excel(pathFile  + "2-5) 특수학교 및 기타학교 현황.xlsx", sheetname ="특수학교")
            schoolDf.columns = schoolDf.iloc[2,0:]
            schoolDf = schoolDf.drop([0,1,2],axis=0)
        elif g == 'o':
            schoolDf = pd.read_excel(pathFile  + "2-5) 특수학교 및 기타학교 현황.xlsx", sheetname ="기타학교")
            schoolDf.columns = schoolDf.iloc[2,0:]
            schoolDf = schoolDf.drop([0,1,2],axis=0)
        elif g == 'u':
            schoolDf = pd.read_excel(pathFile  + "1-1) 대학 현황.xlsx")
            schoolDf.columns = schoolDf.iloc[4,0:]
            schoolDf.rename(columns={"학교명(국문)":"학교명"}, inplace = True)
            schoolDf = schoolDf.drop([0,1,2,3,4],axis=0)
        elif g == 'g':
            schoolDf = pd.read_excel(pathFile  + "1-2) 대학원 현황.xlsx")
            schoolDf.columns = schoolDf.iloc[4,0:]
            schoolDf.rename(columns={"학교명(국문)":"학교명"}, inplace = True)
            schoolDf = schoolDf.drop([0,1,2,3,4],axis=0)
        else:
            pass


        debugLog = '학교 루프 시작'

        countPublic = 0
        countPrivate = 0
#        for idx, row in schoolDf.iloc[:5].iterrows():
        for idx, row in schoolDf.iterrows():

            schoolName = row['학교명'].strip()
            schoolURL = row['홈페이지'].strip()

            debugLog = '웹 호출'
            driver.implicitly_wait(5)
            driver.get('http://www.schoolinfo.go.kr')
            debugLog = '변수 초기화'
            schooltype = 'thead'

            try:
                driver.find_element_by_id("SEARCH_KEYWORD").send_keys("")
                driver.find_element_by_id("SEARCH_KEYWORD").send_keys(schoolName)
                driver.find_element_by_xpath("//button[@title='검색하기']").click()

                debugLog = '학교검색결과 더보기버튼'
                while 1:
                    try:
                        driver.find_element_by_id("btnMore")
                    except NoSuchElementException:
                        break
                    driver.find_element_by_id("btnMore").click()

                debugLog = '학교검색결과 색인'
                driver.find_element_by_xpath("//a[@href='"+schoolURL+"']/parent::span/parent::li/parent::ul/parent::article/h1[@class='School_Name']/a").click()

                debugLog = '국공사립 구분확인'
                establish = driver.find_element_by_xpath("//ul[@class='School_Data']/li[2]").text[5:]

                debugLog = '상세정보 클릭'
                driver.find_element_by_link_text('상세정보').click()

                debugLog = '예결산서 클릭'
                if establish in ('국립','공립'):
                    schooltype = 'thead'
                    colNo01 = '22'
                    colNo02 = '23'
                    colNo03 = '24'
                    colNo04 = '25'
                    colNo05 = '26'
                    colNo06 = '27'
                    colNo07 = '28'
                    colNo08 = '29'
                    colNo09 = '30'
                    colNo10 = '31'
                    colNo11 = '32'
                    colNo12 = '33'
                    colNo13 = '34'
                    colNo14 = '35'
                    colNo15 = '36'
                    driver.find_element_by_link_text('학교회계 예·결산서').click()

                elif establish == '사립':
                    schooltype = 'tbody'
                    colNo01 = '23'
                    colNo02 = '24'
                    colNo03 = '25'
                    colNo04 = '26'
                    colNo05 = '27'
                    colNo06 = '28'
                    colNo07 = '29'
                    colNo08 = '30'
                    colNo09 = '31'
                    colNo10 = '32'
                    colNo11 = '33'
                    colNo12 = '34'
                    colNo13 = '35'
                    colNo14 = '36'
                    colNo15 = '37'
                    colNo16 = '38'
                    colNo17 = '39'
                    driver.find_element_by_link_text('사립학교 교비회계 예·결산서').click()

                else:
                    pass
                    # raise_exception(schoolName + " pass !!!")

                debugLog = 'iframe 해제'
                driver.switch_to_frame(driver.find_element_by_xpath("//iframe"))

                debugLog = '자세히보기 클릭'
                driver.find_element_by_id("btnDetail").click()

                debugLog = '공시년월 목록 선택'
                select = Select(driver.find_element_by_id('select_trans_dt'))

                debugLog = '공시년월별 자세히 보기 루프'
                for index in range(len(select.options)):
                    debugLog = '공시년월별 자세히 보기 루프 select_by_index'
                    select = Select(driver.find_element_by_id('select_trans_dt'))
                    select.select_by_index(index)

                    debugLog = '공시년월별 자세히 보기 루프 existDetail'
                    existDetail = driver.find_element_by_xpath("//div[@id='btnDetail']/a")
                    if existDetail.is_displayed():
                        debugLog = '공시년월별 자세히 보기 루프 existDetail.click()'
                        existDetail.click()

                    debugLog = '공시년월별 자세히 보기 루프 cell'
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
                        acctPblcDf.loc[countPublic] = cell
                        countPublic += 1
                    elif establish == '사립':
                        acctPrvtDf.loc[countPrivate] = cell
                        countPrivate += 1

            except NoSuchElementException:
                print(schoolName + " "+ debugLog + "실패 NoSuchElementException !!!" )
                pass
            except StaleElementReferenceException:
                print(schoolName + " "+ debugLog + "실패 StaleElementReferenceException !!!" )
                pass


        #End Loop schoolDf
        # 파일 저장
        acctPblcDf.to_excel('.\\'+grade.get(g)+'Public.xlsx',  header=True, index=True)
        acctPrvtDf.to_excel('.\\'+grade.get(g)+'Private.xlsx',  header=True, index=True)

    # End Loop Grade
    driver.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='description: 학교알리미 Web Crawler'
                                   , formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-b', '--browser', choices=['i', 'c', 'p'], default='c'
                      , help='''사용할 인터넷 브라우저 선택(팬텀JS는 백그라운드실행)\ni = IE, c = Chrome, p = PhantomJS''')
    parser.add_argument('-l','--latest',choices = ['l','a'] , default='l'
                      , help='''가장 최근에 등록된 예결산서만 취득\n  l = Latest\n, a = All''')
    parser.add_argument('-g', '--grade', choices=['e', 'm', 'h', 'u', 'g', 's', 'o','a'], default='a' 
                      , help='''학교등급 선택\n  e = Elementary School\n, m = Middle School\n, h = High School , u = University\n, g = Graduate School\n, s = SpecialSchool, o = Others\n, a = All Grades''')
    args, unparsed = parser.parse_known_args()
    getParentPaid(args)
