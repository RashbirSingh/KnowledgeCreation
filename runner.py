#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 18:27:46 2019

@author: ubuntu
"""

from Scrapper import Scrapper

try:
    scrap = Scrapper("https://en.wikipedia.org/wiki/List_of_US_Open_men's_singles_champions")
    a = scrap.pageGetter()
    scrap.wikipediaTable(a)
finally:
    a.close()