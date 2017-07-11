# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 21:51:49 2017

@author: Yong-geun
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
driver = webdriver.Chrome('.\\webdriver\\' + "chromedriver")
driver.implicitly_wait(3)
driver.get('http://e-childschoolinfo.moe.go.kr/kinderMt/combineFind.do')
