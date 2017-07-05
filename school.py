# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
from selenium import webdriver
from pandas import DataFrame
import pandas as pd

from selenium.common.exceptions import NoSuchElementException
#from bs4 import BeautifulSoup
#import os
#os.getcwd()

# 1. Retrieve School Name
#schoolDf = pd.read_excel(".\\school\\file\\2. 유초중등교육기관 주소록\\2-4) 고등학교 현황.xlsx")
schoolDf = pd.read_excel("C:\\app\\python\\school\\file\\2. 유초중등교육기관 주소록\\2-4) 고등학교 현황.xlsx")
schoolDf.columns = schoolDf.iloc[2,0:]
schoolDf = schoolDf.drop(0,axis=0)
schoolDf = schoolDf.drop(1,axis=0)
schoolDf = schoolDf.drop(2,axis=0)




moneyDf= DataFrame(columns=( '학교명', '학부모부담수입','등록금','학교운영지원비',
         '수익자부담수입','급식비','방과후학교활동비',
         '현장체험학습비','청소년단체활동비','졸업앨범대금',
         '교과서대금','기숙사비','기타수익자부담수입',
         '누리과정비','교복구입비','운동부운영비'), index=None  )




driver = webdriver.Chrome("C:\\app\\python\\webdriver\\chromedriver")
#driver = webdriver.PhantomJS("..\\webdriver\\phantomjs")
cnt=0
schooltype='thead'

for schoolName in schoolDf['학교명'].head(4):
    # 2. Call Web
    driver.implicitly_wait(5)
    driver.get('http://www.schoolinfo.go.kr')
    driver.find_element_by_id("SEARCH_KEYWORD").send_keys("")
    driver.find_element_by_id("SEARCH_KEYWORD").send_keys(schoolName + " 학교회계 예·결산서")
    driver.find_element_by_xpath("//button[@title='검색하기']").click()
    try:
        try:
            driver.find_element_by_link_text(schoolName).click()
            driver.find_element_by_link_text('상세정보').click()
            try:
                driver.find_element_by_link_text('학교회계 예·결산서').click()
                schooltype='thead'
            except NoSuchElementException:
                driver.find_element_by_link_text('사립학교 교비회계 예·결산서').click()
                schooltype='tbody'
            try:
                driver.find_element_by_xpath("//div[@id='btnDetail']/a").click()
            except NoSuchElementException:
                pass
        except NoSuchElementException:
            pass
        finally:
            driver.switch_to_frame(driver.find_element_by_xpath("//iframe"))
    
            driver.find_element_by_xpath("//div[@id='btnDetail']/a").click()
            cell =[]
            cell.append( schoolName)
            # 학부모부담수입
            cell.append( driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr[22]/td").text)
            #   등록금
            cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr[23]/td").text)
            #     학교운영지원비
            cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr[24]/td").text)
            #   수익자부담수입
            cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr[25]/td").text)
            #     급식비
            cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr[26]/td").text)
            
            #     방과후학교활동비
            cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr[27]/td").text)
            #     현장체험학습비
            cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr[28]/td").text)
            #     청소년단체활동비
            cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr[29]/td").text)
            #     졸업앨범대금
            cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr[30]/td").text)
            #     교과서대금
            cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr[31]/td").text)
            #     기숙사비
            cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr[32]/td").text)
            #     기타수익자부담수입
            cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr[33]/td").text)
            #     누리과정비
            cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr[34]/td").text)
            #     교복구입비
            cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr[35]/td").text)
            #     운동부운영비
            cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/"+schooltype+"/tr[36]/td").text)
            
            # 3. File Write
            moneyDf.loc[cnt] = cell
            cnt += 1
    except NoSuchElementException:
        pass
moneyDf.to_excel('C:\\app\\python\school\\output.xlsx',  header=True, index=True)


#    fw = open( "test.xls", encoding="utf-8", mode="w")
#    fw.write(cell)
#    fw.close()
#    
#driver.close()



#driver.switch_to_frame(driver.find_element_by_xpath("//iframe[@id='pneipp_39']"))

#try:
#except NoSuchElementException:
#    assert 0, "can't find input with XYZ itemcode"
