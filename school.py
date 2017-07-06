# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 13:40:56 2017

@author: 1310615
"""

from selenium import webdriver

from pandas import DataFrame
import pandas as pd
import os 
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
#from bs4 import BeautifulSoup
#os.getcwd()

# 1. Retrieve School Name
#schoolDf = pd.read_excel(".\\school\\file\\2. 유초중등교육기관 주소록\\2-4) 고등학교 현황.xlsx")

#os.getcwd()
os.chdir("D:\\app\\python")
schoolDf = pd.read_excel(".\\school\\file\\2-4) 고등학교 현황.xlsx")
schoolDf.columns = schoolDf.iloc[2,0:]
schoolDf = schoolDf.drop(0,axis=0)
schoolDf = schoolDf.drop(1,axis=0)
schoolDf = schoolDf.drop(2,axis=0)


# 국공립학교 계정
accountNatinalDf = DataFrame(columns=('학교명','구분', '공시년월','학부모부담수입','등록금'
                            ,'학교운영지원비', '수익자부담수입','급식비'
                            ,'방과후학교활동비', '현장체험학습비','청소년단체활동비'
                            ,'졸업앨범대금', '교과서대금','기숙사비','기타수익자부담수입'
                            ,'누리과정비','교복구입비','운동부운영비'), index=None  )
# 사립학교 계정
accountPrivateDf= DataFrame(columns=('학교명','구분', '공시년월','학부모부담수입' ,'등록금'
                                     ,'입학금' ,'수업료' ,'학교운영지원비' ,'수익자부담수입' 
                                     ,'급식비' ,'방과후학교활동비' ,'현장체험학습비' 
                                     ,'청소년단체활동비' ,'졸업앨범대금' ,'교과서대금'
                                     ,'기숙사비' ,'기타수익자부담수입' ,'누리과정비' 
                                     ,'교복구입비','운동부운영비'), index=None  )


# 웹드라이버 선택(팬텀은 화면표시 없음)
driver = webdriver.Chrome(".\\webdriver\\chromedriver")
#driver = webdriver.PhantomJS("..\\webdriver\\phantomjs")




#Exception 클래스를 상속한 클래스를 만든다
class CustomException(Exception):
    #생성할때 value 값을 입력 받는다.
    def __init__(self, value):
        self.value = value
     
    #생성할때 받은 value 값을 확인 한다.
    def __str__(self):
        return self.value

#예외를 발생하는 함수
def raise_exception(err_msg):
    raise CustomException(err_msg)


# 변수 초기화 
countNational = 0
countPrivate = 0
schooltype='thead'
debugStr = '변수 초기화'


for schoolName in schoolDf['학교명'].head(20):
    debugStr = '웹 호출'
    driver.implicitly_wait(5)
    driver.get('http://www.schoolinfo.go.kr')

    try:
        driver.find_element_by_id("SEARCH_KEYWORD").send_keys("")
        driver.find_element_by_id("SEARCH_KEYWORD").send_keys(schoolName)
        driver.find_element_by_xpath("//button[@title='검색하기']").click()
        
        debugStr = '학교 검색 결과 선택 '
        driver.find_element_by_link_text(schoolName).click()
        
        debugStr = '국공사립 구분 확인'
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
            raise_exception(schoolName + " pass !!!")
    
        debugStr = 'iframe 해제'
        driver.switch_to_frame(driver.find_element_by_xpath("//iframe"))

        debugStr = '자세히보기 클릭'
        driver.find_element_by_xpath("//div[@id='btnDetail']/a").click()

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
accountNatinalDf.to_excel('.\\school\\National.xlsx',  header=True, index=True)
accountPrivateDf.to_excel('.\\school\\Private.xlsx',  header=True, index=True)


#    fw = open( "test.xls", encoding="utf-8", mode="w")
#    fw.write(cell)
#    fw.close()
#    
#driver.close()



#driver.switch_to_frame(driver.find_element_by_xpath("//iframe[@id='pneipp_39']"))

#try:
#except NoSuchElementException:
#    assert 0, "can't find input with XYZ itemcode"


#학부모부담수입           colNo01= '22'
#  등록금                 colNo02= '23'
#    학교운영지원비       colNo03= '24'
#  수익자부담수입         colNo04= '25'
#    급식비               colNo05= '26'
#    방과후학교활동비     colNo06= '27'
#    현장체험학습비       colNo07= '28'
#    청소년단체활동비     colNo08= '29'
#    졸업앨범대금         colNo09= '30'
#    교과서대금           colNo10= '31'
#    기숙사비             colNo11= '32'
#    기타수익자부담수입   colNo12= '33'
#    누리과정비           colNo13= '34'
#    교복구입비           colNo14= '35'
#    운동부운영비         colNo15= '36'
#
#
#
#
#
#학부모부담수입           colNo01= '23'
#  등록금                 colNo02= '24'
#    입학금               colNo03= '25'
#    수업료               colNo04= '26'
#    학교운영지원비       colNo05= '27'
#  수익자부담수입         colNo06= '28'
#    급식비               colNo07= '29'
#    방과후학교활동비     colNo08= '30'
#    현장체험학습비       colNo09= '31'
#    청소년단체활동비     colNo10= '32'
#    졸업앨범대금         colNo11= '33'
#    교과서대금           colNo12= '34'
#    기숙사비             colNo13= '35'
#    기타수익자부담수입   colNo14= '36'
#    누리과정비           colNo15= '37'
#    교복구입비           colNo16= '38'
#    운동부운영비         colNo17= '39'
