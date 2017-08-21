# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 08:52:21 2017

@author: 1310615
"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
from pandas import DataFrame

from datetime import datetime

pathList = u'D:\\app\\python\\child\\'
pathWebDriver = u'D:\\app\\python\\webdriver\\'
pathResult= u'D:\\app\\python\\child\\'
kinderDf = pd.read_excel(pathList  + u"kindergarten_list_result.xls")


for idx, row in kinderDf.loc[107:109].iterrows():
    kname = row[u'kindername'].strip()
    kaddr = row[u'addr'].strip()

    driver = webdriver.Chrome(pathWebDriver + 'chromedriver.exe')
    driver.implicitly_wait(3)
    driver.get('http://e-childschoolinfo.moe.go.kr/kinderMt/combineFind.do')

    driver.find_element_by_id('kinderName').send_keys('')
    driver.find_element_by_id('kinderName').send_keys(kname)
    driver.find_element_by_xpath("//a[text()='검색']").click()
    driver.find_element_by_xpath("//td[text()='"+kaddr +"']/../td/a").click()
    driver.find_element_by_xpath("//a[text()='교육·보육비용']").click()


    
    df = DataFrame(columns=( u'ADDRESS'
    ,u'ESTABLISH'
    ,u'KINDERNAME'
    ,u'PUPILCNT3'
    ,u'PUPILCNT4'
    ,u'PUPILCNT5'
    ,u'CC3_BSC_TUITION'
    ,u'CC4_BSC_TUITION'
    ,u'CC5_BSC_TUITION'
    ,u'CC_CYCLE_BSC_TUITION'
    ,u'CC3_BSC_SNACK'
    ,u'CC4_BSC_SNACK'
    ,u'CC5_BSC_SNACK'
    ,u'CC_CYCLE_BSC_SNACK'
    ,u'CC3_BSC_MEAL'
    ,u'CC4_BSC_MEAL'
    ,u'CC5_BSC_MEAL'
    ,u'CC_CYCLE_BSC_MEAL'
    ,u'CC3_BSC_MTRS'
    ,u'CC4_BSC_MTRS'
    ,u'CC5_BSC_MTRS'
    ,u'CC_CYCLE_BSC_MTRS'
    ,u'CC3_BSC_MNTH_SUM'
    ,u'CC4_BSC_MNTH_SUM'
    ,u'CC5_BSC_MNTH_SUM'
    ,u'CC3_OPT_ADDMISION'
    ,u'CC4_OPT_ADDMISION'
    ,u'CC5_OPT_ADDMISION'
    ,u'CC_CYCLE_OPT_ADDMISION'
    ,u'CC3_OPT_UNIFORM'
    ,u'CC4_OPT_UNIFORM'
    ,u'CC5_OPT_UNIFORM'
    ,u'CC_CYCLE_OPT_UNIFORM'
    ,u'CC3_OPT_FIELD'
    ,u'CC4_OPT_FIELD'
    ,u'CC5_OPT_FIELD'
    ,u'CC_CYCLE_OPT_FIELD'
    ,u'CC3_OPT_SHUTTLE'
    ,u'CC4_OPT_SHUTTLE'
    ,u'CC5_OPT_SHUTTLE'
    ,u'CC_CYCLE_OPT_SHUTTLE'
    ,u'CC3_OPT_ETC'
    ,u'CC4_OPT_ETC'
    ,u'CC5_OPT_ETC'
    ,u'CC_CYCLE_OPT_ETC'
    ,u'AS3_BSC_TUITION'
    ,u'AS4_BSC_TUITION'
    ,u'AS5_BSC_TUITION'
    ,u'AS_BILL_CYCLE_BSC_TUITION'
    ,u'AS3_BSC_SNACK'
    ,u'AS4_BSC_SNACK'
    ,u'AS5_BSC_SNACK'
    ,u'AS_BILL_CYCLE_BSC_SNACK'
    ,u'AS3_BSC_MEAL'
    ,u'AS4_BSC_MEAL'
    ,u'AS5_BSC_MEAL'
    ,u'AS_BILL_CYCLE_BSC_MEAL'
    ,u'AS3_BSC_MTRS'
    ,u'AS4_BSC_MTRS'
    ,u'AS5_BSC_MTRS'
    ,u'AS_BILL_CYCLE_BSC_MTRS'
    ,u'AS3_BSC_MNTH_SUM'
    ,u'AS4_BSC_MNTH_SUM'
    ,u'AS5_BSC_MNTH_SUM'
    ,u'AS3_OPT_FIELD'
    ,u'AS4_OPT_FIELD'
    ,u'AS5_OPT_FIELD'
    ,u'AS_BILL_CYCLE_OPT_FIELD'
    ,u'AS3_OPT_SHUTTLE'
    ,u'AS4_OPT_SHUTTLE'
    ,u'AS5_OPT_SHUTTLE'
    ,u'AS_BILL_CYCLE_OPT_SHUTTLE'
    ,u'CH3_ART'
    ,u'CH3_ART_PROGRAM'
    ,u'CH3_ART_COMPANY'
    ,u'CH3_ART_OPR_WEEK'
    ,u'CH3_ART_OPR_TIME'
    ,u'CH3_ART_MM_ENDMNT'
    ,u'CH3_GYM'
    ,u'CH3_GYM_PROGRAM'
    ,u'CH3_GYM_COMPANY'
    ,u'CH3_GYM_OPR_WEEK'
    ,u'CH3_GYM_OPR_TIME'
    ,u'CH3_GYM_MM_ENDMNT'
    ,u'CH3_LAN'
    ,u'CH3_LAN_PROGRAM'
    ,u'CH3_LAN_COMPANY'
    ,u'CH3_LAN_OPR_WEEK'
    ,u'CH3_LAN_OPR_TIME'
    ,u'CH3_LAN_MM_ENDMNT'
    ,u'CH4_ART'
    ,u'CH4_ART_PROGRAM'
    ,u'CH4_ART_COMPANY'
    ,u'CH4_ART_OPR_WEEK'
    ,u'CH4_ART_OPR_TIME'
    ,u'CH4_ART_MM_ENDMNT'
    ,u'CH4_GYM'
    ,u'CH4_GYM_PROGRAM'
    ,u'CH4_GYM_COMPANY'
    ,u'CH4_GYM_OPR_WEEK'
    ,u'CH4_GYM_OPR_TIME'
    ,u'CH4_GYM_MM_ENDMNT'
    ,u'CH4_LAN'
    ,u'CH4_LAN_PROGRAM'
    ,u'CH4_LAN_COMPANY'
    ,u'CH4_LAN_OPR_WEEK'
    ,u'CH4_LAN_OPR_TIME'
    ,u'CH4_LAN_MM_ENDMNT'
    ,u'CH5_ART'
    ,u'CH5_ART_PROGRAM'
    ,u'CH5_ART_COMPANY'
    ,u'CH5_ART_OPR_WEEK'
    ,u'CH5_ART_OPR_TIME'
    ,u'CH5_ART_MM_ENDMNT'
    ,u'CH5_GYM'
    ,u'CH5_GYM_PROGRAM'
    ,u'CH5_GYM_COMPANY'
    ,u'CH5_GYM_OPR_WEEK'
    ,u'CH5_GYM_OPR_TIME'
    ,u'CH5_GYM_MM_ENDMNT'
    ,u'CH5_LAN'
    ,u'CH5_LAN_PROGRAM'
    ,u'CH5_LAN_COMPANY'
    ,u'CH5_LAN_OPR_WEEK'
    ,u'CH5_LAN_OPR_TIME'
    ,u'CH5_LAN_MM_ENDMNT'), index=None)

    cell = []
    cell.append(kaddr)
    cell.append(row[u'establish'].strip())
    cell.append(kname)
    cell.append(str(row[u'ppcnt3']).strip())
    cell.append(str(row[u'ppcnt4']).strip())
    cell.append(str(row[u'ppcnt5']).strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='수업료']/../td[1]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='수업료']/../td[2]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='수업료']/../td[3]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='수업료']/../td[4]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='간식비']/../td[1]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='간식비']/../td[2]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='간식비']/../td[3]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='간식비']/../td[4]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='급식비']/../td[1]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='급식비']/../td[2]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='급식비']/../td[3]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='급식비']/../td[4]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='교재비 및 재료비']/../td[1]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='교재비 및 재료비']/../td[2]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='교재비 및 재료비']/../td[3]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='교재비 및 재료비']/../td[4]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='합계(월)']/../td[1]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='합계(월)']/../td[2]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='합계(월)']/../td[3]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='입학금']/../td[1]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='입학금']/../td[2]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='입학금']/../td[3]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='입학금']/../td[4]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='원복비']/../td[1]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='원복비']/../td[2]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='원복비']/../td[3]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='원복비']/../td[4]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='현장학습비']/../td[1]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='현장학습비']/../td[2]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='현장학습비']/../td[3]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='현장학습비']/../td[4]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='차량운영비']/../td[1]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='차량운영비']/../td[2]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='차량운영비']/../td[3]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='차량운영비']/../td[4]").text.strip())
    
    aaa = ''
    try:
        aaa = driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='기타경비']/../td[1]")
        cell.append(aaa.text.strip())
    except NoSuchElementException as e:
        print u'aaa 없어요'
        pass
    cell.append(aaa)
        
    
    
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='기타경비']/../td[2]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='기타경비']/../td[3]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='교육과정 교육비용']/..//th[text()='기타경비']/../td[4]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='방과후 과정 교육비용']/..//th[text()='수업료']/../td[1]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='방과후 과정 교육비용']/..//th[text()='수업료']/../td[2]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='방과후 과정 교육비용']/..//th[text()='수업료']/../td[3]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='방과후 과정 교육비용']/..//th[text()='수업료']/../td[4]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='방과후 과정 교육비용']/..//th[text()='간식비']/../td[1]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='방과후 과정 교육비용']/..//th[text()='간식비']/../td[2]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='방과후 과정 교육비용']/..//th[text()='간식비']/../td[3]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='방과후 과정 교육비용']/..//th[text()='간식비']/../td[4]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='방과후 과정 교육비용']/..//th[text()='급식비']/../td[1]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='방과후 과정 교육비용']/..//th[text()='급식비']/../td[2]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='방과후 과정 교육비용']/..//th[text()='급식비']/../td[3]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='방과후 과정 교육비용']/..//th[text()='급식비']/../td[4]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='방과후 과정 교육비용']/..//th[text()='교재비 및 재료비']/../td[1]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='방과후 과정 교육비용']/..//th[text()='교재비 및 재료비']/../td[2]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='방과후 과정 교육비용']/..//th[text()='교재비 및 재료비']/../td[3]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='방과후 과정 교육비용']/..//th[text()='교재비 및 재료비']/../td[4]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='방과후 과정 교육비용']/..//th[text()='합계(월)']/../td[1]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='방과후 과정 교육비용']/..//th[text()='합계(월)']/../td[2]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='방과후 과정 교육비용']/..//th[text()='합계(월)']/../td[3]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='방과후 과정 교육비용']/..//th[text()='현장학습비']/../td[1]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='방과후 과정 교육비용']/..//th[text()='현장학습비']/../td[2]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='방과후 과정 교육비용']/..//th[text()='현장학습비']/../td[3]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='방과후 과정 교육비용']/..//th[text()='현장학습비']/../td[4]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='방과후 과정 교육비용']/..//th[text()='차량운영비']/../td[1]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='방과후 과정 교육비용']/..//th[text()='차량운영비']/../td[2]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='방과후 과정 교육비용']/..//th[text()='차량운영비']/../td[3]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='방과후 과정 교육비용']/..//th[text()='차량운영비']/../td[4]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[2]/td[1]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[2]/td[2]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[2]/td[3]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[2]/td[4]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[2]/td[5]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[2]/td[6]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[3]/td[1]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[3]/td[2]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[3]/td[3]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[3]/td[4]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[3]/td[5]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[3]/td[6]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[4]/td[1]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[4]/td[2]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[4]/td[3]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[4]/td[4]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[4]/td[5]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[4]/td[6]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[5]/td[1]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[5]/td[2]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[5]/td[3]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[5]/td[4]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[5]/td[5]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[5]/td[6]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[6]/td[1]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[6]/td[2]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[6]/td[3]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[6]/td[4]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[6]/td[5]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[6]/td[6]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[7]/td[1]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[7]/td[2]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[7]/td[3]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[7]/td[4]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[7]/td[5]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[7]/td[6]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[8]/td[1]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[8]/td[2]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[8]/td[3]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[8]/td[4]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[8]/td[5]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[8]/td[6]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[9]/td[1]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[9]/td[2]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[9]/td[3]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[9]/td[4]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[9]/td[5]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[9]/td[6]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[10]/td[1]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[10]/td[2]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[10]/td[3]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[10]/td[4]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[10]/td[5]").text.strip())
    cell.append(driver.find_element_by_xpath("//caption[text()='특성화 활동비']/../tbody/tr[10]/td[6]").text.strip())

    df.loc[0] = cell
    df.to_excel(pathResult + u'kinderresult'+datetime.today().strftime("%Y%m%d%H%M%S")+'.xlsx',  header=True, index=True)
