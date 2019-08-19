#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 18:27:46 2019

@author: ubuntu
"""

from Scrapper import Scrapper, WikiURLGetter
from KnowledgeCreation import KnowledgeCreation

try:
    URL = WikiURLGetter("Machine learning").getURL()
    scrap = Scrapper(URL)
    a = scrap.createDriver()
    scrap.wikipediaTable(a)
    me = scrap.wikipediaContent()
    KnowledgeCreation(me).textPreprocessing()
    
finally:
    a.close()