#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 03:54:47 2019

@author: ubuntuhome
"""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import wikipediaapi
import re
import os
import csv
import requests


class Scrapper:

    def __init__(self, url, driver = 'driver/geckodriver'):
        self.url = url
        self.driver = driver

    def pageGetter(self,
                   runHeadless=True):
        """
        pageGetter - Creates the driver object based on the URL
        
        Input:
            runHeadless - Boolean
                          Run the driver hedless or not
  
        Return:
            driverpage - Selenium firefox driver object
        """
        options = Options()
        profile = webdriver.FirefoxProfile()
        if runHeadless:
            options.add_argument("--headless")
        
        driverpage = webdriver.Firefox(executable_path = self.driver,
                                       firefox_options=options,
                                       firefox_profile=profile)
        driverpage.get(self.url)
        return driverpage

    def wikipediaContent(self):
        content = {}
        toSearch=re.sub(".*/", "", self.url)
        wiki_wiki = wikipediaapi.Wikipedia('en')
        information = wiki_wiki.page(toSearch)
        content["Main"] = information.text.split("\n\n")[0]
        sectionText = information.sections
        for i in range(len(sectionText)):
            if (len(sectionText[i].text) > 3) and \
            (sectionText[i].title != "References") and \
            (sectionText[i].title != "See also") and \
            (sectionText[i].title != "External links"):
                content[sectionText[i].title] = sectionText[i].text
        return content
        
        

    def wikipediaTable(self,
                       driverpage,
                       tableFileName="Table"):
        """
        wikipediaTable - Reads the wikipedia and create csv for each table found
        
        Input:
            driverpage - Driver object linked to the url
            tableFileName - str
                            Name of the output file to be given
        
        Return:
            null
        """
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
                    df.to_csv(tableFileName+str(i)+'.csv')
                except:
                    pass
