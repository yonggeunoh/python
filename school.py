# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
#from selenium.common.exceptions import NoSuchElementException
#from bs4 import BeautifulSoup
#import os
#os.getcwd()

# 1. Retrieve School Name
kndDf = pd.read_excel("D:\\app\\python\\school\\file\\2-4) 고등학교 현황.xlsx")
kndDf.columns = kndDf.ix[2,0:]
kndDf = kndDf.drop(0,axis=0)
kndDf = kndDf.drop(1,axis=0)
kndDf = kndDf.drop(2,axis=0)


for schoolName in kndDf['학교명'].head(1) :
    # 2. Call Web
    driver = webdriver.Chrome("D:\\app\\python\\webdriver\\chromedriver")
    driver.implicitly_wait(3)
    driver.get('http://www.schoolinfo.go.kr')
    driver.find_element_by_id("SEARCH_KEYWORD").send_keys(schoolName + " 학교회계 예·결산서")
    driver.find_element_by_xpath("//button[@title='검색하기']").click()
    driver.switch_to_frame(driver.find_element_by_xpath("//iframe[@id='pneipp_39']"))
    driver.find_element_by_xpath("//div[@id='btnDetail']/a").click()
    cell = []
    # 학부모부담수입
    cell.append( driver.find_element_by_xpath("//table[@class='TableType1']/thead/tr[22]/td").text)
    #   등록금
    cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/thead/tr[23]/td").text)
    #     학교운영지원비
    cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/thead/tr[24]/td").text)
    #   수익자부담수입
    cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/thead/tr[25]/td").text)
    #     급식비
    cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/thead/tr[26]/td").text)
    
    #     방과후학교활동비
    cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/thead/tr[27]/td").text)
    #     현장체험학습비
    cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/thead/tr[28]/td").text)
    #     청소년단체활동비
    cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/thead/tr[29]/td").text)
    #     졸업앨범대금
    cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/thead/tr[30]/td").text)
    #     교과서대금
    cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/thead/tr[31]/td").text)
    #     기숙사비
    cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/thead/tr[32]/td").text)
    #     기타수익자부담수입
    cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/thead/tr[33]/td").text)
    #     누리과정비
    cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/thead/tr[34]/td").text)
    #     교복구입비
    cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/thead/tr[35]/td").text    )
    #     운동부운영비
    cell.append(driver.find_element_by_xpath("//table[@class='TableType1']/thead/tr[36]/td").text    )
    
    # 3. File Write
    cellpd = pd.DataFrame(cell)
    cellpd.to_excel('output.xlsx', header=False, index=False)


#    fw = open( "test.xls", encoding="utf-8", mode="w")
#    fw.write(cell)
#    fw.close()
#    
    driver.close()



#driver.switch_to_frame(driver.find_element_by_xpath("//iframe[@id='pneipp_39']"))

#try:
#except NoSuchElementException:
#    assert 0, "can't find input with XYZ itemcode"

