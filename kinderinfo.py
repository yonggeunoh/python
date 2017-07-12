# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import argparse
import pandas as pd
import logging
from pandas import DataFrame
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotVisibleException
from bs4 import BeautifulSoup


gv_url = 'http://e-childschoolinfo.moe.go.kr/kinderMt/combineFind.do'
#import os
#os.getcwd()
driver = webdriver.Chrome('.\\chromedriver')

driver.implicitly_wait(3)

driver.get(gv_url)



from urllib.request import urlopen
from bs4 import BeautifulSoup


import csv
import os
import re

html = urlopen(gv_url)
soup = BeautifulSoup(html.read(), "html.parser")

trs = soup.findAll('tbody')[5].findAll('tr')

# todo
trs[1].select('a[href^="javascript:fn_validateURL"]')



header = []
for th in trs[0].find_all('th'):
    header.append(th.text.strip())

rows = []
for tr in trs[1:]:
    row = []
    tds = tr.find_all('td')
    row.append(tds[1].text.strip())
    row.append(tds[2].text.strip().replace(' ','').replace('\r','').replace('\n',''))
    row.append(tds[3].text.strip())
    row.append(tds[4].text.strip())
    rows.append(row)

with open('test.tsv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')
    writer.writerow(header)
    for r in rows:
        try:
            writer.writerow(r)
        except Exception as e:
            print (e)
    

def get_csv_writer(filename, header, rows, delimiter):
    with open(filename, 'w') as csvfile:
        fieldnames = header.key()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=delimiter)
        writer.writeheader()
        for row in rows:
            try:
                writer.writerow(row)
            except Exception as detail:
                print (detail)
		
def get_csv_reader(filename, delimiter):
	reader = []
	if not os.path.isfile(filename):
		csvfile = open(filename, "w")
	else:
		csvfile = open(filename, "rb")
	reader = csv.DictReader(csvfile, delimiter=delimiter)
	return list(reader)




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='description: 학교알리미 Web Crawler'
                                   , formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-b', '--browser', choices=['i', 'c', 'p'], default='c'
                      , help='''사용할 인터넷 브라우저 선택(p는 백그라운드실행)\ni = IE, c = Chrome, p = PhantomJS''')
    parser.add_argument('-g', '--grade', choices=['e', 'm', 'h', 'u', 'g', 's', 'o','a'], default='a' 
                      , help='''학교등급 선택\n  e = Elementary School\n, m = Middle School\n, h = High School\n, u = University\n, g = Graduate School\n, s = SpecialSchool\n, o = Others\n, a = All Grades''')
    args, unparsed = parser.parse_known_args()
    xxxxxxxx(args)
