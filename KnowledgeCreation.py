#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 12:36:08 2019

@author: ubuntu
"""

import re

class KnowledgeCreation:
    
    def __init__(self, ContentTextDict):
        self.ContentTextDict = ContentTextDict
    
    def textPreprocessing(self):
        for key, value in self.ContentTextDict.items():
            print(key, value)        