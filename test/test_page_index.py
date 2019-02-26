#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = 'jimit'
__CreateAt__ = '2019\2\24 10:31'

from selenium import  webdriver

browser = webdriver.Firefox()
browser.get("http://127.0.0.1:8000/index")

assert  "Django" in browser.title