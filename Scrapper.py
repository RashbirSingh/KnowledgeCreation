#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 03:54:47 2019

@author: ubuntuhome
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import csv
import requests


class Scrapper:

    def __init__(self, url, driver = 'driver/geckodriver'):
        self.url = url
        self.driver = driver

    def pageGetter(self):
        driverpage = webdriver.Firefox(executable_path = self.driver)
        driverpage.get(self.url)
        return driverpage

    def wikipediaTable(self, driverpage):
        soup = BeautifulSoup(driverpage.page_source,'lxml')
        i = 0
        for table in soup.find_all('table', {'class': 'sortable'}):
            i = i + 1
            headerList = []
            rowList = []
            
            for rows in table.find_all('tr'):
                dataList=[]
                for header in rows.find_all('th'):
                    headerList.append(header.text)
                for cellData in rows.find_all('td'):
                    dataList.append(cellData.text)
                rowList.append(dataList)
                try:
                    df = pd.DataFrame(rowList)
                    df.columns = headerList
                    df.to_csv('output'+str(i)+'.csv')
                except:
                    pass
